#Librerias
#Libreria de la interfaz grafica
import tkinter as tk
from tkinter import *
#Libreria de calculos matematicos y el analisis de datos
import numpy as np
#Libreria para la creacion  de graficas en 2D
import matplotlib.pyplot as plt
# Libreria de las tablas
from tabulate import tabulate
# Libreria para formulas matematicas
from math import e

#Configuracion de la ventana
window = tk.Tk()
window.geometry("600x500")


text_widget = Text(window,height=40, width=40)
text_widget.pack()


window.title("Metodo del trapecio")

def trapecio(a, b, n):
    # Crear una lista para almacenar los valores
    tabla_resultados = []
    #la funcion de fx 
    fx = lambda x: (e**x**2)
    #fx = lambda x: np.sqrt(x)
    # le asignamos el valor n a la variable tramos
    tramos = n
    
    muestras =tramos+1
    #el valor de la suma de los trapecios
    suma = 0
    #xi valor e donde incia los rectangulos
    xi=a
    #formuala de delta x
    h= (b-a)/tramos
    text_widget.insert(END, f"Valor de Delta x: {h:.6f}\n")
    #ciclo for para sacar los valors x y y de la grafica
    for i in range(0,tramos, 1):
        Atrapecio = h*(fx(xi)+fx(xi+h))/2
        suma = suma+Atrapecio
        xi= xi+h
        fi = fx(xi)
        tabla_resultados.append([i+1, xi,fi])
    integral = suma
    
    # Mostrar la tabla utilizando tabulate
    headers = ["i", "Valor xi", "Valor y"]
    result_table = tabulate(tabla_resultados, headers=headers, tablefmt="grid")
    text_widget.insert(END, result_table)
    text_widget.insert(END, f"\nIntegral: {integral:.6f}\n")
    #grafica
    #marcar puntos de la grafica
    xi = np.linspace(a,b, muestras)
    fi = fx(xi)
    #codigo de la lineas de las grafias y su grosor
    muestraslineas = muestras*10
    xk= np.linspace(a,b, muestras)
    fk = fx(xk)
    #codigo para las lineas de los trapecios
    plt.plot(xi, fi, 'ro')
    plt.plot(xk,fk)
    #codigo de los colores adentro del trapecio
    plt.fill_between(xi,0,fi, color='g')
    for i in range(0,muestras, 1):
        plt.axvline(xi[i], color= "w")
    plt.show()
  


    #valores del metodo
trapecio(a=0, b=1, n=5)

#terminamos la funcion de tkinter
window.mainloop()


