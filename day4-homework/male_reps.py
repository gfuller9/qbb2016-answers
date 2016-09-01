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

df_roi1 = df_metamain["sex"] == "female"
df_new1 = df_metamain[df_roi1]

rep_val = []
for sample in df_newrep[df_rep]["sample"]:
    filename = ctab_dir + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    df_roi2 = df["t_name"]=="FBtr0331261"
    rep_val.append(df[df_roi2]["FPKM"].values)
male_Sxl = []
fem_Sxl = []
male_stage = [4,5,6,7]
df_roi = df_metamain["sex"] == "male"
df_new = df_metamain[df_roi]
for sample in df_metamain[df_roi]["sample"]:
    filename = ctab_dir + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    df_roi2 = df["t_name"] == "FBtr0331261"
    male_Sxl.append(df[df_roi2]["FPKM"].values)
xaxis = ["10","11","12","13","14A","14B","14C","14D"]


for sample in df_metamain[df_roi1]["sample"]:
    #this defines the path to the files which are stored in a directory.  Sample name comes from metadata file, so we add that and this will call the t_data.ctab file for that sample
    filename = ctab_dir + sample + "/t_data.ctab"
    #use panda to open the ctab table
    df = pd.read_table(filename)
    #pull out the transcripts associated with SXL
    df_roi2 = df["t_name"] == "FBtr0331261"
    #now we will have dataframes for the transcript
    #now we append this to the list for all files corresponding female
    #fem_sxl.append(df[df_roi2]["FPKM"])
    #NOTE THAT YOU MUST USE .values TO EXTRACT THE VALUES FROM THE SERIES
    fem_Sxl.append(df[df_roi2]["FPKM"].values)

df_rep = df_metarep["sex"] == "female"
df_newrep = df_metarep[df_rep]
rep_val2 = []
for sample in df_newrep[df_rep]["sample"]:
    filename = ctab_dir + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    df_roi2 = df["t_name"]=="FBtr0331261"
    rep_val2.append(df[df_roi2]["FPKM"].values)

print fem_Sxl

plt.figure()
plt.plot(male_Sxl)
plt.plot(fem_Sxl,color = 'red')
plt.scatter(male_stage,rep_val)
plt.scatter(male_stage,rep_val2,color = 'red')
plt.xticks(range(8), xaxis, rotation = "vertical")
plt.xlabel("Developmental Stage")
plt.ylabel("FPKM")
plt.title("Sxl Transcript Levels in Male Drosophila Embryos")
plt.savefig("Sxl_male.png")

plt.close()
    


    


