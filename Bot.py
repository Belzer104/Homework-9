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

    if len(comand) == 4:

        fullname = f"{comand[1]} {comand[2]}"
        phone = comand[3]
        contacts[fullname] = phone

        return f"Contact {fullname} added"

    elif len(comand) == 3 and comand[2].isdigit():

        firstname = comand[1] 
        phone = comand[2]
        contacts[firstname] = phone

        return f"Contact {firstname} added"
    
    else:
        raise IndexError
    
    
@input_error
def change(comand):

    if len(comand) == 4:

        fullname = f"{comand[1]} {comand[2]}"
        phone = comand[3]
        old_phone = contacts[fullname]
        contacts[fullname] = phone
        
        return f"User {fullname} heve change {old_phone}, new {phone}"
    
    else:

        firstname = comand[1]
        phone = comand[2]
        old_phone = contacts[firstname]
        contacts[firstname] = phone

        return f"User {firstname} heve change {old_phone}, new {phone}"


@input_error
def phone(comand):

    if len(comand) == 3:

        fullname = f"{comand[1]} {comand[2]}" 
        phone = contacts[fullname]

        return f"{fullname}: {phone}"

    else:

        firstname = comand[1]
        phone = contacts[firstname]

        return f"{firstname}: {phone}"


def show_all():

    contact = ""

    for name, phone in contacts.items():
        contact += f"{name}: {phone}\n"

    return contact


def close():
    print("Good bye!")


@error_start
def main():
    bot_start = input("Start bot enter('Hello, Hi, Start'): ").casefold()

    if bot_start == "hello" or bot_start == "hi" or bot_start == "start":
            print(hello())

    else:
        raise ImportError

    while True:

        user_comand = input("Comand to bot ('add, change, phone, show all'): ").casefold()
        comand = user_comand.split()

        if comand[0] == "add":
            print(add(comand))
        
        elif comand[0] == "change":
            print(change(comand))
        
        elif comand[0] == "phone":
            print(phone(comand))

        elif user_comand == "show all":
            print(show_all())
      
        elif user_comand == "exit" or user_comand == "close" or user_comand == "good bye":
            close()
            break
        
        else:
            print("Unknown command or parametrs, please try again")
        
if __name__ == "__main__":
    main()