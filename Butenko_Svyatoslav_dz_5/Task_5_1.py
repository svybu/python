"""Написать генератор нечётных чисел от 1 до n (включительно),
используя ключевое слово yield"""
def odd_to(num_max):
    for num in range(1, num_max + 1, 2):
        yield num

for num in odd_to(20):
    print(num)