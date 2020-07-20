###
#
# Разработчик: Дон Сергей
# 20/07/2020
#
###

from numpy import random
import functions as f

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
	return

for ir in range(3):
	for iy in range(3):
		out = f.sposob(arg[1], ir, iy)
		if out == 1:
			arg = f.antw(AList, tempList)

if (arg[0] == 1):
	f.printList(AList, 'AList')
	return
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
	tempList = f.getTempRowList(BList, arg[0])
	arg = f.antw(arg[0], tempList)
	tempC = f.cloneList(arg[0])
	tempR = f.cloneList(arg[1])
	print('----------------------------------- Попытка №', effort, ' -----------------------------------')
	# print('tempR - ', tempR)
	# print('arg[1] - ', arg[1])
	i = 0
	for x in tempR:
		k = 0
		for y in x:
			if (len(y) > 1 and len(y) < 4):
				check = 0
				t = random.choice(y)
				for item in oldList:
					if (item == [i,k,t]):
						check = 1
				if (check == 0):
					tempR[i][k] = [t]
					oldList.append([i,k,t])
					# print('!!!!------------------------ choise is ', oldList, ' -----------------------------------')
					arguments = f.antw(tempC, tempR)
					#f.printList(arguments[0], 'arguments')
					if (arguments[0] == 1):
						f.printList(tempC, 'tempC')
						return
				else:
					print('choise is went ', t)
				# print('oldList - ', oldList)
			k += 1
		i += 1
	tries.append(oldList.copy())
	print('Подбор ключей - ', oldList)
	#print('Возможные ключей - ', tempR)
	oldList.clear()
print()
print(tries)
print('------------------------')
# f.printList(arguments[0], 'A')
f.printList(tempC, 'tempC')
