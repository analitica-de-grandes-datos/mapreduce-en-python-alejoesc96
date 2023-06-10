#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for row in sys.stdin:
        columnas = row.split("   ")
        letra = columnas[0]
        valor = columnas[2]
        sys.stdout.write(f"{letra},{valor}\n")
