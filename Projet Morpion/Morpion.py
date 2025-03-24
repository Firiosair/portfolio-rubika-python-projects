import pygame #Import de la librairie pygame / Import of pygame library

pygame.init() #Initialisation de la fenêtre affiché / Initialisation of the window
screen = pygame.display.set_mode((800, 800)) #La fenêtre aura pour taille 800 pixels par 800 pixels / The window will be 800 pixels by 800 pixels

Title=pygame.image.load("./assets/Title.png") #Ca sera l'image affichant le titre "morpion" / It will be the image displaying the title "morpion" which is the name of the game in french
Player1=pygame.image.load("./assets/Player1.png") #Ca sera l'image affichant le joueur qui doit jouer / It will be the image displaying the player who has to play
Player2=pygame.image.load("./assets/Player2.png") #Ca sera l'image affichant le joueur qui doit jouer / It will be the image displaying the player who has to play
Player1WIN=pygame.image.load("./assets/Player1WIN.png") #Ca sera l'image affichant le joueur qui a gagner / It will be the image displaying the player who won at the end of the game
Player2WIN=pygame.image.load("./assets/Player2WIN.png") #Ca sera l'image affichant le joueur qui a gagner / It will be the image displaying the player who won at the end of the game
Tie=pygame.image.load("./assets/Tie.png") #Ca sera l'image qui s'affichera s'il y a égalité / It will be the image displaying if there is a Tie
NextGame=pygame.image.load("./assets/NextGame.png") #Ca sera l'image qui représentera le bouton pour passer à la partie suivante / It will be the image displaying to go to the next game

Player = 1 #Cette variable représente le joueur à qui c'est le tour / It respresent the player who is playing
running = True #Cette variable est présente pour vérifier que le joueur n'a pas quitté le jeu / It is here to check if the player didn't quit the game
playable = True #Vérifie qu'il reste au moins une cas disponible sur la grille / Check if there is still at least one case still available to play
win=None #Cette variable prend une valeur si un des deux joueurs à gagner / This variable is affected to a value if one of the two players won the game
grid=[[0,0,0],[0,0,0],[0,0,0]] #Ca représente la grille de jeu, si c'est 0 il n'y a rien à afficher, si c'est 1, il faut afficher un cercle et si c'est deux, il faut afficher une croix / Represents the grid if the value is 0 then there is nothing to display if it's one then we have to display a circle and if it's two then we have to display a cross
black=(0,0,0) #Juste une variable pour garder la couleur noir en mémoire / A variable to keep in mind the color black in memory
white=(255,255,255) #Juste une variable pour garder la couleur blanche en mémoire / A variable to keep in mind the color white in memory

