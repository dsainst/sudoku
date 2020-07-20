from time import sleep
from numpy import random

def firstDec(AList, BList):
	printList(AList, 'AList')
	# создаем список возможных чисел в массиве для каждой ячейки
	tempList = getTempRowList(BList, AList)

	print('tempList - ', tempList)
	arg = decision(AList, tempList)

	if (arg[0] == 1):
		printList(AList, 'AList')
		return 0

	for ir in range(3):
		for iy in range(3):
			out = sposob(arg[1], ir, iy)
			if out == 1:
				arg = decision(AList, tempList)

	if (arg[0] == 1):
		printList(AList, 'AList')
		return 0
	return arg

def randomDec(arg, BList, maxInterval = 3, effAll = 3111):
	oldList = [0]
	tries = [0]
	tries.clear()
	oldList.clear()

	for effort in range(effAll):
		minimal = 100
		maximal = 0
		tempList = getTempRowList(BList, arg[0])
		arg = decision(arg[0], tempList)
		tempC = cloneList(arg[0])
		tempR = cloneList(arg[1])
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
						arguments = decision(tempC, tempR)
						if (arguments[0] == 1):
							printList(tempC, 'tempC')
							return
					else:
						print('choise is went ', t)
				k += 1
			i += 1
		tries.append(oldList.copy())
		printList(tempC, 'tempC')
		oldList.clear()
		if (wrong):
			print('увеличьте интервал подбора - ', minimal, maximal)
			return
	return tries

def sposob(trl, row = 0, kvadrat = 0):
	kvadrat = kvadrat * 3
	row = row * 3
	result = [0]
	result2 = [0]
	result.clear()
	result2.clear()
	for i in range(row, row+3):
		for k in range(kvadrat, kvadrat+3):
			result.append(list(set(trl[i][k]) & set(result2)))
			result2 = list(set(trl[i][k]) ^ set(result2))
			k += 1
		i += 1
	for rem in result:
		for m in rem:
			if m>0:
				try:
					result2.remove(m)
				except ValueError:
					pass
	coords = [0]
	coords.clear()
	if len(result2) == 1:
		for i in range(row, row+3):
			for k in range(kvadrat, kvadrat+3):
				try:
					x = trl[i][k].index(result2[0])
					trl[i][k] = result2
				except ValueError:
					pass
	return 1

def defSquare():
	n = 3
	resT = [0]
	resTRow = [0]
	resT.clear()
	resTRow.clear()
	for i in range(0,7,3):
		for k in range(n):
			resT.append([k,i])
			resT.append([k,1+i])
			resT.append([k,2+i])
		resTRow.append(resT.copy())
		resT.clear()

	resT.clear()
	for i in range(0,7,3):
		for k in range(n,n+3):
			resT.append([k,i])
			resT.append([k,1+i])
			resT.append([k,2+i])
		resTRow.append(resT.copy())
		resT.clear()
	resT.clear()
	for i in range(0,7,3):
		for k in range(n+3,n+6):
			resT.append([k,i])
			resT.append([k,1+i])
			resT.append([k,2+i])
		resTRow.append(resT.copy())
		resT.clear()

	tempClone = [	
					[resTRow[0],resTRow[0],resTRow[0],resTRow[1],resTRow[1],resTRow[1],resTRow[2],resTRow[2],resTRow[2]],
					[resTRow[0],resTRow[0],resTRow[0],resTRow[1],resTRow[1],resTRow[1],resTRow[2],resTRow[2],resTRow[2]],
					[resTRow[0],resTRow[0],resTRow[0],resTRow[1],resTRow[1],resTRow[1],resTRow[2],resTRow[2],resTRow[2]],
					[resTRow[3],resTRow[3],resTRow[3],resTRow[4],resTRow[4],resTRow[4],resTRow[5],resTRow[5],resTRow[5]],
					[resTRow[3],resTRow[3],resTRow[3],resTRow[4],resTRow[4],resTRow[4],resTRow[5],resTRow[5],resTRow[5]],
					[resTRow[3],resTRow[3],resTRow[3],resTRow[4],resTRow[4],resTRow[4],resTRow[5],resTRow[5],resTRow[5]],
					[resTRow[6],resTRow[6],resTRow[6],resTRow[7],resTRow[7],resTRow[7],resTRow[8],resTRow[8],resTRow[8]],
					[resTRow[6],resTRow[6],resTRow[6],resTRow[7],resTRow[7],resTRow[7],resTRow[8],resTRow[8],resTRow[8]],
					[resTRow[6],resTRow[6],resTRow[6],resTRow[7],resTRow[7],resTRow[7],resTRow[8],resTRow[8],resTRow[8]]
					]
	return tempClone

