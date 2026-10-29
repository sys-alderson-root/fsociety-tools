import hashlib
import os
import sys

# Configuration pour éviter les erreurs d'affichage sur Windows
if os.name == 'nt':
    os.system('')

BANNER = """
    ___________                 __  _          
   / ____/ ___/ /___  ____  _____/ /_(_)__  __  
  / /_   \__ \/ / __ \/ __ \/ ___/ __/ / _ \/ /  
 / __/  ___/ / / /_/ / / / / /__/ /_/ /  __/ /   
/_/    /____/_/\____/_/ /_/\___/\__/_/\___/_/    
                                                 
 [ fs0ciety // hello, friend. ]
 [ PASSWORD HASH ANALYZER - Educational Tool ]
===================================================
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(BANNER)
    print(" [ 1 ] Hacher un mot de passe (Générer les empreintes)")
    print(" [ 2 ] Tester la robustesse d'un mot de passe")
    print(" [ 3 ] Simuler une attaque par dictionnaire sur un hash")
    print(" [ 4 ] Quitter fsociety")
    return input("\n[root@fsociety:~]# ")

def hash_password():
    mdp = input("\n[?] Entrez le mot de passe à hacher : ")
    
    md5_hash = hashlib.md5(mdp.encode()).hexdigest()
    sha1_hash = hashlib.sha1(mdp.encode()).hexdigest()
    sha256_hash = hashlib.sha256(mdp.encode()).hexdigest()
    
    print("\n[+] Génération des empreintes cryptographiques...")
    print(f"    MD5     : {md5_hash}")
    print(f"    SHA-1   : {sha1_hash}")
    print(f"    SHA-256 : {sha256_hash}")
    print("\n[!] Rappel : Un site web ne garde jamais ton mot de passe en clair, il garde ce hash.")
    input("\n[>] Appuie sur Entrée pour retourner au terminal...")

def check_strength():
    mdp = input("\n[?] Entrez le mot de passe à analyser : ")
    score = 0
    
    if len(mdp) >= 12: score += 1
    if any(c.isupper() for c in mdp): score += 1
    if any(c.islower() for c in mdp): score += 1
    if any(c.isdigit() for c in mdp): score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in mdp): score += 1
    
    print(f"\n[+] Analyse terminée. Score de résistance : {score}/5")
    
    if score <= 2:
        print("[-] SYSTÈME VULNÉRABLE : Ce mot de passe sera cassé en quelques secondes.")
    elif score <= 4:
        print("[!] SÉCURITÉ MOYENNE : Il résiste aux attaques basiques, mais reste fragile.")
    else:
        print("[+] SÉCURITÉ MAXIMALE : Impossible à casser avec un simple brute force.")
    
    input("\n[>] Appuie sur Entrée pour retourner au terminal...")

def crack_hash():
    print("\n[?] Entrez un hash (MD5, SHA-1 ou SHA-256) pour tenter de le casser :")
    target_hash = input("> ").strip().lower()
    
    # Wordlist intégrée (les mots de passe les plus courants)
    wordlist = [
        "123456", "password", "admin", "root", "hello", "friend", 
        "fsociety", "elliot", "mrrobot", "azerty", "motdepasse", 
        "123456789", "qwerty", "abc123", "cyber"
    ]
    
    print(f"\n[*] Injection de la wordlist ({len(wordlist)} mots) dans le hachoir...")
    print("[*] Comparaison des empreintes en cours...")
    
    found = False
    for mdp in wordlist:
        if hashlib.md5(mdp.encode()).hexdigest() == target_hash:
            print(f"\n[+] MATCH TROUVÉ (MD5) : Le mot de passe est '{mdp}'")
            found = True
            break
        elif hashlib.sha1(mdp.encode()).hexdigest() == target_hash:
            print(f"\n[+] MATCH TROUVÉ (SHA-1) : Le mot de passe est '{mdp}'")
            found = True
            break
        elif hashlib.sha256(mdp.encode()).hexdigest() == target_hash:
            print(f"\n[+] MATCH TROUVÉ (SHA-256) : Le mot de passe est '{mdp}'")
            found = True
            break
            
    if not found:
        print("\n[-] ÉCHEC : Mot de passe introuvable dans cette wordlist éducative.")
        
    input("\n[>] Appuie sur Entrée pour retourner au terminal...")

def main():
    while True:
        clear()
        choix = menu()
        if choix == "1":
            hash_password()
        elif choix == "2":
            check_strength()
        elif choix == "3":
            crack_hash()
        elif choix == "4":
            print("\n[i] Déconnexion du réseau fsociety...")
            print("[i] Effacement des traces...")
            print("\nAu revoir, friend.")
            break
        else:
            print("\n[-] Commande non reconnue par le système.")
            input("[>] Appuie sur Entrée...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[-] Connexion interrompue brutalement.")
        sys.exit()
