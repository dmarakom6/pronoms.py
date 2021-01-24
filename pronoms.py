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
    try:
        print("\n" * 300)
        global pronoms
        pronoms = int(input(("Combien de pronoms?(1,2 ou 3): ")))
        if pronoms > 0:
            if pronoms < 4:
                Temps()
            else:
                print('Erreur')
    except:
        print("Erreur")


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
        if subjonctif == True:
            global touslesdeux
            touslesdeux = True
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
                pronoms = random.sample(PRONOMS, 3)
                print(f"{temp}:")
                for pronom in pronoms:
                    print(f'{pronom}')
                print()
                input()
                print()
                
            pronomsubj = random.sample(PRONOMS_SUBJ, 3)
            print(f"Subjonctif Present:")
            for pronom in pronomsubj:
                print(f"{pronom}")
            print()
            input()
            print()

            pronomsubj = random.sample(PRONOMS_SUBJ, 3)
            print(f"Subjonctif Passe:")
            for pronom in pronomsubj:
                print(f"{pronom}")
            print()
            input()
            print()

        
        elif imperatif == True:
            if subjonctif == False:
                temps.remove("Imperatif Present")
                temps.remove("Imperatif Passe")
                
                for temp in temps:    
                    pronoms = random.sample(PRONOMS, 3)
                    print(f"{temp}:")
                    for pronom in pronoms:
                        print(f'{pronom}')
                    print()
                    input()
                    print()
            
            pronomsimp = random.sample(PRONOMS_IMP, 3)
            print(f"Imperatif Present:")
            for pronom in pronomsimp:
                print(f"{pronom}")
            print()
            input()
            print()

            pronomsimp = random.sample(PRONOMS_IMP, 3)
            print(f"Imperatif Passe:")
            for pronom in pronomsimp:
                print(f"{pronom}")
            print()
            input()
            print()


        
        elif subjonctif == False:
            if imperatif == False:
                for temp in temps:    
                    pronoms = random.sample(PRONOMS, 3)
                    print(f"{temp}:")
                    for pronom in pronoms:
                        print(f'{pronom}')
                    print()
                    input()
                    print()
            
        elif touslesdeux == True:
            for temp in temps:
                pronoms = random.sample(PRONOMS, 3)
                print(f"{temp}:")
                for pronom in pronoms:
                    print(f'{pronom}')
                print()
                input()
                print()
                
        
    elif pronoms == 2:
        if subjonctif == True:
            temps.remove("Subjonctif Present")
            temps.remove("Subjonctif Passe")
            for temp in temps:    
                pronoms = random.sample(PRONOMS, 2)
                print(f"{temp}:")
                for pronom in pronoms:
                    print(f'{pronom}')
                print()
                input()
                print()
                
            pronomsubj = random.sample(PRONOMS_SUBJ, 2)
            print(f"Subjonctif Present:")
            for pronom in pronomsubj:
                print(f"{pronom}")
            print()
            input()
            print()

            pronomsubj = random.sample(PRONOMS_SUBJ, 2)
            print(f"Subjonctif Passe:")
            for pronom in pronomsubj:
                print(f"{pronom}")
            print()
            input()
            print()

        
        elif imperatif == True:
            if subjonctif == False:
                temps.remove("Imperatif Present")
                temps.remove("Imperatif Passe")
                
                for temp in temps:    
                    pronoms = random.sample(PRONOMS, 2)
                    print(f"{temp}:")
                    for pronom in pronoms:
                        print(f'{pronom}')
                    print()
                    input()
                    print()
            
            pronomsimp = random.sample(PRONOMS_IMP, 2)
            print(f"Imperatif Present:")
            for pronom in pronomsimp:
                print(f"{pronom}")
            print()
            input()
            print()

            pronomsimp = random.sample(PRONOMS_IMP, 2)
            print(f"Imperatif Passe:")
            for pronom in pronomsimp:
                print(f"{pronom}")
            print()
            input()
            print()
        
        elif subjonctif == False:
            if imperatif == False:
                for temp in temps:    
                    pronoms = random.sample(PRONOMS, 2)
                    print(f"{temp}:")
                    for pronom in pronoms:
                        print(f'{pronom}')
                    print()
                    input()
                    print()
            
        elif touslesdeux == True:
            for temp in temps:
                pronoms = random.sample(PRONOMS, 2)
                print(f"{temp}:")
                for pronom in pronoms:
                    print(f'{pronom}')
                print()
                input()
                print()

    elif pronoms == 1:
        if subjonctif == True:
            temps.remove("Subjonctif Present")
            temps.remove("Subjonctif Passe")
            for temp in temps:    
                pronoms = random.sample(PRONOMS, 1)
                print(f"{temp}:")
                for pronom in pronoms:
                    print(f'{pronom}')
                print()
                input()
                print()
                
            pronomsubj = random.sample(PRONOMS_SUBJ, 1)
            print(f"Subjonctif Present:")
            for pronom in pronomsubj:
                print(f"{pronom}")
            print()
            input()
            print()

            pronomsubj = random.sample(PRONOMS_SUBJ, 1)
            print(f"Subjonctif Passe:")
            for pronom in pronomsubj:
                print(f"{pronom}")
            print()
            input()
            print()

        
        elif imperatif == True:
            if subjonctif == False:
                temps.remove("Imperatif Present")
                temps.remove("Imperatif Passe")
                
                for temp in temps:    
                    pronoms = random.sample(PRONOMS, 1)
                    print(f"{temp}:")
                    for pronom in pronoms:
                        print(f'{pronom}')
                    print()
                    input()
                    print()
            
            pronomsimp = random.sample(PRONOMS_IMP, 1)
            print(f"Imperatif Present:")
            for pronom in pronomsimp:
                print(f"{pronom}")
            print()
            input()
            print()

            pronomsimp = random.sample(PRONOMS_IMP, 1)
            print(f"Imperatif Passe:")
            for pronom in pronomsimp:
                print(f"{pronom}")
            print()
            input()
            print()


        
        elif subjonctif == False:
            if imperatif == False:
                for temp in temps:    
                    pronoms = random.sample(PRONOMS, 1)
                    print(f"{temp}:")
                    for pronom in pronoms:
                        print(f'{pronom}')
                    print()
                    input()
                    print()
            
        elif touslesdeux == True:
            for temp in temps:
                pronoms = random.sample(PRONOMS, 1)
                print(f"{temp}:")
                for pronom in pronoms:
                    print(f'{pronom}')
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





