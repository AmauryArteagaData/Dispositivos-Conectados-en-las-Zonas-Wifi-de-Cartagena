#LIBRERIAS
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


#RUTA DATASET
data = pd.read_csv("Dispositivos Conectadosn en las zonas WIFI de Cartagena.csv")

# Resumen inicial
print(f"Dataset shape: {data.shape}")

#NORMALIZACION DE DATOS
data["MES"] = data["MES"].str.lower().replace({
    "enero": "Enero",
    "febrero": "Febrero",
    "marzo": "Marzo",
    "abril": "Abril",
    "mayo": "Mayo",
    "junio": "Junio",
    "julio": "Julio",
    "agosto": "Agosto",
    "septiembre": "Septiembre",
    "octubre": "Octubre",
    "noviembre": "Noviembre",
    "diciembre": "Diciembre",
})

data["CORREGIMIENTO/BARRIO"] = data["CORREGIMIENTO/BARRIO"].str.lower()
data["CORREGIMIENTO/BARRIO"] = data["CORREGIMIENTO/BARRIO"].replace({
    "tierra bomba": "Tierra Bomba",
    "ternera": "Ternera",
    "santa ana": "Santa Ana",
    "san francisco": "San Francisco",
    "punta canoa": "Punta Canoa",
    "pontezuela": "Pontezuela",
    "nuevo paraiso": "Nuevo Paraiso",
    "manga": "Manga",
    "los jardines": "Los Jardines",
    "las palmeras": "Las Palmeras",
    "la boquilla": "La Boquilla",
    "fredonia": "Fredonia",
    "el socorro": "El Socorro",
    "el pozon": "El Pozon",
    "el centro": "El Centro",
    "el bosque": "El Bosque",
    "colombiaton": "Colombiaton",
    "ciudadela la paz": "Ciudadela La Paz",
    "ciudadela 2000": "Ciudadela 2000",
    "ciudad del bicentenario": "Ciudad del Bicentenario",
    "centro": "Centro",
    "campestre": "Campestre",
    "bocagrande": "Boca Grande",
    "blas de lezo": "Blas de Lezo",
    "bicentenario": "Bicentenario",
    "bayunca": "Bayunca",
    "barú": "Barú",
    "arroyo grande": "Arroyo Grande",
    "arroyo de piedra": "Arroyo de Piedra",
    "la boquilla": "La Boquilla",
    "nuevo paraiso": "Nuevo Paraiso",
    "san francisco": "San Francisco",
    "bruselas": "Bruselas"
    })

data["ZONA WIFI"] = data["ZONA WIFI"].str.lower()
data["ZONA WIFI"] = data["ZONA WIFI"].replace({
    "zona san fernando la florida": "San Fernando La Florida",
    "zona bruselas": "Zona Bruselas",
    "zona tierra bomba": "Zona Tierra Bomba",
    "zona punta canoa": "Zona Punta Canoa",
    "zona plaza de la aduana": "Zona Plaza de la Aduana",
    "zona patinodromo el campestre": "Zona Patinodromo El Campestre",
    "zona san francisco": "Zona San Francisco",
    "zona parque roman": "Zona Parque Roman",
    "zona jorge artel": "Zona Jorg Artel",
    "zona inspeccion de policia santa ana": "Zona Inspeccion de Policia Santa Ana",
    "zona inspeccion de policia pontezuela": "Zona Inspeccion de Policia Pontezuela",
    "zona inspeccion de policia ternera": "Zona Inspeccion de Policia Ternera",
    "zona inspeccion de policia las palmeras": "Zona Inspeccion de Policia Las Palmeras",
    "zona inspeccion de policia boca grande": "Zona Inspeccion de Policia Boca Grande",
    "zona inspeccion de policia ciudadela 2000": "Zona Inspeccion de Policia Ciudadela 2000",
    "zona inspeccion de policia bosque": "Zona Inspeccion de Policia Bosque",
    "zona inspeccion de policia blaz de lezo": "Zona Inspeccion de Policia Blaz de Lezo",
    "zona inspeccion de policia barú": "Zona Inspeccion de Policia Barú",
    "zona inspeccion de policia arroyo grande": "Zona Inspeccion de Policia Arroyo Grande",
    "zona inspeccion de policia arroyo de piedra": "Zona Inspeccion de Policia Arroyo de Piedra",
    "zona inspeccion de policia el pozon": "Zona Inspeccion de Policia El Pozon",
    "zona inspeccion de policia nuevo paraiso": "Zona Inspeccion de Policia Nuevo Paraiso",
    "zona colegio fredonia": "Zona Colegio Fredonia",
    "zona colegio la paz": "Zona Colegio La Paz",
    "zona biblioteca pontezuela": "Zona Biblioteca Pontezuela",
    "zona biblioteca bayunca": "Zona Biblioteca Bayunca",
    "zona biblioteca colombiaton": "Zona Biblioteca Colombiaton",
    "zona biblioteca la boquilla": "Zona Biblioteca La Boquilla",
    "zona biblioteca bicentenario": "Zona Biblioteca Bicentenario"
    })

