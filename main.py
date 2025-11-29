import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Ver tipos de datos de las columnas
print(df.dtypes)

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])
# Establecer la columna 'Date' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# TODO: Crear funcion para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):
    celsius=kelvin-273.15
    return celsius
    

# TODO: Copiar el DataFrame original y nombralo df_celsius
df_celsius = df.copy()

# TODO: Convertir las temperaturas de cada ciudad de Kelvin a Celsius usando la funcion creada
df_celsius['San Diego'] = df_celsius['San Diego'].apply (kelvin_to_celsius)
df_celsius['Phoenix'] = df_celsius['Phoenix'].apply (kelvin_to_celsius)
df_celsius['Toronto'] = df_celsius['Toronto'].apply (kelvin_to_celsius)
# Analisis

# TODO: Imprime que día y hora se registró la temperatura mínima en Phoenix con el siguiente mensaje: "El día con la temperatura mínima en Phoenix fue: {fecha}"
min_temp_phoenix = df_celsius['Phoenix'].min().round(2)
fecha_min_phoenix = df_celsius['Phoenix'].idxmin()
print(f"El día con la temperatura mínima en Phoenix fue: {fecha_min_phoenix}")
# TODO: Imprime la temperatura mínima en Phoenix con el siguiente mensaje: "La temperatura mínima registrada en Phoenix fue de: ", temperatura, " °C""

print(f"La temperatura mínima registrada en Phoenix fue de: {min_temp_phoenix} °C")
# TODO: Imprime que día y hora se registró la temperatura máxima en Phoenix
temp_max_phoenix = df_celsius['Phoenix'].max().round(2)
fecha_max_temp_phoenix = df_celsius['Phoenix'].idxmax()
print(f"El día con la temperatura máxima en Phoenix fue: {fecha_max_temp_phoenix}")

# TODO: Imprime la temperatura máxima en Phoenix
print(f"La temperatura máxima registrada en Phoenix fue de: {temp_max_phoenix} °C")

# TODO: Imprime la temperatura promedio en Phoenix durante el año 2016
df_phoenix_2016 = df_celsius[df_celsius.index.year == 2016]
promedio_temp_phoenix_2016 = df_phoenix_2016['Phoenix'].mean().round(2)
print(f"La temperatura promedio durante 2016 en Phoenix fue de: {promedio_temp_phoenix_2016} °C")
# Graficar la temperatura de Phoenix durante el año 2016
plt.figure(figsize=(20, 10))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], label='Phoenix')
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV
df_celsius.to_csv("temperatura_celsius.csv")


