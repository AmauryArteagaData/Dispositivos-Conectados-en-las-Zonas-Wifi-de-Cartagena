#LIbrerias
import pandas as pd
import matplotlib.pyplot as plt
import os

#Ruta del dataset
BASE_DIR = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(BASE_DIR, "Dispositivos Conectados en las zonas WIFI de Cartagena.csv"))

#Resumen inicial
print(data.shape)
print(data.info())
print(data.head())

#Crear copia del dataset original se llamará data_limpio
data_limpio = data.copy()

#Limpieza de datos
#Normalizacion de datos
data_limpio["MES"] = data_limpio["MES"].str.lower().replace({
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

data_limpio["CORREGIMIENTO/BARRIO"] = data_limpio["CORREGIMIENTO/BARRIO"].str.lower() .replace({
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

data_limpio["ZONA WIFI"] = data_limpio["ZONA WIFI"].str.lower() .replace({  
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

print("\n")
#Conteo de las columnas categoricas y subniveles
cols_cat = ["AÑO", "MES", "CORREGIMIENTO/BARRIO", "ZONA WIFI" , "DISPOSITIVOS SIN CLASIFICAR", "SMARTPHONE", "TABLET", "PC"]
for col in cols_cat:
    print (f"Columna {col}: {data_limpio[col].nunique()} subniveles")

#Conversion de las Columnas a sus respectivos tipos de datos
#Convertir MES a numero con mapeo explicito (evita warnings de parsing)
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
data_limpio["MES"] = data_limpio["MES"].map(mes_map)

#Conversion de AÑO
data_limpio["AÑO"] = (
    data_limpio["AÑO"].astype(str).str.replace(r"\D", "",regex=True)
)
data_limpio["AÑO"] = pd.to_numeric(data_limpio["AÑO"], errors="coerce").astype("Int64")

#Conversion de SMARTPHONE
data_limpio["SMARTPHONE"] = (
    data_limpio["SMARTPHONE"].astype(str).str.replace(r"\D", "",regex=True)
)
data_limpio["SMARTPHONE"] = pd.to_numeric(data_limpio["SMARTPHONE"], errors="coerce").astype("Int64")

#Conversion de TABLET
data_limpio["TABLET"] = (
    data_limpio["TABLET"].astype(str).str.replace(r"\D", "",regex=True)
)
data_limpio["TABLET"] = pd.to_numeric(data_limpio["TABLET"], errors="coerce").astype("Int64")

#Conversion de PC
data_limpio["PC"] = (
    data_limpio["PC"].astype(str).str.replace(r"\D", "",regex=True)
)
data_limpio["PC"] = pd.to_numeric(data_limpio["PC"], errors="coerce").astype("Int64")

#Conversion de DISPOSITIVOS SIN CLASIFICAR
data_limpio["DISPOSITIVOS SIN CLASIFICAR"] = (
    data_limpio["DISPOSITIVOS SIN CLASIFICAR"].astype(str).str.replace(r"\D", "",regex=True)
)
data_limpio["DISPOSITIVOS SIN CLASIFICAR"] = pd.to_numeric(data_limpio["DISPOSITIVOS SIN CLASIFICAR"], errors="coerce").astype("Int64")

#Cuantos valores cero hay en cada columna
columnas_con_ceros = ["SMARTPHONE", "TABLET", "PC", "DISPOSITIVOS SIN CLASIFICAR"]
for col in columnas_con_ceros:
    print(f"Columna {col}: {data_limpio[col].value_counts().get(0, 0)} ceros")

print("\n")
#Eliminar los ceros de esas columnas 
data_limpio = data_limpio[data_limpio["SMARTPHONE"] != 0]
data_limpio = data_limpio[data_limpio["TABLET"] != 0]
data_limpio = data_limpio[data_limpio["PC"] != 0]
data_limpio = data_limpio[data_limpio["DISPOSITIVOS SIN CLASIFICAR"] != 0]
print(data_limpio)

#Guardamos el dataset limpio en uno nuevo Se llamará data_limpio_nuevo
data_limpio = data_limpio.copy()
data_limpio_nuevo = data_limpio.copy()
data_limpio_nuevo.to_csv(os.path.join(BASE_DIR, "Dispositivos Conectados en las zonas WIFI de Cartagena_limpio_nuevo.csv"), index=False)

#------------------------------------------------------------------------------------------------------------

print("\n")
#Creamos una nueva columna con el total de dispositivos
data_limpio_nuevo["TOTAL_DISPOSITIVOS"] = data_limpio_nuevo["SMARTPHONE"] + data_limpio_nuevo["TABLET"] + data_limpio_nuevo["PC"] + data_limpio_nuevo["DISPOSITIVOS SIN CLASIFICAR"]
total_dispositivos = data_limpio_nuevo["TOTAL_DISPOSITIVOS"].sum()
print("El total de dispositivos es: ",total_dispositivos)

print("\n")
print(data_limpio_nuevo)

print("\n")
#Calculamos la poblacion que no tiene wifi
poblacion_total_cartagena = 1059626
poblacion_no_wifi = poblacion_total_cartagena - total_dispositivos
print("La poblacion que no tiene wifi es: ",poblacion_no_wifi)

print("\n")
total_dispositivos = {
    "SMARTPHONE": data_limpio_nuevo["SMARTPHONE"].sum(),
    "TABLET": data_limpio_nuevo["TABLET"].sum(),
    "PC": data_limpio_nuevo["PC"].sum(),
    "DISPOSITIVOS SIN CLASIFICAR": data_limpio_nuevo["DISPOSITIVOS SIN CLASIFICAR"].sum()
}
data_limpio_nuevo_totales = pd.DataFrame(list(total_dispositivos.items()), columns=["Dispositivo", "Total"])
print(data_limpio_nuevo_totales)

#Dispositivo mas usado por MES y graficar
dispositivo_mas_usado = data_limpio_nuevo["TOTAL_DISPOSITIVOS"].max()
print("El dispositivo mas usado es: ",dispositivo_mas_usado)

ax = data_limpio_nuevo_totales.plot(
    kind="bar", 
    x="Dispositivo", 
    y="Total", 
    legend=False, 
    figsize=(8,5), 
    color="skyblue", 
    edgecolor="black"
)

plt.title("Dispositivos más usados en Cartagena (Zonas WiFi)")
plt.xlabel("Tipo de dispositivo")
plt.ylabel("Total de conexiones")
plt.xticks(rotation=45)
plt.grid(True, axis="y", linestyle="--", alpha=0.6)

# Agregar etiquetas con los valores encima de cada barra
for container in ax.containers:
    ax.bar_label(container, label_type="edge", padding=3, fontsize=10, color="black")
plt.show()

print("\n")
#Dispositivos por mes
dispositivos_por_mes = data_limpio_nuevo.groupby("MES")[["SMARTPHONE","TABLET","PC","DISPOSITIVOS SIN CLASIFICAR"]].sum().reset_index()
dispositivos_por_mes.plot(
    x="MES",
    y=["SMARTPHONE","TABLET","PC","DISPOSITIVOS SIN CLASIFICAR"],
    kind="bar",
    figsize=(10,6)
)
plt.title("Dispositivos usados por mes en Cartagena (Zonas WiFi)")
plt.xlabel("Mes (1=Enero ... 12=Diciembre)")
plt.ylabel("Total de dispositivos")
plt.xticks(rotation=0)
plt.legend(title="Tipo de dispositivo")
plt.grid(True)
plt.show()

print("\n")
#Barrios con mas dispositivos
barrios_con_dispositivos = data_limpio_nuevo.groupby("CORREGIMIENTO/BARRIO")["TOTAL_DISPOSITIVOS"].sum().reset_index()
barrios_con_dispositivos = barrios_con_dispositivos.sort_values(by="TOTAL_DISPOSITIVOS", ascending=False)
print(barrios_con_dispositivos)

barrios_con_dispositivos.plot(kind= "barh", x="CORREGIMIENTO/BARRIO", y="TOTAL_DISPOSITIVOS", legend=False, figsize=(8,5), color="blue", edgecolor="black")
plt.title("Barrios con mas dispositivos")
plt.xlabel("Total de dispositivos")
plt.ylabel("Barrio")
plt.grid(True)
plt.show()
