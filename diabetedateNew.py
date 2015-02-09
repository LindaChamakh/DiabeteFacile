
def diminueinj(injection):
   try:
      assert injection>=0.5
      if injection<5:
         return injection-0.5
      else:
         if injection>=5 and injection<20:
            return injection-1
         else:
            return injection-2
   except:
      return 0

def augmenteinj(injection):
   if injection<5:
      return injection+0,5
   else:
      if injection>=5 and injection<20:
         return injection+1
      else:
         return injection+2

class simulateur():
   def __init__(self):
      self.jour1=[]
      self.jour2=[]
      self.courant=[]
   #jour 1: [matin: {glycemie:[taux d'insuline rapide, taux lente]}, midi: {glycemie:[taux d'insuline rapide, taux lente=0]}, soir: {glycemie:[taux d'insuline rapide, taux lente]}, nuit: {glycemie:[taux d'insuline rapide=0, taux lente=0]}], meme format pour jour2
   #initialisation de jour1 et jour2 avec donnees reelles   
   
   def ajoutedata(self,chemindufichier):
      #ouverture fichier texte et enregistrement donnees
      j=open(chemindufichier,'r')
      data=[]
      #9 lignes maintenant
      for ligne in j.readlines():
         #lignecourante=ligne.split()
         data.append(ligne.split())
         
      #assert len(data)==2 and len(data[0])==12 and len(data[1])==12  
      l=len(data)-10
      #jour1 : on lit les 3 premieres lignes a partir de l
      for i in range(l,l+4):
      	 
         self.jour1.append({float(data[i][1]):[float(data[i][2]),float(data[i][3])]})
    
      for i in range(l+5,l+9):
         self.jour2.append({float(data[i][1]):[float(data[i][2]),float(data[i][3])]})  
               
                  
      
   #moment: entier qui signifie matin/midi/soir/nuit: 0/1/2/3
   #si moment=2, on doit regarder la glycemie de la nuit: moment=3
   #on ne doit pas calculer de dose d'insuline lente a midi (1) et aucune dose la nuit (3)
   #les bornes d'hypoglycemie sont differentes la nuit: pour "tenir" jusqu'au matin, la glycemie doit etre au-dessus de 120 donc une hypoglycemie le jour precedent fait qu'on diminue les doses d'insulines au diner
   #sport et repas: booleen
   
   def insulinerapide(self,moment,sport,repas):
      k=0;
      assert 0<=moment<=2;
      
      #regarder glycemie moment+1 jour 2:
      #1er cas: glycemie de la veille trop basse -> on diminue l'injection
      #cas: moment=matin ou midi / moment=soir --> limite differente
      
      if (self.jour2[moment+1].keys()[0]<50 and moment <=1) or (self.jour2[moment+1].keys()[0]<120 and moment==2):
      #comment faire autrement pour acceder a la cle d'un element de la liste ?
         k=diminueinj(self.jour2[moment].values()[0][0])
         print("on diminue l'insuline rapide")
      
      #2eme cas: glycemie trop elevee sur deux jours-> on augmente l'injection
      else:
         if self.jour2[moment+1].keys()[0]>180 and self.jour1[moment+1].keys()[0]>180:
            k=augmenteinj(self.jour2[moment].values()[0][0])
            print("on augmente l'insuline rapide")
            
         else :
      #if self.jour2[moment+1].keys()[0]=<180 and self.jour2[moment+1].keys()[0]<=50:
            k=self.jour2[moment].values()[0][0]
            print("on garde la meme dose d'insuline rapide")
         
      #si sport -> on diminue l'injection   
      if sport==True:
         k=diminueinj(k);
         print("sport: on diminue la dose d'insuline rapide")
      
      #si bon repas -> on augmente l'injection
      if repas==True:
         k==augmenteink(k);
         print("bon repas: on augmente la dose d'insuline rapide")
      return k
      
      
      
   def insulinelente(self,moment,sport,repas):
      k=0;
      try:
      #regarder glycemie moment+1 jour 1 et jour 2 + insuline jour 1 et jour 2
	         
      	 assert moment==0 or moment==2
      	 if (self.jour2[moment+1].keys()[0]<50 and moment <=1) or (self.jour2[moment+1].keys()[0]<120 and moment==2):
	     #comment faire autrement pour acceder a la cle d'un element de la liste ?
	         k=diminueinj(self.jour2[moment].values()[0][1])
	         print("on diminue l'insuline lente")
	     
	     #2eme cas: glycemie trop elevee sur deux jours-> on augmente l'injection 
         else:
	         if self.jour2[moment+1].keys()[0]>180 and self.jour1[moment+1].keys()[0]>180:
	            k=augmenteinj(self.jour2[moment].values()[0][1])
	            print("on augmente l'insuline rlente")
	            
	         else :
	      #if self.jour2[moment+1].keys()[0]=<180 and self.jour2[moment+1].keys()[0]<=50:
	            k=self.jour2[moment].values()[0][1]
	            print("on garde la meme dose d'insuline lente")
	        
	        
         if sport==True:
		     k=diminueinj(k);
		     print("sport: on diminue la dose d'insuline lente")
		        
         if repas==True:
		     k=augmenteinj(k)
		     print("bon repas: on augmente la dose d'insuline lente")
		        
         return k
            
      except AssertionError:
         print("pas d'injection d'insuline lente le midi !")
      
     
Simuli=simulateur();
Simuli.ajoutedata("/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete89New.txt")
sport=False
repas=False

#simulation d'une journee a partir de vraies donnees

for i in range(3):
   print(i)
   print(Simuli.jour2[i].values()[0][1])
   print("rapide :")
   print(Simuli.insulinerapide(i,sport,repas))
   print("lente :")   
   print(Simuli.insulinelente(i,sport,repas))
   print("\n")

#rapidesoir=Simuli.insulinelente(soir,sport,repas)
#print(rapidesoir)
         
#resultats et comparaison avec les chiffres reels du 8 et 9 janvier 2014:
# simulateur: matin: 6 de rapide, 20 de lente, injecte reellement: idem
# midi: simulateur : 6 de rapide, reel: 6 aussi
# soir: simulateur: 5 de rapide et 7 de lente, reels: 7 de rapide et 9 de lente ! glycemie 3h apres le diner: 65, trop basse. Le simulateur avait raison de vouloir injecter moins.  
         
# objectif: etre en dessous de 120 avant le repas une fois sur deux
# repercussion jusqu'au matin si sport
# hyper puis hypo (acceleration ... --> augmente la glycemie)
      
      
      