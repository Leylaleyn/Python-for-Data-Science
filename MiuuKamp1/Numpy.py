#############################
# NUMPY
#############################
# Neden Numpy? -> numeric işlemler için geliştirilmiş kütüphanedir
# verimli şekilde veri saklar, yüksek seviyede (vektörel ) işlemler yapabilir

import numpy as np
a = [1,2,3,4]
b = [2,3,4,5]

#klasik yontemle
ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# numpy ile

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a * b  # vektorel işlemleri kolayca yapabildik

########################## NUMPY ARRAY OLUŞTURMA ############################

np.array([1,2,3,4,5])

np.zeros(10, dtype=int) # tipleri inteeger olan 10 adet 0 oluşturdu
x = np.random.randint(0,10, size= 15) #sıfır ile 10 arasında 15 adet olacak şekilde rastgele sayılar oluşturuyor
print(x)

y = np.random.normal(10,4,(3,4)) #ortalaması 10 standart sapması 4 olan 3x4 lük bir array oluşturdu
print(y)

#Numpy Özellikler #

# ndim : boyut sayısı
# shape : boyut bilgisi
# size: toplam eleman sayısı
# dtype: array verri tipi

a = np.random.randint(10, size=5)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

################## Yeniden Şekillendirme ( Reshaping) #####################

np.random.randint(1,10, size=9)
a = np.random.randint(1,10, size=9).reshape(3,3)

a.shape

######################3 INDEX SEÇIMI ########################

a = np.random.randint(10, size=10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10, size = (3,5))
m[1,1]

m[2,3] = 2.9 # 2 olarak basıcak çünkü numpy da diğer değerlerle aynı tipte olmalı

m[:,1]
m[1,:]

m[0:2, 0:3]

######################### FANCY INDEX #########################

v = np.arange(0,30,3)
print("v:",v)

catch = [1,2,3]
print(v[catch])

#################### Numpy'da KOŞULLU İŞLEMLER ##################

v = np.array([1,2,3,4,5])

#Klasik yöntemle
for i in v:
    if i<3:
        ab.append(i)

# Numy ile
v < 3
v[v < 3]
v[v == 3]
v[v >= 3]

####################### MATEMATİKSEL İŞLEMLER ####################
v = np.array([1,2,3,4,5])

v/5
v * 5 / 10
v ** 2
v - 1

np.subtract(v,1)
np.add(v,1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

#Numpy ile iki bilinmeyenli denklem çözme

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10
# katsayıları ayrı sonuçları ayrı numpy arrayler içerisine alıp işlemimizi yapıyoruz

a = np.array([[5,1], [1,3]])
b = np.array([12,10])

np.linalg.solve(a,b)

# özet : neden numpy -> hız ( hızın sebebi verimli veri saklamadır yani sabit tipte veri saklar)
# fonksiyonel düzeyde bize kolaylıklar sağlar
# Çok boyutlu dizilerle ve matrislerle çalışma imkanı sağlar




























