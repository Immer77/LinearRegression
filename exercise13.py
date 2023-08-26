# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 20:54:51 2018

@author: Sila
"""

# Python version
import numpy as np
import matplotlib.pyplot as plt


def cost(a, b, X, y):
    ### Evaluate half MSE (Mean square error)
    m = len(y)
    # Vores hypotese minus y for at finde hvor lang væk punktet er fra en eventuel linje.
    # Det er vores cost-funktion
    error = a + b * X - y
    # Bliver sat i anden for at gøre det positivt og dividere med længden for at hvis man havde en milliard punkter
    J = np.sum(error ** 2) / (2 * m)
    return J


# Først vil det bare have været mellem 0 og 1, men fordi vi gange med 2 får vi 100 x-værdier der ligger mellem 0 og 2
X = 2 * np.random.rand(100, 1)
print(X)

# y her er så lidt på samme måde, hvor vi tager og ganger x med 3 så det kan gå helt op til 6
# derefter plusser vi med 4 og 1 så det kan gå op til 11.
y = 4 + 3 * X + np.random.randn(100, 1)
print(y)

plt.plot(X, y, "b.")


# Så tager vi
ainterval = np.arange(1, 10, 0.005)
binterval = np.arange(0.5, 5, 0.01)

low = cost(0, 0, X, y)
bestatheta = 0
bestbtheta = 0

"""
Dette er to for-løkker, der gennemgår alle mulige kombinationer af værdier fra ainterval og binterval. 
For hver kombination beregnes kostnaden ved at bruge cost-funktionen, 
og hvis kostnaden er lavere end den tidligere laveste værdi (low), opdateres low, 
bestatheta og bestbtheta med de aktuelle værdier.
"""
for atheta in ainterval:
    for btheta in binterval:
        # print("xy: %f:%f:%f" % (atheta,btheta,cost(atheta,btheta, X, y)))
        if (cost(atheta, btheta, X, y) < low):
            low = cost(atheta, btheta, X, y)
            bestatheta = atheta
            bestbtheta = btheta

"""
Her udskrives de værdier af bestatheta og bestbtheta, 
som repræsenterer de optimale parametre (a og b) for den laveste kostnadsfunktion, 
hvilket betyder den bedste tilpasning af en lineær model til dataene.
"""
print("a and b: %f:%f" % (bestatheta, bestbtheta))


def myfunc(x):
    return bestbtheta * x + bestatheta

# Her laver jeg min egen plotlib for at se om det passer
nymodel = list(map(myfunc,X))
plt.plot(X, nymodel)
plt.show()