# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:23:27 2018

@author: Sila
"""

# Vi importerer nogle værktøjer: matplotlib.pyplot bruges til at lave grafer,
# og numpy bruges til numeriske beregninger.
import matplotlib.pyplot as plt
import numpy as np

# Her importeres to klasser fra scikit-learn-biblioteket. LinearRegression bruges til at lave en lineær regressionsmodel,
# og PolynomialFeatures bruges til at omdanne vores data til polynomiale funktioner
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Vi genererer 100 tilfældige x-værdier mellem -3 og 3.
# Derefter beregner vi tilfældige y-værdier ved at bruge en polynomisk funktion (0.5 * X * X + X + 2),
# og vi tilføjer lidt tilfældig støj for at gøre det realistisk.
X = 6 * np.random.rand(100, 1) - 3
y = 0.5 * X**3 + 0.5 * X**2 + X + 2 + np.random.randn(100, 1)

# Vi tegner vores datapunkter (x-værdier mod y-værdier) på en graf som grønne prikker.
# Vi indstiller også intervallet på x-aksen fra -3 til 3 og intervallet på y-aksen fra 0 til 10.
plt.plot(X, y, "g.")
plt.axis([-3, 3, 0, 10])

# Vi opretter en PolynomialFeatures-instans med en grad på 2,
# hvilket betyder, at vi vil oprette polynomiale funktioner op til anden grad.
# Vi omdanner vores x-værdier ved at bruge denne instans, så de bliver polynomiale.
poly_features = PolynomialFeatures(3, include_bias=False)
X_poly = poly_features.fit_transform(X)

# Vi opretter en lineær regressionsmodel og træner den ved at bruge de polynomiale x-værdier og de faktiske y-værdier.
lm = LinearRegression()
lm.fit(X_poly, y)

# fit function
#Vi opretter en funktion f, der repræsenterer den tilpassede polynomiale model.
# Vi bruger koefficienterne og skæringen fra den trænede regressionsmodel til at beregne y-værdierne for vores x-værdier.
# Derefter tegner vi denne funktion som blå linje sammen med vores datapunkter på grafen.
f = lambda x: lm.coef_[0][2] * x * x * x + lm.coef_[0][1] * x * x + lm.coef_[0][0] * x + lm.intercept_
plt.plot(X, f(X), "b.")

plt.show()
