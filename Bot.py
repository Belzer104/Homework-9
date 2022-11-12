# def handler():



def main():
    contact = dict()
    user_comand = input("Start bot: enter ('Hello, Hi, Start'): ")
    while True:
        if user_comand.casefold() == "Hello".casefold() or user_comand.casefold() == "Hi".casefold() or user_comand.casefold() == "Start".casefold():
            print("How can I help you?")
        user_comand = input()
        if user_comand.casefold() == "exit".casefold() or user_comand.casefold() == "close".casefold() or user_comand.casefold() == "good bye".casefold():
            print("Good bye!")
            break  
        



if __name__ == "__main__":
    main()