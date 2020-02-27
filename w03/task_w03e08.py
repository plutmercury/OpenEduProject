def func(s):
    result = ''

    first = s.find('f')

    if first >= 0:
        last = s.rfind('f')
        if first != last:
            result = str(first) + ' ' + str(last)
        else:
            result = str(first)

    return result


s = input()

print(func(s))

