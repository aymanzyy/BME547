def get_input():
    print("My Program: Enter something please")
    choice = input("Enter your choice: ")
    return choice
    
def check_HDL(input):
    if input  >= 60:
        return('Normal')
    elif input >=40 and input < 60 :
        return('Borderline Low')
    else:
        return('Low')
        