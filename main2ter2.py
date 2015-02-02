import sys
from PyQt4 import QtGui, QtCore
import diabete



def ecrireOuPasMatin(chemin):

        fichier=open(chemin,'r')
        lignes=fichier.readlines()
        derniereLigne=lignes[len(lignes)-1].split()
        fichier.close()

        
        if moment==0:
                for c in derniereLigne:
                        print("dans m=0")
                        if c=='-1':
                               return False
                return True



def ecrireOuPasMidi(courant):

                print("dans m=1")
                cle=list(courant[1].keys())[0]
                if cle==-1: return False
                
                for c in courant[cle]:
                        print("Dans la fonction  ecrireOuPas, c =")
                        print(c)
                        print("\n")
                        if c=='-1':
                                return False
                return True               
##        elif moment==2:
##                print("dans m=2")
##                for c in derniereLigne[:6]:
##                        if c=='-1':
##                                return False
##                return True
##        
##        elif moment==3:
##                print("dans m=3")
##                for c in derniereLigne[:9]:
##                        if c=='-1':
##                                return False
##                return True
                

        
        
        
        



def miseAJourFichierTexte(simuli,chemin,moment):
        r=0
        infos=simuli.courant
        glycemies=[]

        #mise a jour de glycemies et infos

        for i in range(3):
                l=list(infos[i].keys())
                glycemies.append(l[0])

        
        matin="\n"+str(glycemies[0])+' '+str(infos[0].values()[0][0])+' '+str(infos[0].values()[0][1])
        midi=' '+str(glycemies[1])+' '+str(infos[1].values()[0][0])+' '+ str(infos[1].values()[0][1])
        soir=' '+str(glycemies[2])+' '+str(infos[2].values()[0][0])+' '+ str(infos[2].values()[0][1])+' '

        
        
        fichier=open(chemin,'a')
        
        if moment==0:
               if ecrireOuPasMatin(chemin):
                       fichier.write(matin)
               else:
                       QtGui.QMessageBox.warning(None,"Attention","Rentre d'abord tes chiffres de la veille")
                       
        elif moment==1:
               if ecrireOuPasMidi(simuli.courant):
                       fichier.write(midi)
               else:
                       QtGui.QMessageBox.warning(None,"Attention","Rentre d'abord tes chiffres du matin")
        
        else:
                assert(moment==2)
                if ecrireOuPasSoir(simuli.courant):
                       fichier.write(soir)
                else:
                       QtGui.QMessageBox.warning(None,"Attention","Rentre d'abord tes chiffres d'avant")

        fichier.close() 




