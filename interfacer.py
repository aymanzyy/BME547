def get_input():
    print("Enter  HDL")
    choice = input("Enter your choice: ")
    return choice
    
def check_HDL(input):
    if input  >= 60:
        return('Normal')
    elif input >=40 and input < 60 :
        return('Borderline Low')
    else:
        return('Low')

def check_LDL(input):
    if input < 130:
        print('Normal')
    elif input >= 130 and input <160:
        print('Borderline High')
    elif input >= 160 and input <190:
        print('High')
    elif input >= 190:
        print("Very high")


def printer(message):
    print(message)
    
def driver():
    x = get_input()
    message = check_HDL(x)
    printer(message)

def ldl_driver():
    x = get_input()
    check_LDL(x)


def interface():
    print("My Program")
    print("Options:")
    print('3 - HDL option')
    print('5 - LDL option')
    print("9 - Quit")
    choice = input("Enter your choice: ")
    if choice == 3:
        driver()
    elif choice ==5:
        driver()

    while choice != 9:
        choice == input('Enter another choice: ')
    return
if __name__ == "__main__":
    interface()