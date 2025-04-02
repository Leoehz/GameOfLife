from conf import GRID_SIZE, Celula
import time

def contarVecinos(posX, posY, grid):
	cant_vecinos = 0
	#for fila in grid:
	#	print(" ".join(map(str, fila)))

	#print('\n')
	for i in range(-1, 2):
		for j in range(-1, 2):
			posXi, posYj = i + posX, j + posY
			if 0 <= posXi < GRID_SIZE and 0 <= posYj < GRID_SIZE and (i, j) != (0, 0):
	#			print(posXi, posYj, grid[posXi][posYj])
				if (grid[posXi][posYj] == Celula.VIVA):
					cant_vecinos+=1
	#print("Cant vecinos", cant_vecinos, posX, posY)
	#time.sleep(1)
	return cant_vecinos

def muereCelula(cant_vecinos):
	return cant_vecinos > 3 or cant_vecinos <= 1

def naceCelula(cant_vecinos):
	return cant_vecinos == 3

def viveCelula(cant_vecinos):
	return cant_vecinos == 2 or cant_vecinos == 3

def actualizarCeldas(grid):
	old_grid = list(map(list, grid))
	for i in range(GRID_SIZE):
		for j in range(GRID_SIZE):
			cant_vecinos = contarVecinos(i, j, old_grid)
			if muereCelula(cant_vecinos):
				grid[i][j] = Celula.MUERTA
			elif naceCelula(cant_vecinos):
				grid[i][j] = Celula.VIVA
			#elif viveCelula(cant_vecinos) and grid[i][j] == Celula.VIVA:
			#	grid[i][j] = Celula.VIVA

	return grid
