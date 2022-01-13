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

def printer(message):
    print(message)
    
def driver():
    x = get_input()
    message = check_HDL(x)
    printer(message)


def interface():
    print("My Program")
    print("Options:")
    print('3 - HDL option')
    print("9 - Quit")
    choice = input("Enter your choice: ")
    if choice = 3:
        driver()
    while choice != 9
        choice == input('Enter another choice: ')
    return
   
interface()