#!/usr/bin/env python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

df_roi = (df["gene_name"] == "Sxl") & (df["FPKM"]>0)

df2_roi = (df["gene_name"]=="Sxl") & (df["FPKM"]>0)



df_sx=df[df_roi]
dfp= np.log(df_sx["FPKM"])
df2_sx = df2[df2_roi]
df2p = np.log(df2_sx["FPKM"])
#df_for_plot = pd.dataframe(data,index=index, columns = columns)
#df_for_plot['SRR072893'] = df_sx["SRR072893"]
#df_for_plot['SRR072915']=df2_sx["SRR072915"]

dfplot = (dfp, df2p)
#fpkm_log = np.log(df_sx["FPKM"])
#of_combo = (df1,df2)
print df_sx
descrip = df_sx.describe()
plt.figure()
#plott = dfplot.boxplot(return_type = 'dict')
plt.boxplot(dfplot, labels = ["SRR072893","SRR072915"], )
plt.xlabel("Sample ID")
plt.ylabel("log(FPKM)")
plt.title("Comparision of Sxl Transcript FPKM in Drosophila Embryos")

plt.savefig("box.png")

#plott = df2_sx.boxplot("SRR072915", return_typ = 'dict')

#print plott

#plt.figure()
#plt.boxplot(plott)
#plt.savefig("box.png")
#plt.close

#df_sx_gto=df_sx["FPKM"]>0

df2_sx=df2[df2_roi]

#df2_sx_gto=df2_sx["FPKM"]>0

#df_sx_done = df[df_sx_gto]

#df2_sx_done = df2[df2_sx_gto]



