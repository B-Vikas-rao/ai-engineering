def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    print("Sum =", total)

add(10, 20)
add(10, 20, 30)
add(1, 2, 3, 4, 5)