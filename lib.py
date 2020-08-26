def choice():
    user_input = input('Would you like to repeat -->')
    if user_input.lower() == 'y':
        return True
    elif user_input.lower() == 'n':
        return False
    else:
        print('Enter "Y" or "N"')
        return choice()



def input_int(i):
    if i.isdigit():
        return int(i)
    else:
        print('You can enter only integers')
