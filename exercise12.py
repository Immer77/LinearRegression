# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:54:51 2018

@author: Sila
"""

"""
Her importerer vi to biblioteker: 
matplotlib.pyplot bruges til at lave grafer og plots, 
mens numpy bruges til numeriske beregninger.
"""
import matplotlib.pyplot as plt
import numpy as np


"""
Her genererer vi en matrix X med 100 rækker og 1 kolonne, 
hvor hver værdi er en tilfældig værdi mellem 0 og 2 (fordi vi multiplicerer med 2). 
Dette repræsenterer x-værdierne for vores datapunkter. Vi udskriver X for at se de tilfældige x-værdier.
"""
X = 2 * np.random.rand(100, 1)
print(X)

"""
Her genererer vi en matrix y med de tilsvarende y-værdier til vores x-værdier. 
Vi opretter disse y-værdier ved at bruge en lineær ligning y = 4 + 3 * x + tilfældig støj. 
Støj tilføjes ved at bruge np.random.randn(100, 1), 
hvilket giver små tilfældige værdier til y-værdierne. Vi udskriver y for at se de genererede y-værdier.
"""
y = 4 + 3 * X + np.random.randn(100, 1)
print(y)

"""
Denne linje plotter vores datapunkter som blå prikker. 
X-værdierne er på x-aksen, og de tilsvarende y-værdier er på y-aksen.
"""
plt.plot(X, y, "b.")

# Fra 0 -> 2 på x-aksen og fra 0 -> 15 på y-aksen
plt.axis([0, 2, 0, 15])

plt.plot()
plt.show()
