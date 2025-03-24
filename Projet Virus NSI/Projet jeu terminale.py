import pygame
import time

#Création d'une classe Blok qui va associer aux blocs les informations nécessaires
class Blok:
    def __init__(self,image,coo,gridpos=[]):
        self.image=image
        self.coo=coo
        self.gridpos=gridpos

    def get_image(self):
        return self.image

    def get_coo(self):
        return self.coo
    
    def get_gridpos(self):
        return self.gridpos
      
    def set_coo(self,nvcoo):
        self.coo=nvcoo
    
    def set_gridpos(self,nvgridpos):
        self.gridpos=nvgridpos

    def set_gridposSpe(self,i,j,nvgridpos):
        self.gridpos[i][j]=nvgridpos

#Création d'une classe Button qui va associer aux bouttons les informations nécessaires
class Button:
    def __init__(self,img,coo,dim,page,path):
        self.img=img
        self.coo=coo
        self.dim=dim
        self.page=page
        self.path=path
    
    def get_img(self):
        return self.img

    def get_coo(self):
        return self.coo
    
    def get_dim(self):
        return self.dim
    
    def get_page(self):
        return self.page
    
    def get_path(self):
        return self.path

    def set_coo(self,coo):
        self.coo=coo

#Importation pour le Menu
bg_menu=pygame.image.load("./assets/bgLevelSelect.jpg")
logo=pygame.image.load("./assets/sglLogo.png")
img_St=pygame.image.load("./assets/StarterButton.png")
img_Jun=pygame.image.load("./assets/JuniorButton.png")
img_Exp=pygame.image.load("./assets/ExpertButton.png")
img_Mas=pygame.image.load("./assets/MasterButton.png")
WaitingBG=pygame.image.load("./assets/loading.gif")
Indicator=pygame.image.load("./assets/Indicator.png")

#Importation pour les niveaux
bg=pygame.image.load("./assets/download.jpg")
img_Virus=pygame.image.load("./assets/Virus.png")
img_BlocB=pygame.image.load("./assets/Blue_2.png")
img_BlocB90=pygame.image.load("./assets/Blue_290.png")
img_BlocR=pygame.image.load("./assets/Pink_2.png")
img_BlocV3180=pygame.image.load("./assets/Green_3180.png")
img_BlocV=pygame.image.load("./assets/Purple_3.png")
img_BlocViolet90=pygame.image.load("./assets/Purple_390.png")
img_BlocV2=pygame.image.load("./assets/Green_2.png")
img_Bloc=pygame.image.load("./assets/obstacle.png")
img_Res=pygame.image.load("./assets/btnReset.png")
img_Menu=pygame.image.load("./assets/btnHome.png")
img_Arrows=pygame.image.load("./assets/btnArrows.png")
img_Quit=pygame.image.load("./assets/btnQuit.png")
EndScreen=pygame.image.load("./assets/EndScreen.png")
NumbScreen=pygame.image.load("./assets/NumbScreen.png")

#Création des objects blocs nécessaires
Virus = Blok(img_Virus,(0,0))
BlocB = Blok(img_BlocB,(0,0))
BlocB90 = Blok(img_BlocB90,(0,0))
BlocR = Blok(img_BlocR,(0,0))
BlocV90 = Blok(img_BlocViolet90,(0,0))
BlocV3180 = Blok(img_BlocV3180,(0,0))
BlocV = Blok(img_BlocV,(0,0))
BlocV2 = Blok(img_BlocV2,(0,0))
Bloc1 = Blok(img_Bloc,(0,0))
Bloc2 = Blok(img_Bloc,(0,0))

