from time import sleep

def sposob(trl, row = 0, kvadrat = 0):
	kvadrat = kvadrat * 3
	row = row * 3
	result = [0]
	result2 = [0]
	result.clear()
	result2.clear()
	for i in range(row, row+3):
		for k in range(kvadrat, kvadrat+3):
			# if (len(trl[i][k]) > 0):
			result.append(list(set(trl[i][k]) & set(result2)))
			result2 = list(set(trl[i][k]) ^ set(result2))
			# print('trl[i][k] - ', trl[i][k],i,k)
			k += 1
		i += 1
	for rem in result:
		for m in rem:
			if m>0:
				try:
					result2.remove(m)
				except ValueError:
					pass
	# print('result - ', result2)
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
		#result=list(set(Word) ^ set(Ans))
	return 1

def defSquare():
	n = 3
	resT = [0]
	resTRow = [0]
	resT.clear()
	resTRow.clear()
	for i in range(0,7,3):
		for k in range(n):
			# print(i,k, [[k,i],[k,1+i],[k,2+i]])
			resT.append([k,i])
			resT.append([k,1+i])
			resT.append([k,2+i])
		resTRow.append(resT.copy())
		resT.clear()

	resT.clear()
	for i in range(0,7,3):
		for k in range(n,n+3):
			# print(i,k, [[k,i],[k,1+i],[k,2+i]])
			resT.append([k,i])
			resT.append([k,1+i])
			resT.append([k,2+i])
		resTRow.append(resT.copy())
		resT.clear()
	resT.clear()
	for i in range(0,7,3):
		for k in range(n+3,n+6):
			# print(i,k, [[k,i],[k,1+i],[k,2+i]])
			resT.append([k,i])
			resT.append([k,1+i])
			resT.append([k,2+i])
		resTRow.append(resT.copy())
		resT.clear()
	# print(resTRow)

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
			# print(l, j, y, end='  ')
			if (y > 0):
				tmp[j] = [y]
			else:
				tmp[j] = B.copy()
			j += 1
		tempRowList.append(tmp.copy())
		# print(tmp)
		l += 1
	return tempRowList

def cloneList(list):
	tempList = [0]
	tmp = [0] * len(list)
	tempList.clear()
	for x in list:
		j = 0
		for y in x:
			# print(l, j, y, end='  ')
			tmp[j] = y
			j += 1
		tempList.append(tmp.copy())
		# print(tmp)
	return tempList

def printList(array, name = ''):
	print()
	print(' --- PRINT LIST ', name, ' --- ')
	for temp in array:
		print(temp)
	print(' --- PRINT LIST ', name, ' --- ')
	pass

def antw(A, tempRowList, screen = 0):
	change = 1
	tmpSquare = defSquare()
	while change > 0:
		k = 0
		l = 0
		# print(' ---  NEW CICLE A - ', tempRow)
		change = 0
		varNul = 0
		for row in A:
			#print()
			# print(' --- NEW CICLE --- ', k)
			i = 0
			# temp = B.copy()
			for elem in row:
				#print()
				# print(' --- NEW ROW --- ', i)
				if elem>0:
					try:
						# print('A - ', A)
						# print('row - ', row)
						# print('tempRow - ', tempRow)
						# print('temp - ', temp)
						# print('k - ', k)
						# print('i - ', i)
						# print('elem - ', elem)
						# temp.remove(elem)
						r = 0
						for temp in range(9):
							try:
								# print('r,i,elem - ', r,i,elem)
								tempRowList[r][i].remove(elem)
							except ValueError:
								if (screen):
									print('-', end='')
							try:
								# print('k,r,elem - ', k,r,elem)
								tempRowList[k][r].remove(elem)
							except ValueError:
								if (screen):
									print('-', end='')
							r += 1

						
							res = tmpSquare[k][i]
							# print('res - ', res)
							for item in res:
								try:
									# print('k,i - ', k,i)
									# print('item,elem - ', item,elem)
									tempRowList[item[0]][item[1]].remove(elem)
								except ValueError:
									if (screen):
										print('-', end='')
						

						# print('tempRow - ', tempRow)
						# print('temp - ', temp)
					except ValueError:
						if (screen):
							print(' Неверный шаг - откатываемся!')
						# A[lastRow][lastIndex] = 0
				else:
					index = i
					varNul += 1
				i += 1

			# print('temp, index, k, A[index][k-1]', temp, index, k, A[k][index])
			# if (len(temp) == 1 and A[k][index] == 0):
			# 	A[k][index] = temp[0]
			# 	change = 1
				# print('temp[0], index, k - ', int(temp[0]), index, k)
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
	tempRowList = [1,2,3,4,5,6,7,8,9]
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
