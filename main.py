def function_one(my_string):
    length = len(my_string)
    reversed_string = ""
    for i in range(length):
        reversed_string += my_string[length - i - 1]
    return reversed_string


def function_two(all_integers):
    largest = 0
    for i in range(len(all_integers)):
        if integers[i] > largest:
            largest = integers[i]
    return largest


def function_three(n):
    if n != 1:
        return function_three(n - 1) * n
    return 1


def function_four(n):
    first = 1
    second = 1
    for i in range(n):
        if i >= 2:
            next_entry = first + second
            first = second
            second = next_entry
    return second


if __name__ == '__main__':
    string = "I like poop"
    print(function_one(string))
    integers = [1, 3, 2, 89, 56, 23543245, 6756, 2355, 336457567, 34464567467, 46765756, 7567, 535, 635, 645, 3654, 67,
                546]
    print(function_two(integers))
    print(function_three(3))
    print(function_four(3))
