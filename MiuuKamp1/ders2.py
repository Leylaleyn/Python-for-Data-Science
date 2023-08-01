###############################
# COMPREHENSIONS
###############################

# List Comprehension

salaries = [1000, 2000, 3000, 4000, 5000]
null_list = []

def new_salary(x):
    return x * 20 / 100 + x

""" for i in salaries:
      null_list.append(new_salary(i))  """

""" for i in salaries:
    if i > 3000:
        null_list.append(new_salary(i))
    else:
        null_list.append(new_salary(i * 2))
print(null_list)
"""
# şimdi comprehension kullanarak tek bir satırda bu yaptığımız işlemleri halledeleim
# [new_salary(i * 2) if i > 3000 else new_salary(i) for i in salaries]

print([new_salary(i * 2) if i > 3000 else new_salary(i) for i in salaries])

[new_salary(salary * 2) for salary in salaries]

[new_salary(salary * 2) for salary in salaries if salary < 3000]
# tek başına if kullanıyorsak bu en sağ tarafta olur

# dikkat eğer else de kullanacaksak for yapısı en sağ tarafta olur

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

####### Örnek #######

students = ["John","Mark","Venessa","Mariam"]

students_no =  ["John","Venessa"]

print([i.lower() if i in students_no else i.upper() for i in students ])

##################
#Dict Comprekension
##################

dictionary = { 'a' : 1,
               'b' : 2,
               'c' : 3,
               'd' : 4}

dictionary.keys()
dictionary.values()
dictionary.items()

#  sözlük içerisindeki her bir value'nin karesini almak istiyoruz

{k : v ** 2 for (k,v) in dictionary.items() }

{k.upper() : v * 2 for (k,v) in dictionary.items() }

##################################
# UYGULAMA - MÜLAKAT SORUSU

# Amaç : çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir
#key ler orjinal değerler value'lar ise değiştirilmiş değerler olacak

numbers = range(10)
new_dict = {}

for i in numbers:
    if i % 2 == 0:
        new_dict[i] = i ** 2

# dict comperehension ile çözümü
{n : n ** 2 for n in numbers if n % 2 == 0}


##########################  UYGULAMALAR #############################

# bir veri setindeki değişken isimlerini değiştirmek

import seaborn as sns
df = sns.load_dataset("car_crashes")
print(df.columns)

# klasik yöntemle
A = []
for i in df.columns:
    A.append(i.upper())

print(A)
print("************************************************ \n")
# comprehension ile
df.columns = [i.upper() for i in df.columns]
print(df.columns)

########### UYGULAMA 2 ############
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz

[col for col in df.columns if "INS" in col]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns ]
print(df.columns)
print("*********************")
#################### UYGULAMA 3 ########################
# Amaç key'i string, value'su bir liste olan sözlük oluşturmak
# Sadece sayısal değişkenler için yapmak istiyoruz
# {'total' : ['mean','min','max'] } .. gibi

num_cols = [col for col in df.columns if df[col].dtype != "O"]  # O ifadesi objectir kategorik ifadeleri temsil eder
print(num_cols)

sozluk = {}
agg_list = ['mean','min','max','sum']

for col in num_cols:
    sozluk[col] = agg_list

# comprehension ile çözümü
new_dict = {col : agg_list for col in num_cols}

print(df[num_cols].head())

print(df[num_cols].agg(new_dict))