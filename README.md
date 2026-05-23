# Proyecto de Ciencia de Datos - AquaLimpia S. A.

## 1. Descripción del caso

AquaLimpia S. A. opera plantas de tratamiento de aguas residuales urbanas e industriales. Durante el último trimestre se detectaron incumplimientos intermitentes en parámetros críticos, especialmente DBO de salida y eficiencia del tratamiento.

## 2. Objetivo general

Analizar el desempeño de las plantas de tratamiento para identificar patrones de incumplimiento, evaluar eficiencia operacional y apoyar la toma de decisiones de las áreas de Operaciones y Gestión Ambiental.

## 3. Datos utilizados

Archivo: `dataset_set_A_aguas_residuales.xlsx`

Variables principales:

- fecha_registro
- planta
- caudal_entrada_m3_d
- DBO_entrada_mg_L
- SST_entrada_mg_L
- pH_entrada
- energia_aeracion_kWh
- lodos_generados_kg_d
- DBO_salida_mg_L
- cumplimiento_norma

## 4. Metodología

1. Carga del dataset.
2. Limpieza y validación de datos.
3. Cálculo de eficiencia de remoción de DBO.
4. Análisis exploratorio por planta.
5. Evaluación de calidad de datos.
6. Generación de reportes Excel.
7. Construcción de dashboard.
8. Publicación en GitHub.

## 5. Principales resultados

- Se analizaron 200 registros.
- El cumplimiento global fue de 22,5 %.
- La Planta Norte presentó el menor cumplimiento normativo.
- La DBO de entrada mostró una correlación positiva alta con la DBO de salida.
- Se detectaron posibles inconsistencias entre DBO de salida y la variable cumplimiento_norma.

## 6. Limitaciones

- El dataset no incluye variables climáticas, mantenciones, fallas operacionales ni dosificación química.
- La variable cumplimiento_norma puede depender de criterios adicionales no incluidos.
- El análisis es exploratorio y no causal.

## 7. Ejecución

```bash
pip install -r requirements.txt
python main.py
streamlit run dashboard/app_dashboard.py