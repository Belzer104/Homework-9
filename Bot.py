import functools

def error_start(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ImportError:
                pass
    return wrapper

def input_error(func):
    def inner(*args, **kwargs):

        try:           
            return func(*args, **kwargs)
                        
        except KeyError:
            return 'This contact doesnt exist, please try again.'

        except ValueError as exception:
            return exception.args[0]

        except IndexError:
            return 'This contac cannot be added, it exists already'

        except TypeError:
            return 'Unknown command or parametrs, please try again.'
                       
    return inner

contacts = {}

def hello():
    return "How can I help you?"

def add():
    print(274)

def change():
    pass

def phone():
    pass

def show_all():
    return contacts

def close():
    print("Good bye!")
    quit()


@error_start
def main():
    user_comand = input("Start bot enter('Hello, Hi, Start'): ")

    if user_comand.casefold() == "Hello".casefold() or user_comand.casefold() == "Hi".casefold() or user_comand == "Start".casefold():
            print(hello())
    else:
        raise ImportError

    while True:
        user_comand = input("Comand to bot ('add, change, phone, show all'): ").casefold()
        comand = user_comand.split()

        if comand[0] == "add":
            add()

        if user_comand == "show all":
            print(contacts)
      
        if user_comand == "exit" or user_comand == "close" or user_comand == "good bye":
            close()
            break
        
        

if __name__ == "__main__":
    main()