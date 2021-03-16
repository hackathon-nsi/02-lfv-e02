txt = open("PDC.txt", "r+")

a = txt.read()

dico = {"e":"\U0001F600"}

txt.close

with open("N.txt","x",encoding="utf-8")as final:

    for lettre in a:
        try:
            final.write(dico[lettre])
        except:
            final.write(lettre)
