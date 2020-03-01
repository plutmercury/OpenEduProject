# В форме интернет-магазина пользователю нужно ввести свой номер телефона.
# Номер телефона состоит из 10 цифр, однако некоторые пользователи вводят его
# в формате +7145236789, некоторые - 8123456789, а некоторые и вовсе вводят
# только 9 цифр (без первой) 123456789.
#
# Вам необходимо привести номер к стандарту +7123456789
#
# Sample Input:
#
# 8123456789
#
# Sample Output:
#
# +7123456789

phone = input()

phone = '+7123458912'
good_phone = '+7'

if phone.startswith('+7') and len(phone) == 11:
    for s in phone[2:]:
        if s.isdigit():
            good_phone += s

elif phone.startswith('8') and len(phone) == 10:
    for s in phone[1:]:
        if s.isdigit():
            good_phone += s

elif len(phone) == 9:
    for s in phone:
        if s.isdigit():
            good_phone += s

print(good_phone)

