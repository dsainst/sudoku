###
#
# Разработчик: Дон Сергей
# 20/07/2020
#
###

from numpy import random
import functions as f
import sys

# оптимальная интервал до 5
maxInterval = 3

a = [0] * int(input('Введите кол-во строк: '))
b = [0] * int(input('Введите кол-во столбцов: '))

AList = [0]
tempList = [0]
AList.clear()
tempList.clear()

for i in range(len(a)):
	for j in range(len(b)):
		print('ячейка: ', i,j)
		try:
			tempList.append(int(input('Введите цифру: ')))
		except ValueError:
			tempList.append(0)
	AList.append(tempList.copy())
	tempList.clear()

print(AList, 'Input Array')

BList = 	[1,2,3,4,5,6,7,8,9]

f.printList(AList, 'AList')
# создаем список возможных чисел в массиве для каждой ячейки
tempList = f.getTempRowList(BList, AList)

arg = f.antw(AList, tempList)


if (arg[0] == 1):
	f.printList(AList, 'AList')
	sys.exit()

for ir in range(3):
	for iy in range(3):
		out = f.sposob(arg[1], ir, iy)
		if out == 1:
			arg = f.antw(AList, tempList)

if (arg[0] == 1):
	f.printList(AList, 'AList')
	sys.exit()
#f.printList(arg[0], 'arg[0]')

tempC = f.cloneList(arg[0])
tempR = f.cloneList(arg[1])

# перерыв перед запуском генератора

oldList = [0]
tries = [0]
tries.clear()
oldList.clear()

effAll = 3111
for effort in range(effAll):
	minimal = 100
	maximal = 0
	tempList = f.getTempRowList(BList, arg[0])
	arg = f.antw(arg[0], tempList)
	tempC = f.cloneList(arg[0])
	tempR = f.cloneList(arg[1])
	print('----------------------------------- Попытка №', effort, ' -----------------------------------')
	wrong = 1
	i = 0
	for x in tempR:
		k = 0
		for y in x:
			if (len(y) > maximal):
				maximal = len(y)
			if (len(y) > 0 and len(y) < minimal):
				minimal = len(y)

			if (len(y) > 1 and len(y) <= maxInterval):
				check = 0
				t = random.choice(y)
				wrong = 0
				for item in oldList:
					if (item == [i,k,t]):
						check = 1
				if (check == 0):
					tempR[i][k] = [t]
					oldList.append([i,k,t])
					arguments = f.antw(tempC, tempR)
					if (arguments[0] == 1):
						f.printList(tempC, 'tempC')
						sys.exit()
				else:
					print('choise is went ', t)
			k += 1
		i += 1
	tries.append(oldList.copy())
	f.printList(tempC, 'tempC')
	oldList.clear()
	if (wrong):
		print('увеличьте интервал подбора - ', minimal, maximal)
		sys.exit()
print()
print(tries)
print('------------------------')
f.printList(tempC, 'tempC')
