import os
cont = True
while(cont):
    
    verb = input("Input Verb: ")
    ar_endings = ["o", "as", "a", "amos", "áis", "an"]
    er_endings = ["o", "es", "e", "emos", "éis", "en"]
    ir_endings = ["o", "es", "e", "imos", "ís", "en"]

    def conjugate(verb):
        
        raiz = verb[0:len(verb)-2]
        ending = verb[len(verb)-2:]
        conjugated = ["Yo ", "Tú ", "Él/Ella/Usted ", "Nosotros/as ", "Vosotors/as ", "Ellos/Ellas/Ustedes "]
        if(ending == "ar"):
            for i in range(len(er_endings)):
                conjugated[i] = conjugated[i] + raiz + ar_endings[i]
            return conjugated
        elif(ending == "er"):
            for i in range(len(er_endings)):
                conjugated[i] = conjugated[i] + raiz + er_endings[i]
            return conjugated
        elif(ending == "ir"):
            for i in range(len(er_endings)):
                conjugated[i] = conjugated[i] + raiz + ir_endings[i]
            return conjugated

    conjugated = conjugate(verb)
    for i in range(len(conjugated)):
        print(conjugated[i] + "\r\n")
    
    answer = input("Do you want to conjugate another verb? (y/n)")
    if(answer == "y"):
        cont = True
        os.system('CLS')
    else:
        cont = False

