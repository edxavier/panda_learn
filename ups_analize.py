__author__ = 'Eder Xavier Rojas'
import pandas as pd
import numpy
import matplotlib.pyplot as plt



#df = pd.read_csv('CR_UPS2.txt', header=None, sep=r":")
file = open('CR_UPS2.txt', 'r')
dates = []
desc = []
codes = []
for line in file:
    cols = line.split(':')
    colsd = line.split(' ')
    dtime  = colsd[0]
    dates.append(dtime)
    desc.append(cols[-1].replace('\n','').strip())
    cols2 = cols[2].split()
    codes.append(cols2[1])

hist_data = {'DATE':dates, 'CODE':codes, 'LABEL':desc}

df = pd.DataFrame(hist_data,)
df['DATE'] = pd.to_datetime(df['DATE'],format="%d/%m/%Y")
#print df.groupby('DATE').count()
co = df.groupby('DATE').count()
print "Numero de eventos x fecha"
print co['CODE']
print co['CODE'].describe()
#co = df.groupby(['LABEL', 'DATE',]).count()
#co.plot()
#plt.show()

print "Numero de eventos"
print df['LABEL'].value_counts()
df2 = df['LABEL'].value_counts()

#df2.plot(kind='bar', title ="Numero de eventos", figsize=(15,10),legend=True,).set_xlabel("Eventos",fontsize=8)
#plt.show()


print "-----------------------------"
print "Numero de eventos x fecha"
df =  df['DATE'].value_counts()
print df

#res =  df1['LABEL'].resample('D', how={'tot':len})
#res = res[res['tot']>0]
#print res.sort(['tot'])r