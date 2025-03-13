age = int(input())
price = float(input())
p = int(input())
brother_tax = 1
accumulated_money = 0
money_for_birthday = 0

for num in range(1, age + 1):

    if num % 2 == 0:
        money_for_birthday += 10
        accumulated_money = accumulated_money + money_for_birthday


    else:
        accumulated_money = accumulated_money + p - brother_tax

if accumulated_money >= price:
    print(f'Yes! {accumulated_money - price:.2f}')

else:
    print(f'No! {abs(accumulated_money - price):.2f}')