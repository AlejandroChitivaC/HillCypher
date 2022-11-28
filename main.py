import math

import numpy
from numpy.linalg import det
import sympy
import re

# Diccionarios de Encriptacion y Desencriptacion
encrypt = {
    'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4', 'F': '5', 'G': '6', 'H': '7', 'I': '8', 'J': '9', 'K': '10',
    'L': '11', 'M': '12', 'N': '13', 'O': '14', 'P': '15', 'Q': '16', 'R': '17', 'S': '18', 'T': '19', 'U': '20',
    'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25', '0': '26', '1': '27', '2': '28', '3': '29', '4': '30',
    '5': '31', '6': '32', '7': '33', '8': '34', '9': '35', '_': '36'
}
decrypt = {
    '0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K',
    '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U',
    '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': '0', '27': '1', '28': '2', '29': '3', '30': '4',
    '31': '5', '32': '6', '33': '7', '34': '8', '35': '9', '36': '_'
}


# Metodo para obtener el mensaje a cifrar
def getMessage():
    message = input("Ingrese el mensaje, tenga en cuenta que el espacio está representado por '_' : ").upper()
    if (message == ""):
        print("No ingresó ningún mensaje")
        getMessage()
    if (len(message) > 16):
        print("El mensaje no puede tener más de 16 caracteres")
        message = getMessage()
    specialChar = re.compile(r'[^a-zA-Z0-9_]')
    if specialChar.search(message) or message == "":
        print("Mensaje inválido intente nuevamente")
        return getMessage()
    else:
        print("El mensaje a cifrar es: " + message.upper()),
        keySize = int(input("Ingrese el tamaño de la clave, puede estar entre 2,3 y 4 caracteres: "))
        if (keySize > 4 or keySize < 2 or keySize == str):
            keySize = int(input("El tamaño de la clave debe ser un número entero entre 2 y 4: "))
        while (keySize < 2 or keySize > 4):
            print("La clave debe tener entre 2 y 4 caracteres")
            keySize = int(input("Ingrese el tamaño de la clave, puede estar entre 2,3 y 4 caracteres: "))
        else:
            print("El tamaño de la clave es: " + str(keySize))
            key = input("Ingrese la clave: ")
            while (len(key) != (keySize * keySize)):
                print("La clave debe tener " + str(keySize * keySize) + " caracteres")
                key = input("Ingrese la clave: ")
            else:
                key = key.upper()
                print("La clave es: " + key)
                letterToNumber(message)
                letterToNumber(key)
                print('--------------------------------------- \n'
                      'Matriz de la clave: ')
                keyMatrix = createKeyMatrix(key, keySize)
                print('--------------------------------------- \n'
                      'Matriz del mensaje: ')
                messageMatrix = createMessageMatrix(message, keySize)
                print(encryptMessage(message, key))
            return


def createKeyMatrix(key, keySize):
    keyMatrix = []
    key = letterToNumber(key)
    for i in range(keySize):
        keyMatrix.append(key[keySize * i:keySize * (i + 1)])
    print("Matriz de la clave: ")
    print(numpy.transpose(keyMatrix))
    return keyMatrix


def createMessageMatrix(message, keySize):
    messageMatrix = []
    message = letterToNumber(message)
    for i in range(keySize):
        messageMatrix.append(message[keySize * i:keySize * (i + 1)])
    while len(messageMatrix[-1]) != keySize:
        messageMatrix[-1].append('26')
    print("Matriz del mensaje: ")
    print(numpy.transpose(messageMatrix))
    return messageMatrix


def letterToNumber(message):
    message = message.upper()
    new_message = []
    for i in message:
        new_message.append(encrypt[i])
        print(new_message)
    return new_message


# Funcion para dividir el mensaje en grupos de tamaño de la clave
def createGroups(message, keySize):
    groups = []
    for i in range(0, len(message), keySize):
        groups.append(message[i:i + keySize])
    return groups

# Metodo para cifrar el mensaje con la clave


def main():
    opc = input("Seleccione una opcion \n 1. Cifrar \n 2. Descifrar \n")
    if (opc == "1"):
        print("Cifrar por medio de Hill Cipher")
        getMessage()

    elif (opc == "2"):
        print("Descifrar")
    elif (opc != "1" or opc != "2"):
        print("ADVERTENCIA: Ingrese una opción válida, 1 para Cifrar y 2 para Descifrar")
        main()


if __name__ == "__main__":
    main()