print("Primeras filas (vista rápida):")
print(data.head(3))
print("\n")

#CONTEO DE LAS COLUMNAS CATEGORICAS Y SUBNIVELES. SI UNA COLUMNA TIENE 1 SUBNIVEL, ESA COLUMNA NO APORTA INFORMACION REELEVANTE
cols_cat = ["AÑO", "MES", "CORREGIMIENTO/BARRIO", "ZONA WIFI" , "DISPOSITIVOS SIN CLASIFICAR", "SMARTPHONE", "TABLET", "PC"]
for col in cols_cat:
    print (f"Columna {col}: {data[col].nunique()} subniveles")

print("\n")

# CONVERTIR MES A NÚMERO CON MAPE0 EXPLÍCITO (evita warnings de parsing)
mes_map = {
    "Enero": 1,
    "Febrero": 2,
    "Marzo": 3,
    "Abril": 4,
    "Mayo": 5,
    "Junio": 6,
    "Julio": 7,
    "Agosto": 8,
    "Septiembre": 9,
    "Octubre": 10,
    "Noviembre": 11,
    "Diciembre": 12,
}
data["MES"] = data["MES"].map(mes_map)

# LIMPIAR Y CONVERTIR AÑO A INT (el dataset trae valores como "2.024")
data["AÑO"] = (
    data["AÑO"].astype(str).str.replace(r"\D", "",regex=True)
)
data["AÑO"] = pd.to_numeric(data["AÑO"], errors="coerce").astype("Int64")

# LIMPIAR Y CONVERTIR SMARTPHONE A NUMÉRICO
data["SMARTPHONE"] = (
    data["SMARTPHONE"].astype(str)
    .str.replace(r"\D", "", regex=True)
    .replace("", pd.NA)
)
data["SMARTPHONE"] = pd.to_numeric(data["SMARTPHONE"], errors="coerce").astype("Int64")

# LIMPIAR Y CONVERTIR TABLET y PC A NUMÉRICO
data["TABLET"] = (
    data["TABLET"].astype(str)
    .str.replace(r"\D", "", regex=True)
    .replace("", pd.NA)
)
data["TABLET"] = pd.to_numeric(data["TABLET"], errors="coerce").astype("Int64")
data["PC"] = (
    data["PC"].astype(str)
    .str.replace(r"\D", "", regex=True)
    .replace("", pd.NA)
)
data["PC"] = pd.to_numeric(data["PC"], errors="coerce").astype("Int64")

# CÁLCULO DE OUTLIERS PARA SMARTPHONE (método IQR)
data["SMARTPHONE"] = data["SMARTPHONE"].astype("Int64")
Q1 = data["SMARTPHONE"].dropna().quantile(0.25)
Q3 = data["SMARTPHONE"].dropna().quantile(0.75)
IQR = Q3 - Q1

limite_superior = Q3 + 1.5 * IQR
limite_inferior = Q1 - 1.5 * IQR

outliers = data[
    (data["SMARTPHONE"].notna()) &
    ((data["SMARTPHONE"] < limite_inferior) | (data["SMARTPHONE"] > limite_superior))
]
print(f"Outliers SMARTPHONE: {len(outliers)} registros")

# Filtrar solo los valores normales
valores_normales = data[(data["SMARTPHONE"] >= limite_inferior) & (data["SMARTPHONE"] <= limite_superior)]

# Calcular la media de los valores válidos
media_sin_outliers = valores_normales["SMARTPHONE"].mean()
print("Media de SMARTPHONE sin outliers:", media_sin_outliers)
print("\n")

# Crear una copia para no modificar el original
data_limpio = data.copy()

# Reemplazar valores fuera de los límites por la media
data_limpio.loc[(data_limpio["SMARTPHONE"] < limite_inferior) | (data_limpio["SMARTPHONE"] > limite_superior), "SMARTPHONE"] = int(media_sin_outliers)

## Verificar cambios (vista rápida)
print(data_limpio.head(3))
print("\n")

# Reemplazar ceros por la media de cada columna existente (sobre data_limpio)
columnas_con_ceros = ["SMARTPHONE", "TABLET", "PC", "DISPOSITIVOS SIN CLASIFICAR"]
for col in columnas_con_ceros:
    if col in data_limpio.columns:
        media_col = data_limpio.loc[data_limpio[col].notna() & (data_limpio[col] != 0), col].mean()
        if pd.notna(media_col):
            data_limpio.loc[data_limpio[col] == 0, col] = int(round(media_col))

