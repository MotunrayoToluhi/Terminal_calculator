import sys


def get_num_1():
    try:
        global num_1
        num_1 = int(input("Input first number: "))
    except ValueError:
        print("Please enter a number")
        get_num_1()
    return num_1


def get_num_2():
    try:
        global num_2
        num_2 = int(input("Input second number: "))
    except ValueError:
        print("Please enter a number")
        get_num_2()

    return num_2


def add():
    user_inputs = get_num_1(), get_num_2()
    num_1 = user_inputs[0]
    num_2 = user_inputs[1]
    add_ans = int(num_1) + int(num_2)
    print(add_ans)
    pass


def subtract():
    user_inputs = get_num_1(), get_num_2()
    num_1 = user_inputs[0]
    num_2 = user_inputs[1]
    sub_ans = int(num_1) - int(num_2)
    print(sub_ans)
    pass


def multi():
    user_inputs = get_num_1(), get_num_2()
    num_1 = user_inputs[0]
    num_2 = user_inputs[1]
    mult_ans = int(num_1) * int(num_2)
    print(mult_ans)
    pass


def division():
    user_inputs = get_num_1(), get_num_2()
    num_1 = user_inputs[0]
    num_2 = user_inputs[1]
    div_ans = int(num_1) / int(num_2)
    print(div_ans)
    pass


def run():
    try:
        global chosen_operation
        chosen_operation = int(input("""Choose an operation or exit the calculator: 
        1. Add 
        2. Subtract 
        3. Multiply 
        4. Divide 
        5. Exit 
        """))
    except ValueError:
        print("Please enter either 1, 2 ,3 ,4 or 5")
        run()

    if int(chosen_operation) == 1:
        add()
        run()
    elif int(chosen_operation) == 2:
        subtract()
        run()
    elif int(chosen_operation) == 3:
        multi()
        run()
    elif int(chosen_operation) == 4:
        division()
        run()
    elif int(chosen_operation) == 5:
        sys.exit(0)
    elif chosen_operation not in [1, 2, 3, 4, 5]:
        print("Please enter either 1, 2 ,3 , 4 or 5")
        run()
    else:
        pass


run()
