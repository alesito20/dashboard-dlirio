"""Datos del proyecto D'Lirio extraídos del archivo Excel (hojas 'Objetivo 1' a 'Objetivo 5').
Si cambias una cifra en el Excel, actualízala aquí."""

EMPRESA = "D'Lirio Lencería"

OBJETIVOS = {
    1: dict(
        corto="Trabajo estandarizado", herramienta="HTE, ficha técnica y manuales de procedimiento",
        descripcion="Estandarizar la costura de brasieres para reducir el tiempo de ciclo y los defectos.",
        indicador="Tiempo de ciclo (con esperas)", antes=774, despues=706, unidad="min/lote",
        inversion=3028.00, ahorro=4327.65, beneficio=1299.65, roi=0.429, pri=None,
        costos=[("Costo de defectos", 370.80, 156.56),
                ("Costo anual del tiempo de producción", 16686.00, 2974.64)],
        nota="Ahorro = S/ 214.24 (defectos) + 30% del ahorro de tiempo (S/ 4,113.41).",
        inv_detalle=[("Diseño e impresión de HTE y fichas técnicas", 180), ("Manual de procedimientos y de máquinas", 420),
                     ("Capacitación del personal", 768), ("Tableros de gestión visual", 750),
                     ("Calibración inicial de máquinas", 270), ("Plantillas y guías de costura", 540),
                     ("Checklists y formatos", 100)]),
    2: dict(
        corto="Inspección de calidad", herramienta="SOP + Catálogo visual de defectos + Checklist",
        descripcion="Reducir el escape de prendas defectuosas al cliente con inspección estandarizada.",
        indicador="Eficacia de inspección (EIC)", antes=73.43, despues=96.08, unidad="%",
        inversion=1850.00, ahorro=2590.00, beneficio=740.00, roi=0.40, pri="8.57 meses",
        costos=[("Costo anual de escapes a clientes", 2660.00, 70.00)],
        nota="Escapes evitados: de 76 a 2 prendas/año × S/ 35 por devolución.",
        inv_detalle=[("Tableros del catálogo visual", 1000), ("Diseño e impresión de SOPs", 150),
                     ("Capacitación del personal", 600), ("Checklists y carpetas", 100)],
        flujo=[-1850, 2590, 2590, 2590, 2590, 2590],
        van_tir=[("1 año", 0.40, 504.55), ("3 años", 1.282, 4590.95), ("5 años", 1.382, 7968.14)]),
    3: dict(
        corto="SMED (cambio de modelo)", herramienta="SMED: tareas internas → externas, kits y 5S",
        descripcion="Reducir el tiempo de paro de línea por cambio de modelo.",
        indicador="Paro por cambio de modelo", antes=347.0, despues=125.8, unidad="min/ciclo",
        inversion=1282.00, ahorro=2831.36, beneficio=1429.36, roi=1.1149, pri="5.7 meses",
        costos=[("Costo anual del tiempo de paro", 8883.20, 3220.48)],
        nota="Ahorro = 50% del ahorro de tiempo (S/ 5,662.72). Sostenimiento anual: S/ 120.",
        inv_detalle=[("Carritos de kit de materiales", 240), ("Tablero de sombras 5S", 300),
                     ("Organizadores de agujas e hilos", 160), ("Rotulado de guías y prensatelas", 150),
                     ("Tablas de parámetros estándar", 60), ("Tablero de programación", 120),
                     ("Checklists y formatos", 60), ("Capacitación en SMED", 192)],
        desglose=("Paro por producto (min/ciclo)", [("Brasier", 114.0, 41.5), ("Tanga", 85.0, 30.9), ("Conjunto", 148.0, 53.4)])),
    4: dict(
        corto="Six Sigma (alineación)", herramienta="Six Sigma DMAIC + guía de alineación de piezas",
        descripcion="Reducir los defectos de costura por posicionamiento y alineación de piezas.",
        indicador="Defectos por alineación", antes=15.0, despues=4.1, unidad="%",
        inversion=300.00, ahorro=872.00, beneficio=552.00, roi=1.84, pri="10.32 días*",
        costos=[("Costo de retrabajos", 1200.00, 328.00)],
        nota="Beneficio = 872 − 300 (inversión) − 20 (mantenimiento). *Unidad de PRI tal como figura en el Excel: revisar.",
        inv_detalle=[("Material para fabricar la guía", 120), ("Fabricación y mecanizado", 80),
                     ("Instalación y adaptación", 40), ("Capacitación del operario", 60)]),
    5: dict(
        corto="Jidoka (materiales)", herramienta="Jidoka + gestión visual de materiales no conformes",
        descripcion="Detectar y contener materiales no conformes antes de la confección.",
        indicador="Prendas defectuosas", antes=15.32, despues=10.34, unidad="%",
        inversion=600.00, ahorro=816.32, beneficio=96.32, roi=0.1605, pri=None,
        costos=[("Pérdida económica por defectos", 2419.47, 1603.15)],
        nota="Ahorro bruto S/ 816.32 − costos operativos S/ 120 = S/ 696.32; menos inversión = S/ 96.32.",
        inv_detalle=[("Tablero de gestión visual", 180), ("Fichas de inspección", 60), ("Etiquetas y tarjetas de lote", 48),
                     ("Instrumentos de medición", 90), ("Kit de prueba de elasticidad", 120),
                     ("Capacitación del personal", 64), ("Materiales de señalización", 38)],
        flujo=[-600, 288.16, 288.16, 288.16, 288.16, 288.16],
        desglose=("Defectos por producto (%)", [("Brasieres", 15.92, 10.89), ("Tangas", 22.86, 16.40), ("Conjuntos", 11.97, 7.62)])),
}
