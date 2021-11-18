prices = [99.01, 33.44, 55.66, 11.22, 77.88, 87, 199.50]

print('Основа')
for price in prices:
    print(f'{int(price)} руб {(price - int(price)) * 100:02.0f} коп')

print('Сравнение ID после сортировки')

print(id(prices))
prices.sort()
print(id(prices))

print('Сортировка цен по возрастанию')

for price in sorted(prices):
    print(f'{int(price)} руб {(price - int(price)) * 100:02.0f} коп')

print('Сортировка по убыванию и 5 самых дорогих товаров')

for price in sorted(prices)[::-1][:5]:
    print(f'{int(price)} руб {(price - int(price)) * 100:02.0f} коп')