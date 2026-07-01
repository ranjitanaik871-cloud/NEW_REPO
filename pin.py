pin=1234
attempt=0
while attempt<=3:
    name=input("enter the PIN:")

    if int(name)==pin:
        print("pin is correct")
        break
    else:
        print("pin is incorrect")
        attempt=attempt+1
if attempt>3:
    print("your account is locked")