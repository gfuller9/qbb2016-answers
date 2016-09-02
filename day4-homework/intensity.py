#!/usr/bin/env python

"""
usage: ./intensity.py <ctab file>
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.stats import gaussian_kde

df1 = pd.read_table(sys.argv[1])
data = df1["FPKM"].values

density = gaussian_kde(data)


xs = np.linspace(np.min(data), 100, 1000)


#x = numpy.arrange(0, 10000,100000)
#density.covariance_factor = lambda : .25
#density._compute_covariance()
plt.figure
plt.plot(xs,density(xs))
plt.title("Intensity Plot of SRR072893 FPKMs")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.savefig("intensity.png")
plt.close()
