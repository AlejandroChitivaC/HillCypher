import re


def createCharacaters():
    # Generating the alphabet and digits
    alp = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
    # Adding the special characters to the list
    alp.append("_")
    # print(len(alp))
    return print(alp);


def getMessage():
    # Getting the message from the user
    message = input("Ingrese el mensaje: ")
    specialChar = re.compile(r'[^a-zA-Z0-9_]')
    #Comprobar que el mensaje no contenga caracteres especiales por medio de un Regex
    if specialChar.search(message) or message == "":
        print("Mensaje inválido intente nuevamente")
        return getMessage()
    else:
        return print(message.upper())



createCharacaters()
getMessage()