fInput = open("fInput.txt", "r")
text = fInput.readlines()
fInput.close()

fOutput = open("fOutput.txt", "a+", encoding="utf8")
fOutput.truncate(0)

dic = {"princesse":"\U0001F478","roi":"\U0001F451","prince":"\U0001F934","plus":"\U00002795","moins":"\U00002796"}

for ligne in text:
    for mot in ligne.split():
        final = mot
        for key in dic:
            if len(key) <= len(mot) <= len(key)+2:
                if mot.lower()[0:len(key)] == key:
                    final = dic[key]

        fOutput.write(final + " ")
    fOutput.write("\n")

fOutput.close()









