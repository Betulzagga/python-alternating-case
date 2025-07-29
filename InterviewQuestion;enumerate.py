def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter
        else:
            new_string += letter.upper()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")
