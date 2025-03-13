from statistics import mean
unsatisfactory_grades_threshold = int(input())
unsatisfactory_grades = 0
grades = []
problems = []

while unsatisfactory_grades < unsatisfactory_grades_threshold:
    problem = input()
    if problem == 'Enough':
        print(f"Average score: {mean(grades):.2f}")
        print(f"Number of problems: {len(problems)}")
        print(f"Last problem: {problems[-1]}")
        break

    problems.append(problem)
    grade = int(input())
    grades.append(grade)
    if grade <= 4:
        unsatisfactory_grades += 1


if unsatisfactory_grades == unsatisfactory_grades_threshold:
    print(f"You need a break, {unsatisfactory_grades} poor grades.")