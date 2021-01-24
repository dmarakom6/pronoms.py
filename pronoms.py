#random french pronouns generator for excersices
import random
import os

global PRONOMS, PRONOMS_SUBJ, PRONOMS_IMP, PRONOUNS, temps
PRONOMS = ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"]
PRONOMS_SUBJ = ["que " + pronom for pronom in PRONOMS if pronom.startswith("j") or pronom.startswith("t") or pronom.startswith("n") or pronom.startswith("v")]
PRONOMS_SUBJ_TROIXEME = ["qu' " + pronom for pronom in PRONOMS if pronom.startswith("i") or pronom.startswith("e") or pronom.startswith("o")]
PRONOMS_SUBJ += PRONOMS_SUBJ_TROIXEME   
PRONOMS_IMP = ["tu", "nous", "vous"]
temps = ["Present", "PC", "Imparfait", "PQP", "Futur Simple", "Futur Anterieur"]
randompronom = random.choice(PRONOMS)
randompronomsubj = random.choice(PRONOMS_SUBJ)
randompronomimp = random.choice(PRONOMS_IMP)

#combien (de) pronoms

def combienPronoms():


    print("\n" * 300)
    global pronoms
    pronoms = int(input(("Combien de pronoms?(1,2 ou 3): ")))
    if pronoms > 0:
        if pronoms < 4:
            Temps()
        else:
            print('Erreur')



#temps

def Temps():
    print("\n" * 300)
    print("Choisir les temps\n")
    print("TEMPS")
    print("*****")
    print()
    for temp in temps:
        print(temp)
    print()
    add = input("Ajouter P.S et P.A?[oui/non]: ")
    if add in ["oui", "o", "OUI", "Oui"]:
        temps.append("Passe Simple")
        temps.append("Passe Anterieur")
        print("\n" * 300)
        print("TEMPS")
        print("*****")
        print()
        for temp in temps:
            print(temp)
    print()
    add = input("Ajouter CONDITIONNEL?[oui/non]: ")
    if add in ["oui", "o", "OUI", "Oui"]:
        temps.append("Conditionnel Present")
        temps.append("Conditionnel Passe")
        print("\n" * 300)
        print("TEMPS")
        print("*****")
        print()
        for temp in temps:
            print(temp)
    print()
    add = input("Ajouter SUBJONCTIF?[oui/non]: ")
    if add in ["oui", "o", "OUI", "Oui"]:
        global subjonctif
        subjonctif = True
        temps.append("Subjonctif Present")
        temps.append("Subjonctif Passe")
        print("\n" * 300)
        print("TEMPS")
        print("*****")
        print()
        for temp in temps:
            print(temp)
    else:
        subjonctif = False
    print()
    add = input("Ajouter IMPERATIF?[oui/non]: ")
    if add in ["oui", "o", "OUI", "Oui"]:
        global imperatif
        imperatif = True
        temps.append("Imperatif Present")
        temps.append("Imperatif Passe")
        print("\n" * 300)
        print("TEMPS")
        print("*****")
        print()
        for temp in temps:
            print(temp)
    else:
        imperatif = False
    print()
    print("*****")
    print()
    add = input("Commencer l' exercice?[oui/non]: ")
    if add in ["oui", "o", "OUI", "Oui"]:
        print("\n" * 300)
        generatePronoms(PRONOMS, randompronom, pronoms, temps)
    else:
        print("ANNULATION")
    
#generatepronoms    

