number = 1
while number <= 100:
    if number % 10 == 1 and number != 11:
        print(f"{number} процент")
    elif (number % 10 == 2 or number % 10 == 3 or number % 10 == 4) and number // 10 != 1:
        print(f"{number} процента")
    else:
        print(f"{number} процентов")

    number += 1