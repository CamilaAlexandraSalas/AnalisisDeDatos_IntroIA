
# **Tarea de Numpy**

#!pip install numpy
import numpy as np

# Probando si si jala el numpy
my_arreglow = np.array([1, 2, 3, 4, 5])

print(my_arreglow)
print(np.mean(my_arreglow))

## Ejercicios de refuerzo

### **Ejercicio 1 - Crear un array de ceros:**
##Crea un array de tamaño (3, 4) lleno de ceros.

# Solución (:
arr_ceros = np.zeros((3, 4))
print(arr_ceros)

### **Ejercicio 2-  Suma de elementos:**
###Dado el array [1, 2, 3, 4, 5], calcula la suma de todos sus elementos usando NumPy.


# Solucion :)
arr = np.array([1, 2, 3, 4, 5])
print("Suma:", np.sum(arr))

### **Ejercicio 3 - Encontrar el máximo y mínimo:**
###Dado el array [10, 20, 30, 40, 50], encuentra el valor máximo y mínimo.

array = np.array([10, 20, 30, 40, 50])

# Solución:)
print("Valor máximo:", np.max(array))
print("Valor mínimo:", np.min(array))

### **Ejercicio 4 - Encontrar el máximo y mínimo:**
###Dado el array [10, 20, 30, 40, 50], encuentra el valor máximo y mínimo.

# Solución:)
array = np.array([10, 20, 30, 40, 50])
print("Valor máximo:", np.max(array))
print("Valor mínimo:", np.min(array))

### **Ejercicio 5 - Generar números aleatorios:**
###Genera un array de 5 números aleatorios entre 0 y 1.

# Solución:)
print("Resultado:",  np.random.rand(5))

### **Ejercicio 6 - Promedio de un array:**
###Dado el array [5, 10, 15, 20, 25], calcula su promedio usando NumPy.

#Solucion:)
array = np.array([5, 10, 15, 20, 25])
print("Promedio:", np.mean(array))

### **Ejercicio 7 - Concatenar dos arrays**
###Dados los arrays A = [1, 2, 3] y B = [4, 5, 6], concaténalos en un solo array.

#Solucion:)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Array concatenado:", np.concatenate((a, b)))

### **Ejercicio 8 - Reshape de un Array**
###Dado el array [1, 2, 3, 4, 5, 6], cámbialo a una matriz de 2x3.


#Solución:)
array = np.array([1, 2, 3, 4, 5, 6])
print("Reshape a 2x3:\n",array.reshape((2, 3)) )

### **Ejercicio 9 - Producto punto (dot product):**
###Dados dos arrays A = [1, 2, 3] y B = [4, 5, 6], calcula su producto punto

#Solución:)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Producto punto:", np.dot(a, b))

### **Ejercicio 10 - Reorganizar un array:**
###Dado el array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], conviértelo en una matriz (2, 5).

#Solución:)
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Reorganizar 2x5:\n",array.reshape((2, 5)) )

