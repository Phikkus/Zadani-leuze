
from tkinter import W

try:
    import crc
except:
    import pip
    pip.main(['install', '--user', 'crc'])
    import crc
    input("Knihovna importovana\n")
    

from crc import CrcCalculator, Crc8
import crc8



#crc setup
crc_calculator = CrcCalculator(Crc8.MAXIM_DOW)

#deklarace promenych
hdict="0123456789abcdefABCDEF"
ddict="0123456789"
bdict="01"
prefix=""
sous=0
checksum=0
cisla=[]
crc=[]
main=True
initq=True



#deklarace funkci
def outCis():
    inkCount=0
    if not crc:
        for i in cisla:
            inkCount+=1
            print(str(inkCount) + " - " + prefix + f"{i}")
    else:
        for i in cisla:
            inkCount+=1
            try:
                print(str(inkCount) + " - " + prefix + f"{i}" + " - CRC: " + str(crc[inkCount-1]))
            except:
                print(str(inkCount) + " - " + prefix + f"{i}" + " - CRC: Neni vypocitano" )
        

def Kon(y):
    d=""
    inc=0
    if sous==1:
        d=hdict
    elif sous == 2:
        d=ddict
    elif sous == 3:
        d=bdict
    for char in y:
        if char not in d:
            inc = 1
            break
        else:
            pass
    if inc:
        print("Spatny format zadanych cisel.")
    else:
        return y
        
while(initq):
    try:
        sous=int(input("Zadejte volbu cislicove soustavy.\n1) Hexadecimalni\n2) Decimalni\n3) Binarni\n>"))
    except ValueError:
        print("Zadana moznost musi byt cislo.")
    else:
        if sous <=3 and sous>0:
            if sous==1:
                prefix="0x"
            elif sous==2:
                prefix="0#"
            elif sous==3:
                prefix="0b"
            initq=False
        else:
            print("Zadana moznost neni dostupna")
        
    

while(main):
    c=int(input("Zvolte nasledujici operaci.\n1) Vlozit cislo\n2) Smaz cislo\n3) Vypis cisel a CRC (pokud bylo vypocitano)\n4) Spocti CRC zadanych cisel\n5) Vypis do souboru\n6) Ukoncit\n>"))
#cykl zadavani
    if c==1:
        cloop=True
        while(cloop):
            k=""
            i=input("Zadejte cislo: ")
            k=Kon(i)
            if k is not None:
                cisla.append(k)
            inp=input("Chces zadat dalsi? (Y/N)")
            if inp.upper() == "N":
                cloop=False
    elif c==2:
        #smazat cislo
        outCis()
        s=int(input("Zadej index cisla co chces smazat: "))
        if s <= len(cisla) and s>0:
            cisla.pop(s-1)
        else:
            print("Zadane cislo neodpovida dostupnemu indexu.")
    elif c==3:
    #vypis
        outCis()
    elif c==4:
        #crc + vypis
        crc=[]
        for i in cisla:
            e=bytearray.fromhex(i)
            checksum=crc_calculator.calculate_checksum(e)
            cksumbajt=hex(checksum)
            crc.append(cksumbajt)
        print("CRC vypocitano")
    elif c==5:
        #output do souboru
        try:
            fn=str(input("Zadejte nazev souboru, ktery se chystate ulozit. Pokud soubor jiz existuje, bude prepsan.\n>"))
        except TypeError:
            print("Pri zadavani jmena souboru vznikla chyba.")
        else:
            f = open(fn + ".txt", W)
            inkCount=0
            if not crc:
                for i in cisla:
                    inkCount+=1
                    f.write(str(inkCount) + " - " + prefix + f"{i}" + "\n")
            else:
               for i in cisla:
                    inkCount+=1
                    f.write(str(inkCount) + " - " + prefix + f"{i}" + " - CRC: " + str(crc[inkCount-1] + "\n"))
    elif c==6:
        main=False
