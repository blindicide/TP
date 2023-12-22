in1 = int(input("Введите программу, которую хотите использовать: "))

if in1 == 1:
    inp = float(input("Введите ваш порог CTR:"))

    show1 = 1000000
    show2 = 100000
    cl1 = 983
    cl2 = 4
    ctr1 = float(cl1/show1)
    ctr2 = float(cl2/show2)
    formatted_value = format(ctr2, '.5f')
    print(float(formatted_value))

    a1 = "CTR первого баннера равен " + str(ctr1) + "%, второго - " + str(formatted_value) + "%."
    print(a1)
    if ctr1 > inp:
        print("CTR первого баннера превысил порог.")
    elif ctr1 == inp:
        print("CTR первого баннера равен порогу.")
    else:
        print("CTR первого баннера ниже порога.")
    if ctr2 > inp:
        print("CTR второго баннера превысил порог.")
    elif ctr2 == inp:
        print("CTR второго баннера равен порогу.")
    else:
        print("CTR второга баннера ниже порога.")
elif in1 == 2:
    a = 8
    b = 10
    c = 12
    d = 18
    a = a^2
    outp1 = (a - 3)*(b - 8)
    outp2 = (c - 2)*d
    res = outp1/outp2
    print(res)
elif in1 == 3:
    str1 = input("Введите четыре числа, разделяя их пробелами: ")
    strs = str1.split(' ')
    a1 = int(strs[0])
    a2 = int(strs[1])
    a3 = int(strs[2])
    a4 = int(strs[3])
    aa = a1 + a2
    ab = a3 + a4
    result = aa/ab
    formatted_value = format(result, '.3f')
    outline = "Отношение прибыли за 1-е полугодие к 2-му полугодию: " + str(formatted_value)
    print(outline)
    if result > 1:
        print("Прибыль за второе полугодие снизилась.")
    elif result < 1:
        print("Прибыль за второе полугодие увеличилась.")
    else:
        print("Прибыль за второе полугодие не изменилась.")
elif in1 == 5:
    str1 = input("Введите количество звонков и сообщений за последний месяц.")
    strs = str1.split(' ')
    a1 = int(strs[0])
    a2 = int(strs[1])
    total_expend = 15
    a1 = a1 - 50
    a2 = a2 - 50
    if a1 > 0:
        total_expend += a1*0.25
    else:
        pass
    if a2 > 0:
        total_expend += a2*0.15
    else:
        pass
    total_expend += 0.44
    total_expend *= 1.05
    total_expend = format(total_expend, '.2f')
    result = "Ваш счёт за телефон в этом месяце - " + total_expend + " долларов."
    print(result)
elif in1 == 4:
    in2 = int(input("Введите номинал банкноты: "))
    if in2 == 10:
        print("Красноярск")
    elif in2 == 50:
        print("Санкт-Петербург")
    elif in2 == 100:
        print("Москва")
    elif in2 == 500:
        print("Архангельск")
    elif in2 == 1000:
        print("Ярославль")
    elif in2 == 5000:
        print("Хабаровск")
    elif in2 == 200:
        print("Севастополь")
    elif in2 == 2000:
        print("Владивосток")
    else:
        print("Такой банкноты не существует.")
elif in1 == 6:
    print("")
    print("Старая цена - Сумма скидки - Цена со скидкой")
    price = 4.95
    for i in range(0, 5):
        price += 5*i
        e1 = price*0.4
        e1 = round(e1, 2)
        e2 = price-e1
        e2 = round(e2, 2)
        print(price, '   ', e1, '   ', e2)
elif in1 == 7:
    print('Введите возраста всех посетителей:')
    plist = []
    while True:
        a = input()
        if not a:
            break
        else:
            a = int(a)
            plist.append(a)
    gensum = 0
    for i in plist:
        if i < 3:
            gensum += 0
        elif i >= 3 and i < 12:
            gensum += 140.00
        elif i >= 12 and i < 65:
            gensum += 280.00
        elif i >= 65:
            gensum += 140.00
        else:
            pass
    gensum = round(gensum, 2)
    print('Общая сумма билетов:', gensum, 'рублей')