
#Code and Developed by Caleb Gucciardi
#A PasswordList Generetor that use KeyWords 

file="passw.txt"
old="OverPower"

#
#                         TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT                
#                         TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT                 
#                                               TTTT                                  
#   BBBBBBBBB       RRRRRRRRRR    UU       UU   TTTT    EEEEEEEEEE       
#   BB      B       RR       R    UU       UU   TTTT   EEEE                
#   BB      B       RR       R    UU       UU   TTTT   EEE                
#   BB      B       RRRRRRRRRR    UU       UU   TTTT   EEEEEEEEE         
#   BBBBBBBBBBBBB   RR   R R      UU       UU   TTTT   EEEEEEEEE         
#   BB          B   RR    R R     UU       UU   TTTT   EEE                
#   BB          B   RR     R R    UU       UU   TTTT   EEEE                
#   BBBBBBBBBBBBB   RR      R R   UUUUUUUUUUU   TTTT    EEEEEEEEEE         
# 

def help_():
    print("------------------------------HELP----------------------------------------")
    print("--Create your own Password Dictionary using sensitive victim information--")
    print("--Use the spaces to divide one seed from another--")
    print("--Commands:")
    print(" SET [name] => set the name of the output file.  ps. Include .txt at the name")
    print(" MAKE [seed] [seed] ... => make the Dictionary with the specif seeds ")
    print(" CLOSE => exit from BruteList")
    print("--------------------------------------------------------------------")

def SET(com):
    global file
    com,file = com.split(" ")
    print("Output File Name =>",file)



def MAKE(com):
    seed=com.split(" ")
    seed.pop(0)
    for sd in seed:
        BL(sd)
        
    
def BL(seed):
    global file,old
    f=open(file,"a+")
    f.write("123{}\n".format(seed))
    f.write("{}1234\n".format(seed))
    f.write("{}1234\n".format(seed.lower()))
    f.write("{}1234\n".format(seed.upper()))
    f.write("{}TheKing\n".format(seed))
    f.write("123{}\n".format(seed))
    f.write("Master{}\n".format(seed))
    f.write("Shadow{}\n".format(seed))
    f.write("ilove{}\n".format(seed))
    f.write("ILove{}\n".format(seed))
    f.write("Ilove{}\n".format(seed))
    f.write("Love{}\n".format(seed))
    f.write("MyLove{}\n".format(seed))
    f.write("mylove{}\n".format(seed))
    f.write("myLove{}\n".format(seed))
    f.write("Instagram{}\n".format(seed))
    f.write("instagram{}\n".format(seed))
    f.write("Facebook{}\n".format(seed))
    f.write("facebook{}\n".format(seed))
    f.write("{}instagram\n".format(seed))
    f.write("{}Instagram\n".format(seed))
    f.write("{}facebook\n".format(seed))
    f.write("{}Facebook\n".format(seed))
    f.write("123{}123\n".format(seed))
    f.write("{}\n".format(seed))
    f.write("{}\n".format(seed.lower()))
    f.write("{}\n".format(seed.upper()))
    f.write("Diamond{}\n".format(seed))
    f.write("{}Diamond\n".format(seed))
    f.write("abc{}\n".format(seed))
    f.write("{}abc\n".format(seed))
    f.write("{}{}\n".format(seed,old))
    f.write("{}{}\n".format(old,seed))
    f.write("{}{}\n".format(old.upper(),seed))
    f.write("{}{}\n".format(old.lower(),seed))
    f.write("{}{}\n".format(old,seed.upper()))
    f.write("{}{}\n".format(old,seed.lower()))
    f.write("{}{}\n".format(old.upper(),seed.lower()))
    f.write("{}{}\n".format(old.lower(),seed.upper()))
    f.write("{}{}\n".format(old.lower(),seed.lower()))
    f.write("{}{}\n".format(old.upper(),seed.upper()))
    f.write("{}99\n".format(seed))
    f.write("{}98\n".format(seed))
    f.write("{}69\n".format(seed))
    f.write("{}68\n".format(seed))
    f.write("{}66\n".format(seed))
    f.write("{}73\n".format(seed))
    f.write("{}72\n".format(seed))
    f.write("{}00\n".format(seed))
    f.write("{}01\n".format(seed))
    f.write("{}998\n".format(seed))
    f.write("{}997\n".format(seed))
    f.write("{}767\n".format(seed))
    f.write("{}898\n".format(seed))
    f.write("{}{}\n".format(seed[0],seed))
    f.write("{}{}\n".format(old[0],seed))
    f.write("{}\n".format(seed[0],old))
    f.write("Black{}\n".format(seed))
    f.write("black{}\n".format(seed))
    f.write("Mr{}\n".format(seed))
    f.write("mr{}\n".format(seed))
    f.write("hack{}\n".format(seed))
    f.write("NobodyLove{}\n".format(seed))
    f.write("nobodylove{}\n".format(seed))
    f.write("NobodyLove{}\n".format(seed.upper()))
    f.write("nobodylove{}\n".format(seed.upper()))
    f.write("NobodyLove{}\n".format(seed.lower()))
    f.write("nobodylove{}\n".format(seed.lower()))
    f.write("{}666\n".format(seed))
    f.write("$${}$$\n".format(seed))
    f.write("@@{}@@\n".format(seed))
    f.write("&&{}&&\n".format(seed))
    f.write("%%{}%%\n".format(seed))
    f.write("££{}££\n".format(seed))
    f.write("root{}\n".format(seed))
    f.write("{}root\n".format(seed))
    f.write("admin{}\n".format(seed))
    f.write("{}admin\n".format(seed))
    f.close()
    old=seed

def main():
    print("-----------------------------------")
    print("-------Welcome to BruteList--------")
    print("--Type help for a list of command--")
    print("-----------------------------------")
    while(1):
        com=input("BL::")
        if(com=="help"):
            help_()
        elif("SET" in com):
            SET(com)
        elif("MAKE" in com):
            MAKE(com)
        elif(com =="CLOSE"):
            break

if __name__=="__main__":
    main()
