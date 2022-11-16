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