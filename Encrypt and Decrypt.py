lists=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypted(value,shift):
    strs=''
    for i in value:
        for j in range(26):
            if i==lists[j]:
                encrypts=(j+shift)%26
                strs+=lists[encrypts]
        if i==" ":
            strs+=i
    print(strs)
def decrypted(value,shift):
    strd=''
    for i in value:
        for j in range(26):
            if i==lists[j]:
                decrypts=(j-shift)
                if decrypts<0:
                    decrypts+=26
                else:
                    decrypts%=26
                strd+=lists[decrypts]
        if i==" ":
            strd+=i
    print(strd)
want_end=False
while not want_end:
    initals=input("Type 'encrypt' for encryption and type 'decrypt' for decryption")
    inital=initals.lower()
    if inital=='encrypt' or inital=='decrypt':
        value=input("Enter the message").lower()
        shift=int(input("Enter the shift number"))
        if inital=='encrypt':
            encrypted(value,shift)
        elif inital=='decrypt':
            decrypted(value,shift)
        play_again=input("Type 'yes' to continue or type 'no' to exit")
        if play_again=='no':
            want_end=True
            print("Good bye")
    else:
        print("Please enter valid input")



