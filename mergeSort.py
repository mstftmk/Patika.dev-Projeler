"""
[16,21,11,8,12,22] -> Merge Sort

Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
Big-O gösterimini yazınız.

"""

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    result = []
    mid = int(len(arr) / 2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result

soru1 = [16,21,11,8,12,22] 
print(mergeSort(soru1))
"""
Cevaplar:
- Elimizdeki array'i, sürekli ikiye bölerek, array'i en küçük hale getiriyoruz. Daha sonra bunları sıralayıp, array'i tekrar birleştiriyoruz.
- Big-O: O(n log n)
"""