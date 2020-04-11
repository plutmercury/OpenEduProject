# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, какое количество элементов этой последовательности, равны ее
# наибольшему элементу.
#
# Формат ввода
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число
# 0 в последовательность не входит, а служит как признак ее окончания).
#
# Формат вывода
# Выведите ответ на задачу.
#
# Подсказка
# Обработайте первое число до цикла. Проверьте случай пустой последовательности.
# Не забывайте устанавливать счетчик максимальных элементов в единицу при
# обновлении максимума.
#
# Sample Input:
#
# 1
# 7
# 9
# 0
#
# Sample Output:
#
# 1

number = int(input())
counter = 1
maximal_number = number

while number != 0:
    number = int(input())
    if number == maximal_number:
        counter += 1
    elif number > maximal_number:
        counter = 1
        maximal_number = number

print(counter)