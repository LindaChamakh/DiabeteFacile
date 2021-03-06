import sys
from PyQt4 import QtGui, QtCore
import diabetedate
import datetime


def ecrireOuPasMatin(chemin):
	f=open("/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete89new.txt",'r')
	lignes=f.readlines()
	
	sautLigne=lignes[len(lignes)-1]
	derniereLigne=lignes[len(lignes)-2]
	f.close()
	assert(sautLigne=='\n')
	mots=derniereLigne.split()
	print('\n mots:')
	print(mots[0])
	try:
		if mots[0]!='nuit':
		    return False
		aujourdhui=datetime.date.today()
		derniereInfo=mots[len(mots)-1]
		print("mots[3]=")
		print(mots[3])
		jour, mois, annee = derniereInfo.split('-')
		derniereDate=datetime.date(int(annee),int(mois),int(jour))
		unJour = datetime.timedelta(days=1)
		print(unJour)
		if aujourdhui!=derniereDate+unJour:
		    print('ok')
		    return False
		return True
	except:
		return False


def ecrireOuPasMidi(chemin):
	f=open("/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete89new.txt",'r')
	lignes=f.readlines()
	derniereLigne=lignes[len(lignes)-1]
	f.close()
	mots=derniereLigne.split()
	try:
		if mots[0]!='matin':
			return False
		aujourdhui=datetime.date.today()
		derniereInfo=mots[len(mots)-1]
		print("mots[3]=")
		print(mots[3])
		jour, mois, annee = derniereInfo.split('-')
		derniereDate=datetime.date(int(annee),int(mois),int(jour))
		if aujourdhui!=derniereDate:
			return False
		return True
	except:
		return False
	
	

def ecrireOuPasSoir(chemin):
	f=open("/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete89new.txt",'r')
	lignes=f.readlines()
	derniereLigne=lignes[len(lignes)-1]
	f.close()
	mots=derniereLigne.split()
	try:
		if mots[0]!='midi':
			return False
		aujourdhui=datetime.date.today()
		derniereInfo=mots[len(mots)-1]
		jour, mois, annee = derniereInfo.split('-')
		derniereDate=datetime.date(int(annee),int(mois),int(jour))
		if aujourdhui!=derniereDate:
			return False	
		return True   
	except:
		return False
	
def ecrireOuPasNuit(chemin):
	f=open("/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete89new.txt",'r')
	lignes=f.readlines()
	derniereLigne=lignes[len(lignes)-1]
	f.close()
	mots=derniereLigne.split()
	try:
		if mots[0]!='soir':
			return False
		aujourdhui=datetime.date.today()
		derniereInfo=mots[len(mots)-1]
		jour, mois, annee = derniereInfo.split('-')
		derniereDate=datetime.date(int(annee),int(mois),int(jour))
		if aujourdhui!=derniereDate:
			return False
		return True             
	except :
	    return False
        
        
        
        



def miseAJourFichierTexte(simuli,chemin,moment):
        r=0
        infos=simuli.courant
        glycemies=[]

        #mise a jour de glycemies et infos

        for i in range(3):
                l=list(infos[i].keys())
                glycemies.append(l[0])
             

        aujourdhui=datetime.datetime.now()
        jour=aujourdhui.day
        mois=aujourdhui.month
        annee=aujourdhui.year
        date=" "+str(jour)+'-'+str(mois)+'-'+str(annee)
        fichier=open(chemin,'a')
        
        if moment==0:
               if ecrireOuPasMatin(chemin):
               	matin="matin "+str(glycemies[0])+' '+str(infos[0].values()[0][0])+' '+str(infos[0].values()[0][1])+date+'\n'
               	fichier.write(matin)
               else:
                       QtGui.QMessageBox.warning(None,"Attention","Rentre d'abord tes chiffres de la veille")
                       
        elif moment==1:
               if ecrireOuPasMidi(simuli.courant):
               	midi="midi "+str(glycemies[1])+' '+str(infos[1].values()[0][0])+' '+ str(0)+date+'\n'
               	fichier.write(midi)
               else:
                QtGui.QMessageBox.warning(None,"Attention","Rentre d'abord tes chiffres du matin")
        
        else:
                assert(moment==2)
                if ecrireOuPasSoir(simuli.courant):
                	soir='soir '+str(glycemies[2])+' '+str(infos[2].values()[0][0])+' '+ str(infos[2].values()[0][1])+date+'\n'
                	fichier.write(soir)
                else:
                    QtGui.QMessageBox.warning(None,"Attention","Rentre d'abord tes chiffres d'avant")

        fichier.close() 




