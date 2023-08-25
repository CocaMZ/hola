import pandas as pd
datos={
    "nombre":["Maria","Luis","Carmen"],
    "materias": ["Matematicas","Programacion", "Mercadotecnia"],
    "promedios":[80,90,100]
}

df_alumnos=pd.DataFrame(datos)
print(df_alumnos)

df_colesterol= pd.read_csv("https://raw.githubusercontent.com/asalber/"
                           "manual-python/master/datos/colesteroles.csv", sep=";", decimal=",")
#print(df_colesterol)
#print(df_colesterol.head())#sipones un numero dentro del parentesis te van a aparecer los datos que hayas indicado
#si en vex de head ponemos sample van a agarrar un dato de forma aleatoria y si poes un numero en el rentesis va  escoger aleatoriament
# e lo que hayas indicado

"""
print(df_colesterol.shape)#Imprime las dimensiones
print(df_colesterol.size)#cantidad de datos totales que hay
print(df_colesterol.columns)#lista de columnas, como se llaman
print(df_colesterol.dtypes)#Imprime el tipo de dato de las columnas
print(df_colesterol.index)#muestra todos los indices

"""

#print(df_colesterol.nombre)#solamente funciona si la columna no tiene espacios en blaco
#print(df_colesterol[["nombre", "edad","colesterol"]])#asi ya se pueden usar si tienes espacios en blanco

df_colesterol["colesterol"].plot(kind="")#ocupamos instalar libreria matplotlib

