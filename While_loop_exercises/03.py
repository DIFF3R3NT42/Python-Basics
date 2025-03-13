excursion_price = float(input())
current_balance = float(input())
spending_counter = 0
day_counter = 0

while current_balance < excursion_price and spending_counter < 5:
    action = input()
    money = float(input())
    day_counter += 1

    if action == 'spend':
        spending_counter += 1
        current_balance -= money
        if current_balance < 0:
            current_balance = 0

    if action == 'save':
        spending_counter = 0

        current_balance += money

if spending_counter == 5:
    print(f"You can't save the money.")
    print(f'{day_counter}')

if current_balance >= excursion_price:
    print(f"You saved the money for {day_counter} days.")