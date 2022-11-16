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
            return 'This contac cannot be added, please add phone'

        except TypeError:
            return 'Unknown command or parametrs, please try again.'
                       
    return inner

contacts = {}

def hello():
    return "How can I help you?"

@input_error
def add(comand):
    name = comand[1] 
    phone = comand[2]
    contacts[name] = phone
    return f"Contact {name} added"
    

def change(comand):
    pass

def phone(comand):
    pass

def show_all():
    contact = ""
    for name, phone in contacts.items():
        contact += f"{name}: {phone}\n"
    return contact

def close():
    print("Good bye!")


@error_start
def main():
    bot_start = input("Start bot enter('Hello, Hi, Start'): ")

    if bot_start.casefold() == "Hello".casefold() or bot_start.casefold() == "Hi".casefold() or bot_start == "Start".casefold():
            print(hello())
    else:
        raise ImportError

    while True:
        user_comand = input("Comand to bot ('add, change, phone, show all'): ").casefold()
        comand = user_comand.split()

        if comand[0] == "add":
            print(add(comand))

        if user_comand == "show all":
            print(show_all())
      
        if user_comand == "exit" or user_comand == "close" or user_comand == "good bye":
            close()
            break
        
        

if __name__ == "__main__":
    main()