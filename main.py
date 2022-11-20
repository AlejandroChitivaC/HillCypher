import re


def createCharacters():
    # Generating the alphabet and digits
    alp = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
    # Adding the special characters to the list
    alp.append("_")
    return print(alp);


def getMessage():
    # Getting the message from the user
    message = input("Ingrese el mensaje, tenga en cuenta que el espacio está representado por '_' : ")
    if (message == ""):
        print("No ingresó ningún mensaje")
        getMessage()
    if (len(message) > 16):
        print("El mensaje no puede tener más de 16 caracteres")
        message = getMessage()
    specialChar = re.compile(r'[^a-zA-Z0-9_]')
    # Comprobar que el mensaje no contenga caracteres especiales por medio de un Regex
    if specialChar.search(message) or message == "":
        print("Mensaje inválido intente nuevamente")
        return getMessage()
    else:
        print("El mensaje a cifrar es: " + message.upper()),
        key = int(input("Ingrese el tamaño de la clave, puede estar entre 2,3 y 4 caracteres: "))
        if (key < 2 or key > 4):
            print("La clave debe tener entre 2 y 4 caracteres")
            key = int(input("Ingrese el tamaño de la clave, puede estar entre 2,3 y 4 caracteres: "))
        else:
            print("La clave es: " + str(key))
            return convertMessage(message, key)

    return


def convertMessage(msg, k):
    for index in range(len(msg)):
        if index % k == 0:
            sub = msg[index:index + k]
            my_list = []
            for j in sub:
                my_list.append(j)
            print(' '.join(my_list))


def main():
    createCharacters()
    getMessage()


if __name__ == "__main__":
    main()
