######## Genel Resim ##########

import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns',None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

def check_df(dataframe, head = 5):
    print(" SHAPE : ", dataframe.shape)
    print("TYPES : ", dataframe.dtypes)
    print("HEAD : ", dataframe.head(head))
    print("TAIL  : ", dataframe.tail(head))
    print("NA : ", dataframe.isnull().sum())
    print("QUANTILES : ", dataframe.describe(([0,0.05,0.50,0.95,0.99,1])).T)  # sayısal değişkenlerin dağılım bilgisine erişmek istersek

check_df(df)

# başka bir veri seti için de bu bilgileri özetlemek istersek
df = sns.load_dataset("tips")
check_df(df)

################ KATEGORİK DEĞİŞKEN ANALİZİ #################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.dtypes

df["embarked"].value_counts()
df["sex"].unique()
df["sex"].nunique()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]
# olası kategorik değişkenleri tip bilgisine göre yakalanması sağlandı

cat_cols

# str(df[col].dtypes) burada ilgili değişkenin tip bilgisini stringe çeviriyoruz ve
# in ["category","object","bool"] diyerek bunların içinde var olup olmadığını kontrol ediyoruz

df["survived"].value_counts()
#iki kategorik değişkene sahip ama 0 ve 1 lerden ifade edildiğinden dolayı bunu yakalamak zor

# integer ve float tipte olup olup kategorik değer taşıyan değişkenleri bulmak istersek
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
num_but_cat

#categorik tipte olup kategorik değer taşımayan bilgilere erişmek için
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_but_car
# yani bir kategorik değişkenin çok fazla sınıf taşıması bilgi taşımadığı anlamına gelebilir değerli bilgiler olmayabilir
# (mesela isim değişkeni ve içerisinde yolcuların isimlerini taşıması)

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique()

num_degisken = [col for col in df.columns if col not in cat_cols]

df.head()

df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)  #Yüzdelik karşılığını bulmak için

#  otomatikleştirelim
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))

cat_summary(df,"sex")

#bütün kategorik değişkenlerin oranlarına bakmak istersek
for col in cat_cols:
    cat_summary(df,col)


print("***************************************** PART 2 *********************************************")

def cat_summary(dataframe, col_name, plot = False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    if plot :
         sns.countplot(x = dataframe[col_name], data= dataframe)
         plt.show(block = True)

cat_summary(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print(col)
    else :
        cat_summary(df, col, plot=True)

# grafik oluşturmada bool tiplerini oluşturamıyor bu yüzden plot oluşturamıyoruz
# bool tipini dönüştürerek uygulayalım
df["adult_male"].astype(int) # true false değerlerini 1-0 olarak çevirdi


for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else :
        cat_summary(df, col, plot=True)

################################# SAYISAL DEĞİŞKEN ANALİZİ #######################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.dtypes
df[["age","fare"]].describe().T

num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float64"]]  # nedense int ve float yazınca direkt sayısal değer olan age ve fare geliyor ?

num_cols = [col for col in num_cols if col not in cat_cols]

def num_summary(dataframe,numerical_col):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.99]
    print(dataframe[numerical_col].describe(quantiles).T)


num_summary(df,"age")

for col in num_cols:
    num_summary(df,col)

# eğer grafik eklemek istersek
def num_summary(dataframe,numerical_col, plot = False):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block = True)

num_summary(df,"age",plot=True)

for col in num_cols:
    num_summary(df,col,plot=True)


###################  DEĞİŞKENLERİN YAKALANMASI VE İŞLMELERİN GENELLEŞTİRİLMESİ #######################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()
df.info()

