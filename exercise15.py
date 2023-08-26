# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 18:05:18 2018

@author: Sila
"""

import matplotlib.pyplot as plt
import numpy as np

"""
Dette er en funktion kaldet linear_regression, der udfører en simpel lineær regression på givne data. 
Funktionen tager nogle inputparametre: X er en række af x-værdier, y er en række af tilsvarende y-værdier, 
theta0 og theta1 er de oprindelige værdier for hældningen og skæringen på linjen, 
epochs er antallet af træningsomgange, og learning_rate er hastigheden, hvormed justeringer foretages.
"""


def linear_regression(X, y, theta0=0, theta1=0, epochs=10000, learning_rate=0.0001):
     #Her regnes længden af y (antal datapunkter), og resultatet gemmes i variablen N.
     N = float(len(y))
     #Dette starter en for-løkke, der gentager træningsprocessen et visst antal gange (angivet af epochs).
     for i in range(epochs):
          #Her beregnes den forudsagte y-værdi (hypothesen) ved at multiplicere theta1 med X (x-værdierne)
          # og tilføje theta0 (skæringen).
          y_hypothesis = (theta1 * X) + theta0

          #Dette beregner omkostningen (fejl) mellem de faktiske y-værdier (y) og de forudsagte y-værdier (y_hypothesis).
          # Det tager kvadratet af forskellen mellem hver faktisk og forudsagt y-værdi,
          # summerer dem op og dividerer med antallet af datapunkter (N).
          cost = sum([data ** 2 for data in (y - y_hypothesis)]) / N

          #Her beregnes gradienten for justering af theta1 og theta0 ved at tage afledningen af omkostningsfunktionen.
          # Gradienten hjælper med at finde den retning og størrelse, hvormed parametrene skal justeres for at reducere fejlen.
          theta1_gradient = -(2 / N) * sum(X * (y - y_hypothesis))
          theta0_gradient = -(2 / N) * sum(y - y_hypothesis)

          #Her foretages justering af parametrene theta0 og theta1
          # ved at trække fra et lille produkt af learning_rate og den tilsvarende gradient.
          # Dette hjælper med at opdatere parametrene i retning af lavere omkostninger.
          theta0 = theta0 - (learning_rate * theta0_gradient)
          theta1 = theta1 - (learning_rate * theta1_gradient)

     return theta0, theta1, cost


X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

theta0, theta1, cost = linear_regression(X, y, 0, 0, 1000, 0.01)

plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])

# lets plot that line:
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot([theta0, theta1])

plt.plot(X_new, y_predict, "g-")
