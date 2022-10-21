# Программа для онлайн-конференции, которая подсчитывает общую стоимость билетов.
# numbers_of_tickets количество билетов
# age_of_the_visitor возраст посетителя
ticket_price18 = 0 # цена билета посетителю до 18 лет
ticket_price1825 = 990 # цена билета посетителю от 18 до 25 лет
ticket_price25 = 1390 # цена билета посетителю от 25 лет
total_ticket_price = 0 # общая стоимость билетов
discount = 0.9 # коэффициент-скидка 10% на посещение группы из 3 и более человек
a = 0

numbers_of_tickets = int(input('Введите количество билетов,приобретаемое на мероприятие: \n'))
while a < numbers_of_tickets:
    age_of_the_visitor = int(input('Введите возраст посетителя: '))
    if age_of_the_visitor < 18:
        total_ticket_price += ticket_price18
    if 18 <= age_of_the_visitor < 25:
        total_ticket_price += ticket_price1825
    if age_of_the_visitor >= 25:
        total_ticket_price += ticket_price25
    a += 1

print('Общая сумма: ' + str(total_ticket_price))
if numbers_of_tickets > 3 and total_ticket_price != 0:
    total_ticket_price = total_ticket_price * discount
    print('Сумма к оплате со скидкой: ' + str(total_ticket_price))
else:
    print('Сумма к оплате: ' + str(total_ticket_price))
#13.8.19
