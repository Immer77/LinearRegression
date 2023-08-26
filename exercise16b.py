# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:23:27 2018

@author: Sila
"""

from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np


X = 2 * np.random.rand(500, 1)
y = 4 + 3 * X + np.random.randn(500, 1)

#Her bruger vi sklearns linearregression metode som laver udregningen for os for den.
lm = linear_model.LinearRegression()
# Modellen skal så fittes på x og y værdierne
model = lm.fit(X,y)

# Så plotter vi x og y ind på en akse
plt.plot(X,y, "g.")
# Vi sætter x-aksen til at være fra 0 -> 2 og y aksen fra 0 -> 15
plt.axis([0,2,0,15])

#fit function
# Ligner meget f(x) = bX + a
"""
f er bare et navn, vi giver til vores formel. Du kan tænke på f som en måde at beskrive en funktion.
lambda x: fortæller computeren, at vi opretter en lille anonym funktion, der tager en inputvariabel, som vi kalder x.
lm.coef_ repræsenterer hældningen (stigningen) på den lige linje, som vores maskine har lært.
*x betyder, at vi ganger denne hældning med inputvariablen x, som er vores x-værdier.
lm.intercept_ repræsenterer skæringen på y-aksen, som vores maskine har fundet.
Til sidst lægger vi disse to dele sammen for at få den forudsagte y-værdi (y_pred), 
som er det, vi vil bruge til at tegne den lige linje.
"""
f = lambda x: lm.coef_*x + lm.intercept_

plt.plot(X,f(X), c="red")

plt.plot()
plt.show()

