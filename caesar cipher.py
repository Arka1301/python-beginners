from art import cc_logo


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
    print(cc_logo)
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