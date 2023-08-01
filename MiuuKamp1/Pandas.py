############### PANDAS ##################
# Veri Manipülasyonu ve Veri Analizi dendiğinde akla gelen kütüphanelerden biridir

####### Pandas Series

import pandas as pd

s = pd.Series([11,70,12,4,5])
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)  # değerleri aldığımızdan dolayı
s.head(3)
s.tail(3)

################## VERİ OKUMA #############3

pd.read_csv("advertising.csv")


###############3 Veriye Hızlı Bakış
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.index
df.describe().T
df.isnull().values.any() #veri setinin herhangi bir yerinde null değer varsa True döndürür
df.isnull().sum() #her bir değerde eksik bilgiler varsa kaç tane olduğunu gösterdi

df["sex"].value_counts()

############ Pandas'ta Seçim İşlemleri #####################

df.head()
df[0:5]

df.drop(1,axis=0).head() # 1. indexteki elemanlar silinmiş oldu axis = 0 satır axis = 1 sütunu temsil eder

#Kalıcı hale getirmek istersek
# df = df.drop(1,axis=0).head() veya
# df.drop(1,axis=0, inplace = True)

###### Değişkeni Indexe Çevirmek  #############

df["age"].head()
df.age.head()  # bu iki kullanımda aynı sonucu verir

df.index = df["age"] # age bilgisi bir değişken olarak indexe eklenmiş oldu

df.drop("age",axis=1, inplace=True)

########3 Indexi Değişkene Çevirmek

df["age"] = df.index
df.head()
df.drop("age",axis=1, inplace=True)
# 2. yol
df = df.reset_index().head()
df.head()

########## Değişkenler Üzerinde İşlemler ########
# Çıktıdaki ... ( 3 noktalardan kurtulmak istersek )
pd.set_option('display.max_columns',None)
df.head()

"age" in df # age değişkeni dataframe iççerisinde var mı ?

df["age"].head()
df.age.head()

type(df["age"].head())  # bu bir pandas serisidir

# eğer değişken seçmek istersek ve bu şekilde seçersek hata alacağız çünkü bu bir pandas serisidir oysa bize dataframe gerekir
# bu yüzden dataframe olarak kalmasını istiyorsak [[]] iki defa kapalı parantezi kullanmamız gerekir

df[["age"]].head()
type(df[["age"]].head())

df[["age","alive"]]

col_names = ["age","adult_male","alive"]
df[col_names]

# yeni bir değişkeni veri setine eklemek istersek

df["age2"] = df["age"] ** 2
df.head()

# Silme işlemi yapmak istersek

df["age3"] = df["age"] / df["age2"]
df.drop("age3", axis = 1).head()

df.head()

df.loc[:, ~df.columns.str.contains("age")].head() # ~ dışındaki demek
# ~: Tilde işareti, str.contains ile yapılan eşleşmeyi tersine çevirir, yani "age" içeren sütunları hariç tutar.
#df.columns.str.contains("age")  Bu, veri çerçevesinin sütun adları üzerinde "age" kelimesini içeren sütunları tespit etmek için kullanılan bir dizi metotdur.


################## LOC  ILOC YAPISI ##########################

# iloc : integer baseed selection
df.iloc[0:3]

# loc : label based selection
df.loc[0:3]

# df.iloc[0:3,"age"] hata alırız

df.loc[0:3, "age"]

col_names = ["age","embarked","alive"]
df.loc[0:3, col_names]

###################### KOŞULLU SEÇİM #######################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count() #yaşı 50 den büyük kaç kişi var

df.loc[df["age"] > 50,"class"].head() #yaşı 50 den büyük olanların sınıf bilgisi
df.loc[df["age"] > 50,["age","class"]].head()


df.loc[(df["age"] > 50 ) & (df["sex"] == "male"), ["age","class"]].head()

