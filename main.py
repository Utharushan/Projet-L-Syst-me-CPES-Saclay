from turtle import * # importe toutes les fonctions du module turtle

##color('red')
####couleur du crayon
####La boucle while contient toutes les instructions donnees a la tortue
##pos()
####affichage de la position initiale de la tortue : l'origine (0,0)

#-------------------------------------------------------------------------------
#DESSINER AVEC LE MODULE TURTLE

def carre():
    """Trace un carré à l'aide d'une boucle while"""
    while True :
        forward(100) # avance de 100 pixels
        left(90) # tourne a gauche de 90 degres
        if abs(pos())<1 : # si la position est a une distance de (0,0) inferieur a 1
            break # on sort de la boucle
    done()# On lance la construction
##carre()

def triangle_equi():
    """Trace un triangle équilatéral"""
    while True:
        forward(100)
        left(120)
        if abs(pos())<1:
            break
    done()
##triangle_equi()

def hexagone():
    """Trace un hexagone"""
    while True:
        forward(100)
        left(60)
        if abs(pos())<1:
            break
    done()
##hexagone()

def carre_for():
    """Dessine un trait de 100 pixels, forme un angle de 90° et le répète 4 fois.
Il dessine donc un carré."""
    for i in range(4):
        forward(100)
        left(90)
    done()
##carre_for()

def cercles_og():
    """Dessine 8 cercles de rayon croissant depuis la même origine."""
    rayon = 20
    while rayon<100:
        circle(rayon)
        rayon += 10
    done()
##cercles_og()


def cercle_con():
    """Dessine 8 cercles concentriques avec un rayon qui augmente de 10 pixels à chaque itération."""
    rayon =20
    while rayon < 100 :
        circle(rayon)
        up()
        right(90)
        forward(10)
        left(90)
        down()
        rayon+=10
    done()
##cercle_con()



#------------------------------------------------------------------------------
#TRACER UN MOT
    
def traceLsysteme(mot, angle=90, echelle=1):
    """Trace le dessin correspondant aux lettres du mot"""
    for e in mot:
        if e=="A" or e=="B":
            forward(100*echelle)
        elif e=="g":
            left(angle)
        elif e=="d":
            right(angle)
##traceLsysteme("AgAdAAdAdA")


#------------------------------------------------------------------------------
#L-SYSTEME AVEC UNE SEULE REGLE DE REMPLACEMENT

def remplacer1(mot, lettre, motif):
    """Remplace une lettre par un motif dans un mot"""
    nouveau_mot=''
    for e in mot:
        if e==lettre:
            nouveau_mot+=motif
        else:
            nouveau_mot+=e 
    return nouveau_mot
##print(remplacer1("BgAdB", "A", "ABA"))

def itereLsysteme1(depart, regle, k):
    """Renvoie le k-ième itéré du L-système"""
    for i in range(k):
        depart = remplacer1(depart, regle[0], regle[1])
    return depart
depart="A"
regle=("A", "AgAdAdAgA")
k = 3
##print(itereLsysteme1(depart, regle, k))

def traceK_Lsysteme(depart, regle, angle=90):
    """Trace les k-ième itéré d'un L-système"""
    up()
    goto(-300, -300)
    down()
    speed(0)
    for i in range(6):
        traceLsysteme(depart, angle, 1/(2**i))
        depart = itereLsysteme1(depart, regle, i)
    done()
##traceK_Lsysteme(depart, regle)
####Trace une fractale de pyramides avec l'angle par défaut.

traceK_Lsysteme("A", ("A", "AgAddAgA"), 60)
####Flocon de Von Koch


#------------------------------------------------------------------------------
#AVEC DEUX REGLES DE REMPLACEMENT - TRIANGLE DE SIERPINSKI

def remplacer2(mot, lettre1, motif1, lettre2, motif2):
    """Remplace simultanément deux lettres différentes avec deux motifs différents dans un mot"""
    new_word = ''
    for i in range(len(mot)):
        if mot[i]==lettre1:
            new_word += motif1
        elif mot[i]==lettre2:
            new_word += motif2
        else:
            new_word += mot[i]
    return new_word

def itereLsysteme2(depart, regle1, regle2, k):
    """Renvoie le k-ième itéré du L-système avec deux règles de remplacement"""
    for i in range(k):
        depart = remplacer2(depart, regle1[0], regle1[1], regle2[0], regle2[1])
    return depart

def traceK_Lsysteme2(depart, regle1, regle2, k, angle=-120):
    """Trace les k-ième itéré d'un L-système avec deux règles de remplacement"""
    up()
    goto(-100, -100)
    down()
    speed(0)
    for i in range(k):
        depart = remplacer2(depart, regle1[0], regle1[1], regle2[0], regle2[1])
    traceLsysteme(depart, angle, 1/(i+1))
    done()

##traceK_Lsysteme2("AdBdB", ("A", "AdBgAgBdA"), ("B", "BB"), 4)
####Triangle de Sierpinski

#------------------------------------------------------------------------------
#REPRESENTER DES PLANTES

#6.1 AVANCER SANS TRACER
    
def traceLsysteme(mot, angle=90, echelle=1):
    """Trace le dessin correspondant aux lettres du mot avec les lettres a et b"""
    for e in mot:
        if e=="A" or e=="B":
            forward(6*echelle)
        elif e=='a':
            up()
            forward(6*echelle)
            down()
        elif e=="g":
            left(angle)
        elif e=="d":
            right(angle)

##traceK_Lsysteme2("AdAdAdA", ("A", "AgadAAgAgAAgAagAAdagAAdAdAAdAadAAA"), ("a", "aaaaaa"), 2, 90)


#6.2 RETOUR EN ARRIERE
            
def traceLsysteme(mot, angle=90, echelle=1):
    """Trace le dessin correspondant aux lettres du mot avec les lettres a et b
et en gérant les cas où le caractère rencontré est [ ou ]"""
    L = []
    for e in mot:
        if e=="A" or e=="B":
            forward(6*echelle)
        elif e=='a':
            up()
            forward(6*echelle)
            down()
        elif e=="g":
            left(angle)
        elif e=="d":
            right(angle)
        elif e=='[':
            L.append(position())
            L.append(heading())
        elif e==']':
            up()
            setheading(L.pop())
            goto(L.pop())
            down()

def traceK_Lsysteme(depart, regle, angle=90):
    """Trace les k-ième itéré d'un L-système avec la gestion des crochets"""
    setheading(90)
    speed(0)
    for i in range(5):
        traceLsysteme(depart, angle, 1)
        depart = itereLsysteme1(depart, regle, i)
    done()

##traceK_Lsysteme("A", ("A", "A[gA]A[dA][A]"), 25)
##traceK_Lsysteme("A", ("A", "A[gA]A[dA]A"), 25)

def traceK_Lsysteme2(depart, regle1, regle2,angle=25):
    """Trace les k-ième itéré d'un L-système avec deux règles de remplacement avec la gestion des crochets"""    
    setheading(90)
    speed(0)
    for i in range(5):
        depart = remplacer2(depart, regle1[0], regle1[1], regle2[0], regle2[1])
    traceLsysteme(depart, 25)
    done()
    
##traceK_Lsysteme2("X", ("X", "A[gX][X]A[gX]dAX"), ("A", "AA"))
##traceK_Lsysteme2("X", ("X", "A[gX]A[dX]AX"), ("A", "AA"))
##traceK_Lsysteme2("X", ("X", "Ad[[X]gX]gA[gAX]dX"), ("A", "AA"))            


    
