import pandas as pd
import plotly.express as px
import streamlit as st

from datos import EMPRESA, OBJETIVOS as O

st.set_page_config(page_title=f"Dashboard {EMPRESA}", page_icon="📊", layout="wide")
ROJO, VERDE = "#C44536", "#2E8B57"
sol = lambda v: f"S/ {v:,.2f}"


def barras(df, x, ylab, fmt=",.0f"):
    f = px.bar(df, x=x, y=["Antes", "Después"], barmode="group", text_auto=fmt,
               color_discrete_map={"Antes": ROJO, "Después": VERDE}, labels={"value": ylab, "variable": ""})
    f.update_layout(margin=dict(t=10, b=10), height=340, xaxis_title=None, legend_title_text="")
    return f


with st.sidebar:
    st.title(EMPRESA)
    st.caption("Lean Manufacturing · Gestión de operaciones")
    st.divider()
    st.info("Dashboard construido con los datos del archivo Excel del proyecto. "
            "Los supuestos y datos pendientes se identifican en cada módulo.")

st.title("📊 Dashboard de Gestión de Operaciones")
st.caption(f"{EMPRESA} | Comparación AS IS vs. TO BE | Evaluación técnica y económica")

tabs = st.tabs(["Resumen general"] + [f"Objetivo {i} · {o['corto']}" for i, o in O.items()])

# ---------------------------------------------------------------- RESUMEN
with tabs[0]:
    st.header("Panel ejecutivo")
    st.info("Vista consolidada de los cinco objetivos. Los beneficios económicos no se suman en un único total "
            "porque incluyen ahorros de tiempo, calidad y retrabajos calculados con supuestos distintos.")
    n = len(O)
    cards = [("Objetivos desarrollados", n, f"{n} módulos"),
             ("Inversión inicial registrada", sol(sum(o["inversion"] for o in O.values())), "Suma de inversiones"),
             ("Objetivos con comparación AS IS / TO BE", f"{n} de {n}", "Información disponible"),
             ("Objetivos con PRI documentado", sum(1 for o in O.values() if o["pri"]),
              "Objetivos " + ", ".join(str(i) for i, o in O.items() if o["pri"]))]
    for col, (t, v, d) in zip(st.columns(4), cards):
        with col.container(border=True):
            st.metric(t, v, d, delta_color="off")

    st.subheader("Comparación de indicadores principales")
    ind = pd.DataFrame([{"Objetivo": f"O{i} · {o['corto']}", "Indicador": o["indicador"], "Antes": o["antes"],
                         "Después": o["despues"], "Unidad": o["unidad"],
                         "Variación": f"{(o['despues'] - o['antes']) / o['antes'] * 100:+.1f}%"} for i, o in O.items()])
    st.dataframe(ind, hide_index=True)

    st.subheader("Antes y después económico por objetivo")
    eco = pd.DataFrame([{"Objetivo": f"O{i}", "Antes": sum(c[1] for c in o["costos"]),
                         "Después": sum(c[2] for c in o["costos"])} for i, o in O.items()])
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Costo anual relacionado: antes y después (S/)**")
        st.plotly_chart(barras(eco, "Objetivo", "S/ al año"), key="res_eco")
    with c2:
        st.markdown("**Inversión, ahorro anual y beneficio neto 1.er año (S/)**")
        rent = pd.DataFrame([{"Objetivo": f"O{i}", "Inversión": o["inversion"], "Ahorro anual": o["ahorro"],
                              "Beneficio neto 1.er año": o["beneficio"]} for i, o in O.items()])
        f = px.bar(rent, x="Objetivo", y=["Inversión", "Ahorro anual", "Beneficio neto 1.er año"], barmode="group",
                   text_auto=",.0f", labels={"value": "S/", "variable": ""},
                   color_discrete_sequence=["#6B7280", VERDE, "#2563EB"])
        f.update_layout(margin=dict(t=10, b=10), height=340, xaxis_title=None)
        st.plotly_chart(f, key="res_rent")

    st.subheader("Resumen de rentabilidad")
    tabla = pd.DataFrame([{"Objetivo": f"O{i} · {o['corto']}", "Inversión": sol(o["inversion"]),
                           "Ahorro anual": sol(o["ahorro"]), "Beneficio neto 1.er año": sol(o["beneficio"]),
                           "ROI": f"{o['roi'] * 100:.1f}%", "PRI": o["pri"] or "No documentado"} for i, o in O.items()])
    st.dataframe(tabla, hide_index=True)

