#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import statistics as sts
import matplotlib.pyplot as plt


dataset = pd.read_csv('C:/Users/ramon/Desktop/OncidiumDados/DadosCSV.csv', sep=';')


# In[253]:


#Criando gráfico de 0,05% 4 Dias
##########################################

plantas054 = dataset.query("COLCHICINA == '0,1' and DIAS == 7")

def MostrarTabela():
    return plantas054['DNA'].value_counts()

def FiltrarPorDNA(tipoDeDNA):
    return plantas054[['DNA', 'Tempo']].loc[plantas054['DNA'] == tipoDeDNA]
    
def FiltrarPorTempo(tempo):
    return plantas054[['DNA', 'Tempo']].loc[plantas054['Tempo'] == tempo]

def FiltrarPoliploides():
    return plantas054[['DNA', 'Tempo']].loc[(plantas054.DNA == '2C') | (plantas054.DNA == '4C') | (plantas054.DNA == '2C+++') | (plantas054.DNA == '8C') | (plantas054.DNA == '4C++')]

def FiltrarMixoploides():
    return plantas054[['DNA', 'Tempo']].loc[plantas054.DNA == 'Mixo']

#print(MostrarTabela())
#print(FiltrarPorDNA('Mixo'))
#print(FiltrarPorTempo(6))
#print(FiltrarPoliploides())


# In[254]:


poliploides = FiltrarPoliploides()
mixoploides = FiltrarMixoploides()

#Filtrando poliploides pelo Tempo de 6, 12 e 18 meses
############################################################

def FiltrarPoliploidesPorTempo(tempo):
    return poliploides[['DNA', 'Tempo']].loc[poliploides['Tempo'] == tempo]

poliploides6Meses = FiltrarPoliploidesPorTempo(6)
poliploides12Meses = FiltrarPoliploidesPorTempo(12)
poliploides18Meses = FiltrarPoliploidesPorTempo(18)


#Filtrando mixoploides pelo Tempo de 6, 12 e 18 meses
############################################################

def FiltrarMixoploidesPorTempo(tempo):
    return mixoploides[['DNA', 'Tempo']].loc[mixoploides['Tempo'] == tempo]

mixoploides6Meses = FiltrarMixoploidesPorTempo(6)
mixoploides12Meses = FiltrarMixoploidesPorTempo(12)
mixoploides18Meses = FiltrarMixoploidesPorTempo(18)


# In[255]:


quantidadeDeMixoploides6Meses = len(mixoploides6Meses)
quantidadeDeMixoploides12Meses = len(mixoploides12Meses)
quantidadeDeMixoploides18Meses = len(mixoploides18Meses)

quantidadeDePoliploides6Meses = len(poliploides6Meses)
quantidadeDePoliploides12Meses = len(poliploides12Meses)
quantidadeDePoliploides18Meses = len(poliploides18Meses)

somatorio6Meses = quantidadeDeMixoploides6Meses + quantidadeDePoliploides6Meses
somatorio12Meses = quantidadeDeMixoploides12Meses + quantidadeDePoliploides12Meses
somatorio18Meses = quantidadeDeMixoploides18Meses + quantidadeDePoliploides18Meses

df = pd.DataFrame({ 
    'Meses': ['6','12', '18'], 
    'Mixoploides': [quantidadeDeMixoploides6Meses/somatorio6Meses, quantidadeDeMixoploides12Meses/somatorio12Meses, quantidadeDeMixoploides18Meses/somatorio18Meses], 
    'Poliploides': [quantidadeDePoliploides6Meses/somatorio6Meses, quantidadeDePoliploides12Meses/somatorio12Meses, quantidadeDePoliploides18Meses/somatorio18Meses] 
}) 


# In[256]:


df.plot(x="Meses", y=["Mixoploides", "Poliploides"], kind="bar", title="Oncidium 0,1% 7 Dias", color=["#ff3d00", "#002c2b"])
plt.savefig('C:/Users/ramon/Desktop/OncidiumDados/GraficoDeBarra017.png', dpi = 300)


# In[257]:


df.plot(x="Meses", y=["Mixoploides", "Poliploides"], kind="line", title="Oncidium 0,1% 7 Dias", color=["#ff3d00", "#002c2b"])
plt.savefig('C:/Users/ramon/Desktop/OncidiumDados/GraficoDeLinha017.png', dpi = 300)


# In[258]:


df.plot(x="Meses", y=["Mixoploides", "Poliploides"], kind="hist", title="Oncidium 0,1% 7 Dias", color=["#ff3d00", "#002c2b"])


# In[ ]:




