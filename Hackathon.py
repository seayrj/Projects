# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 12:21:26 2025

@author: rylan
"""

import matplotlib.pyplot as pyplot
x = [10, 20, 30, 40, 50, 60]
y = [5, 20, 18, 34, 30, 48]

fig, ax = pyplot.subplots()


ax.scatter(x, y)

pyplot.show()