df.loc[(df["age"] > 50 ) &
       (df["sex"] == "male") &
       ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age","class","embark_town"]].head()

############################## TOPLULAŞTIRMA VE GRUPLAMA ################################
# Özet istatistikler veren fonksiyonlardır
# count()
# first()
# last()
# mean()
# median()                      # groupby ile kullanılabilen fonksiyonlardır pivot table hariç
# min()
# max()
# std()
# var()
# sum()
# pivot table

#cinsiyete göre yaşlarının ortalamasını bulmak istersek

df["age"].mean()
df["age"].loc[df["sex"] == "female"].mean()
df["age"].loc[df["sex"] == "male"].mean()

# groupby kullanarak
df.groupby("sex")["age"].mean()

# farklı kullanım şekilleri
df.groupby("sex").agg({"age": "mean"}) #bu kullanım daha iyi çünkü birden fazla işlemi gerçekleştirebiliriz örneğin
df.groupby("sex").agg({"age": ["mean","sum"]})

df.groupby(["sex","embark_town"]).agg({"age": ["mean","sum"],
                       "survived" : "mean"})

df.groupby(["sex","embark_town","class"]).agg({"age": ["mean","sum"],
                       "survived" : "mean",
                       "sex" : "count"})


#########################3 PİVOT TABLE ############################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived","sex","embarked") # pivot_table(kesişim,index/satır,sütun)  ön tanım değeri mean dır bu yüzden ortalama gösteriyor
df.pivot_table("survived","sex","embarked", aggfunc="std")

df.pivot_table("survived","sex",["embarked","class"])

# Soru : hem cinsiyet hem locasyon hem yaş değişimlerini istiyorum fakat yaş değişkenimiz sayısal bir değişken

# şimdi yaş değişkenlerini kategorik değişkenlere çevirelim
df["new_age"] = pd.cut(df["age"], [0,10,18,25,40,90])
df.head()

df.pivot_table("survived","sex","new_age") #yaş değişkenine göre hayatta kalma oranları

pd.set_option('display.width',500)


##################### APPLY VE LAMBDA ########################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
df = sns.load_dataset("titanic")
df.head()
# Apply -> satır ya da sütunlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar
# Lambda -> bir fonksiyon tanımlama şeklidir kullan at

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()  # tek tek böyle uğraşmak yerine bir döngü yazalım

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())
        # df[col] = df[col]/10 kaydetmek isteseydik

#  LAMBDA İLE
df[["age","age2","age3"]].apply(lambda x: x/10).head() #apply ile lambda fonksiyonunu uyguladık

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/ 10).head()  #içerisinde age olan değişkenleri aldık

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / s.std()).head()  #değerleri standartlaştırmak için (x - x.mean()) / s.std() kullandık

# Ya da bir fonksiyon belirleyip oyle de yapabilirdik

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

"""Yaptığımız değişiklikleri kaydetmek istersek """

# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
#ya da
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()


####################### BİRLEŞTİRME İŞLEMLERİ #######################
import numpy as np
m = np.random.randint(1,20,size=(5,3))
df1 = pd.DataFrame(m, columns=["var1","var2","var3"])
df2 = df1 + 99

# şimdi iki dataframe i birleştirelim
pd.concat([df1,df2], ignore_index=True) # ignore_index demezsek indexler 01234 01234 diye oluşuyordu

# Merge ile birleştirme işlemleri

df3 = pd.DataFrame({"employees" : ["john","dennis","mark","maria"],
                    "group" : ["accounting","engineering","engineering","hr"]})

df4 = pd.DataFrame({"employees" : ["mark","john","dennis","maria"],
                    "start_date" : [2010,2009,2014,2019]})

pd.merge(df3,df4)
# pd.merge(df3,df4 on = "employees") employees tanımlamadan da birleştirdi

# Amaç : Her çalışanın müdürünün bilgisine erişmek istiyoruz

df5 = pd.merge(df3,df4)

df6 = pd.DataFrame({'group' : ["accounting","engineering","hr"],
                    "manager" : ["Caner", "Mustafa", "Berkcan"]})

pd.merge(df5,df6)

series = pd.Series([1,2,3])
series ** 2