class fenetre3(QtGui.QDialog):
        def __init__(self,d="/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete89New.txt",parent=None):
                super(fenetre3,self).__init__(parent)
                self.databaseChemin=d
                self.initUI()

        def initUI(self):
                self.setGeometry(300,300,441,226)
                self.setStyleSheet("background:white")
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
                if ecrireOuPasNuit(self.databaseChemin)== True:
                        aujourdhui=datetime.datetime.now()
                        jour=aujourdhui.day
                        mois=aujourdhui.month
                        annee=aujourdhui.year
                        date=" "+str(jour)+'-'+str(mois)+'-'+str(annee)
                        glycemieNuit=self.saisieGlycemieNuit.text()
                        fichier=open(self.databaseChemin,'a')
                        fichier.write('nuit '+unicode(glycemieNuit)+' 0'+' 0'+date+'\n'+'\n')
                        fichier.close()
                        self.close()
                        print('lol')
                else:
                        QtGui.QMessageBox.warning(self,"Attention","Rentre d'abord tes chiffres de la journee")
        def slot(self):
        		self.closeApp2.emit()
        
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
                self.setGeometry(0,0,450,239)
                self.setStyleSheet("background:white")
                self.setWindowTitle('Simulation')
                self.simulationFaite=QtGui.QLabel('Simulation faite !',self)
                self.simulationFaite.move(10,30)
                self.info="Tu devrais t'injecter "+str(self.insulineLente)+" unites d'insuline lente"+'\n'+ "et "+str(self.insulineRapide)+" unites d'insuline rapide"
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
        def __init__(self,s=diabetedate.simulateur(),d="/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete89New.txt",m=0,sp=False,rep=False):
        
                self.simuli=s
                self.databaseInitialChemin=d
                self.moment=m
                self.sport=sp
                self.repasRiche=rep
                super(pageAccueil,self).__init__()

                self.initUI()

        def initUI(self):
                
                # Definition des widgets
                # Textes
                self.QuelRepas=QtGui.QLabel('Quel repas ?',self)
                self.QuelRepas.move(40,30)
                self.Sport=QtGui.QLabel('Sport ?',self)
                self.Sport.move(188,30)
                self.RepasRiche=QtGui.QLabel('Repas riche ?',self)
                self.RepasRiche.move(298,30)
                self.CombienGlycemie=QtGui.QLabel('Glycemie ?',self)
                self.CombienGlycemie.move(40,170)
                # Cases a cocher
                self.PtitDej=QtGui.QCheckBox('Ptit dej', self)
                self.PtitDej.move(40,60)
                self.Dejeuner=QtGui.QCheckBox('Dejeuner', self)
                self.Dejeuner.move(40,80)
                self.Diner=QtGui.QCheckBox('Diner', self)
                self.Diner.move(40,100)
                self.SportOui=QtGui.QCheckBox('Oui', self)
                self.SportOui.move(188,60)
                self.SportNon=QtGui.QCheckBox('Non', self)
                self.SportNon.move(188,80)
                self.RepasRicheOui=QtGui.QCheckBox('Oui', self)
                self.RepasRicheOui.move(298,60)
                self.RepasRicheNon=QtGui.QCheckBox('Non', self)
                self.RepasRicheNon.move(298,80)
                # Zone de saisie de texte
                self.ZoneEntreeGlycemie=QtGui.QLineEdit(self)
                self.ZoneEntreeGlycemie.move(160,170)
                
                # Bouton "simuler"
                self.BoutonSimuler=QtGui.QPushButton('S I M U L E R',self)
                self.BoutonSimuler.move(50,240)
                self.BoutonSimuler.resize(431,50)
                self.BoutonSimuler.setStyleSheet('QPushButton {background-color: red}')
                # Bouton glycemie nuit
                self.BoutonGlycemieNuit=QtGui.QPushButton('Glycemie nuit',self)
                self.BoutonGlycemieNuit.move(300,170)
                self.BoutonGlycemieNuit.resize(181,41)
                self.BoutonGlycemieNuit.setStyleSheet('QPushButton {background-color: blue}')
               
                
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
                self.setGeometry(300,250,550,350)
                self.color = QtGui.QColor(25, 80, 0)
                self.setStyleSheet("background:white")
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
                

        def changeCouleurFond(self):
        		couleur = QtGui.QColorDialog.getColor()
        		if couleur.isValid():
        			self.setStyleSheet("QWidget { background-color: %s }"% couleur.name())
        
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
                
                
                	
 
                
                # Calculs 
                try:
                    glycemieValue=self.ZoneEntreeGlycemie.text()
	                    
                    if self.moment==0:
                	   self.simuli.ajoutedata(self.databaseInitialChemin)
                	   
                	
                    insulineLenteSimulee=self.simuli.insulinelente(self.moment,self.sport,self.repasRiche)
                    insulineRapideSimulee=self.simuli.insulinerapide(self.moment,self.sport,self.repasRiche)
                 # Affichage d'une nouvelle fenetre avec le resultat de la simulation dessus
                    affichageSimulation=fenetre2(self.simuli,float(unicode(glycemieValue)),0,self.databaseInitialChemin,self.moment,self.sport,self.repasRiche,insulineLenteSimulee,insulineRapideSimulee)
                    affichageSimulation.exec_()
                except ValueError:
	                QtGui.QMessageBox.warning(self,'',"Merci d'entrer ta glycemie")  
               


                                                     
        		    
        def saisieGlycemieNuit(self):
                fenetreSaisieGlycemie=fenetre3(self.databaseInitialChemin)
                fenetreSaisieGlycemie.exec_()
 
def main():
        app=QtGui.QApplication(sys.argv)
        ex=pageAccueil()
        sys.exit(app.exec_())

if __name__=='__main__':
        main()
