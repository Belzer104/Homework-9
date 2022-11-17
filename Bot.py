'''
Создаем деккоратор который отлавливает ошибки
(Неверная команда, не достаточно аргументов, не найдены контакты)
'''
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

'''
Создаем словарь для записи телефонной книги
'''
contacts = {}

'''
Создаем функцию "hello" которая будет возвращать ответ 
после того как пользователь запустит бот
'''
def hello():
    return "How can I help you?"

'''
Создаем функцию "add" которая добавляет контакт 
и номер телефона в словарь "contacts", где имя-ключ
телефон-значение
'''
@input_error
def add(comand):

    if len(comand) == 4:

        '''
        Условие если пользователь решил использовать 
        полное имя имя пользователя и его телефон
        '''
       
        fullname = f"{comand[1]} {comand[2]}"
        phone = comand[3]
        contacts[fullname] = phone

        return f"Contact {fullname} added"
    
    elif len(comand) == 3:

        '''
        Условие если пользователь решил использовать 
        просто имя пользователя и его телефон
        '''

        firstname = comand[1] 
        phone = comand[2]
        contacts[firstname] = phone

        return f"Contact {firstname} added"
    
    else:
        raise IndexError
    
'''    
Создаем функцию "change" которая изменяет номер телефона 
на новый (ищет имя пользователя в словаре "contacts" и 
присваивает ключу новое значение тоесть новый номер телефона)
'''    
@input_error
def change(comand):

    if len(comand) == 4:

        '''
        Условие если у пользователя полное имя
        '''

        fullname = f"{comand[1]} {comand[2]}"
        phone = comand[3]
        old_phone = contacts[fullname]
        contacts[fullname] = phone
        
        return f"User {fullname} heve change {old_phone}, new {phone}"
    
    else:

        '''
        Условие если у пользователя только имя и тд
        '''

        firstname = comand[1]
        phone = comand[2]
        old_phone = contacts[firstname]
        contacts[firstname] = phone

        return f"User {firstname} heve change {old_phone}, new {phone}"

'''
Создаем функцию "phone" которая ищет данные по ключу и выводит: 
ключ и текущее значение, которое есть в словаре "contacts" 
'''
@input_error
def phone(comand):

    if len(comand) == 3:

        '''
        Условие если у пользователя полное имя
        '''

        fullname = f"{comand[1]} {comand[2]}" 
        phone = contacts[fullname]

        return f"{fullname}: {phone}"

    else:

        '''
        Условие если у пользователя только имя и тд
        '''

        firstname = comand[1]
        phone = contacts[firstname]

        return f"{firstname}: {phone}"

'''
Создаем функцию "show_all" которая выводит:
всю книгу контактов хранящуюся в словаре "contacts"
'''
def show_all():

    contact = ""

    for name, phone in contacts.items():
        contact += f"{name}: {phone}\n"

    return contact

"""
Создаем функцию "close" которая завершает работу
бота (прирывает цикл в функции "main")
"""
def close():
    print("Good bye!")
    quit()

'''
Создаем фукцию "main" в которой прописана вся логика
взаимодействия пользователя
'''
def main():

    '''
    Ожидается запуск бота
    '''
    bot_start = input("Start bot enter('Hello, Hi, Start'): ").casefold()

    if bot_start in ("hello","hi","start"): 
        '''
        Условия для запуски бота при определенных значениях
        '''  
        print(hello())

        '''
        Бесконечный цикл в котором обрабатываются команды
        '''
        while True:
            '''
            Ожидается действие от пользователя
            '''
            user_comand = input("Comand to bot ('add, change, phone, show all'): ").casefold()
            comand = user_comand.split()

            if comand[0] == "add":
                '''
                Команда для добавления пользователей и их номеров телефонов
                '''
                print(add(comand))
            
            elif comand[0] == "change":
                '''
                Команда для иззменения номеров телефонов, если такой пользователь имеется
                '''
                print(change(comand))
            
            elif comand[0] == "phone":
                '''
                Команда для отображения данных конкретного пользователя
                '''
                print(phone(comand))

            elif user_comand == "show all":
                '''
                Команда для отображения всех добавленых пользователей и их номеров телефонов
                '''
                print(show_all())
        
            elif user_comand == "exit" or user_comand == "close" or user_comand == "good bye":
                '''
                Команда для завершения работы с ботом
                '''
                close()
                
            else:
                '''
                Условие если пользователь вводит ерунду
                '''
                print("Unknown command or parametrs, please try again")
    
    elif bot_start == "exit" or bot_start == "close" or bot_start == "good bye":
        '''
        Условие для закрытия бота если пользователь передумал
        ''' 
        close()

    else:
        '''
        Условие если пользователь не запустил бот
        '''
        print("Bot don't start") 

        
if __name__ == "__main__":
    main()