number_of_groups = int(input())
climbing_musala = 0
climbing_monblan = 0
climbing_kilimandjaro = 0
climbing_k2 = 0
climbing_everest = 0
all_people = 0
if 1 > number_of_groups > 1000:
    raise ValueError("The value must be between 1 and 1000")

for i in range(number_of_groups):
    group = int(input())
    if 1 > number_of_groups > 1000:
        raise ValueError("The value must be between 1 and 1000")

    all_people += group

    if group < 6:
        climbing_musala += group
    elif group < 13:
        climbing_monblan += group
    elif group < 26:
        climbing_kilimandjaro += group
    elif group < 41:
        climbing_k2 += group
    elif group >= 41:
        climbing_everest += group


print(f'{(climbing_musala / all_people) * 100:.2f}%')
print(f'{(climbing_monblan / all_people) * 100:.2f}%')
print(f'{(climbing_kilimandjaro / all_people) * 100:.2f}%')
print(f'{(climbing_k2 / all_people) * 100:.2f}%')
print(f'{(climbing_everest / all_people) * 100:.2f}%')
