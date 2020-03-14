# Некоторый банк хочет внедрить систему управления счетами клиентов,
# поддерживающую следующие операции:
#
# Пополнение счета клиента. Снятие денег со счета. Запрос остатка средств на
# счете. Перевод денег между счетами клиентов. Начисление процентов всем
# клиентам.
#
# Вам необходимо реализовать такую систему. Клиенты банка идентифицируются
# именами (уникальная строка, не содержащая пробелов). Первоначально у банка
# нет ни одного клиента. Как только для клиента проводится операция пололнения,
# снятия или перевода денег, ему заводится счет с нулевым балансом. Все
# дальнейшие операции проводятся только с этим счетом. Сумма на счету может
# быть как положительной, так и отрицательной, при этом всегда является целым
# числом.
#
# Входной данные содержат количество и последовательность операций. Возможны
# следующие операции:
# DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента
# нет счета, то счет создается.
# WITHDRAW name sum - снять сумму sum со счета клиента name. Если у клиента нет
# счета, то счет создается.
# BALANCE name - узнать остаток средств на счету клиента name.
# TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет
# клиента name2. Если у какого-либо клиента нет счета, то ему создается счет.
# INCOME p - начислить всем клиентам, у которых открыты счета, p от суммы
# счета. Проценты начисляются только клиентам с положительным остатком на
# счету, если у клиента остаток отрицательный, то его счет не меняется. После
# начисления процентов сумма на счету остается целой, то есть начисляется
# только целое число денежных единиц. Дробная часть начисленных процентов
# отбрасывается.
#
# Для каждого запроса BALANCE программа должна вывести остаток на счету данного
# клиента. Если же у клиента с запрашиваемым именем не открыт счет в банке,
# выведите ERROR.
#
# Sample Input:
#
# 7
# DEPOSIT Ivanov 100
# INCOME 5
# BALANCE Ivanov
# TRANSFER Ivanov Petrov 50
# WITHDRAW Petrov 100
# BALANCE Petrov
# BALANCE Sidorov
#
# Sample Output:
#
# 105
# -50
# ERROR


N = int(input()) # количество операций

operations = []
for _ in range(N):
    operations.append(input())

"""
operations = [
    'DEPOSIT Ivanov 100',
    'INCOME 5',
    'BALANCE Ivanov',
    'TRANSFER Ivanov Petrov 50',
    'WITHDRAW Petrov 100',
    'BALANCE Petrov',
    'BALANCE Sidorov',
    'DEPOSIT Sidorov 200',
    'INCOME 10'
]
"""
accounts = {}


def parse_operation(operation):
    w = operation.split()
    return w[0], w[1:]


def deposit(params):
    if not params[0] in accounts:
        accounts[params[0]] = 0

    accounts[params[0]] += int(params[1])


def income(params):
    for account in accounts:
        if accounts[account] > 0:
            accounts[account] += int(accounts[account] * (int(params[0]) / 100))


def balance(params):
    if params[0] in accounts:
        print(accounts[params[0]])
    else:
        print('ERROR')


def transfer(params):
    if not params[0] in accounts:
        accounts[params[0]] = 0

    if not params[1] in accounts:
        accounts[params[1]] = 0

    accounts[params[0]] -= int(params[2])
    accounts[params[1]] += int(params[2])


def withdraw(params):
    if not params[0] in accounts:
        accounts[params[0]] = 0

    accounts[params[0]] -= int(params[1])


for operation in operations:
    verb, params = parse_operation(operation)
    if verb == 'DEPOSIT':
        deposit(params)
    elif verb == 'INCOME':
        income(params)
    elif verb == 'BALANCE':
        balance(params)
    elif verb == 'TRANSFER':
        transfer(params)
    elif verb == 'WITHDRAW':
        withdraw(params)
    else:
        print('ERROR')