# eşsiz değer sayısı 10 dan küçükse kateegorik değişken diyeceğiz,
# eger kategorik deşiken eşsiz değer sayısı 20 den büyükse buna cardinal değişken muamelesi yapılacaktır
def grab_col_names(dataframe, cat_th = 10, car_th = 30):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat  kardinal değişkenlerin isimlerini verir
    Parameters
    ----------
    dataframe
       değişken isimleri alınmak istenen dataframe'dir.

    cat_th : int, float
        numerik fakat kategorik olan değişkenler içim sınıf eeşik değeri
    car_th : int, float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols : list
               Kategorik değişken listesi
        num_cols : list
               Numeric Değişken listesi
        cat_but_car : list
               Kategorik görünümlü kardinal değişken liste

    Notes
    ------
    cat_cols + num_cols + cat_but_car =  toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde
    """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat

    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int64",
                                                                "float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observation : , {dataframe.shape[0]}")
    print(f"Variables : , {dataframe.shape[1]}")
    print(f"cat_cols : , {len(cat_cols)}")
    print(f"num_cols : , {len(num_cols)}")
    print(f"cat_but_car : , {len(cat_but_car)}")
    print(f"num_but_cat : , {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car

help(grab_col_names) # yazdığımız bilgilere erişebiliyoruz

cat_cols, num_cols, cat_but_car = grab_col_names(df)


grab_col_names(df)

# şimdi ayrı ayrı bütün kategorik bilgiler için bilgileri özetlemek istersek
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("*****************************************************")

for col in cat_cols:
    cat_summary(df,col)

# numeric değişkenler için bütün bilgileri özetlersek
def num_summary(dataframe,numerical_col):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

for col in num_cols:
    num_summary(df,col)

#  BONUS
# bool tipindeki değişkenleri int'e çevirdik
df = sns.load_dataset("titanic")
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols, num_cols, cat_but_car = grab_col_names(df)

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
def num_summary(dataframe,numerical_col):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

for col in cat_cols:
    cat_summary(df,col)

for col in num_cols:
    num_summary(df,col)

################## HEDEF DEĞİŞKEN ANALİZİ ###################

# hedef değişkenimizi "survived" olarak seçtik

df["survived"].value_counts()
cat_summary(df,"survived")

# Hedef Değişkenin Kategorik Değişkenler ile Analizi

df.groupby("sex")["survived"].mean()

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN " : dataframe.groupby(categorical_col)[target].mean()}))

target_summary_with_cat(df,"survived","pclass")

# bütün kategorik değişkenlerle target'ın durumunu incelemek istersek
for col in cat_cols:
    target_summary_with_cat(df,"survived",col)


# Hedef Değişkenin Sayısal Değişken ile Analizi

df.groupby("survived")["age"].mean()  # burada tam tersi olarak groupby' a bağımlı değişkenimizi getiririz

df.groupby("survived").agg({"age":"mean"})

def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col : "mean"}), end="\n\n")


target_summary_with_num(df,"survived","age")

for col in num_cols:
    target_summary_with_num(df,"survived",col)


################## KORELASYON ANALİZİ ###################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = pd.read_csv("breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()

num_col = [col for col in df.columns if df[col].dtype in [int,float]]

# korelasyonu hesaplamak için corr() kullanıyoruz
#korelasyon : değişkenlerin birbiriyle ilişkisini ifade eden bir istatiksel ölçümdür

corr = df[num_col].corr()

#Not : genelde analitik çalışmalarda birbiriyle yüksek korelasyona sahip değişkenleri çalışmalarda istemeyiz çünkü ikisi de neredeyse aynı şeyi ifade ediyor bu yüzden birini dışarda tutmalıyız

sns.set(rc = {"figure.figsize": (12,12)})
sns.heatmap(corr)
plt.show()

## Yüksek Korelasyonlu Değişkenlerin Silinmesi

cor_matrix = df.corr(numeric_only=True).abs() #korelasyonların negatif ya da pozitif olduklarıyla ilgilenmiyorum bu yüzden hepsini mutlak değer içinde yazdık

#ayrıca gereksiz bilgileri de silmeliyiz ornegin 1 ile 2 nin korelasyonu varken 2 ile 1 in korelasyonu da varsa bir tanesi silinmeli
##çıktı matrisi köşegene göre simetrik olacak şekilde aynı verileri veriyor bu yüzden üst üçgensel matris yapıyoruz
# bunu yapmak için
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_)) #boş bir numpy array oluşturup istenilen koşulla dolduruyoruz

# sütunlardaki elemanlardan herhangi biri %90 dan büyükse onu silen bir fonksiyon yazalım(%90ı biz belirledik

drop_list = [ col for col in upper_triangle_matrix if any(upper_triangle_matrix[col] > 0.90)]
drop_list

df.drop(drop_list, axis = 1)

def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr(numeric_only=True)
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={"figure.figsize": (15, 15)})
        sns.heatmap(corr)
        plt.show(block=True)
    return drop_list

drop_list = high_correlated_cols(df,plot=True)
df.drop(drop_list, axis = 1)

high_correlated_cols(df.drop(drop_list, axis = 1), plot=True)








