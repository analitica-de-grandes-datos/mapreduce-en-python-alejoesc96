#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    atrib = {}
    for row in sys.stdin:
        columns = row.split(",")
        if len(columns) == 2:
            letter = columns[0]
            amount = float(columns[1])
            if letter in atrib:
                atrib[letter] = {
                    'max': max(atrib[letter]['max'], amount),
                    'min': min(atrib[letter]['min'], amount)
                }
            else:
                atrib[letter] = {'max': amount, 'min': amount}

    atrib_sort = sorted(atrib.items(), key=lambda x: x[0])
    for atrib, value in atrib_sort:
        sys.stdout.write(f"{atrib}\t{value['max']}\t{value['min']}\n")
