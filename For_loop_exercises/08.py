from statistics import mean

number_of_tournaments = int(input())
initial_points = int(input())
won_tournaments = 0
points_from_tournaments = []

for tournament in range(number_of_tournaments):
    end_resuilt = input()

    if end_resuilt == 'W':
        points_from_tournaments.append(2000)
        won_tournaments += 1

    elif end_resuilt == 'F':
        points_from_tournaments.append(1200)

    elif end_resuilt == 'SF':
        points_from_tournaments.append(720)

print(f"Final points: {initial_points + sum(points_from_tournaments)}")
print(f"Average points: {mean(points_from_tournaments)}")
print(f"{(won_tournaments / number_of_tournaments) * 100}%")