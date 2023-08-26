# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:23:27 2018

@author: Sila
"""

import matplotlib.pyplot as plt
import numpy as np

# Vi laver 50 tilfældige x-værdier og regner y-værdierne ud for en lige linje med stigning 3 og skæring 4.
# Vi tilføjer også en smule tilfældig støj til y-værdierne.
X = 2 * np.random.rand(50, 1)
y = 4 + 3 * X + np.random.randn(50, 1)

# Vi laver en ny x-værdi ved at tilføje en kolonne af 1'ere foran vores oprindelige x-værdier.
# Dette hjælper os med at udføre matematikken i næste trin.
# Vi beregner den bedste lige linje (regressionslinje) ved hjælp af ligningerne i matematikken ved at invertere en matrix.
X_b = np.c_[np.ones((50, 1)), X]
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Vi laver to nye x-værdier, 0 og 2, og tilføjer en kolonne af 1'ere foran dem, ligesom vi gjorde tidligere.
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]

# Vi bruger vores beregnede theta-værdier (stigning og skæring) til at forudsige y-værdierne
# for de nye x-værdier ved at udføre nogle matematiske beregninger.
y_predict = X_new_b.dot(theta_best)

plt.plot(X, y, "g.")
plt.axis([0, 2, 0, 15])
plt.plot(X_new, y_predict, "r-")

plt.plot()
plt.show()
