# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:39:35 2022

@author: Besma Djebaili, Sham Gnanaseelan, Gauthier Guyaz
"""

def draw():
    print(dico["A1"], dico["B1"], dico["C1"])
    print(dico["A2"], dico["B2"], dico["C2"])
    print(dico["A3"], dico["B3"], dico["C3"],"\n")
 

def main():
    global flag, dico
    
    valeurs = input(f"Joueur {flag}: Entrez valeurs (A/B/C,1/2/3): ")
    
    if dico.get((valeurs),None) == "—":
        dico[valeurs] = flag
    else:
            echec()
            main()
        
    draw()
    test_winner()
    
    if flag == "X":
        flag = "O"
        
    elif flag == "O":
        flag = "X"

    if flag != "fin":
        main()


#créer avec boucle while
def test_winner():
    global flag, flag_end
    
    flag_end += 1
        
    #if liste[0] == liste[1] == liste[2] == 
        
    if dico["A1"] == dico["B1"] == dico["C1"] == flag:
            win()
            print("Joueur ",flag, "a gagné    ;) ")
            flag = "fin"
    
    if dico["A2"] == dico["B2"] == dico["C2"] == flag:
            win()
            print("Joueur ",flag, "a gagné    ;) ")
            flag = "fin"
        
    if dico["A3"] == dico["B3"] == dico["C3"] == flag:
            win()
            print("Joueur ",flag, "a gagné    ;) ")
            flag = "fin"
    
    if dico["A1"] == dico["A2"] == dico["A3"] == flag:
            win()
            print("Joueur ",flag, "a gagné    ;) ")
            flag = "fin"
        
    if dico["B1"] == dico["B2"] == dico["B3"] == flag:
            win()
            print("Joueur ",flag, "a gagné    ;) ")
            flag = "fin"
        
    if dico["C1"] == dico["C2"] == dico["C3"] == flag:
            win()
            print("Joueur ",flag, "a gagné    ;) ")
            flag = "fin"
        
    if dico["A1"] == dico["B2"] == dico["C3"] == flag:
            win()
            print("Joueur ",flag, "a gagné    ;) ")
            flag = "fin"
            
    if dico["C1"] == dico["B2"] == dico["A3"] == flag:
            win()
            print("Joueur ",flag, "a gagné    ;) ")
            flag = "fin"
            
    if flag_end == 9:
        print("MATCH NUL")
        flag = "fin"
    
    
###---Fonction graphique affichage pour les erreurs---###        
def echec():
    fichier = open('echec.txt','r', encoding='utf-8')
    echec = fichier.read()
    print(echec)
    fichier.close()


###---Fonction graphique affichage pour gagnant---###
def win():
    fichier = open('kiss.txt','r', encoding='utf-8')
    kiss = fichier.read()
    print(kiss)
    fichier.close()
            

###---Variables générales---###

flag = "X"
flag_end = 1
dico = { 
        "A1":"—", "B1":"—", "C1":"—",
        "A2":"—", "B2":"—", "C2":"—",
        "A3":"—", "B3":"—", "C3":"—",
        }

###---Programme de démarrage ---###

fichier = open('intro.txt','r', encoding='utf-8')
intro = fichier.read()
print(intro)
fichier.close()  

asw = input("Etes-vous prêt (oui/non) ")

if asw != "oui" :
    print("""
          Tant pis ¯\_(ツ)_/¯
              --------
          """)  

main()
