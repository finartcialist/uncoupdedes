import getpass

import random

def check_number(hc):
    while not(hc in ("1","2","3","4","5","6")) or not(len(hc)==1):
        print("...please try again... ")
        hc = getpass.getpass("Enter a number from 1 to 6:")
    return hc

def main():
    try_again = True
    while try_again == True:
        print("--------------------------------------")
        print("--------------------------------------")

        print("--------------------------------------")

        print("UN COUP DE DÉS (DU DESTIN)")
        print("When Mallarmé meets Turing: a test.")
        print("Quand Mallarmé rencontre Turing: un test.")
        print("--------------------------------------")
        print("--------------------------------------")

        print("--------------------------------------")



        input("Press Enter to continue...")

        print("--------------------------------------")
        print("FR: Dans un monde dominé par les machines, l'humain arriverait-t-il à se dissimuler de façon convaincante ? \n") 
        print("Ce jeu se joue à deux.")
        print("La première personne doit se dissimuler parmi les machines.")
        print("Elle doit produire dix chiffres entre 1 et 6 de façon arbitraire et aléatoire.")
        print("La machine fera la même chose.")
        print("Deux séries de 10 chiffres sont ainsi produites, l'une par la machine, l'autre par l'être humain.\n")
        print("Le rôle de la deuxième personne est de tenter de déterminer quelle série a été produite par l'être humain.")
        print("--------------------------------------")

        input("Appuyez sur Entrée pour continuer...")

        print("--------------------------------------")
        print("EN: In a machine-dominated world, would humans be able to camouflage convincingly ? \n") 
        print("This is a two-player game.")
        print("The first player has to camouflage amongst machine.") 
        print("They will randomly but arbitrairly pick ten numbers from 1 to 6.")
        print("The machine will then do the same thing.")
        print("Two series of ten numbers each now exists, one by the machine, the other by a human.\n")
        print("The second player role is to try and find the human-created series of number.")
        print("--------------------------------------")

        input("Press Enter to begin / Appuyez sur Entrée pour commencer.")

        print("--------------------------------------")

        print("Please choose ten (10) numbers from one (1) to six (6):")
        print("Choisissez dix (10) chiffres entre un (1) et six (6):")
        temp1 = getpass.getpass("Your first choice - Premier choix :")
        hc1 = check_number(temp1)
        temp2 = getpass.getpass("Your second choice - Deuxième choix:")
        hc2 = check_number(temp2)
        temp3 = getpass.getpass("Your third choice - Troisième choix:")
        hc3 = check_number(temp3)
        temp4 = getpass.getpass("Your fourth choice - Quatrième choix:")
        hc4 = check_number(temp4)
        temp5 = getpass.getpass("Your fifth choice - Cinquième choix:")
        hc5 = check_number(temp5)
        temp6 = getpass.getpass("Your sixth choice - Sixième choix:")
        hc6 = check_number(temp6)
        temp7 = getpass.getpass("Your seventh choice - Septième choix:")
        hc7 = check_number(temp7)
        temp8 = getpass.getpass("Your eight choice - Huitième choix:")
        hc8 = check_number(temp8)
        temp9 = getpass.getpass("Your nineth choice - Neuvième choix:")
        hc9 = check_number(temp9)
        temp10 = getpass.getpass("Your tenth choice - Dixième choix:")
        hc10 = check_number(temp10)

        human_choice = hc1 + "," + hc2 + "," + hc3 + "," + hc4 + "," + \
            hc5 + "," + hc6 + "," + hc7 + "," + hc8 + "," + hc9 + "," + hc10
        robot_choice = str(random.randint(1, 6)) + ","
        temp = 0
        for i in range(8):
            temp = random.randint(1, 6)
            robot_choice = robot_choice + str(temp) + ","

        robot_choice = robot_choice + str(random.randint(1, 6))

        print("---------------------------------")
        print("Les jeux sont faits ! ")
        print("Game is over!")
        input("")
        print("Pick the human created serie amongst the following two options.")
        print("Parmi les deux options suivantes, quel est la série créé par un humain ?")
        input("")

        if temp < 3:
            print("Option A:")
            print(human_choice)
            print("Option B:")
            print(robot_choice)
            input("")
            right_answer = "A"
            print("Saisissez l'identifiant de la série créée par un humain : ")
            discriminator = input(
                "Enter the option that you think was the human created series:")
        else:
            print("Option A:")
            print(robot_choice)
            print("Option B:")
            print(human_choice)
            input("")
            right_answer = "B"
            print("Saisissez l'identifiant de la série créée par un humain : ")

            discriminator = input(
                "Enter the option that you think was the human choice:")


        print("--------------------------------------")
        print("--------------------------------------")

        print("Avez-vous été dupé.e par l'être humain ?")
        print("Where you fooled by the human?")

        input("")

        print("--------------------------------------")

        print("Vérifions...")
        print("Let's see...")

        input("")

        print("La série créée par un être humain était...")
        print("The human-created serie was... : " + right_answer)
        input("")
        print("Et votre réponse était...")
        print("And your answer was... : " + discriminator)
        print("Vous avez trouvé l'humain : ")
        print("You found the human: " +
          str(right_answer == discriminator.upper()))

        input("")
        
        print("Voulez-vous rejouer ? O/N")
        try_a = input("Do you want to try again ? Y/N \n")
        if (try_a.upper() == "Y") or try_a.upper() == "O":
            try_again = True
        else:
            try_again = False
    print("Thanks for playing!")
    print("Merci d'avoir joué !")


if __name__ == '__main__':
    main()
