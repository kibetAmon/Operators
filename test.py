def main():
    print("This program converts a text message to sequence")
    message = input("please enter the message to encode: ")
    for ch in message:
        print("\nHere are the unicode codes: ")
        print(ord(ch), end=" ")
    print()



main()