while running:
    for event in pygame.event.get():
        #Ca vérifie juste qu'il ne faut pas fermer le jeu / It just check if we have to close the game
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: #On regarde si le joueur clique sur la souris / We check if the player presse a button of the mouse
                #Ca vérifie si le joueur à appuyer sur le bouton rejouer pour relancer une partie et donc pour redémarre le jeu / It checks whether the player has pressed the replay button to restart a game
                if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[0] < 600 and pygame.mouse.get_pos()[1] < 598 and win != None:
                    #On remet les valeurs à 0 / Reset values to 0
                    win=None 
                    playable=True
                    grid=[[0,0,0],[0,0,0],[0,0,0]]
            if event.type == pygame.MOUSEBUTTONDOWN and (win==None or not playable): #Si un des boutons de la souris est pressé et que personne n'a encore gagné, alors on passe cette condition / If one button of the mouse is pressed and that no one already won then we go trough this condition
                for i in range (len(grid)):
                    for j in range(len(grid[i])):
                        #Ensuite, on vérifie si le clique est sur une case vide, en faisant une boucle pour vérifier pour chaque case avec donc les coordonées de la case en haut à gauche puis on ajoute en fonction de i et j le nombre de coordonées pour vérifier chaque case / Next, we check whether the click is on an empty square, by making a loop to check each square with the coordinates of the square in the top left-hand corner, then we add the number of coordinates to check each square as a function of i and j
                        if pygame.mouse.get_pos()[0]>160+i*160 and pygame.mouse.get_pos()[1]>160+j*160 and pygame.mouse.get_pos()[0]<320+i*160 and pygame.mouse.get_pos()[1]<320+j*160 and grid[j][i]==0:
                            grid[j][i]=Player #Si ces conditions sont remplies alors, la case sur laquelle le joueur a cliqué est associé au numéro du joueur afin de plus tard la récupérer pour afficher le symbole associé au joueur / If these conditions are met, the square on which the player has clicked is associated with the player's number so that it can later be retrieved to display the symbol associated with the player
                            #Puis on passe au joueur suivant / Then we move on to the next player
                            if Player==1:
                                Player=2
                            else:
                                Player=1

    screen.fill(black) #On affiche le fond noir / We display the black background
    screen.blit(Title,(200,50)) #On affiche le titre / We display the title

    #Ici on vérifie si le joueur 1 a gagné, si oui alors on affiche un texte félicitant le joueur et un bouton pour redémarrer le jeu / Here, we check if the player 1 won if he has then we display a congratulations screen and a next game button to do another game
    if win == "Player 1":
        screen.blit(Player1WIN,(100,300))
        screen.blit(NextGame,(200,500))
        for event in pygame.event.get():
            #Ca vérifie juste qu'il ne faut pas fermer le jeu / It just check if we have to close the game
            if event.type == pygame.QUIT: 
                running = False
            #Ca vérifie si le joueur à appuyer sur le bouton rejouer pour relancer une partie et donc pour redémarre le jeu / It checks whether the player has pressed the replay button to restart the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[0] < 600 and pygame.mouse.get_pos()[1] < 598:
                    #On remet les valeurs à 0 / Reset values to 0
                    win=None
                    playable=True
                    grid=[[0,0,0],[0,0,0],[0,0,0]]
    
    #Ici on vérifie si le joueur 2 a gagné, si oui alors on affiche un texte félicitant le joueur et un bouton pour redémarrer le jeu / Here, we check if the player 2 won if he has then we display a congratulations screen and a next game button to do another game
    elif win == "Player 2":
        screen.blit(Player2WIN,(100,300))
        screen.blit(NextGame,(200,500))
        for event in pygame.event.get():
            #Ca vérifie juste qu'il ne faut pas fermer le jeu / It just check if we have to close the game
            if event.type == pygame.QUIT:
                running = False
            #Ca vérifie si le joueur à appuyer sur le bouton rejouer pour relancer une partie et donc pour redémarre le jeu / It checks whether the player has pressed the replay button to restart the game
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[0] < 600 and pygame.mouse.get_pos()[1] < 598:
                    #On remet les valeurs à 0 / Reset values to 0
                    win=None
                    playable=True
                    grid=[[0,0,0],[0,0,0],[0,0,0]]

    #Ici on vérifie si la grille est pleine, si oui alors on affiche égalité et un bouton pour redémarrer le jeu / Here, we check if there is a tien then we display a tie screen and a next game button to do another game
    elif not playable:
        screen.blit(Tie,(336,300))
        screen.blit(NextGame,(200,500))
        for event in pygame.event.get():
            #Ca vérifie juste qu'il ne faut pas fermer le jeu / It just check if we have to close the game
            if event.type == pygame.QUIT:
                running = False
            #Ca vérifie si le joueur à appuyer sur le bouton rejouer pour relancer une partie et donc pour redémarre le jeu / It checks whether the player has pressed the replay button to restart the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[0] < 600 and pygame.mouse.get_pos()[1] < 598:
                    #On remet les valeurs à 0 / Reset values to 0
                    win=None
                    playable=True
                    grid=[[0,0,0],[0,0,0],[0,0,0]]
    #Ici, on vérifie que personne n'a gagné pour lancer les actions liés au jeu / Here, we check that no-one has won to launch the actions linked to the game
    elif win == None or not playable:
        i=0
        j=0
        #On affiche les quatres lignes formant la grille de jeu / We display the four lines representing the grid of the game
        pygame.draw.line(screen, white, (480,160), (480,640),15)
        pygame.draw.line(screen, white, (320,160), (320,640),15)
        pygame.draw.line(screen, white, (160,480), (640,480),15)
        pygame.draw.line(screen, white, (160,320), (640,320),15)
        #On affiche le joueur à qui c'est le tour en bas à droite de la fenêtre de jeu / We display the player whose turn it is in the bottom rigth corner of the game window
        if Player==1:
            screen.blit(Player1,(500,700)) 
        else:
            screen.blit(Player2,(500,700))
        for event in pygame.event.get():
            #Ca vérifie juste qu'il ne faut pas fermer le jeu / It just check if we have to close the game
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  #Si un des boutons de la souris est pressé et que personne n'a encore gagné, alors on passe cette condition / If one button of the mouse is pressed and that no one already won then we go trough this condition
                for i in range (len(grid)):
                    for j in range(len(grid[i])):
                        #Ensuite, on vérifie si le clique est sur une case vide, en faisant une boucle pour vérifier pour chaque case avec donc les coordonées de la case en haut à gauche puis on ajoute en fonction de i et j le nombre de coordonées pour vérifier chaque case / Next, we check whether the click is on an empty square, by making a loop to check each square with the coordinates of the square in the top left-hand corner, then we add the number of coordinates to check each square as a function of i and j 
                        if pygame.mouse.get_pos()[0]>160+i*160 and pygame.mouse.get_pos()[1]>160+j*160 and pygame.mouse.get_pos()[0]<320+i*160 and pygame.mouse.get_pos()[1]<320+j*160 and grid[j][i]==0:
                            grid[j][i]=Player #Si ces conditions sont remplies alors, la case sur laquelle le joueur a cliqué est associé au numéro du joueur afin de plus tard la récupérer pour afficher le symbole associé au joueur / If these conditions are met, the square on which the player has clicked is associated with the player's number so that it can later be retrieved to display the symbol associated with the player
                            #Puis on passe au joueur suivant / Then we move on to the next player
                            if Player==1:
                                Player=2
                            else:
                                Player=1
        playable=False #Ici, on mets la variable playable à false / Here we set the playable variable to false 
        i=0
        j=0
        #Ici il y a deux boucles pour vérifier  chaque case de la grille si elle est associé avec le chiffre 1 ou 2 si elle est associé à 1 alors on affiche un rond à l'emplacement souchhaité, si c'est 2 alors on affiche deux lignes formant une croix/ Here there are two loops to check whether each cell of the grid is associated with the number 1 or 2. If it is associated with 1, then a circle is displayed at the desired location, if it is 2, then two lines forming a cross are displayed.
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]==1:
                    pygame.draw.circle(screen, white, (80+160*(j+1), 80+160*(i+1)), 50)
                elif grid[i][j]==2:
                    pygame.draw.line(screen, white, (30+160*(j+1), 30+160*(i+1)), (130+160*(j+1), 130+160*(i+1)),10)
                    pygame.draw.line(screen, white, (130+160*(j+1), 30+160*(i+1)), (30+160*(j+1), 130+160*(i+1)),10)
                    #Ici si une des cases est égale à 0 et donc vide alors on repasse playable à true car le jeu peut continuer / Here, if one of the cells in the grid is equal to 0 and therefore empty, then playable is set back to true because the game can continue 
                elif grid[i][j]==0:
                    playable=True
        i=0
        j=0
        #On vérifie pour chaque différentes possibilités de victoire si elle est complétés, si oui alors on mets la valeur win au bon joueur / We check for each different possibility of victory if it is completed, if yes then we put the win value to the right player.
        for i in range(len(grid)):
            if grid[i][0]==grid[i][1]==grid[i][2]!=0: #Par exemple ici on vérifie s'il des lignes sont faites tout en vérifiant que ce n'est pas égale à 0 car ce serait des lignes vides / For example, here we check whether any rows have been created, while making sure that this is not equal to 0, as these would be empty rows
                win = "Player " + str(grid[i][0])
            elif grid[0][i]==grid[1][i]==grid[2][i]!=0:
                win = "Player " + str(grid[0][i])
            elif grid[0][0]==grid[1][1]==grid[2][2]!=0:
                win = "Player " + str(grid[1][1])
            elif grid[2][0]==grid[1][1]==grid[0][2]!=0:
                win = "Player " + str(grid[1][1])
    pygame.display.flip() #On actualise la fenêtre de jeu / We update the game window

pygame.quit()