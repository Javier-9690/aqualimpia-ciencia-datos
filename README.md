# Proyecto de Ciencia de Datos - AquaLimpia S. A.

## 1. Descripción del caso

AquaLimpia S. A. es una empresa dedicada al tratamiento de aguas residuales urbanas e industriales. La empresa opera distintas plantas de tratamiento que reciben caudales variables y cargas contaminantes diferentes.

Durante el último trimestre se detectaron incumplimientos intermitentes en parámetros críticos de calidad del efluente tratado, especialmente en la demanda biológica de oxígeno (DBO) y en la eficiencia del tratamiento.

El objetivo del proyecto es desarrollar un análisis de datos reproducible que permita evaluar el desempeño de las plantas, identificar patrones relevantes y generar información útil para las áreas de Operaciones, Gestión Ambiental y Gerencia.

---

## 2. Objetivo general

Analizar el desempeño de las plantas de tratamiento de AquaLimpia S. A. mediante Python, reportes automatizados y un dashboard exploratorio, con el fin de apoyar la toma de decisiones operativas y ambientales.

---

## 3. Objetivos específicos

- Cargar y explorar el dataset oficial de aguas residuales.
- Calcular indicadores de eficiencia de remoción de DBO.
- Evaluar el cumplimiento normativo por planta.
- Identificar alertas operativas.
- Generar reportes diferenciados para Operaciones y Gestión Ambiental.
- Evaluar la calidad de los datos utilizados.
- Construir un dashboard exploratorio.
- Documentar el proyecto en un repositorio GitHub.

---

## 4. Preguntas de análisis

1. ¿Qué plantas presentan menor cumplimiento normativo?
2. ¿Cuál es el promedio de DBO de entrada y DBO de salida?
3. ¿Qué relación existe entre la DBO de entrada y la DBO de salida?
4. ¿Qué registros deben considerarse alertas operativas?
5. ¿Qué limitaciones presenta la calidad de los datos?
6. ¿Qué información requiere cada área de la empresa para tomar decisiones?

---

## 5. Dataset utilizado

El archivo utilizado es:

dataset_set_A_aguas_residuales.xlsx

El dataset contiene 200 registros y 10 variables relacionadas con el tratamiento de aguas residuales.

### Variables principales

| Variable | Descripción |
|---|---|
| fecha_registro | Fecha del registro operacional |
| planta | Planta de tratamiento |
| caudal_entrada_m3_d | Caudal de entrada en metros cúbicos por día |
| DBO_entrada_mg_L | DBO del agua residual de entrada |
| SST_entrada_mg_L | Sólidos suspendidos totales de entrada |
| pH_entrada | Nivel de pH del agua residual |
| energia_aeracion_kWh | Consumo de energía en aireación |
| lodos_generados_kg_d | Cantidad de lodos generados |
| DBO_salida_mg_L | DBO del efluente tratado |
| cumplimiento_norma | Estado de cumplimiento normativo |

---

## 6. Estructura del proyecto

```text
aqualimpia-ciencia-datos/
│
├── data/
│   └── raw/
│       └── dataset_set_A_aguas_residuales.xlsx
│
├── src/
│   ├── __init__.py
│   └── funciones_aqualimpia.py
│
├── dashboard/
│   └── dashboard.py
│
├── outputs/
│   ├── reporte_operaciones.xlsx
│   ├── reporte_gestion_ambiental.xlsx
│   ├── resumen_por_planta.csv
│   ├── calidad_datos.json
│   └── resultados_aqualimpia.joblib
│
├── notebooks/
│   └── analisis_aqualimpia.ipynb
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
