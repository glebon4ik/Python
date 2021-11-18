list_temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx, name in enumerate(list_temp):
    if name.isdigit():
        digit = list_temp.pop(idx).zfill(2)
        list_temp.insert(idx, f'"{digit}"')
    elif name[1:].isdigit() and (name[0] == '+' or name[0] == '-'):
        digit = list_temp.pop(idx)
        if len(digit) == 2:
            list_temp.insert(idx, f'"{name[0]}{int(name[1]):02}" ')
        elif len(digit) > 2:
            list_temp.insert(idx, f'"{digit}"')

print(' '.join(list_temp))