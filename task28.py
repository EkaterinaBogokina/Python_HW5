# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
#     4 
a = int(input("enter number A: "))
b = int(input("enter number B: "))
def summa(a,b):
    if a==0:
        return b
    if b==0:
        return a
    else:
        return summa(a-1,b+1)
print(summa (a,b))
    