def getTempRowList(B, A):
	tempRowList = B.copy()
	tmp = B.copy()
	tempRowList.clear()
	l = 0

	for x in A:
		j = 0
		for y in x:
			if (y > 0):
				tmp[j] = [y]
			else:
				tmp[j] = B.copy()
			j += 1
		tempRowList.append(tmp.copy())
		l += 1
	return tempRowList

def cloneList(list):
	tempList = [0]
	tmp = [0] * len(list)
	tempList.clear()
	for x in list:
		j = 0
		for y in x:
			tmp[j] = y
			j += 1
		tempList.append(tmp.copy())
	return tempList

def printList(array, name = ''):
	print()
	print(' --- PRINT LIST ', name, ' --- ')
	for temp in array:
		print(temp)
	print(' --- PRINT LIST ', name, ' --- ')
	pass

def decision(A, tempRowList, screen = 0):
	change = 1
	square = 1
	if (len(tempRowList) != 9):
		square = 0
	if (square):
		tmpSquare = defSquare()

	while change > 0:
		k = 0
		l = 0
		change = 0
		varNul = 0
		for row in A:
			i = 0
			for elem in row:
				if elem>0:
					try:
						r = 0
						for temp in range(len(tempRowList)):
							try:
								tempRowList[r][i].remove(elem)
							except ValueError:
								if (screen):
									print('-', r, i, '-', end='')
							try:
								tempRowList[k][r].remove(elem)
							except ValueError:
								if (screen):
									print('-', k, r, '-', end='')
							r += 1

							if (square):
								res = tmpSquare[k][i]
								for item in res:
									try:
										tempRowList[item[0]][item[1]].remove(elem)
									except ValueError:
										if (screen):
											print('-', end='')
					except ValueError:
						if (screen):
							print(' Неверный шаг - откатываемся!')
				else:
					index = i
					varNul += 1
				i += 1
			k += 1

		i = 0
		for stroka in tempRowList:
			j = 0
			for stolbec in stroka:
				if (len(stolbec) == 1):
					if (screen):
						print(i,j,stolbec)
					A[i][j] = stolbec[0]
					change = 1
				j += 1
			i += 1

		if (screen):
			printList(tempRowList)
			printList(A)
		# sleep(0.1)
	if (varNul > 0):
		return [A, tempRowList]
	else:
		out = verificate(A)
		if (out):
			return [1, 1]
		else:
			return [A, tempRowList]

def verificate(array, debug = 0):
	tempRowList = [0]
	tempRowList.clear()
	for i in range(len(array)):
		tempRowList.append(i+1)
	tmpX = [0]
	tmpX.clear()
	tmpY = [0]
	tmpY.clear()

	testX = 1
	testY = 1
	for x in array:
		for y in x:
			tmpX.append(y)
		dif = list(set(tempRowList) - set(tmpX))
		if (debug):
			print('tempRowList - ', tempRowList)
			print('tmpX - ', tmpX)
			print('dif - ', dif)
		tmpX.clear()
		if (len(dif) > 0):
			testX = 0

	arrayTr = list(map(list, zip(*array)))
	for x in arrayTr:
		for y in x:
			tmpY.append(y)
		dif = list(set(tempRowList) - set(tmpY))
		if (debug):
			print('tempRowList - ', tempRowList)
			print('tmpY - ', tmpY)
			print('dif - ', dif)
		tmpY.clear()
		if (len(dif) > 0):
			testY = 0

	if (testX and testY):
		print('----------------------------------- Верификация пройдена!!! -----------------------------------')
		return 1
	else:
		print('----------------------------------- Верификация не прошла!!! -----------------------------------')
		sleep(0.2)
		return 0
