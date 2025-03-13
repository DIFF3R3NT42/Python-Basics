actor_name = input()
academic_points = float(input())
n_evaluators = int(input())

for evaluator in range(n_evaluators):
    name_evaluator = input()
    points_from_evaluator = float(input())
    academic_points += (len(name_evaluator) * points_from_evaluator) / 2

    if academic_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academic_points:.1f}!")
        break

    if evaluator == n_evaluators - 1 and academic_points < 1250.5:
        print(f"Sorry, {actor_name} you need {abs(academic_points - 1250.5):.1f} more!")