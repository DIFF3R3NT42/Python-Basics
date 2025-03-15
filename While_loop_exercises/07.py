width = int(input())
length = int(input())
height = int(input())
size = width * length * height

while size > 0:
    box = input()
    if box == 'Done':
        if size >= 0:
            print(f"{size} Cubic meters left.")
        break
    integer_box = int(box)
    size -= integer_box
    if size - integer_box <= 0:
        print(f"No more free space! You need {abs(size)} Cubic meters more.")

