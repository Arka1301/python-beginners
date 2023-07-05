logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text,shift):
    new = ''
    for ch in text:
        if ch.isalpha():
            newloc = alphabet.index(ch)+shift
            if newloc > 25:
                newloc %= 26
            new+=alphabet[newloc]
        else:
            new += ch
    print(f"The encoded message is: {new}")

def decrypt(text,shift):
    new = ''
    for ch in text:
        if ch.isalpha():
            newloc = alphabet.index(ch)-shift
            new+=alphabet[newloc]
        else:
            new+=ch
    print(f"The encoded message is: {new}")

def main():
    print(logo)
    op = 'yes'
    while op == 'yes':
        choice = input("Type 'encode to encrypt, type 'decode' to decrypt:\n")
        st = input("Enter the word: ").lower()
        sh = int(input("Enter the shift: "))
        if choice == 'encode':
            encrypt(st,sh)
        elif choice == 'decode':
            decrypt(st,sh)
        else:
            print("Wrong choice")
        op = input("Do you want to restart the cipher program? \nType yes to go again, otherwise type no.\n")

main()