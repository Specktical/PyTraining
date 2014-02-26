#coding:utf-8
####### LANG
lang_input_money = "Введите кол-во наличных денег"
doubledot = ": "
lang_buy = 'Куплено'

money = raw_input(lang_input_money + doubledot)
if not money.isdigit() and money.isalpha():
    print("Введены не верные данные")
    exit()
money = float(money)
snickers = 4.25
water = 1.99
gum = 0.11
snickers_total = []
water_total = []
gum_total = []
x_snickers_total = 0
x_run = 0

while True:
    if money > (water + snickers):
        money -= (snickers + water)
        x_snickers_total += 1
        x_run += 1
        water_total.append(1)
    elif money > water:
        money -= water
        water_total.append(1)
        x_run += 1
    elif money > gum:
        money -= gum
        gum_total.append(1)
        x_run += 1
    else:
        if money < 0.1:
            print("{} {} сникерсов, {} бутылок воды и {} жевачек, за {} походов в магазин. Денег не осталось вовсе"
                .format(lang_buy, x_snickers_total, sum(water_total), sum(gum_total), x_run))
        else:
            print("{} {} сникерсов, {} бутылок воды и {} жевачек. Остаток денег {} UAH. В магазин - ходили {} раз"
              .format(lang_buy, x_snickers_total, sum(water_total), sum(gum_total), round(money, 2), x_run))
        break