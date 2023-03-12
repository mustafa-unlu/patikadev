# Patika.dev Python-temel egitimi projesi

'''
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[7, 6, 5], [4, 3], [2, 1]]
'''
# COZUM 1
list_1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

li = []


def flatten(n):
    for item in n:
        if isinstance(item, list):
            flatten(item)
        else:
            li.append(item)


flatten(list_1)
print(li)

# COZUM 2
list_2 = [[1, 2], [3, 4], [5, 6, 7]]


def reverse_list(n):
    n = n[::-1]
    n = [item[::-1] for item in n]
    return n


print(reverse_list(list_2))
