s = input("Enter a string to test: ")

if len(s) != 12:
    print("Not a Phone!")

elif not s[0:3].isdecimal():
    print("Not a Phone!")

elif s[3] == '-' and not s[7] == '-':
    print ("Not a Phone!")

print("big booty bitches")
("yeah")