#Création des objets buttons
Starter=Button(img_St,(115,325),(272,59),"Menu",[True,False,1])
Junior=Button(img_Jun,(115,235),(272,59),"Menu",[True,False,3])
Expert=Button(img_Exp,(575,235),(272,59),"Menu",[True,False,5])
Master=Button(img_Mas,(575,325),(272,57),"Menu",[True,False,6])
Menu=Button(img_Menu,(850,190),(102,102),"Level",[True,True,0])
Reset=Button(img_Res,(850,120),(102,57),"Level",[True,False,11])
Arrows=Button(img_Arrows,(800,400),(125,82),"Level",[True,False,10])
End=Button(img_Quit,(850,50),(102,57),"All",[False,False,0])
ListBut=[Starter,Junior,Expert,Master,Reset,Menu,Arrows,End]

pygame.init()
screen = pygame.display.set_mode((960, 600))

#Initialisation des variables
running = True #Variable pour vérifier si le jeu est lancé
InMenu = True #Variable pour vérifier si on est dans la fenêtre du menu
CurrentLevel = 0 #Variable qui définit sur quelle niveau on est
NumbScreenBOOL = False #Variable qui vérifie si on est dans la fenêtre pour afficher les touches associés aux blocs
bo = False #Variable qui est à False lorsque les valeurs de base de chaque blocs ne sont pas mises à jour et qui passe à True lorsque ces variables sont actualisés
key_pressed = False #Variable vérfifiant si une touche du clavier est pressé 
changeable = True #Variable qui va servir à passer key_pressed en true ou false pour qu'un déplacement de pièce ne s'effectue qu'une seule fois lorsque les bonnes touches sont pressés
movingB = Virus #Variable qui va être associer à un Blok déplacable afin de savoir sur quelle bloc on est en train d'agir
moving = True #Variable qui va rester en True si le bloc peut se déplacer à l'endroit attendu et qui passera en False sinon
grid=[[True,True,True,True],[True,True,True],[True,True,True,True],[True,True,True],[True,True,True,True],[True,True,True],[True,True,True,True]] #Un tableau de tableaux qui représente la grille de jeu et qui va donc se modifier au fur et à mesure des places disponibles ou indisponibles de la grille

