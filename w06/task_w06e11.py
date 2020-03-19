# Вася составил таблицу с ценами на продукты в разных магазинах. В первой
# строке таблицы (кроме первой ячейки) записаны названия продуктов. Во всех
# строках, начиная со второй, записана информация о ценах в магазине. В первой
# ячейки написано название магазина, а в ячейках, начиная со второй - цена на
# товар, название которого записано в первой строке соответствующего столбца.
#
# Таблица задана как csv-файл, разделителем ячеек выступает точка с запятой, а
# строковые константы не окружаются кавычками.
#
# Вася очень хочет поесть, но денег у него мало. Поэтому помогите ему
# определить самый дешевый продукт и в каком магазине он продается. Название
# продукта следует записать в первой строке, а название магазина - во второй.
# Если несколько товаров стоят одинаково, то выведите то название, которое
# раньше в алфавитном порядке. Если этот товар продается в нескольких магазинах
# по одной минимальной цене, то выведите минимальное в алфавитном порядке
# название магазина.
#
# Ссылка на csv-файл:
# https://stepik.org/media/attachments/lesson/258925/input.csv

fin = open('input_w06e10.csv', 'r', encoding='utf8')

text = fin.read()

lines = list(filter(None, text.split('\n')))

prod_names = lines[0].split(';')

shops = {}

for i in range(1, len(lines)):

    arr_prices = lines[i].split(';')

    shops[arr_prices[0]] = {}

    for j in range(1, len(prod_names)):
        shops[arr_prices[0]][ prod_names[j]] = int(arr_prices[j])

lowest_price = 9999
lowest_price_shop = []
lowest_price_product = []

for shop, prod_price in shops.items():
    for product, price in prod_price.items():
        if price < lowest_price:
            lowest_price = price
            lowest_price_shop = [shop]
            lowest_price_product = [product]
        elif price == lowest_price:
            lowest_price_product.append(product)
            lowest_price_shop.append(shop)

print(sorted(lowest_price_product)[0])
print(sorted(lowest_price_shop)[0])