from tkinter import W
import crc8



#deklarace promenych
hash=crc8.crc8()
sous=0
cisla=[]
crc=[]
polynom=0x31
main=True


#deklarace funkci
def outCis():
    inkCount=0
    for i in cisla:
        inkCount+=1
        print(str(inkCount) + " - " + f"{i}")

def Kon(y):
    if type(y)==hex and sous==1:
        return y
    elif type(y)==int and sous == 2:
        return y
    elif type(y)==bin and sous == 3:
        return y
    else:
        print("Vstup neodpovida vybrane cislicove soustave.")       

sous=int(input("Zadejte volbu cislicove soustavy.\n1) Hexadecimalni\n2) Decimalni\n3) Binarni\n>"))

while(main):
    c=int(input("Zvolte nasledujici operaci.\n1) Vlozit cislo\n2) Smaz cislo\n3) Vypis cisel\n4) Spocti a vypis CRC zadanych cisel\n5) Vypis do souboru\n6) Ukoncit\n>"))
#cykl zadavani
    if c==1:
        cloop=True
        while(cloop):
            i=0
            print(type(i))
            i=input()
            i=bin(i)
            print(type(i))
            Kon(i)
            if i!=0:
                cisla.append(i)
            inp=input("Chces zadat dalsi? (Y/N)")
            if inp.upper() == "N":
                cloop=False
    elif c==2:
        #smazat cislo
        outCis()
        s=int(input("Zadej index cisla co chces smazat: "))
        cisla.pop(s-1)
    elif c==3:
    #vypis
        outCis()
    elif c==4:
        #crc + vypis
        buffik=bytearray(cisla)
        print(cisla)
        hash.update(buffik)
        hash.hexdigest() == polynom
        print(hash)
    elif c==5:
        #output do soubor)u =
        fn=str(input("Zadejte nazev souboru, ktery se chystate ulozit. Pokud soubor jiz existuje, bude prepsan.\n>"))
        f = open(fn + ".txt", W)
        inkCount=0
        for i in cisla:
            inkCount+=1
            f.write(str(inkCount) + " - " + f"{i}\n")
    elif c==6:
        main=False