def generatePronoms(PRONOMS, randompronom, pronoms, temps):
    print("EXERCICE")
    print("---------\n")
    if pronoms == 3:
        if subjonctif == True:
            temps.remove("Subjonctif Present")
            temps.remove("Subjonctif Passe")
        
            for temp in temps:
                print(f"{temp}: \n{randompronom}")
                randompronom = random.choice(PRONOMS)
                print(f'{randompronom}')
                randompronom = random.choice(PRONOMS)
                print(f'{randompronom}')
                print()
                input()
                print()
            
            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print(f"Subjonctif Present: \n{randompronomsubj}")
            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print(f'{randompronomsubj}')
            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print(f'{randompronomsubj}')
            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print()
            input()
            print()
            print(f"Subjonctif Passe: \n{randompronomsubj}")
            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print(f'{randompronomsubj}')
            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print(f'{randompronomsubj}')
            print()
            input()
            print()

            
        
        
        if imperatif == True:
            if subjonctif == False:
                temps.remove("Imperatif Present")
                temps.remove("Imperatif Passe")
                
                for temp in temps:
                    randompronom = random.choice(PRONOMS)
                    print(f"{temp}: \n{randompronom}")
                    randompronom = random.choice(PRONOMS)
                    print(f'{randompronom}')
                    randompronom = random.choice(PRONOMS)
                    print(f'{randompronom}')
                    print()
                    input()
                    print()
            
                print(f"Imperatif Present: \ntu")
                print("nous")
                print("vous")
                print()
                input()
                print()
                print(f"Imperatif Passe: \ntu")
                print("nous")
                print("vous")
                print()
                input()
                print()

        else:
            if subjonctif == False:
                if imperatif == False:
                    for temp in temps:
                        print(f"{temp}: \n{randompronom}")
                        randompronom = random.choice(PRONOMS)
                        print(f'{randompronom}')
                        randompronom = random.choice(PRONOMS)
                        print(f'{randompronom}')
                        print()
                        input()
                        print()

    elif pronoms == 2:
        if subjonctif == True:
            temps.remove("Subjonctif Present")
            temps.remove("Subjonctif Passe")
        
            for temp in temps:
                print(f"{temp}: \n{randompronom}")
                randompronom = random.choice(PRONOMS)
                print(f'{randompronom}')
                print()
                input()
                print()
            
            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print(f"Subjonctif Present: \n{randompronomsubj}")
            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print(f'{randompronomsubj}')
            print()
            input()
            print()
            print(f"Subjonctif Passe: \n{randompronomsubj}")
            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print(f'{randompronomsubj}')
            print()
            input()
            print()

            
        
        
        if imperatif == True:
            if subjonctif == False:
                temps.remove("Imperatif Present")
                temps.remove("Imperatif Passe")
                
                for temp in temps:
                    randompronom = random.choice(PRONOMS)
                    print(f"{temp}: \n{randompronom}")
                    randompronom = random.choice(PRONOMS)
                    print(f'{randompronom}')
                    print()
                    input()
                    print()
            
                print(f"Imperatif Present:")
                print("tu")
                print("vous")
                print()
                input()
                print()
                print(f"Imperatif Passe: ")
                print("nous")
                print("vous")
                print()
                input()
                print()

        else:
            if subjonctif == False:
                if imperatif == False:
                    for temp in temps:
                        print(f"{temp}: \n{randompronom}")
                        randompronom = random.choice(PRONOMS)
                        print(f'{randompronom}')
                        randompronom = random.choice(PRONOMS)
                        print(f'{randompronom}')
                        print()
                        input()
                        print()


    elif pronoms == 1:
        if subjonctif == True:
            temps.remove("Subjonctif Present")
            temps.remove("Subjonctif Passe")
            for temp in temps:
                randompronom = random.choice(PRONOMS)
                print(f"{temp}: \n{randompronom}")
                print()
                input()
                print()

            randompronomsubj = random.choice(PRONOMS_SUBJ)
            print(f"Subjonctif Present: \n{randompronomsubj}")
            print()
            input()
            if subjonctif == True:
                temps.remove("Subjonctif Present")
                temps.remove("Subjonctif Passe")
            
                for temp in temps:
                    print(f"{temp}: \n{randompronom}")
                    print()
                    input()
                    print()
                
                randompronomsubj = random.choice(PRONOMS_SUBJ)
                print(f"Subjonctif Present: \n{randompronomsubj}")
                print()
                input()
                print()
                print(f"Subjonctif Passe: \n{randompronomsubj}")
                print()
                input()
                print()

            
            if imperatif == True:
                if subjonctif == False:
                    temps.remove("Imperatif Present")
                    temps.remove("Imperatif Passe")
                    
                    for temp in temps:
                        randompronom = random.choice(PRONOMS)
                        print(f"{temp}: \n{randompronom}")
                        print()
                        input()
                        print()
                
                    print(f"Imperatif Present:")
                    print("vous")
                    print()
                    input()
                    print()
                    print(f"Imperatif Passe: ")
                    print("tu")
                    print()
                    input()
                    print()

            else:
                if subjonctif == False:
                    if imperatif == False:
                        for temp in temps:
                            print(f"{temp}: \n{randompronom}")
                            print()
                            input()
                            print()

        
        
        
    print("\n***FIN D'EXERCICE***\n")

#main

print("PRONOMS GENERATEUR v.1.0")
print("-------------------------------------------\n")

commencer = input("Commencer?[oui/non]: ")
if commencer in ["oui", "o", "OUI", "Oui"]:
    combienPronoms()
    
elif commencer in ["non", "n", "Non", "NON"]:
    print("ANNULATION")
else:
    print("Erreur.")
    


input("***Taper sur 'Enter' pour fermer l'application***")
exit(0)

#AVOID DISPLAYING THE SAME PRONOUN AGAIN 




