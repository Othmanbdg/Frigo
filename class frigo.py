import random
from tkinter import *
path=r"C:/Users/Vil/Desktop/"
class KNN:
    def __init__(self,k,temoin):
        self.ingredient=['sauces','yaourts','fruits','legumes','viandes','eau','soda','glace','fromage','lait']
        self.prsn=[]
        self.temoin=temoin
        self.legumex=[140,440,740]
        self.legumey=[280,280,280]
        self.saucex=[250,550,850]
        self.saucey=[290,290,290]
        self.sodax=[200,500,800]
        self.soday=[290,290,290]
        self.steakx=[135,435,735]
        self.steaky=[330,330,330]
        self.yaourtx=[230,530,830]
        self.yaourty=[330,330,330]
        self.X=[100,400,700,1000,1300,100,400,700,1000,1300]
        self.Y=[100,100,100,100,100,600,600,600,600,600]
        self.vide=[]
        self.legume=''
        self.sauces=''
        self.soda=''
        self.steak=''
        self.yaourt= ''
        self.image= ''
        self.app = Tk()
        self.k=k
    def frigo(self,num):
        L=[]
        for i in range (num):
            a=random.randint(0,len(self.ingredient)-1)
            b=self.ingredient[a]
            if b in L:
                a=random.randint(0,len(self.ingredient)-1)
                b=self.ingredient[a]
            else:
                L.append(b)
        return L
    def gens(self):
        var = 1
        secu=[]
        for i in range(3):
            a = random.randint(0,len(self.ingredient)-1)
            while a == 0:
                a = random.randint(0,len(self.ingredient)-1)
            b=self.frigo(a)
            if b in secu:
                b=self.frigo(a)
            b.append(var)
            var = var +1
            self.prsn.append(b)
            secu.append(b)
    def knn(self):
        vide=[]
        for elt in self.temoin:
            for i in range (len(self.prsn) - 1):
                a = self.prsn[i]
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
        
    def autre(self):
        zzz= []
        for item in self.prsn:
            if item not in self.vide:
                zzz.append(item)
        return zzz
    
    def affiche(self):
        for i in range (10):
            btn = Button(app,image=self.image)
            btn.pack()
            btn.place(x=self.X[i],y=self.Y[i])
    
    
    def test(self):
        for i in range(self.vide[-1][-1]):
            for item in self.vide[i]:
                o=0
                if item=='legumes':
                    leg= Button(self.app,image=self.legume)
                    leg.pack()
                    leg.place(x=self.legumex[i],y=self.legumey[o])
                if item=='sauces':
                    sauc= Button(self.app,image=self.sauces)
                    sauc.pack()
                    sauc.place(x=self.saucex[i],y=self.saucey[o])        
                if item=='viandes':
                    stak=Button(self.app,image=self.steak)
                    stak.pack()
                    stak.place(x=self.steakx[i],y=self.steaky[o])
                if item=='yaourts':
                    yaa = Button(self.app,image=self.yaourt)
                    yaa.pack()
                    yaa.place(x=self.yaourtx[i],y=self.yaourty[o])
                if item=='soda':
                    sod= Button(self.app,image=self.soda)
                    sod.pack()
                    sod.place(x=self.sodax[i],y=self.soday[o])
                o=o+1
    def voisin(self):
        if self.k > len(self.vide):
            print("vous avez dépassé le nombre d'element de la liste")
        if self.k == 1:
            print('Le voisin le plus proche est la liste numéros'+" "+str(slef.vide[0][-1]))
        
        if self.k<len(self.vide) and self.k<1:
            T=self.vide[:self.K]
            beto=''
            for elt in T:
                q = elt[-1]
                beto = beto + str(q) + ','
                print("les "+ " " + str(self.K)+" "+" plus proches voisins sont les numeros " + beto)

                
    def launch(self):
        self.gens()
        self.vide = self.knn()
        sss = self.autre()
        self.vide.extend(sss)
        self.app.title("KNN")
        screen_x=int(self.app.winfo_screenwidth())
        screen_y=int(self.app.winfo_screenheight())
        window_x=1024
        window_y=768
        posX= ( screen_x // 2) - (window_x // 2)
        posY= ( screen_y // 2) - (window_y // 2)
        geo="{}x{}+{}+{}".format(window_x,window_y,posX,posY)
        self.app.geometry(geo)
        self.app.configure(bg="#8c7ae6")
        self.legume=PhotoImage(file=path+"legumes.png")
        self.sauces=PhotoImage(file=path+"sauces.png")
        self.soda=PhotoImage(file=path+"soda.png")
        self.steak= PhotoImage(file=path+"steak.png")
        self.yaourt= PhotoImage(file=path+"yaourt.png")
        self.image= PhotoImage(file=path+"frigo.png")
        for i in range (10):
            btn = Button(self.app,image=self.image)
            btn.pack()
            btn.place(x=self.X[i],y=self.Y[i])
        self.voisin()
        self.test()
        self.app.mainloop()
    
        