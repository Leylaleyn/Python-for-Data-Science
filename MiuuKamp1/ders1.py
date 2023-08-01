dir(int)  # int ile kullanılabilecek metodlar

dir(str)

name = "Aleyna"

name.upper()

hi = "Hello AI Era"
hi.replace("l","p")


print("ofofofof".strip("o"))

# fonksiyon tanımlama

def calculate(x):
    print(x*2)

calculate(5)

#iki argümanlı/parametreli bir fonksiyon tanımlayalım

def summer(arg1,arg2):
    print(arg1+arg2)

summer(8,3)

#Docstring -> fonksiyonlarımıza herkesin anlayabilecek bir bilgi notudur

def summer(arg1,arg2):

   """
   Sum of two number
   Parameters
   ----------
   arg1 : int, float
   arg2 : int, float

   Returns
   int float
   -------

   """


# girilen değerleri bir liste içinde saklayacak fonksiyon

list_store = []

def add_element(a,b):
    c = a*b
    list_store.append(c)
    print(list_store)

add_element(12,4)

add_element(12,6)


def square(a):
    return a*2

print(square("hello"))

# FOR DONGUSU

salary = [1000,2000,3000,4000,5000]

def new_salary(salary,rate):
    return int(salary*rate/100+ salary)

print(new_salary(2000,10))

for i in salary:
    print(new_salary(i,10))

    # ÖRNEK SORU #

# Amaç : Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.
# before: "hi my name is john and i am learning python"
# after : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

a = "hi my name is john and i am learning python"

def fonk(metin):
    new_metin = ""
    for i in range(len(metin)):
        if i % 2 == 0:
            new_metin += metin[i].upper()

        else:
            new_metin += metin[i].lower()

    print(new_metin)

fonk(a)

## ENUMERATE : Otomatik Counter/ Indexer ile for loop

students = ["John","Mark","Venessa","Mariam"]

for i in students:
    print(i)

print("\n")

for index, student in enumerate(students):
    print(index, student)


A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0 :
        A.append(student)

    else:
        B.append(student)

print(A)
print(B)
#################################
#UYGULAMA - MÜLAKAT SORUSU
#################################

# DİVİDE_STUDENTS FONKSİYONU YAZINIZ
# Çift indexte yer alan öğrencileri bir listeye alınız
# Tek indexte yer alan öğrencileri başka bir listeye alınız
#fakat bu iki liste tek bir liste olarak return olsun

students = ["John","Mark","Venessa","Mariam"]

def divide_students(students):

    gruplar = [[],[]]

    for index, student in enumerate(students):
        if index % 2 == 0:
            gruplar[0].append(student)

        else:
            gruplar[1].append(student)
    print("Çift grup:", gruplar[0])
    print("Tek grup:",gruplar[1])

    return gruplar

divide_students(students)

########################################################
# Alternating Fonksiyonunun enumerate ile yazılması
########################################################

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()

    print(new_string)

alternating_with_enumerate("hi my name is aleyna and i am learning python")

#####################
# Zip -> birbirinden farklı olan listeleri bir arada değerlendirme imkanı sağlar
#####################

students = ["John","Mark","Venessa","Mariam"]

departments = ["mathematics","statik","fizik","astronomi"]

ages = [23,30,21,23]

print(list(zip(students,departments,ages)))
# ayrı lisiteleri tek bir liste içerisinde , her birinde bulunan elemanları aynı sırada zipleyerek bir araya getirir

#################################
# lambda, map, filter, reduce
#################################

# lambda

def summer(a,b):
    return a+b

new_sum = lambda a, b: a+b   #lambda' da bir fonksiyon tanımlama şeklidir

new_sum(4,5)

# map

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x*20 / 100 + x

for i in salaries:
    print(new_salary(i))

print("MAP")
# map for döngüsüne gerek kalmadan fonksiyonla istediğimiz nesneyi map işlemi yapıyor döngü yazmaktan kurtulmuş oluyoruz
print(list(map(new_salary,salaries)))

print("\n")
# syntax ->  map(fonksiyon,nesne)
print("lambda ve map birlikte kullanımı :", list(map(lambda x: x * 10 / 100 + x,salaries)))
print("\n")
# FILTER -> verilen koşulu filtreleyip bize gösterir
print("FILTER ")
list_store = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x : x%2 ==0, list_store)))



students = ["Denise", "Arsen", "Tony", "Audrey"]

print([student[0].upper() if len(student) %2 != 0 else
 student[0].lower() for student in students])
