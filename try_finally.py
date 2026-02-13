def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return 
    
    except ValueError:
        print("Error: Enter an Integer")
        return 

    finally:
        print("Thank you!")

main()