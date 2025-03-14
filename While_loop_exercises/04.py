steps_a_day = 10000
steps = 0
while steps < steps_a_day:
    command = input()
    if command == 'Going home':
        progress = int(input())
        steps += progress
        if steps < steps_a_day:
            print(f"{abs(steps - steps_a_day)} more steps to reach goal.")
        break
    else:
        steps += int(command)

if steps >= steps_a_day:
    print(f"Goal reached! Good job!")
    print(f"{steps - steps_a_day} steps over the goal!")