while running: #Vérification de si le jeu est bien lancé

    while InMenu and running: #Vérification de si le jeu est dans le Menu
        screen.blit(bg_menu,(0,0)) #Affichage du fond du menu
        screen.blit(logo,(50,50)) #Affichage du logo sur le menu
        for but in ListBut:     #Affichage de tous les boutons devant s'afficher sur le menu, on vérifie certains atributs de chaque bouton pour savoir s'il faut l'afficher ou non
            if Button.get_page(but)=="All" or Button.get_page(but)=="Menu":
                screen.blit(Button.get_img(but),Button.get_coo(but))
        screen.blit(Indicator,(309,140)) #Affichage de l'indicateur de niveau

        if CurrentLevel!=0:  #Ici, on repasse la varaible CurrentLevel à 0 au cas ou par exemple on quitte un niveau au milieu, c'est une vérification non obligatoire
            CurrentLevel==0

        for event in pygame.event.get(): #Dans cette boucle, on vérifie toute sorte d'action
            if event.type == pygame.QUIT: #En premier lieu si le joueur a fermé le jeu
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for but in ListBut: #Puis lors d'un click, on vérifie pour chaque boutton si c'est sur celui ci qu'on a cliqué et si oui, déclenché l'action associé
                    if Button.get_page(but)=="Menu" or Button.get_page(but)=="All" : #On vérifie si le boutton nest affiché sur le menu
                        if pygame.mouse.get_pos()[0] > Button.get_coo(but)[0] and pygame.mouse.get_pos()[1] > Button.get_coo(but)[1] and pygame.mouse.get_pos()[0] < Button.get_coo(but)[0] + Button.get_dim(but)[0] and pygame.mouse.get_pos()[1] < Button.get_coo(but)[1] + Button.get_dim(but)[1]:
                            if Button.get_path(but)[0]==False: #Le boutton X sert à fermer le jeu
                                running=False
                            elif Button.get_path(but)[1]==False: #On vérifie si le boutton ne doit pas fermer le jeu
                                if Button.get_path(but)[2]!=0: #Puis si le bouton doit changer le niveau actuel alors le jeu doit se lancer et donc ces actions se font
                                    bo=False #On remet bo à false pour bien reseter les positions des blocs au début du niveau
                                    screen.blit(WaitingBG,(0,0)) #Ici, c'est pour simuler un temps de chargement entre le menu et les niveaux
                                    pygame.display.flip()
                                    time.sleep(0.5)
                                    CurrentLevel=Button.get_path(but)[2] #On met currentLevel au niveau qu'il doit lancer puis on lance le jeu
                                    InMenu = False  
        pygame.display.flip()

    while not InMenu and running and NumbScreenBOOL:
        Button.set_coo(End,(840,20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > Button.get_coo(End)[0] and pygame.mouse.get_pos()[1] > Button.get_coo(End)[1] and pygame.mouse.get_pos()[0] < Button.get_coo(End)[0] + Button.get_dim(End)[0] and pygame.mouse.get_pos()[1] < Button.get_coo(End)[1] + Button.get_dim(End)[1]:
                    Button.set_coo(End,(850,50))
                    NumbScreenBOOL=False
        screen.blit(WaitingBG,(0,0))
        screen.blit(NumbScreen,(0,100))
        screen.blit(Button.get_img(End),Button.get_coo(End))
        pygame.display.flip()

    while not InMenu and running and not NumbScreenBOOL:
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and changeable == True:
                key_pressed = True
                changeable = False
            elif event.type == pygame.KEYUP:
                key_pressed = False
                changeable = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for but in ListBut:
                    if Button.get_page(but)=="Level" or Button.get_page(but)=="All":
                        if pygame.mouse.get_pos()[0] > Button.get_coo(but)[0] and pygame.mouse.get_pos()[1] > Button.get_coo(but)[1] and pygame.mouse.get_pos()[0] < Button.get_coo(but)[0] + Button.get_dim(but)[0] and pygame.mouse.get_pos()[1] < Button.get_coo(but)[1] + Button.get_dim(but)[1]:
                            if Button.get_path(but)[0]==True:
                                if Button.get_path(but)[1]==True:
                                    screen.blit(WaitingBG,(0,0))
                                    pygame.display.flip()
                                    time.sleep(0.5)
                                    InMenu = True
                                else:
                                    if Button.get_path(but)[2]==11:
                                        bo=False
                                    elif Button.get_path(but)[2]==10:
                                        NumbScreenBOOL=True
                            elif Button.get_path(but)[0]==False:
                                running=False

        if bo == False and CurrentLevel==1:
            Blok.set_coo(Virus,(358,180))
            Blok.set_coo(BlocV,(287,109))
            Blok.set_coo(Bloc1,(500,322))
            Blok.set_gridpos(Virus,[[(2,1),(3,1)],[(3,1)],[(2,1),(3,1)],[(2,1)],[(2,1),(3,1)]])
            Blok.set_gridpos(BlocV,[[(1,0),(1,1),(3,0)],[(1,0),(1,1),(3,0)],[(1,0),(1,1),(3,0)],[(1,0),(1,1),(3,0)],[(1,0),(1,1),(3,0)]])
            Blok.set_gridpos(Bloc1,[(4,4)])
            grid=[[True,True,True,True,None],[False,False,True,None],[True,False,True,True,None],[True,False,True,None],[True,True,False,True,None],[True,True,True,None],[True,True,True,True,None],[None,None,None,None,None]]
        elif bo == False and CurrentLevel==2:
            Blok.set_coo(Virus,(571,109))
            Blok.set_coo(BlocR,(287,109))
            Blok.set_coo(Bloc1,(571,251))
            Blok.set_coo(Bloc2,(287,251))
            Blok.set_gridpos(Virus,[[(1,2),(2,3)],[(2,3)],[(1,2),(2,3)],[(1,2)],[(1,2),(2,3)]])
            Blok.set_gridpos(BlocR,[[(1,0),(1,1)],[(1,0),(1,1)],[(1,0),(1,1)],[(1,0),(1,1)],[(1,0),(1,1)]])
            Blok.set_gridpos(Bloc1,[(3,2)])
            Blok.set_gridpos(Bloc2,[(3,0)])
            grid=[[True,True,True,True,None],[False,False,False,None],[True,True,True,False,None],[False,True,False,None],[True,True,True,True,None],[True,True,True,None],[True,True,True,True,None],[None,None,None,None,None],[None,None,None,None,None,None]]
        elif bo == False and CurrentLevel==3:
            Blok.set_coo(Virus,(571,251))
            Blok.set_coo(BlocV3180,(429,109))
            Blok.set_coo(Bloc1,(500,170))
            Blok.set_coo(Bloc2,(287,393))
            Blok.set_gridpos(Virus,[[(3,2),(4,3)],[(4,3)],[(3,2),(4,3)],[(3,2)],[(3,2),(4,3)]])
            Blok.set_gridpos(BlocV3180,[[(1,1),(3,1),(4,2)],[(1,1),(4,2)],[(1,1),(3,1),(4,2)],[(1,1),(3,1)],[(1,1),(3,1),(4,2)]])
            Blok.set_gridpos(Bloc1,[(2,2)])
            Blok.set_gridpos(Bloc2,[(5,0)])
            grid=[[True,True,True,True,None],[True,False,True,None],[True,True,False,True,None],[True,False,False,None],[True,True,False,False,None],[False,True,True,None],[True,True,True,True,None],[None,None,None,None,None],[None,None,None,None,None,None]]
        elif bo == False and CurrentLevel==4:
            Blok.set_coo(Virus,(571,109))
            Blok.set_coo(BlocB90,(216,109))
            Blok.set_coo(Bloc1,(429,38))
            Blok.set_coo(Bloc2,(429,251))
            Blok.set_gridpos(Virus,[[(1,2),(2,3)],[(2,3)],[(1,2),(2,3)],[(1,2)],[(1,2),(2,3)]])
            Blok.set_gridpos(BlocB90,[[(1,0),(2,0)],[(1,0),(2,0)],[(1,0)],[(1,0),(2,0)],[(2,0)]])
            Blok.set_gridpos(Bloc1,[(2,2)])
            Blok.set_gridpos(Bloc2,[(5,0)])
            grid=[[True,True,True,True,None],[False,False,False,None],[False,True,True,False,None],[True,False,True,None],[True,True,True,True,None],[True,True,True,None],[True,True,True,True,None],[None,None,None,None,None],[None,None,None,None,None,None]]
        elif bo == False and CurrentLevel==5:
            Blok.set_coo(Virus,(500,322))
            Blok.set_coo(BlocV90,(287,251))
            Blok.set_coo(Bloc1,(500,170))
            Blok.set_coo(Bloc2,(216,322))
            Blok.set_gridpos(Virus,[[(4,2),(5,2)],[(5,2)],[(4,2),(5,2)],[(4,2)],[(4,2),(5,2)]])
            Blok.set_gridpos(BlocV90,[[(3,0),(3,1),(5,1)],[(3,0),(3,1),(5,1)],[(3,0),(3,1),(5,1)],[(3,0),(3,1),(5,1)],[(3,0),(3,1),(5,1)]])
            Blok.set_gridpos(Bloc1,[(2,2)])
            Blok.set_gridpos(Bloc2,[(5,0)])
            grid=[[True,True,True,True,None],[True,True,True,None],[True,True,False,True,None],[False,False,True,None],[False,True,False,True,None],[True,False,False,None],[True,True,True,True,None],[None,None,None,None,None],[None,None,None,None,None,None]]
        elif bo == False and CurrentLevel==6:
            Blok.set_coo(Virus,(500,38))
            Blok.set_coo(BlocV2,(642,38))
            Blok.set_coo(BlocR,(358,180))
            Blok.set_coo(Bloc1,(439,251))
            Blok.set_coo(Bloc2,(216,322))
            Blok.set_gridpos(Virus,[[(0,2),(1,2)],[(1,2)],[(0,2),(1,2)],[(0,2)],[(0,2),(1,2)]])
            Blok.set_gridpos(BlocV2,[[(0,3),(2,3)],[(0,3),(2,3)],[(0,3),(2,3)],[(0,3),(2,3)],[(0,3),(2,3)]])
            Blok.set_gridpos(BlocR,[[(2,1),(2,2)],[(2,1),(2,2)],[(2,1),(2,2)],[(2,1),(2,2)],[(2,1),(2,2)]])
            Blok.set_gridpos(Bloc1,[(2,2)])
            Blok.set_gridpos(Bloc2,[(5,0)])
            grid=[[True,True,False,False,None],[True,True,False,None],[True,False,False,False,None],[True,False,True,None],[False,True,True,True,None],[True,True,True,None],[True,True,True,True,None],[None,None,None,None,None],[None,None,None,None,None,None]]

        keys = pygame.key.get_pressed()
        bo = True

        if key_pressed == True:
            if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
                for i in range (len(Blok.get_gridpos(movingB)[1])):
                    if Blok.get_gridpos(movingB)[1][i][0]%2!=0:
                        if grid[Blok.get_gridpos(movingB)[1][i][0]+1][Blok.get_gridpos(movingB)[1][i][1]+1]==True and moving:
                            moving=True
                        else:
                            moving=False
                    else:
                        if grid[Blok.get_gridpos(movingB)[1][i][0]+1][Blok.get_gridpos(movingB)[1][i][1]]==True and moving:
                            moving=True
                        else:
                            moving=False
                if moving:
                    for i in range(len(Blok.get_gridpos(movingB))):
                        for j in range(len(Blok.get_gridpos(movingB)[i])):
                            grid[Blok.get_gridpos(movingB)[i][j][0]][Blok.get_gridpos(movingB)[i][j][1]]=True
                    for n in range(len(Blok.get_gridpos(movingB))):
                        for h in range(len(Blok.get_gridpos(movingB)[n])):
                            if Blok.get_gridpos(movingB)[n][h][0]%2!=0:
                                grid[Blok.get_gridpos(movingB)[n][h][0]+1][Blok.get_gridpos(movingB)[n][h][1]+1]=False
                                Blok.set_gridposSpe(movingB,n,h,(Blok.get_gridpos(movingB)[n][h][0]+1,Blok.get_gridpos(movingB)[n][h][1]+1))
                            else:
                                grid[Blok.get_gridpos(movingB)[n][h][0]+1][Blok.get_gridpos(movingB)[n][h][1]]=False
                                Blok.set_gridposSpe(movingB,n,h,(Blok.get_gridpos(movingB)[n][h][0]+1,Blok.get_gridpos(movingB)[n][h][1]))
                    Blok.set_coo(movingB,(Blok.get_coo(movingB)[0]+71,Blok.get_coo(movingB)[1]+71))
                    key_pressed = False

            elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
                for i in range (len(Blok.get_gridpos(movingB)[2])):
                    if Blok.get_gridpos(movingB)[2][i][0]%2!=0:
                        if grid[Blok.get_gridpos(movingB)[2][i][0]-1][Blok.get_gridpos(movingB)[2][i][1]+1]==True and moving:
                            moving=True
                        else:
                            moving=False
                    else:
                        if grid[Blok.get_gridpos(movingB)[2][i][0]-1][Blok.get_gridpos(movingB)[2][i][1]]==True and moving:
                            moving=True
                        else:
                            moving=False
                if moving:
                    for i in range(len(Blok.get_gridpos(movingB))):
                        for j in range(len(Blok.get_gridpos(movingB)[i])):
                            grid[Blok.get_gridpos(movingB)[i][j][0]][Blok.get_gridpos(movingB)[i][j][1]]=True
                    for n in range(len(Blok.get_gridpos(movingB))):
                        for h in range(len(Blok.get_gridpos(movingB)[n])):
                            if Blok.get_gridpos(movingB)[n][h][0]%2!=0:
                                grid[Blok.get_gridpos(movingB)[n][h][0]-1][Blok.get_gridpos(movingB)[n][h][1]+1]=False
                                Blok.set_gridposSpe(movingB,n,h,(Blok.get_gridpos(movingB)[n][h][0]-1,Blok.get_gridpos(movingB)[n][h][1]+1))
                            else:
                                grid[Blok.get_gridpos(movingB)[n][h][0]-1][Blok.get_gridpos(movingB)[n][h][1]]=False
                                Blok.set_gridposSpe(movingB,n,h,(Blok.get_gridpos(movingB)[n][h][0]-1,Blok.get_gridpos(movingB)[n][h][1]))
                    Blok.set_coo(movingB,(Blok.get_coo(movingB)[0]+71,Blok.get_coo(movingB)[1]-71))
                    key_pressed = False
            
            elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:
                for i in range (len(Blok.get_gridpos(movingB)[3])):
                    if Blok.get_gridpos(movingB)[3][i][0]%2!=0:
                        if grid[Blok.get_gridpos(movingB)[3][i][0]-1][Blok.get_gridpos(movingB)[3][i][1]]==True and moving:
                            moving=True
                        else:
                            moving=False
                    else:
                        if grid[Blok.get_gridpos(movingB)[3][i][0]-1][Blok.get_gridpos(movingB)[3][i][1]-1]==True and moving:
                            moving=True
                        else:
                            moving=False
                if moving:
                    for i in range(len(Blok.get_gridpos(movingB))):
                        for j in range(len(Blok.get_gridpos(movingB)[i])):
                            grid[Blok.get_gridpos(movingB)[i][j][0]][Blok.get_gridpos(movingB)[i][j][1]]=True
                    for n in range(len(Blok.get_gridpos(movingB))):
                        for h in range(len(Blok.get_gridpos(movingB)[n])):
                            if Blok.get_gridpos(movingB)[n][h][0]%2!=0:
                                grid[Blok.get_gridpos(movingB)[n][h][0]-1][Blok.get_gridpos(movingB)[n][h][1]]=False
                                Blok.set_gridposSpe(movingB,n,h,(Blok.get_gridpos(movingB)[n][h][0]-1,Blok.get_gridpos(movingB)[n][h][1]))
                            else:
                                grid[Blok.get_gridpos(movingB)[n][h][0]-1][Blok.get_gridpos(movingB)[n][h][1]-1]=False
                                Blok.set_gridposSpe(movingB,n,h,(Blok.get_gridpos(movingB)[n][h][0]-1,Blok.get_gridpos(movingB)[n][h][1]-1))
                    Blok.set_coo(movingB,(Blok.get_coo(movingB)[0]-71,Blok.get_coo(movingB)[1]-71))
                    key_pressed = False

            elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
                for i in range (len(Blok.get_gridpos(movingB)[4])):
                    if Blok.get_gridpos(movingB)[4][i][0]%2!=0:
                        if grid[Blok.get_gridpos(movingB)[4][i][0]+1][Blok.get_gridpos(movingB)[4][i][1]]==True and moving:
                            moving=True
                        else:
                            moving=False
                    else:
                        if grid[Blok.get_gridpos(movingB)[4][i][0]+1][Blok.get_gridpos(movingB)[4][i][1]-1]==True and moving:
                            moving=True
                        else:
                            moving=False
                if moving:
                    for i in range(len(Blok.get_gridpos(movingB))):
                        for j in range(len(Blok.get_gridpos(movingB)[i])):
                            grid[Blok.get_gridpos(movingB)[i][j][0]][Blok.get_gridpos(movingB)[i][j][1]]=True
                    for n in range(len(Blok.get_gridpos(movingB))):
                        for h in range(len(Blok.get_gridpos(movingB)[n])):
                            if Blok.get_gridpos(movingB)[n][h][0]%2!=0:
                                grid[Blok.get_gridpos(movingB)[n][h][0]+1][Blok.get_gridpos(movingB)[n][h][1]]=False
                                Blok.set_gridposSpe(movingB,n,h,(Blok.get_gridpos(movingB)[n][h][0]+1,Blok.get_gridpos(movingB)[n][h][1]))
                            else:
                                grid[Blok.get_gridpos(movingB)[n][h][0]+1][Blok.get_gridpos(movingB)[i][j][1]-1]=False
                                Blok.set_gridposSpe(movingB,n,h,(Blok.get_gridpos(movingB)[n][h][0]+1,Blok.get_gridpos(movingB)[n][h][1]-1))
                    Blok.set_coo(movingB,(Blok.get_coo(movingB)[0]-71,Blok.get_coo(movingB)[1]+71))
                    key_pressed = False
        moving=True
        
        screen.blit(Blok.get_image(Virus),Blok.get_coo(Virus))
        for but in ListBut:
            if Button.get_page(but)=="All" or Button.get_page(but)=="Level":
                screen.blit(Button.get_img(but),Button.get_coo(but))

        if keys[pygame.K_KP_0]:
            movingB = Virus

        if CurrentLevel==1:
            if keys[pygame.K_KP_5]:
                movingB = BlocV
            screen.blit(Blok.get_image(BlocV),Blok.get_coo(BlocV))
            screen.blit(Blok.get_image(Bloc1),Blok.get_coo(Bloc1))
        elif CurrentLevel==2:
            if keys[pygame.K_KP_8]:
                movingB = BlocR
            screen.blit(Blok.get_image(BlocR),Blok.get_coo(BlocR))
            screen.blit(Blok.get_image(Bloc1),Blok.get_coo(Bloc1))
            screen.blit(Blok.get_image(Bloc2),Blok.get_coo(Bloc2))
        elif CurrentLevel==3:
            if keys[pygame.K_KP_1]:
                movingB = BlocV3180
            screen.blit(Blok.get_image(BlocV3180),Blok.get_coo(BlocV3180))
            screen.blit(Blok.get_image(Bloc1),Blok.get_coo(Bloc1))
            screen.blit(Blok.get_image(Bloc2),Blok.get_coo(Bloc2))
        elif CurrentLevel==4:
            if keys[pygame.K_KP_3]:
                movingB = BlocB90
            screen.blit(Blok.get_image(BlocB90),Blok.get_coo(BlocB90))
            screen.blit(Blok.get_image(Bloc1),Blok.get_coo(Bloc1))
            screen.blit(Blok.get_image(Bloc2),Blok.get_coo(Bloc2))
        elif CurrentLevel==5:
            if keys[pygame.K_KP_5]:
                movingB = BlocV90
            screen.blit(Blok.get_image(BlocV90),Blok.get_coo(BlocV90))
            screen.blit(Blok.get_image(Bloc1),Blok.get_coo(Bloc1))
            screen.blit(Blok.get_image(Bloc2),Blok.get_coo(Bloc2))
        elif CurrentLevel==6:
            if keys[pygame.K_KP_7]:
                movingB = BlocV2
            elif keys[pygame.K_KP_8]:
                movingB = BlocR
            screen.blit(Blok.get_image(BlocV2),Blok.get_coo(BlocV2))
            screen.blit(Blok.get_image(BlocR),Blok.get_coo(BlocR))
            screen.blit(Blok.get_image(Bloc1),Blok.get_coo(Bloc1))
            screen.blit(Blok.get_image(Bloc2),Blok.get_coo(Bloc2))

        if InMenu==False:
            pygame.display.flip()
        if Blok.get_coo(Virus)==(216,38):
            screen.blit(EndScreen,(274,100))
            pygame.display.flip()
            time.sleep(0.5)
            bo=False
            CurrentLevel+=1
            if CurrentLevel==7:
                InMenu=True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()