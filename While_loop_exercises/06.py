length_cake = int(input())
width_cake = int(input())
pieces_cake = length_cake * width_cake

while pieces_cake > 0:
    command = input()

    if command == 'STOP':
        break

    taken_cake = int(command)

    if pieces_cake - taken_cake < 0:
        print(f"No more cake left! You need {abs(pieces_cake - taken_cake)} pieces more.")
        pieces_cake -= taken_cake
        break

    pieces_cake -= taken_cake


if pieces_cake >= 0:
    print(f"{pieces_cake} pieces are left.")