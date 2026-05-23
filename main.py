import os
import json

from src.funciones_aqualimpia import (
    cargar_datos,
    preparar_datos,
    resumen_por_planta,
    intervalo_confianza_dbo_salida,
    evaluar_calidad_datos,
    exportar_reportes,
    guardar_resultados
)

RUTA_DATOS = "data/raw/dataset_set_A_aguas_residuales.xlsx"
CARPETA_SALIDA = "outputs"

os.makedirs(CARPETA_SALIDA, exist_ok=True)

df = cargar_datos(RUTA_DATOS)
df = preparar_datos(df)

resumen = resumen_por_planta(df)
calidad = evaluar_calidad_datos(df)
ic_dbo = intervalo_confianza_dbo_salida(df)

resultados = {
    "resumen_por_planta": resumen.to_dict(orient="records"),
    "calidad_datos": calidad,
    "intervalo_confianza_DBO_salida": ic_dbo
}

exportar_reportes(df, resumen, CARPETA_SALIDA)

with open(f"{CARPETA_SALIDA}/calidad_datos.json", "w", encoding="utf-8") as archivo:
    json.dump(calidad, archivo, indent=4, ensure_ascii=False)

guardar_resultados(resultados, f"{CARPETA_SALIDA}/resultados_aqualimpia.joblib")

print("Análisis ejecutado correctamente.")
print(resumen)