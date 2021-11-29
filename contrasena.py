# Natalia Andrea Flores Perez
# 29/10/21

def validar_contrasena(password):
    """ Verificación de contraseña """
    characters_adm = 0
    no_characters = 0
    digit = 0
    if len(password) == 8:
        for charac in password:
            if charac == 'b':
                characters_adm += 1
            elif charac == 'k':
                no_characters += 1
            elif charac == '*' or charac == '+' or charac == '%':
                digit += 1
        return characters_adm >= 2 and no_characters == 1 and digit == 1
    else:
        print("ERROR: Password length must be 8 characters")
        return False

user_input = u'Natbb*ks'
#user_input = input("Enter your password: \n")
if (validar_contrasena(user_input)): 
    print("Password is valid") 
else: 
    print("Invalid Password!!") 

