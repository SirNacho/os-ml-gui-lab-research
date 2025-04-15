#This is a python script mostly to clean tokens and response
#1/21/2025 edit: Should probably clean this code itself, it look crappy... Can't blame myself tho, I wrote this in my early freshman year.

def check_Input(the_input):
    if the_input == "":
        output = input("Can you repeat that? Use 'y' or 'n': ")
        return check_Input(output)

    if the_input.lower() == "yes" or the_input.lower() == "y":
        return True

    elif the_input.lower() == "no" or the_input.lower() == "n":
        return False

    else:
        output = input("Can you repeat that? Use 'y' or 'n': ")
        return check_Input(output)

def check_int(the_input):
    if the_input == "":
        output = input("Can you repeat that? Please put your answer in numbers: ")
        return check_int(output)

    try:
        int(the_input)
    except ValueError:
        output = input("Can you repeat that? Please put your answer in numbers: ")
        return check_int(output)

    the_input = check_space(the_input, "int")
    try:
        return int(the_input)
    except ValueError:
        output = input("Can you repeat that? Please put your answer in numbers: ")
        return check_int(output)

def check_str(the_input, space_check: bool):
    if the_input == "":
        output = input("Can you repeat that? Please put your answer in words: ")
        return check_str(output, space_check)

    try:
        str(the_input)
    except ValueError:
        output = input("Can you repeat that? Please put your answer in words: ")
        return check_str(output, space_check)

    if the_input.isdigit():
        output = input("Can you repeat that? Please put your answer in words: ")
        return check_str(output, space_check)

    if space_check:
        the_output = check_space(the_input, "str")

        try:
            return str(the_output).lower()
        except ValueError:
            output = input("Can you repeat that? Please put your answer in words: ")
            return check_str(output, space_check)

    else:
        return the_input.lower()

def check_space(the_input, value_check : str):
    if the_input == "":
        output = input("Can you repeat that? Please don't use spaces: ")
        return check_space(output, value_check)

    if " " in the_input:
        output = input("Can you repeat that? Please don't use spaces: ")
        return check_space(output, value_check)

    if value_check == "int":
        try:
            return int(the_input)
        except ValueError:
            output = input("Can you repeat that? Please put your answer in numbers: ")
            return check_space(output, value_check)

    if value_check == "str":
        try:
            if the_input.isdigit():
                output = input("Can you repeat that? Please put your answer in words: ")
                return check_space(output, value_check)

            return str(the_input)
        except ValueError:
            output = input("Can you repeat that? Please put your answer in words: ")
            return check_space(output, value_check)

    return the_input