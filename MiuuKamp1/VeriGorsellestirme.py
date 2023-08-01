import matplotlib.pyplot as plt
########################### VERİ GÖRSELLEŞTİRME : MATPLOTLIB & SEABORN #######################

#**********************
#MATPLOTLIB
#**********************

# Kategorik Değişken : sütun grafik, countplot bar
# Sayısal Değişken : hist, boxplot
# görselleştirme işlemleri için iş zekası araçları daha kullanışlıdır :) !

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
df.head()

df["sex"].value_counts() #value_counts() kategorik değişkenlerle işlem yaptığımızda aklımıza gelmesi gereken ilk fonksiyondur
df["sex"].value_counts().plot(kind = 'bar')

#Sayısal Değişken Görselleştirme

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()


################### Matplotlib'in Özellikleri #################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

###############
# plot -> veriyi görselleştirmek için kullanılır
###############

x = np.array([1,8])
y = np.array([0,150])

plt.plot(x,y)
plt.show()

plt.plot(x,y,"o")
plt.show()

x1 = np.array([2,4,6,8,10])
y1 = np.array([1,3,5,7,9])

plt.plot(x1,y1)
plt.show()

plt.plot(x1,y1,'o')
plt.show()

###### MARKER ######

y = np.array([13,28,11,100])
plt.plot(y, marker = "*")
plt.show()

##### Line #######

plt.plot(y, linestyle = "dotted", color = "r")
plt.show()

########### Multiple Lines  ##############

x = np.array(([23,18,31,10]))
y = np.array([13,28,11,100])
plt.plot(x)
plt.plot(y)
plt.show()

############### LABELS  ####################

x = np.array([80,85,90,95,100])
y = np.array([240,250,260,270,280])
plt.plot(x,y)
plt.title("ANA BAŞLIK")
plt.xlabel("X EKSENİ ")
plt.ylabel(" Y EKSENİ ")

plt.grid()
plt.show()

############### SUBPLOT ###############

x = np.array([80,85,90,95,100])
y = np.array([240,250,260,270,280])
plt.subplot(1,2,1) # 1 satırlık 2 sütunluk grafik oluştur 1. grafiği oluşturuyor
plt.title("1")
plt.plot(x,y)

x = np.array([80,85,90,95,100])
y = np.array([240,250,260,270,280])
plt.subplot(1,2,2) # 1 satırlık 2 sütunluk grafik oluştur 1. grafiği oluşturuyor
plt.title("2")
plt.plot(x,y)

############################ SEABORN İLE VERİ GÖRSELLEŞTİRME ############################
# yüksek seviyeli kütüphanedir -> daha az çabayla daha çok iş yapabilir

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()
# seaborn ile
df["sex"].value_counts()
sns.countplot(x = df["sex"],data = df)
plt.show()
#veya
df["sex"].value_counts().plot(kind = "bar")
plt.show()

######### Sayısal değişken görselleştirme

sns.boxplot(x =df["total_bill"]) # boxplot
plt.show()

df["total_bill"].hist()  # histogram
plt.show()


# plot.barh() -> yatay çubuk grafik oluşturur

import pandas as pd
import matplotlib.pyplot as plt

# Örnek veri çerçevesi oluşturalım
data = {
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Population': [8537673, 8908081, 2140526, 13929286, 5312163]
}

df = pd.DataFrame(data)

# 'City' sütununu indeks olarak belirleyelim
df.set_index('City', inplace=True)

# Yatay çubuk grafik (barh plot) kullanarak verileri görselleştirelim
df.plot.barh()


"""NOTLAR :
'Outlier', bir veri kümesinde diğer verilere göre önemli ölçüde farklı değerlere sahip olan nadir gözlemlerdir. 
Yani, genellikle veri kümesinin genel eğiliminden büyük ölçüde sapmış olan değerlerdir.
 Outlier'ları tespit etmek için görselleştirme, sık kullanılan bir yöntemdir.
 En uygun grafik çeşidi, outlier'ları tespit etmek için genellikle 
 "Kutu Grafiği (Box Plot)" olarak da bilinen "Kutu ve Bıyık Grafiği"dir"""


import seaborn as sns
df = sns.load_dataset("titanic")


df[["sex","survived"]].groupby("sex")