class fenetre3(QtGui.QDialog):

        closeApp = QtCore.pyqtSignal()

        def __init__(self,d="/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete8-9janv2014.txt",parent=None):
                super(fenetre3,self).__init__(parent)
                self.databaseChemin=d
                self.initUI()

        def initUI(self):
                self.setGeometry(300,300,441,226)
                self.CombienGlycemie=QtGui.QLabel("Rentrez la glycemie de la nuit",self)
                self.CombienGlycemie.move(30,30)
                self.CombienGlycemie.resize(211,21)
                # Zone de saisie
                self.saisieGlycemieNuit=QtGui.QLineEdit(self)
                self.saisieGlycemieNuit.move(20,70)
                self.saisieGlycemieNuit.resize(161,31)
                # Bouton
                self.bouton=QtGui.QPushButton('Enregistrer',self)
                self.bouton.move(240,130)
                self.bouton.resize(171,31)
                self.bouton.clicked.connect(self.enregistrerGN)



        def enregistrerGN(self):
                fichier=open(self.databaseChemin,'r')
                lignes=fichier.readlines()
                derniereLigne=lignes[len(lignes)-1].split()
                fichier.close()
                if(len(derniereLigne)!=9 and ecrireOuPas(self.databaseChemin,3)):
                        QtGui.QMessageBox.warning(self,"Attention","Rentre d'abord tes chiffres de la journee")
                        self.closeApp.emit()
                else:
                        QtGui.QMessageBox.information(self,"Info'","Enregistrement de la glycemie de la nuit")
                        glycemieNuit=self.saisieGlycemieNuit.text()
                        fichier=open(self.databaseChemin,'a')
                        fichier.write(unicode(glycemieNuit)+' '+str(0)+' '+str(0))
                        fichier.close()
                        self.closeApp.emit()


        
        def closeEvent(self,event):
                reply = QtGui.QMessageBox.question(self, 'Message',"Es-tu sur de ton choix ?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                        event.accept()
                else:
                        event.ignore()
                        
                        
                        
                
                        
                


class fenetre2(QtGui.QDialog):

        closeApp = QtCore.pyqtSignal()
        
        def __init__(self,simulateur,g,gn,d,mom,sp,rep,il,ir,parent=None,c='Oui'):
                super(fenetre2,self).__init__(parent)
                self.simuli=simulateur
                self.glycemieValue=g
                self.glycemieNuitValue=gn
                self.databaseInitialChemin=d
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
                self.setGeometry(0,0,650,239)
                self.simulationFaite=QtGui.QLabel('Simulation faite !',self)
                self.simulationFaite.move(10,30)
                self.info="Tu devrais t'injecter "+str(self.insulineLente)+" d'insuline lente et "+str(self.insulineRapide)+" d'insuline rapide"
                self.affichageSimulation=QtGui.QLabel(self.info,self)
                self.affichageSimulation.move(10,60)
                self.daccOuPas=QtGui.QLabel("Tu es d'accord ?",self)
                self.daccOuPas.move(10,130) 
                # Boutons "oui" et "non" (utilisateur d'accord ou pas avec la simulation
                self.daccord=QtGui.QPushButton('Oui',self)
                self.daccord.move(80,180)
                self.pasDaccord=QtGui.QPushButton('Non',self)
                self.pasDaccord.move(210,180)
                # Connexion des deux boutons 'Oui' et 'Non'
                self.daccord.clicked.connect(self.slot)
                self.pasDaccord.clicked.connect(self.slot)

        def slot(self):
                sender=self.sender()
                if sender.text()=='Oui':
                        
                        self.caseCochee='Oui'
                else:
                        assert sender.text()=='Non'
                        self.caseCochee='Non'

                        
                cC=self.caseCochee
                self.traitementDecision(cC)

        def traitementDecision(self,cC):

                for i in range(3):
                        self.simuli.courant.append({-1:[-1,-1]})
                
                               
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
                              msg="Merci de rentrer combien tu t'injecteras en insuline rapide !"
                              QtGui.QMessageBox.warning(self,'',msg)
                                                     
                               
                        tauxLente, ok = QtGui.QInputDialog.getDouble(self,'Ton choix', 'Combien t injecteras tu d insuline lente ?')
                        if ok:
                              d[self.glycemieValue].append(tauxLente)
                              self.closeApp.emit()
                        else: # Idem
                              msg="Merci de rentrer combien tu t'injecteras en insuline rapide !"
                              QtGui.QMessageBox.warning(self,'',msg)
                        
                        self.simuli.courant[self.moment]=d
                        #pas sure que ca marche:
                        QtGui.QMessageBox.information(self,"Info'","Ces donnees que tu viens de saisir sont rajoutees a la base de donnee :\n"+self.databaseChemin)
                print("self.moment=")
                print(self.moment)
                print("\n")
                miseAJourFichierTexte(self.simuli,self.databaseInitialChemin,self.moment)



                
 

        def closeEvent(self,event):
        		reply = QtGui.QMessageBox.question(self, 'Message',"Es-tu sur de ton choix ?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        		if reply == QtGui.QMessageBox.Yes:
            			event.accept()
        		else:
            			event.ignore()


class pageAccueil(QtGui.QMainWindow):
        def __init__(self,s=diabete.simulateur(),d="/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete8-9janv2014.txt",m=0,sp=False,rep=False):
        
                self.simuli=s
                self.databaseInitialChemin=d
                self.moment=m
                self.sport=sp
                self.repasRiche=rep
                super(pageAccueil,self).__init__()

                self.initUI()

#s=diabete.simulateur()
        def initUI(self):
                
                # Definition des widgets
                # Textes
                self.QuelRepas=QtGui.QLabel('Quel repas ?',self)
                self.QuelRepas.move(20,30)
                self.Sport=QtGui.QLabel('Sport ?',self)
                self.Sport.move(168,30)
                self.RepasRiche=QtGui.QLabel('Repas riche ?',self)
                self.RepasRiche.move(278,30)
                self.CombienGlycemie=QtGui.QLabel('Glycemie ?',self)
                self.CombienGlycemie.move(40,170)
                # Cases a cocher
                self.PtitDej=QtGui.QCheckBox('Ptit dej', self)
                self.PtitDej.move(18,60)
                self.Dejeuner=QtGui.QCheckBox('Dejeuner', self)
                self.Dejeuner.move(18,80)
                self.Diner=QtGui.QCheckBox('Diner', self)
                self.Diner.move(18,100)
                self.SportOui=QtGui.QCheckBox('Oui', self)
                self.SportOui.move(148,60)
                self.SportNon=QtGui.QCheckBox('Non', self)
                self.SportNon.move(148,80)
                self.RepasRicheOui=QtGui.QCheckBox('Oui', self)
                self.RepasRicheOui.move(268,60)
                self.RepasRicheNon=QtGui.QCheckBox('Non', self)
                self.RepasRicheNon.move(268,80)
                # Zone de saisie de texte
                self.ZoneEntreeGlycemie=QtGui.QLineEdit(self)
                self.ZoneEntreeGlycemie.move(60,220)
                # Bouton "simuler"
                self.BoutonSimuler=QtGui.QPushButton('Simuler',self)
                self.BoutonSimuler.move(450,210)
                # Bouton glycemie nuit
                self.BoutonGlycemieNuit=QtGui.QPushButton('Glycemie nuit',self)
                self.BoutonGlycemieNuit.move(400,40)
                self.BoutonGlycemieNuit.resize(201,41)
                
                
                
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
                # Connexion glycemie nuit
                self.BoutonGlycemieNuit.clicked.connect(self.saisieGlycemieNuit)
                # Geometrie et affichage de la fenetre principale 
                self.setGeometry(300,300,680,290)
                self.setWindowTitle('DiabeteFacile')
                self.show()
                
                menuApparence=self.menuBar().addMenu("&Apparence de la fenetre")
                # Modifier la couleur de fond
                actionCouleurFond=QtGui.QAction('&Couleur de fond',self)
                actionCouleurFond.setStatusTip("Modifier la couleur de fond de l'interface")
                actionCouleurFond.triggered.connect(self.changeCouleurFond)
                menuApparence.addAction(actionCouleurFond)
                # Modifier la couleur du bouton simuler
                actionCouleurBoutonSimuler=QtGui.QAction('&Couleur du bouton Simuler',self)
                actionCouleurBoutonSimuler.setStatusTip("Modifier la couleur du bouton Simuler")
                actionCouleurBoutonSimuler.triggered.connect(self.changeCouleurBouton)
                menuApparence.addAction(actionCouleurBoutonSimuler)
                # Modifier la police des zones de texte
                actionPolice=QtGui.QAction('&Police',self)
                actionPolice.setStatusTip("Modifier la police des zones de texte")
                actionPolice.triggered.connect(self.changePolice)
                menuApparence.addAction(actionPolice)
                # Modifier la police de la zone de saisie
                actionPoliceSaisie=QtGui.QAction('Police de la saisie',self)
                actionPoliceSaisie.setStatusTip("Modifier la police de la zone de saisie 'Glycemie'")
                actionPoliceSaisie.triggered.connect(self.changePoliceSaisie)
                menuApparence.addAction(actionPoliceSaisie)
                
                #se trouvent pas dans derniere version
                # Allocation memoire pour courant

                        
                        
        def changeCouleurFond(self):
                couleur=QtGui.QColorDialog.getColor(Qt.white,self)
                palette=QtGui.QPalette()
                palette.setColor(QtGui.QPalette.Background,couleur)
                self.setPalette(palette)

        def changeCouleurBouton(self):
                couleur=QtGui.QColorDialog.getColor(Qt.white,self)
                palette=QtGui.QPalette()
                palette.setColor(QtGui.QPalette.Button,couleur)
                self.BoutonSimuler.setPalette(palette)


        def changePolice(self):
                default=self.QuelRepas.font()
                police, ok=QtGui.QFontDialog.getFont(default,self,"Choisis une police")
                if ok:
                        self.QuelRepas.setFont(police)
                        self.Sport.setFont(police)
                        self.RepasRiche.setFont(police)
                        self.CombienGlycemie.setFont(police)


        def changePoliceSaisie(self):
                default=self.QuelRepas.font()
                police, ok=QtGui.QFontDialog.getFont(default,self,"Choisis une police")
                if ok:
                        self.ZoneEntreeGlycemie.setFont(police)
                              



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



        def simulerClicked(self):
                
                # Initialisation de simuli.courant
                glycemieValue=self.ZoneEntreeGlycemie.text()
                
                self.simuli.ajoutedata(self.databaseInitialChemin)
 
                
                # Calculs 
                insulineLenteSimulee=self.simuli.insulinelente(self.moment,self.sport,self.repasRiche)
                insulineRapideSimulee=self.simuli.insulinerapide(self.moment,self.sport,self.repasRiche)
                
                # Affichage d'une nouvelle fenetre avec le resultat de la simulation dessus
                affichageSimulation=fenetre2(self.simuli,float(unicode(glycemieValue)),0,self.databaseInitialChemin,self.moment,self.sport,self.repasRiche,insulineLenteSimulee,insulineRapideSimulee)
                affichageSimulation.exec_()
# float(unicode(glycemieNuitValue))

        def saisieGlycemieNuit(self):
                fenetreSaisieGlycemie=fenetre3(self.databaseInitialChemin)
                fenetreSaisieGlycemie.exec_()
 
def main():
        app=QtGui.QApplication(sys.argv)
        ex=pageAccueil()
        sys.exit(app.exec_())

if __name__=='__main__':
        main()
