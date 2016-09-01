#!/usr/bin/env python
"""
Usage: ./male_reps.py <metadat.csv of main files> <metadat.csv of replicates> <ctab_dir>  gender (m/f)
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_metamain = pd.read_csv(sys.argv[1])
df_metarep = pd.read_csv(sys.argv[2])
ctab_dir = sys.argv[3]



df_rep = df_metarep["sex"] == "male"
df_newrep = df_metarep[df_rep]

rep_val = []
for sample in df_newrep[df_rep]["sample"]:
    filename = ctab_dir + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    df_roi2 = df["t_name"]=="FBtr0331261"
    rep_val.append(df[df_roi2]["FPKM"].values)
male_Sxl = []
male_stage = [4,5,6,7]
df_roi = df_metamain["sex"] == "male"
df_new = df_metamain[df_roi]
for sample in df_metamain[df_roi]["sample"]:
    filename = ctab_dir + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    df_roi2 = df["t_name"] == "FBtr0331261"
    male_Sxl.append(df[df_roi2]["FPKM"].values)
xaxis = ["10","11","12","13","14A","14B","14C","14D"]

plt.figure()
plt.plot(male_Sxl)
plt.scatter(male_stage,rep_val)
plt.xticks(range(8), xaxis, rotation = "vertical")
plt.xlabel("Developmental Stage")
plt.ylabel("FPKM")
plt.title("Sxl Transcript Levels in Male Drosophila Embryos")
plt.savefig("scatterline.png")

plt.close()
    


    


