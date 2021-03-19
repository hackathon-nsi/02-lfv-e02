msg=input("votre message")
msg=str(msg)
msg=msg.split(" ")
dic={"princesse":"\U0001F609\n","prince":"\U0001F934\n","avion":"\U00002708\n"}
for mot in msg:
    if mot in dic:
        print(dic[mot],end=" ")
    else :
        print(mot,end=" ")
