"""Написать генератор нечётных чисел от 1 до n (включительно),
используя ключевое слово yield"""
numlist = []

def odd_to(num_max):
    for num in range(1, num_max+1):
        numlist.append(num)
        num = num+2
        return odd_to(num_max)
    else:
        return None
odd_to(20)
print(numlist)