# Verificación rápida: conteo de ceros restantes por columna imputada
for col in columnas_con_ceros:
    if col in data_limpio.columns:
        print(f"Ceros restantes en {col}: {(data_limpio[col] == 0).sum()}")

print("\n")

# Guardar el DataFrame limpio en un nuevo archivo CSV
data_limpio.to_csv("Dispositivos Conectadosn en las zonas WIFI de Cartagena_limpio.csv", index=False)

# REALIZAR LAS 3 MEDIDAS DE TENDENCIA (MEDIA, MEDIANA, MODA)
print("Media de SMARTPHONE:", data_limpio["SMARTPHONE"].mean())
print("Mediana de SMARTPHONE:", data_limpio["SMARTPHONE"].median())
print("Moda de SMARTPHONE:", data_limpio["SMARTPHONE"].mode())

print("\n")

print("Media de DISPOSITIVOS SIN CLASIFICAR:", data_limpio["DISPOSITIVOS SIN CLASIFICAR"].mean())
print("Mediana de DISPOSITIVOS SIN CLASIFICAR:", data_limpio["DISPOSITIVOS SIN CLASIFICAR"].median())
print("Moda de DISPOSITIVOS SIN CLASIFICAR:", data_limpio["DISPOSITIVOS SIN CLASIFICAR"].mode())

print("\n")

print("Media de TABLET:", data_limpio["TABLET"].mean())
print("Mediana de TABLET:", data_limpio["TABLET"].median())
print("Moda de TABLET:", data_limpio["TABLET"].mode())

print("\n")

print("Media de PC:", data_limpio["PC"].mean())
print("Mediana de PC:", data_limpio["PC"].median())
print("Moda de PC:", data_limpio["PC"].mode())

# Las columnas ya fueron convertidas a numéricas anteriormente; no es necesario reconvertir aquí

#CREAR COLUMNA TOTAL DE DISPOSITIVOS
data_limpio["TOTAL_DISPOSITIVOS"] = data_limpio["SMARTPHONE"] + data_limpio["TABLET"] + data_limpio["PC"] + data_limpio["DISPOSITIVOS SIN CLASIFICAR"]

print("\n")

#AGRUPO POR CORREGIMIENTO/BARRIO Y SUMO LOS VALORES DE TOTAL_DISPOSITIVOS
trafico_barrios = data_limpio.groupby("CORREGIMIENTO/BARRIO")["TOTAL_DISPOSITIVOS"].sum().reset_index()

#ORDENAR DE MAYOR A MENOR
trafico_barrios = trafico_barrios.sort_values(by="TOTAL_DISPOSITIVOS", ascending=False)

#IMPRIMIR LOS 10 PRIMEROS CON VISUALIZACION
print(trafico_barrios.head(5))
plt.figure(figsize=(12,6))
plt.bar(trafico_barrios["CORREGIMIENTO/BARRIO"].head(5), trafico_barrios["TOTAL_DISPOSITIVOS"].head(5))
plt.xticks(rotation=45, ha="right")
plt.title("Top 5 barrios con mayor volumen de conexión en dispositivos")
plt.xlabel("Barrio / Corregimiento")
plt.ylabel("Total de dispositivos conectados")
plt.show()

print("\n")

#IMPRIMIR LOS 10 PRIMEROS DISPOSITIVOS MAS USADOSCON VISUALIZACION
totales_dispositivos = {
    "SMARTPHONE": data_limpio["SMARTPHONE"].sum(),
    "TABLET": data_limpio["TABLET"].sum(),
    "PC": data_limpio["PC"].sum(),
    "DISPOSITIVOS SIN CLASIFICAR": data_limpio["DISPOSITIVOS SIN CLASIFICAR"].sum()
}
print("Uso total por tipo de dispositivo")
print(totales_dispositivos)
plt.figure(figsize=(12,6))
plt.bar(totales_dispositivos.keys(), totales_dispositivos.values())
plt.xlabel("Tipo de dispositivo")
plt.ylabel("Total de dispositivos conectados")
plt.show()

print("\n")

# MES QUE PRESENTA EL MAYOR PICO DE USO DE DISPOSITIVOS
uso_mensual = (
    data_limpio.groupby("MES", as_index=False)["TOTAL_DISPOSITIVOS"].sum()
    .sort_values("MES")
)

plt.figure(figsize=(12,6))
plt.bar(uso_mensual["MES"], uso_mensual["TOTAL_DISPOSITIVOS"])
plt.xlabel("Mes")
plt.ylabel("Total de dispositivos conectados")
plt.show()