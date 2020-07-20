###
#
# Разработчик: Дон Сергей
# Дата создания: 20/07/2020
#
###

import functions as f

# оптимальная интервал до 5
maxInterval = 3

a = [0] * int(input('Введите кол-во строк и столбцов: '))

AList = [0]
BList = [0]
tempList = [0]
AList.clear()
BList.clear()
tempList.clear()

for i in range(len(a)):
	BList.append(i+1)
	for j in range(len(a)):
		print('ячейка: ', i,j)
		try:
			tempList.append(int(input('Введите цифру: ')))
		except ValueError:
			tempList.append(0)
	AList.append(tempList.copy())
	tempList.clear()

print(AList, 'Input Array')
print(BList, 'Input Array B')

arg = f.firstDec(AList, BList)
tries = ''
if (arg != 0):
	tries = f.randomDec(arg, BList, maxInterval)

print()
if (tries):
	print(tries)
