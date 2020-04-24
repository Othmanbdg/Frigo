import random
from tkinter import *

ingredient=['sauces','yaourts','fruits','legumes','viandes','eau','soda','glace','fromage','lait']

temoin=['sauces','yaourts','fruits']

prsn=[]
path=r"C:/Users/Vil/Desktop/"
def gens(num):
    var = 1
    secu=[]
    prsn.clear()
    for i in range(num):
        a = random.randint(0,len(ingredient)-1)
        while a == 0:
            a = random.randint(0,len(ingredient)-1)
        b=frigo(a)
        if b in secu:
            b=frigo(a)
        b.append(var)
        var = var +1
        prsn.append(b)
        secu.append(b)


def frigo(num):
    L=[]
    cuse=[]
    for i in range (num):
        a=random.randint(0,len(ingredient)-1)
        b=ingredient[a]
        if b in L:
            a=random.randint(0,len(ingredient)-1)
            b=ingredient[a]
        else:
            L.append(b)
    return L


def knn(temoin):
    vide=[]
    for elt in temoin:
        for i in range (len(prsn) - 1):
            a = prsn[i]
            for elts in a:
                if  elt == elts:
                    if a not in vide:
                        vide.append(a)
    c=len(vide)
    dede=''
    for i in range(c):
        d=vide[i]
        x=d[-1]
        dede=dede+str(x)+","
    if len(dede) == 2:
        print("le frigo similaire est le numero: "+dede)
    if len(dede) > 2:
        print('les frigos similaires ont le numero:'+dede)
    if vide==[]:
        print('aucun frigo similaire')
    return vide


def autre(prsn,vide):
    zzz= []
    for item in prsn:
        if item not in vide:
            zzz.append(item)
    return zzz


def voisin(vide,K):
    if K > len(vide):
        print("vous avez dépassé le nombre d'element de la liste")
    if K == 1:
        print('Le voisin le plus proche est la liste numéros'+" "+str(vide[0][-1]))
    
    if K<len(vide) and K<1:
        T=vide[:K]
        beto=''
        for elt in T:
            q = elt[-1]
            beto = beto + str(q) + ','
            print("les "+ " " + str(K)+" "+" plus proches voisins sont les numeros " + beto)
    if K==len(vide):
        print(vide)


gens(3)
vide = knn(temoin)
sss = autre(prsn,vide)
vide.extend(sss)


app = Tk()
app.title("KNN")
screen_x=int(app.winfo_screenwidth())
screen_y=int(app.winfo_screenheight())
window_x=1024
window_y=768
posX= ( screen_x // 2) - (window_x // 2)
posY= ( screen_y // 2) - (window_y // 2)
geo="{}x{}+{}+{}".format(window_x,window_y,posX,posY)
app.geometry(geo)
app.configure(bg="#8c7ae6")


image= PhotoImage(file=path+"frigo.png")
btn = Button(app,image=image)
btn.pack()
btn.place(x=400,y=100)
X=[100,400,700,1000,1300,100,400,700,1000,1300]
Y=[100,100,100,100,100,600,600,600,600,600]
def affiche(o):
    for i in range (o):
        btn = Button(app,image=image)
        btn.pack()
        btn.place(x=X[i],y=Y[i])
affiche(len(vide))
#légumes sauces soda steak et yaourt
legumex=[140,440,740]
legumey=[280,280,280]
saucex=[250,550,850]
saucey=[290,290,290]
sodax=[200,500,800]
soday=[290,290,290]
steakx=[135,435,735]
steaky=[330,330,330]
yaourtx=[230,530,830]
yaourty=[330,330,330]
legume=PhotoImage(file=path+"legumes.png")
sauces=PhotoImage(file=path+"sauces.png")
soda=PhotoImage(file=path+"soda.png")
steak= PhotoImage(file=path+"steak.png")
yaourt= PhotoImage(file=path+"yaourt.png")





def test(vide):
    for i in range(vide[-1][-1]):
        for item in vide[i]:
            o=0
            if item=='legumes':
                leg= Button(app,image=legume)
                leg.pack()
                leg.place(x=legumex[i],y=legumey[o])
            if item=='sauces':
                sauc= Button(app,image=sauces)
                sauc.pack()
                sauc.place(x=saucex[i],y=saucey[o])        
            if item=='viandes':
                stak=Button(app,image=steak)
                stak.pack()
                stak.place(x=steakx[i],y=steaky[o])
            if item=='yaourts':
                yaa = Button(app,image=yaourt)
                yaa.pack()
                yaa.place(x=yaourtx[i],y=yaourty[o])
            if item=='soda':
                sod= Button(app,image=soda)
                sod.pack()
                sod.place(x=sodax[i],y=soday[o])
            
            
            o=o+1
test(vide)

        

app.mainloop()
























