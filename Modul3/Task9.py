#------==================Задача 9 (7/10)#====================------
#Дана последовательность натуральных чисел x₁, x₂ ..., xn. #Стандартным отклонением называется величина
#
#σ=sqrt(((x₁-s)²+(x₂-s)²+…+(xn-s)²) / (n-1))
#
#где s = ((x₁+x₂+…+xn) / n) — среднее арифметическое #последовательности, а sqrt - квадратный корень. Определите #стандартное отклонение для данной последовательности #натуральных чисел, завершающейся числом 0.
#
#Формат ввода
#Вводится последовательность целых чисел, оканчивающаяся #числом 0 (само число 0 в последовательность не входит, а #служит как признак ее окончания).
#
#Формат вывода
#Выведите ответ на задачу.
x = []

while x == 0 :
	x = int(input("Вводьте значення х, 0 припиняє ввод"))
	x.append(x)