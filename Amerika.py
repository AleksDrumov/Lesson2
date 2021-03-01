one_presidential_term = 4
George_Washington = 2
Thomas_Jefferson = 2
Herbert_Hoover = 1
Barack_Obama = 2
input_count_presidential_term = int(input('Сколько терминов был на посту президент?(больше 2 нельзя)'))
if input_count_presidential_term > 2:
    print('Президент не може бути на посту президента більше 2 термінів')
elif input_count_presidential_term < 1:
    print('Ты что самый/самая умный/умная?!')
else:
    print("Президент правил(шутка про капитализм):", one_presidential_term * input_count_presidential_term)
print("Георгий Вшингтон правил:" ,George_Washington * one_presidential_term)
print("Томас Джефферсон правил:" ,Thomas_Jefferson * one_presidential_term)
print("Герберт Гувер правил:" ,Herbert_Hoover * one_presidential_term)
print("Барак Обама правил:" ,Barack_Obama * one_presidential_term)

