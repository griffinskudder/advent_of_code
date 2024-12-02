import csv
from collections import Counter
from functools import reduce


def main():
    column_0 = []
    column_1 = []
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            row = line.strip().split('   ')
            column_0.append(int(row[0]))
            column_1.append(int(row[1]))
    column_0.sort() # sort in place
    column_1.sort()
    result_part_1 = 0
    for i in range(0, len(column_0)):
        result_part_1 += abs(column_0[i] - column_1[i])
    
    column_1_counts = Counter(column_1)
    
    result_part_2 = 0
    for value in column_0:
        result_part_2 += (value * column_1_counts.get(value, 0))
    
    return result_part_1, result_part_2
            

if __name__ == '__main__':
    print(main())