# ---------------------------------------------------------------- OBJETIVOS
for (i, o), tab in zip(O.items(), tabs[1:]):
    with tab:
        st.header(f"Objetivo {i} · {o['corto']}")
        st.caption(f"{o['descripcion']} Herramienta: {o['herramienta']}.")
        kpis = [("Inversión inicial", sol(o["inversion"])), ("Ahorro anual", sol(o["ahorro"])),
                ("Beneficio neto 1.er año", sol(o["beneficio"])), ("ROI primer año", f"{o['roi'] * 100:.1f}%")]
        for col, (t, v) in zip(st.columns(4), kpis):
            with col.container(border=True):
                st.metric(t, v)
        st.caption(f"ℹ️ {o['nota']}" + (f"  ·  PRI: {o['pri']}" if o["pri"] else "  ·  PRI: no documentado en el Excel"))

        a, b = st.columns(2)
        with a:
            st.subheader("Antes y después económico (S/ al año)")
            df = pd.DataFrame(o["costos"], columns=["Concepto", "Antes", "Después"])
            st.plotly_chart(barras(df, "Concepto", "S/ al año"), key=f"eco{i}")
            show = df.assign(Ahorro=df["Antes"] - df["Después"])
            st.dataframe(show.assign(**{c: show[c].map(sol) for c in ["Antes", "Después", "Ahorro"]}), hide_index=True)
        with b:
            st.subheader("Antes y después técnico")
            if "desglose" in o:
                tit, filas = o["desglose"]
                st.caption(tit)
                dt = pd.DataFrame(filas, columns=["Producto", "Antes", "Después"])
                st.plotly_chart(barras(dt, "Producto", o["unidad"], ",.1f"), key=f"tec{i}")
            else:
                dt = pd.DataFrame([{"Indicador": o["indicador"], "Antes": o["antes"], "Después": o["despues"]}])
                st.plotly_chart(barras(dt, "Indicador", o["unidad"], ",.2f"), key=f"tec{i}")
            var = (o["despues"] - o["antes"]) / o["antes"] * 100
            st.metric(f"{o['indicador']} ({o['unidad']})", f"{o['antes']:,.2f} → {o['despues']:,.2f}",
                      f"{var:+.1f}%", delta_color="inverse" if var < 0 else "normal")

        c, d = st.columns(2)
        with c:
            st.subheader("Detalle de la inversión inicial")
            inv = pd.DataFrame(o["inv_detalle"], columns=["Concepto", "Costo (S/)"])
            inv.loc[len(inv)] = ["TOTAL", inv["Costo (S/)"].sum()]
            st.dataframe(inv.assign(**{"Costo (S/)": inv["Costo (S/)"].map(sol)}), hide_index=True)
        with d:
            if "flujo" in o:
                st.subheader("Flujo de caja neto (S/)")
                fl = pd.DataFrame({"Año": [f"Año {k}" for k in range(len(o["flujo"]))], "Flujo neto": o["flujo"]})
                g = px.bar(fl, x="Año", y="Flujo neto", text_auto=",.0f", color_discrete_sequence=[VERDE])
                g.update_layout(margin=dict(t=10, b=10), height=300, xaxis_title=None)
                st.plotly_chart(g, key=f"flujo{i}")
            if "van_tir" in o:
                st.markdown("**VAN (COK 10%) y TIR según horizonte**")
                st.dataframe(pd.DataFrame([{"Horizonte": h, "TIR": f"{t * 100:.1f}%", "VAN": sol(v)}
                                           for h, t, v in o["van_tir"]]), hide_index=True)
