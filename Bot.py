import functools

def input_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except IndexError:    
                print("Please start bot")
    return wrapper


@input_error
def main():
    contact = dict()
    user_comand = input("Start bot: enter ('Hello, Hi, Start'): ")

    if user_comand.casefold() == "Hello".casefold() or user_comand.casefold() == "Hi".casefold() or user_comand.casefold() == "Start".casefold():
            print("How can I help you?")
    else:
        raise IndexError

    while True:
        user_comand = input("Comand to bot ('add, change, phone, show all'): ")
        comand = user_comand.split()

        

        if user_comand.casefold() == "show all".casefold():
            print(contact)
      
        if user_comand.casefold() == "exit".casefold() or user_comand.casefold() == "close".casefold() or user_comand.casefold() == "good bye".casefold():
            print("Good bye!")
            break  
        



if __name__ == "__main__":
    main()