import sys
from PyQt4 import QtGui, QtCore
import diabete



class fenetre2(QtGui.QDialog):

        closeApp = QtCore.pyqtSignal()
        
        def __init__(self,simulateur,g,d,mom,sp,rep,il,ir,parent=None,c='Oui'):
                super(fenetre2,self).__init__(parent)
                self.simuli=simulateur
                self.glycemieValue=g
                self.databaseChemin=d
                self.moment=mom
                self.sport=sp
                self.repasRiche=rep
                self.insulineLente=il
                self.insulineRapide=ir
                self.caseCochee=c
                self.closeApp.connect(self.close) 
                self.initUI()


        def initUI(self):
                # Geometrie de la fenetre
                self.setGeometry(0,0,739,274)
                self.simulationFaite=QtGui.QLabel('Simulation faite !',self)
                self.simulationFaite.move(10,30)
                self.info='Tu devrais t injecter '+str(self.insulineLente)+' d insuline lente et '+str(self.insulineRapide)+' d insuline rapide'
                self.affichageSimulation=QtGui.QLabel(self.info,self)
                self.affichageSimulation.move(10,60)
                self.daccOuPas=QtGui.QLabel('Tu es d accord ?',self)
                self.daccOuPas.move(10,130) 
                # Boutons "oui" et "non" (utilisateur d'accord ou pas avec la simulation
                self.daccord=QtGui.QPushButton('Oui',self)
                self.daccord.move(80,180)
                self.pasDaccord=QtGui.QPushButton('Non',self)
                self.pasDaccord.move(210,180)
                # Affichage
               # self.show()
                # Connexion des deux boutons 'Oui' et 'Non'
                self.daccord.clicked.connect(self.slot)
                
                self.pasDaccord.clicked.connect(self.slot)

        def slot(self):
                sender=self.sender()
                if sender.text()=='Oui':
                        
                        self.caseCochee='Oui'
                        
                        #partie enregistrement
                else:
                        assert sender.text()=='Non'
                        self.caseCochee='Non'
                        #partie ouverture d'une nouvelle fenetre
                        
                cC=self.caseCochee
                self.traitementDecision(cC)

        def traitementDecision(self,cC):               
                               
                if cC=='Oui':
                        d=dict([])
                        print(self.glycemieValue)
                        d[self.glycemieValue]=[]
                        d[self.glycemieValue].append(self.insulineRapide)
                        d[self.glycemieValue].append(self.insulineLente)
                        self.simuli.courant[self.moment]=d
                        print(self.simuli.courant)
                        self.closeApp.emit()
                                          

                else:  
                        assert(cC=='Non')
                        d=dict([])
                        #d[0]={}
                        d[self.glycemieValue]=[]

                        tauxRapide, ok = QtGui.QInputDialog.getDouble(self,'Ton choix', 'Combien t injecteras tu d insuline rapide ?')
                        if ok:
                               d[self.glycemieValue].append(tauxRapide)
                               
                               
                        else: # Normalement il devrait pas y avoir d'erreur ici mais on sait jamais
                               reponse=QtGui.QMessageBox.question(self,'Un probleme est arrive',
                                                          'Je vais devoir quitter, dsl ! Merci de me laisser partir en cliquant sur ok ;)',
                                                          QtGui.QMessageBox.Yes)
                                                     
                               assert(reponse==QtGui.QMessageBox.Yes)
                               QtCore.QCoreApplication.instance().quit()
                               
                        tauxLente, ok = QtGui.QInputDialog.getDouble(self,'Ton choix', 'Combien t injecteras tu d insuline lente ?')
                        if ok:
                              d[self.glycemieValue].append(tauxLente)
                              self.closeApp.emit()
                        else: # Idem
                               reponse=QtGui.QMessageBox.question(self,'Un probleme est arrive',
                                                                  'Je vais devoir quitter, dsl ! Merci de me laisser partir en cliquant sur ok ;)',
                                                                  QtGui.QMessageBox.Yes)
                                                             
                               #ces lignes ne marchent pas je crois:
                               assert(reponse==QtGui.QMessageBox.Yes)
                               QtCore.QCoreApplication.instance().quit()
                        
                        self.simuli.courant[self.moment]=d
                               
                self.miseAJourFichierTexte()


        
        def miseAJourFichierTexte(self):
                r=0
                infos=self.simuli.courant
                glycemies=[]
                for i in range(3):
                		if (self.simuli.courant[i]==dict([])):
                			r=1
                		#glycemies.append(list(infos[i].keys())[0])
                #for i in range(3):
                 #       if (self.simuli.courant[i]==dict([])):
                  #             r=1
                if (r==0):
                # (len(self.simuli.courant)==4): # i.e si toutes les donnees du matin au soir ont ete rajoutees a courant
                               
                        infos=self.simuli.courant
                        #probleme ici: infos n'est pas forcement un dico 
                        glycemies=list(infos.keys())
                        infosJourPrecedent=''
                        fichier=open(self.databaseInitialChemin,'r')
                        lignes=fichier.readlines()
                        infosJourPrecedent=lignes[1]
                        fichier.close()

                        fichier=open(self.databaseInitialChemin,'w')
                        fichier.write(infosJourPrecedent)
                        fichier.close()
                               
                        fichier=open(self.databaseInitialChemin,'a')
                        fichier.write('\n',
                                             glycemies[0],'\t',     # glycemie du matin
                                             infos[0][0],'\t',      # insuline rapide du matin 
                                             infos[0][1],'\t',      # insuline lente du matin
                                             glycemies[1],'\t',     # glycemie du midi
                                             infos[1][0],'\t',      # insuline rapide du midi                                                              
                                             infos[1][1],'\t',      # insuline lente du midi                        
                                             glycemies[2],'\t',     # glycemie du soir
                                             infos[2][0],'\t',      # insuline rapide du soir                               
                                             infos[2][1],'\t',)     # insuline lente du soir
                        fichier.close()


        def closeEvent(self,event):
        		reply = QtGui.QMessageBox.question(self, 'Message',"Es-tu sur de ton choix ?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        		if reply == QtGui.QMessageBox.Yes:
            			event.accept()
        		else:
            			event.ignore()


class pageAccueil(QtGui.QMainWindow):
        def __init__(self,s=diabete.simulateur(),d="C:\Users\alexandre\Desktop\Ponts\Python\DiabeteFacile\diabete8-9janv2014.txt",m=0,sp=False,rep=False):
			super(pageAccueil,self).__init__()
			self.simuli=s
			self.databaseInitialChemin=d
			self.moment=m
			self.sport=sp
			self.repasRiche=rep
			self.initUI()

#s=diabete.simulateur()
        def initUI(self):
                
                # Definition des widgets
                # Textes
                self.QuelRepas=QtGui.QLabel('Quel repas ?',self)
                self.QuelRepas.move(2,30)
                self.Sport=QtGui.QLabel('Sport ?',self)
                self.Sport.move(140,30)
                self.RepasRiche=QtGui.QLabel('Repas riche ?',self)
                self.RepasRiche.move(250,30)
                self.CombienGlycemie=QtGui.QLabel('Glycemie ?',self)
                self.CombienGlycemie.move(10,140)
                # Cases a cocher
                self.PtitDej=QtGui.QCheckBox('Ptit dej', self)
                self.PtitDej.move(0,60)
                self.Dejeuner=QtGui.QCheckBox('Dejeuner', self)
                self.Dejeuner.move(0,80)
                self.Diner=QtGui.QCheckBox('Diner', self)
                self.Diner.move(0,100)
                self.SportOui=QtGui.QCheckBox('Oui', self)
                self.SportOui.move(130,60)
                self.SportNon=QtGui.QCheckBox('Non', self)
                self.SportNon.move(130,80)
                self.RepasRicheOui=QtGui.QCheckBox('Oui', self)
                self.RepasRicheOui.move(250,60)
                self.RepasRicheNon=QtGui.QCheckBox('Non', self)
                self.RepasRicheNon.move(250,80)
                # Zone de saisie de texte
                self.ZoneEntreeGlycemie=QtGui.QLineEdit(self)
                self.ZoneEntreeGlycemie.move(20,190)
                # Bouton "simuler"
                self.BoutonSimuler=QtGui.QPushButton('Simuler',self)
                self.BoutonSimuler.move(330,190)
                
                
                # Connexion des widgets		
                # Connexion des checkbox
                self.PtitDej.stateChanged.connect(self.choixRepas)
                self.Dejeuner.stateChanged.connect(self.choixRepas)
                self.Diner.stateChanged.connect(self.choixRepas)
                self.SportOui.stateChanged.connect(self.choixSport)
                self.SportOui.stateChanged.connect(self.choixSport)
                self.RepasRicheOui.stateChanged.connect(self.choixRepasRiche)
                self.RepasRicheNon.stateChanged.connect(self.choixRepasRiche)
                # Connexion du bouton 'Simuler'
                self.BoutonSimuler.clicked.connect(self.simulerClicked)
                # Geometrie et affichage de la fenetre principale 
                self.setGeometry(300,300,534,339)
                self.setWindowTitle('DiabeteFacile')
                self.show()
                # Allocation memoire pour courant
                for i in range(3):
                        self.simuli.courant.append(dict([]))
                      



        # Mise a jour de l'attribut moment selon la case coche
        def choixRepas(self):
                sender=self.sender()
                if sender.text()==self.trUtf8("Ptit dej"):
                        self.moment=0
                elif sender.text()==self.trUtf8("Dejeuner"):
                        self.moment=1
                else:
                        assert(sender.text()=='Diner')
                        self.moment=2
                        


        # Mise a jour de l'attribut sport selon la case coche
        def choixSport(self):
                sender=self.sender()
                if sender.text()=='Oui':
                        self.sport=True
                else:
                        assert(sender.text()=='Non')
                        self.sport=False

        # Mise a jour de l'attribut  selon la case coche
        def choixRepasRiche(self):
                sender=self.sender()
                if sender.text()=='Oui':
                        self.repasRiche=True
                else:
                        assert(sender.text()=='Non')
                        self.repasRiche=False


# La methode simulerClicked() enregistre le taux de glycemie saisi par l'utilisateur
        def simulerClicked(self):
                
                # Initialisation de simuli.courant
                glycemieValue=self.ZoneEntreeGlycemie.text()
                #self.ajouteData(databaseInitialChemin)
                self.simuli.ajoutedata(self.databaseInitialChemin)
                #d=dict([])
                #dbis=dict([])
                #dbis[glycemieValue]=[]
                #d[moment]=dbis
                #self.simuli.courant[moment]=d
                
                # Calculs 
                insulineLenteSimulee=self.simuli.insulinelente(self.moment,self.sport,self.repasRiche)
                insulineRapideSimulee=self.simuli.insulinerapide(self.moment,self.sport,self.repasRiche)
                
                # Affichage d'une nouvelle fenetre avec le resultat de la simulation dessus
                affichageSimulation=fenetre2(self.simuli,float(unicode(glycemieValue)), self.databaseInitialChemin,self.moment,self.sport,self.repasRiche,insulineLenteSimulee,insulineRapideSimulee)
                #affichageSimulation.show()
                affichageSimulation.exec_()
                               
                # decision est soit 'Oui' soit 'Non' pour savoir si l'utilisateur a accepte la simulation ou pas 
                #decision=affichageSimulation.getCaseCochee()
                               
     #           if decision=='Oui':
      #                  d=dict([])
       #                 d[glycemieValue]=[]
        #                d[glycemieValue].append(insulineRapideSimulee)
         #               d[glycemieValue].append(insulineLenteSimulee)
          #              self.simuli.courant[moment]=d                       

           #     else: # Normalement il devrait pas y avoir d'erreur ici mais on sait jamais 
            #            assert(decision=='Non')
             #           d=dict([])
              #          d[glycemieValue]=[]
               #                
                #        tauxRapide, ok = QtGui.QInputDialog.getDouble(self,'Ton choix', 'Combien t injecteras tu d insuline rapide ?')
                 #       if ok:
                  #             dbis[glycemieValue].append(tauxRapide)
                   #     else:
                    #           reponse=QtGui.QMessageBox.question(self,'Un probleme est arrive',
                     #                                     'Je vais devoir quitter, dsl ! Merci de me laisser partir en cliquant sur ok ;)',
                        #                                  QtGui.QMessageBox.Yes)
                         #                            
                          #     assert(reponse==QtGui.QMessageBox.Yes)
                           #    QtCore.QCoreApplication.instance().quit()
                               
 #                       tauxLente, ok = QtGui.QInputDialog.getDouble(self,'Ton choix', 'Combien t injecteras tu d insuline lente ?')
  #                      if ok:
   #                           dbis[glycemieValue].append(tauxLente)
    #                    else: # Idem
     #                          reponse=QtGui.QMessageBox.question(self,'Un probleme est arrive',
      #                                                            'Je vais devoir quitter, dsl ! Merci de me laisser partir en cliquant sur ok ;)',
       #                                                           QtGui.QMessageBox.Yes)
        #                                                     
         #                      assert(reponse==QtGui.QMessageBox.Yes)
          #                     QtCore.QCoreApplication.instance().quit()
           #             d[moment]=dbis
            #            self.simuli.courant[moment]=d
             #   self.miseAJourFichierTexte()


        # Mise a jour du fichier texte contenant les injections et taux de glycemie des deux jours precedents
#        def miseAJourFichierTexte(self):
 #               r=0
  #              for i in range(3):
   #                     if (self.simuli.courant[i]==dict([])):
    #                           r=1
     #           if (r==0): # i.e si toutes les donnes du matin au soir ont ete rajoutees a courant
      #                         
       #                 infos=self.simuli.courant
        #                glycemies=list(infos.keys())
         #               infosJourPrecedent=''
#
 #                       with open(self.databaseInitialChemin,'r') as fichier:
  #                             lignes=fichier.readlines()
   #                            infosJourPrecedent=lignes[1]
#
 #                       with open(self.databaseInitialChemin,'w') as fichier:
  #                             fichier.write(infosJourPrecedent)
   #                            
    #                    with open(self.databaseInitialChemin,'a') as fichier:
     #                          fichier.write('\n',
      #                                       glycemies[0],'\t',     # glycemie du matin
       #                                      infos[0][0],'\t',      # insuline rapide du matin 
        #                                     infos[0][1],'\t',      # insuline lente du matin
         #                                    glycemies[1],'\t',     # glycemie du midi
          #                                   infos[1][0],'\t',      # insuline rapide du midi                                                              
           #                                  infos[1][1],'\t',      # insuline lente du midi                        
            #                                 glycemies[2],'\t',     # glycemie du soir
             #                                infos[2][0],'\t',      # insuline rapide du soir                               
              #                               infos[2][1],'\t',)     # insuline lente du soir                
                        

def main():
        app=QtGui.QApplication(sys.argv)
        ex=pageAccueil()
        sys.exit(app.exec_())

if __name__=='__main__':
        main()
