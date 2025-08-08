import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset ficticio
datos_estudiantes = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}

df = pd.DataFrame(datos_estudiantes)
print(df)


#Crea una serie con los nombres y altura de los esrudiantes

df2 =pd.DataFrame(datos_estudiantes,
    columns=["altura"],
    index=["Ana", "Carlos", "Daniela", "Eduardo", "Fenanda"]
)
print(df2)

#Accede al promedio de calificacion de carlos de 3 formas diferentes
print("Segundo punto")
calificacion_carlos=pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana","Carlos","Daniela","Eduardo","Fernanda"])
print(calificacion_carlos)

#forma 1 (acceder al elemnto del objeto)
print(calificacion_carlos["Carlos"])

#forma 2 (acceder a posicion)
print(calificacion_carlos.iloc[2])
print(calificacion_carlos.loc["Carlos"])

#forma 3 (aceder al segundo y tecer elmento por posicion)
print(calificacion_carlos.iloc[2:2])

#filtre a los estudiantes con un promedio mayor o igual a 4.0
print("Tercer_punto")
Proemdio_mayor =df.query("promedio>=4.0")
print(Proemdio_mayor)

#Agrega una nueva columna que indique si el estudiante es mayor de edad
print("Cuarto_punto")
datos_estudiantes2 = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "MayoriaDeEdad":pd.Series(["menor", "mayor", "menor", "mayor", "mayor"], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
}
ME=(datos_estudiantes2["edad"]>=18)
df3= pd.DataFrame(datos_estudiantes2)
print(df3)
print(ME)

#Agrega un acolumna con le año de nacimiento (suponiendo que estamos en 2025)
print("Quinto punto")
AN=((datos_estudiantes2["edad"]-2025)*-1)
print(AN)

#visualiza los promedios de los estudiantes en un grafico
print("septimo punto")
df["promedio"].plot(kind="bar", title="Promedio de estudiantes")
plt.xlabel("Estudiante")
plt.ylabel("Nota promedio")
plt.show()

#filtra los estudiantes con altura entre 165 y 175 cm
print("octavo punto")
df
Alturacm=()

#Copia el dataframe y elimina la columna "peso"

#Crea un nuevo Dataframe con solo 3 columnas: nombew, edad y año de nacimiento
