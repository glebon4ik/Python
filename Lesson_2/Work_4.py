new_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in new_list:
    g = list(reversed(i))
    name_revers = g[:g.index(" ")]
    name = list(reversed(name_revers))
    name1 = "".join(name)
    name2 = name1.capitalize()
    message = f'Привет, {name2}!'
    print(message)