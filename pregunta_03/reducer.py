#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

list = []

for row in sys.stdin:
  row_separada = row.split(",")
  list.append((row_separada[0],row_separada[1]))
  list.sort(key=lambda x: x[1])

for tuple in list:
  sys.stdout.write(tuple[0] + "," + str(tuple[1])) 
