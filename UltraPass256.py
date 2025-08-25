#!/usr/bin/env python3
import secrets
import string
import random

def generate_password(length=256, min_digits=9, min_special=10):
    """
    Génère un mot de passe sécurisé.
    Arguments:
        length (int): longueur totale du mot de passe.
        min_digits (int): nombre minimal de chiffres dans le mot de passe.
        min_special (int): nombre minimal de caractères spéciaux dans le mot de passe.
    Retour:
        str: mot de passe généré.
    """
    if min_digits + min_special > length:
        raise ValueError("La somme des chiffres et des caractères spéciaux minimaux dépasse la longueur totale.")
    
    digits = string.digits
    specials = '!@#$%^&*()_+-='
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    password_chars = []
    password_chars += [secrets.choice(digits) for _ in range(min_digits)]
    password_chars += [secrets.choice(specials) for _ in range(min_special)]

    rest_length = length - len(password_chars)
    password_chars += [secrets.choice(uppercase) for _ in range(rest_length // 2)]
    password_chars += [secrets.choice(lowercase) for _ in range(rest_length - rest_length // 2)]

    random.shuffle(password_chars)
    return ''.join(password_chars)

def main():
    print("UltraPass256 - Générateur sécurisé de mots de passe\n")
    while True:
        try:
            length_input = input("Entrez la longueur désirée pour le mot de passe (entre 32 et 256) : ")
            length = int(length_input)
            if length < 32 or length > 256:
                print("Erreur : la longueur doit être comprise entre 32 et 256 caractères.")
                continue
            break
        except ValueError:
            print("Erreur : merci de saisir un nombre entier valide.")

    password = generate_password(length=length)
    print("\nMot de passe généré :\n")
    print(password)

if __name__ == "__main__":
    main()
