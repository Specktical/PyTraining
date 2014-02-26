#coding=utf-8
#-------------------------START OF INPUT---------------------------------#
in_time = raw_input("Введите входное время в формате ЧЧ:мм или ММ:сс и укажите их тип (h-час или m-минуты): ")
in_items1 = in_time.split(' ')
convert_to = raw_input("Конвертировать в (m,s,h): ")
convert_to = str(convert_to)
if convert_to not in ('m', 's', 'h'):
    print 'Не верный формат ввода (введите h - для получения в часах m - для минут, s - для секунд'
    exit()
#---------------------------DEFAULT VARS---------------------------------#
time_format = 0
time = 0
in_master = 0
in_secondary = 0
h_to_m = 0
h_to_s = 0
m_to_s = 0
m_to_h = 0
s_to_m = 0
s_to_h = 0
l_seconds = 'секунд'
#---------------------------PARSING INPUT--------------------------------#
if len(in_items1) == 2:
    time = in_items1[0]
    time_format = in_items1[1]
    time_format = str(time_format)
    if not time.isdigit() and time.isalpha():
        print('Должны быть введены часы/минуты, минуты и секунды или просто секунды. Данные не верны.')
        exit()
elif len(in_items1) == 1:
    time = in_items1[0]
    time_format = 's'
    print('Не было введено разделителей и якоря (h,m,s) - работаю как с секундами.')
else:
    print('Введены не корректные данные')

if time_format == 's':
    in_items2 = 0
    in_master = float(time)
    print(in_master)
elif not time.isdigit():
    in_items2 = time.split(':')
    in_master = int(in_items2[0])
    in_secondary = int(in_items2[1])
else:
    in_master = int(in_items1[0])
    time_format = str(in_items1[1])
    in_secondary = int(0)
#---------------------------CALCULATE DATA-------------------------------#
if time_format == "h":
    print('Конвертирование из часов')
    if convert_to == 'm':
        print('в минуты')
        h_to_m = in_master * 60
        h_to_m += in_secondary
        print('{} {}'.format(h_to_m, 'минут'))
    elif convert_to == 's':
        print('в секунды')
        h_to_s = int(in_master) * 60 * 60
        h_to_s += int(in_secondary) * 60
        print("{} {}".format(h_to_s, 'секунд'))
    else:
        print('При конвертировании из часов - что то пошло не так.')
if time_format == 'm':
    print('Конвертирование из минут')
    if convert_to == 's':
        print('в секунды')
        m_to_s = in_master * 60
        m_to_s += in_secondary
        print('{} {}'.format(m_to_s, 'секунд'))
    elif convert_to == 'h':
        print('в часы')
        m_to_h = float(in_master) / 60
        print(m_to_h)
        m_to_h += float(in_secondary)
        print(type(m_to_h))
        print('{} {}'.format(float(m_to_h), 'часов'))
    else:
        print('При конвертировании из минут - что то пошло не так.')
if time_format == 's':
    print('Конвертирование из сенунд')
    if convert_to == 'm':
        print('в минуты')
        s_to_m = float(in_master) / 60
        print('{} {}'.format(s_to_m, 'минут'))
    elif convert_to == 'h':
        print('в часы')
        s_to_h = float(in_master) / 60 / 60
        print('{} {}'.format(round(float(s_to_h), 2), 'часов'))
    else:
        print('При конвертировании из секунд - что то пошло не так.')
