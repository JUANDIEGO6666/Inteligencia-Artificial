import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creacion de objeto serie
s= pd.Series([2,4,6,8,10])
print(s)

# Creacion de objeto en serie inclinizado con un diccionario de python
altura={"santiago":180,"marcelo":172,"Luis":174,"Alejandra":160}
s= pd.Series(altura)
print(s)

"""
creacion de un objeto series inclinandolo con algunos de los elementos de un diccionario de python 
"""

altura={"santiago":180,"marcelo":172,"Luis":174,"Alejandra":160}
s= pd.Series(altura,index=["marcelo","Luis"])
print(s)

#creacion de un objeto serie iniciandolo con un escalar

s= pd.Series(34,["test1","test2","test3"])
print(s)

# Acceso a los elementos de un objeto series
# cada elemento de objetos series tiwnw un identificador unico
s=pd.Series([2,4,6,8], index=["num1","num2","num3","num4"])
print(s)
# acccediendo al tercer elemento del objeto
print(s["num3"])
# acceder por la posicion
print(s.iloc[2])
print(s.loc["num3"])
# acedoendo al segundo y tercer elemento por posicion
print(s.iloc[2:4])

# operaciones aritmeticas con series
#sumar
print(f"suma{np.sum(s)}")
print("suma",np.sum(s))

# Creación de un objeto series denominado temperaturas
temperaturas=pd.Series([4.4,5.1,6.1,6.2,6.1,6.1,5.2,4.7,4.1,3.9])
s=pd.Series(temperaturas,name="temperaturas")
print(s)
s.plot()
plt.show()

#creacion de un objeto

personas={
    "peso":pd.Series([90,80,70,60],["Santiago","Marcelo","Luis","Alejandra"]),
    "altura":pd.Series({"santiago":180,"marcelo":172,"Luis":174,"Alejandra":16}),
    "hijos":pd.Series([2,3],["Luis","Marcelo"])
}
df =pd.DataFrame(personas)
print(df)
df2=pd.DataFrame(
    personas,
    columns=["altura","peso",],
    index=["santiago","Luis","Marcelo"]

)
print(df2)
#Acceso a los elementos
print(df["peso"])
#combinar metodos
df3=(df["peso"]>=60) & (df["peso"]<80)
print(df3)

print(df.iloc[1:3])
#consulta avanzada
df4=df.query("altura >= 170 and peso >70")
print(df4)
#Acoplar un dataframe
df_copy =df.copy()
#Añadir una nueva columna
df_copy["cumpleaños"]=[1990,1878,1780,1994]
print(df_copy)
#Añadir columna calculada
df_copy["años"]=2025 - df_copy["cumpleaños"]
print(df_copy)
#Añadir una nueva columna creando un dataframe nuevo 
df_mod=df_copy.assign(mascotas=[1,3,0,0])
print(df_mod)
#Eliminar una columna
del df_mod["peso"]
print(df_mod)