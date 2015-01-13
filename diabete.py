# creation de la classe simulateur

donneesj=[200,5,5,100,5,200,5,5,200,200,5,5,100,5,200,5,5,200]

def diminueinj(injection):
   if injection<5:
      return injection-0.5
   if injection>=5 and injection<20:
      return injection-1
   else:
      return injection-2

def augmenteinj(injection):
   if injection<5:
      return injection+0,5
   if injection>=5 and injection<20:
      return injection+1
   else:
      return injection+2

class simulateur():
   def __init__(self):
      self.jour1=[]
      self.jour2=[]
   #data2jours=[jour 1: [matin: [ , , ], midi: [ , ], aprem: [ , , ], nuit: []], jour 2: [matin: [ , , ], midi: [ , ], soir: [ , , ], nuit: []]]
   #initialisation de data2jours avec donnees reelles   
   def ajoutedata(self,chemindufichier):
      #ouverture fichier texte et enregistrement donnees
      j=open(chemindufichier,'r')
      data=[]
      for ligne in j.readlines():
         #lignecourante=ligne.split()
         data.append(ligne.split())
      assert len(data)==2 and len(data[0])==12 and len(data[1])==12  
      for k in range(0,12,3):
         self.jour1.append({int(data[0][k]):[int(data[0][k+1]),int(data[0][k+2])]})
         self.jour2.append({int(data[1][k]):[int(data[1][k+1]),int(data[1][k+2])]})
         
      
   #moment: entier qui signifie matin/midi/soir/nuit
   #sport et repas: booleen
   
   def insulinerapide(self,moment,sport,repas):
      k=0;
      
      #regarder glycemie moment+1 jour 2:
      
      #1er cas: glycemie de la veille trop basse -> on diminue l'injection
      if self.jour2[moment+1].keys()[0]<50:
      #comment faire autrement pour acceder a la cle d'un element de la liste ?
         k=diminueinj(self.jour2[moment].values()[0][0])
      
      #2eme cas: glycemie trop elevee -> on augmente l'injection
      if self.jour2[moment+1].keys()[0]>180:
         k=augmenteinj(self.jour2[moment].values()[0][0])
            
      else :
      #if self.jour2[moment+1].keys()[0]=<180 and self.jour2[moment+1].keys()[0]<=50:
         k=self.jour2[moment].values()[0][0]
         
      #si sport -> on diminue l'injection   
      if sport==True:
         k=diminueinj(k);
      
      #si bon repas -> on augmente l'injection
      if repas==True:
         k==augmenteink(k);
      
      return k
      
   def insulinelente(self,moment,sport,repas):
      k=0;
      
      #regarder glycemie moment+1 jour 1 et jour 2 + insuline jour 1 et jour 2
      
      #si les injections sont differentes ou si on a une bonne glycemie le premier jour, on reste sur la meme injection que la veille
      if (self.jour1[moment].values()[1]!=self.jour2[moment].values()[1] or (self.jour2[moment].keys()[0]<=180 and self.jour2[moment].keys()[0]>=50)):
         k=self.jour2[moment].values()[0][1]
      
      #maintenant on traite les cas ou on est sur la meme injection de lente depuis deux jours avec une mauvaise glycemie apres le repas depuis deux jours
      #si ca fait deux jours qu'on est en hyperglycemie, on diminue    
      if self.jour1[moment].keys()[0]>180 and self.jour2[moment].keys()[0]>180:
         k=augmenteing(self.jour2[moment].values()[0][1]);
         
      else :
      #if self.data2jour[0][moment][0]<50 and self.data2jour[1][moment][0]<50:
         k=diminueinj(self.jour2[moment].values()[0][1]);
      
 #en fait, je me demande si les if s'executent bien successivement ?     
      if sport==TRUE:
         k=diminueinj(k);
      
      if repas==TRUE:
         k==augmenteink(k);
      
      return k

#if __name__ == '__main__':      
Simul=simulateur();
Simul.ajoutedata("/Users/lindachamakh/Desktop/diabete.txt")
sport=False
repas=False
k=Simul.insulinerapide(1,sport,repas)
print(k)
         
         
         
      
      
      
      
      
      
      
      
      
      