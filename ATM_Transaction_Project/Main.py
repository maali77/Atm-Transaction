from objects import Atm

def main():
    while True:
        print("Hello!..")
        first = input("Please enter your fist name: ")
        idNumber = input("Enter a valid ID number: ")
        
        customer = Atm(first,idNumber)
        customer.showMenu()
        keepGoing = input("Contiue? (y/n): ")
        
        if keepGoing == 'n':
            print("Exiting the program now!/nBYE!")
            break
    
if __name__ == '__main__':
        main()
