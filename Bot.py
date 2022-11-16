import functools

def error_start(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ImportError:
                print("Bot don't start")
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
            return 'This contac cannot be added, please write user or phone'

        except TypeError:
            return 'Unknown command or parametrs, please try again.'
                       
    return inner

contacts = {}

def hello():
    return "How can I help you?"

@input_error
def add(comand):
    if comand == 4:
        fullname = f"{comand[1]} {comand[2]}"
        phone = comand[3]
        contacts[fullname] = phone
        return f"Contact {fullname} added"
    else:
        firstname = comand[1] 
        phone = comand[2]
        contacts[firstname] = phone
        return f"Contact {firstname} added"
    
    
@input_error
def change(comand):
    firstname = comand[1]
    phone = comand[2]
    old_phone = contacts[firstname]
    contacts[firstname] = phone
    return f"User {firstname} heve change {old_phone}, new{phone}"

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
        
        if comand[0] == "change":
            print(change(comand))

        if user_comand == "show all":
            print(show_all())
      
        if user_comand == "exit" or user_comand == "close" or user_comand == "good bye":
            close()
            break
        
        

if __name__ == "__main__":
    main()