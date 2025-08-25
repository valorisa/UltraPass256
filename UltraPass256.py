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
        raise ValueError("La somme des chiffres et des caractères spéciaux minimal dépasse la longueur totale.")

    # Définir les ensembles de caractères
    digits = string.digits
    specials = '!@#$%^&*()_+-='
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    all_chars = uppercase + lowercase + digits + specials
    
    # Générer la base du mot de passe avec les contraintes minimales
    password_chars = []
    password_chars += [secrets.choice(digits) for _ in range(min_digits)]
    password_chars += [secrets.choice(specials) for _ in range(min_special)]
    password_chars += [secrets.choice(uppercase) for _ in range((length - min_digits - min_special)//2)]
    password_chars += [secrets.choice(lowercase) for _ in range(length - len(password_chars))]

    # Mélanger pour éviter tout ordre prévisible
    random.shuffle(password_chars)
    return ''.join(password_chars)

def main():
    password = generate_password()
    print("Mot de passe généré :\n")
    print(password)

if __name__ == "__main__":
    main()
