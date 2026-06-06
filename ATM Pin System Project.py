print(" == ATM Pin System == ")
pin = "123"
attemp = 3
while attemp > 0:
    user_pin = input("Enter Pin: ")
    if user_pin == pin:
        print(" Welcom")
        break
    attemp -= 1
    print("Attempt left: ",attemp)