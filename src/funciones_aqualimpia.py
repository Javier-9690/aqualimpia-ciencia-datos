import pandas as pd
import numpy as np
from scipy import stats
from joblib import dump


def cargar_datos(ruta):
    return pd.read_excel(ruta)


def preparar_datos(df):
    df = df.copy()
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"])

    df["eficiencia_DBO_pct"] = (
        (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"])
        / df["DBO_entrada_mg_L"]
    ) * 100

    df["alerta_operativa"] = np.where(
        (df["cumplimiento_norma"] == 0) |
        (df["eficiencia_DBO_pct"] < 85),
        "Alerta",
        "Normal"
    )

    return df


def resumen_por_planta(df):
    return df.groupby("planta").agg(
        registros=("planta", "count"),
        caudal_promedio=("caudal_entrada_m3_d", "mean"),
        DBO_entrada_promedio=("DBO_entrada_mg_L", "mean"),
        DBO_salida_promedio=("DBO_salida_mg_L", "mean"),
        eficiencia_promedio=("eficiencia_DBO_pct", "mean"),
        cumplimiento_pct=("cumplimiento_norma", "mean"),
        energia_promedio=("energia_aeracion_kWh", "mean"),
        lodos_promedio=("lodos_generados_kg_d", "mean")
    ).reset_index()


def intervalo_confianza_dbo_salida(df):
    media = df["DBO_salida_mg_L"].mean()
    error = stats.sem(df["DBO_salida_mg_L"])

    intervalo = stats.t.interval(
        confidence=0.95,
        df=len(df) - 1,
        loc=media,
        scale=error
    )

    return {
        "media_DBO_salida": media,
        "IC95_inferior": intervalo[0],
        "IC95_superior": intervalo[1]
    }


def evaluar_calidad_datos(df):
    calidad = {
        "filas": len(df),
        "columnas": len(df.columns),
        "valores_nulos": df.isnull().sum().to_dict(),
        "duplicados": int(df.duplicated().sum()),
        "registros_DBO_menor_igual_30_incumplen": int(
            ((df["DBO_salida_mg_L"] <= 30) &
             (df["cumplimiento_norma"] == 0)).sum()
        )
    }

    return calidad


def exportar_reportes(df, resumen, carpeta_salida):
    operaciones = df[[
        "fecha_registro",
        "planta",
        "caudal_entrada_m3_d",
        "DBO_entrada_mg_L",
        "DBO_salida_mg_L",
        "energia_aeracion_kWh",
        "lodos_generados_kg_d",
        "eficiencia_DBO_pct",
        "alerta_operativa"
    ]]

    gestion_ambiental = df[[
        "fecha_registro",
        "planta",
        "DBO_salida_mg_L",
        "cumplimiento_norma",
        "alerta_operativa"
    ]]

    operaciones.to_excel(f"{carpeta_salida}/reporte_operaciones.xlsx", index=False)
    gestion_ambiental.to_excel(f"{carpeta_salida}/reporte_gestion_ambiental.xlsx", index=False)
    resumen.to_csv(f"{carpeta_salida}/resumen_por_planta.csv", index=False)


def guardar_resultados(objeto, ruta):
    dump(objeto, ruta)