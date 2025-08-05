# Introducción Pandas
Python 3.13.5

## Librerias
```
import pandas as pd
s = pd.series ([2,4,6,8,10])
print(s)
```

## creacion de objetos serie
```
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
```

# Creacion de objeto en serie inclinizado con un diccionario de python
```
altura={"santiago":180,"marcelo":172;"Luis":174;"Alejandra":160}
s= pd.Series(altura)
print(s)
```
# Acceso a los elementos de un objeto series
# cada elemento de objetos series tiwnw un identificador unico
```
s=pd.Series([2,4,6,8], index=["num1","num2","num3","num4"])
print(s)
```
# acccediendo al tercer elemento del objeto
```
print(s["num3"])
```
# acceder por la posicion
```
print(s.iloc[2])
print(s.loc["num3"])
```
# acedoendo al segundo y tercer elemento por posicion
```
print(s.iloc[2:4])
````