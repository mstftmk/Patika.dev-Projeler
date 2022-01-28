"""
[22,27,16,2,18,6] -> Insertion Sort

Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
Big-O gösterimini yazınız.
Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.


[7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.

"""

def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i-1
      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         j -= 1
      arr[j+1] = key
      print(arr)



soru1 = [22,27,16,2,18,6]
soru2 = [7,3,5,8,2,9,4,15,6]

insertionSort(soru1)
#cevaplar:
#1'den n e kadar iterate ediyoruz.indexteki sayıyı bir önceki ile karşılaştırıyoruz.Eğer önceki sayıdan küçük ise, yerlerini değiştiriyoruz.
#Time Complexity: O(n^2) 
#Sıralandıktan sonra 18 eklenmesi "Average Case"
insertionSort(soru2)
#cevaplar:
#1'den n e kadar iterate ediyoruz.indexteki sayıyı bir önceki ile karşılaştırıyoruz.Eğer önceki sayıdan küçük ise, yerlerini değiştiriyoruz.
#Time Complexity: O(n^2) 
#Sıralandıktan sonra 18 eklenmesi "Worst Case"