import sys
from PyQt4 import QtGui, QtCore
import diabete


def info(il,ir):
        re

class fenetre2(QtGui.QDialog):
        def __init__(self,parent=None,il,ir,c='Oui'):
                super(fenetre2,self).__init__(parent)
                self.insulineLente=il
                self.insulineRapide=ir
                self.caseCochee=c
                self.initUI()


        def initUI(self):
            # Geometrie de la fenetre
                self.setgeometry(0,0,339,474)
                simulationFaite=QtGui.QLabel('Simulation faite !',self)
                simulationFaite.move(10,30)
                info='Tu devrais t injecter '+str(insulineLente)+' d insuline lente et '+str(insulineRapide)+' d insuline rapide'
                affichageSimulation=QtGui.QLabel(info,self)
                affichageSimulation.move(10,60)
                daccOuPas=QtGui.QLabel('Tu es d accord ?',self)
                daccOuPas.move(10,130) 
	    # Boutons "oui" et "non" (utilisateur d'accord ou pas avec la simulation
                daccord=QtGui.QPushButton('Oui',self)
                BoutonSimuler.move(80,180)
                pasDaccord=QtGui.QPushButton('Non',self)
                pasDaccord.move(210,180)
           # Affichage
                self.show()
           # Connexion des deux boutons 'Oui' et 'Non'
                daccord.clicked.connect(self.slot)
                pasDaccord.clicked.connect(self.slot)
                
        def slot(self):
                sender=self.sender()
                if sender.text()=='Oui':
                        caseCochee='Oui'
                else:
                        assert sender.text()=='Non'
                        caseCochee='Non'

                        
        def getCaseCochee(self):
                return caseCochee
                






                
class pageAccueil(QtGui.QMainWindow):
	def __init__(self,s=diabete.simulateur(),d="/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabete8-9janv2014.txt",m=0,sp=False,rep=False):
		super(pageAccueil,self).__init__()
		self.simuli=s
		self.databaseInitialChemin=d
		self.moment=m
		self.sport=sp
		self.repasRiche=rep
		self.initUI()
		
		
	def initUI(self):
	
	# Definition des widgets
            # Textes
		QuelRepas=QtGui.QLabel('Quel repas ?',self)
		QuelRepas.move(2,30)
		Sport=QtGui.QLabel('Sport ?',self)
		Sport.move(140,30)
		RepasRiche=QtGui.QLabel('Repas riche ?',self)
		RepasRiche.move(250,30)
		CombienGlycemie=QtGui.QLabel('Combien glycemie ?',self)
		CombienGlycemie.move(10,140)
            # Cases à cocher
		PtitDej=QtGui.QCheckBox('Ptit dej', self)
		PtitDej.move(0,60)
		Dejeuner=QtGui.QCheckBox('Dejeuner', self)
		Dejeuner.move(0,80)
		Diner=QtGui.QCheckBox('Diner', self)
		Diner.move(0,100)
		SportOui=QtGui.QCheckBox('Oui', self)
		SportOui.move(130,60)
		SportNon=QtGui.QCheckBox('Non', self)
		SportNon.move(130,80)
		RepasRicheOui=QtGui.QCheckBox('Oui', self)
		RepasRicheOui.move(250,60)
		RepasRicheNon=QtGui.QCheckBox('Non', self)
		RepasRicheNon.move(250,80)
            # Zone de saisie de texte
		ZoneEntreeGlycemie=QtGui.QLineEdit(self)
		ZoneEntreeGlycemie.move(20,190)
	    # Bouton "simuler"
                BoutonSimuler=QtGui.QPushButton('Simuler',self)
                BoutonSimuler.move(330,190)
            # Geometrie et affichage de la fenetre principale 
		self.setGeometry(300,300,534,339)
		self.setWindowTitle('DiabeteFacile')
		self.show()
	# Connexion des widgets		
	    # Connexion des checkbox
                PtitDej.stateChanged.connect(self.choixRepas)
                Dejeuner.stateChanged.connect(self.choixRepas)
                Diner.stateChanged.connect(self.choixRepas)
                SportOui.stateChanged.connect(self.choixSport)
                SportOui.stateChanged.connect(self.choixSport)
                RepasRicheOui.stateChanged.connect(self.choixRepasRiche)
                RepasRicheNon.stateChanged.connect(self.choixRepasRiche)
            # Connexion du bouton 'Simuler'
                BoutonSimuler.clicked.connect(self.simulerClicked)
            # Allocation mémoire pour courant
                for i in range(3):
                        self.simuli.courant.append([])
                

                
        # Mise a jour de l'attribut moment selon la case cochée
        def choixRepas(self):
                sender=self.sender()
                if sender.text()=='Ptit dej':
                        self.moment=0
                elif sender.text()=='Dejeuner':
                        self.moment=1
                else:
                        assert(sender.text()=='Diner'
                        self.moment=2


        # Mise a jour de l'attribut sport selon la case cochée
        def choixSport(self):
               sender=self.sender()
                if sender.text()=='Oui':
                        self.sport=True
                else:
                        assert(sender.text()=='Non')
                        self.sport=False

        # Mise a jour de l'attribut  selon la case cochée
        def choixRepasRiche(self):
               sender=self.sender()
                if sender.text()=='Oui':
                        self.repasRiche=True
                else:
                        assert(sender.text()=='Non')
                        self.repasRiche=False

        # La methode simulerClicked() enregistre le taux de glycemie saisi par l'utilisateur
        def simulerClicked(self):
                simuli.ajoutedata(databaseInitialChemin)
                # Initialisation de simuli.courant
                glycemieValue=ZoneEntreeGlycemie.text()
                d=dict([])
                dbis=dict([])
                dbis[glycemieValue]=[]
                d[moment]=dbis
                self.simuli.courant[moment]=d
                # Calculs 
                insulineLenteSimulee=self.simuli.insulinelente(self.moment,
                                                               self.sport,
                                                               self.repasRiche)
                insulineRapideSimulee=self.simuli.insulinerapide(self.moment,
                                                                 self.sport,
                                                                 self.repasRiche)
                # Affichage d'une nouvelle fenetre avec le resultat de la simulation dessus
                affichageSimulation=fenetre2(insulineLenteSimulee,insulineRapideSimulee)
                affichageSimulation.exec_()
                               
                # decision est soit 'Oui' soit 'Non' pour savoir si l'utilisateur a accepte la simulation ou pas 
                decision=affichageSimulation.getCaseCochee()
                               
                if decision=='Oui':
                        dbis[glycemieValue].append(insulineRapideSimulee)
                        dbis[glycemieValue].append(insulineLenteSimulee)
                        d[moment]=dbis
                        self.simuli.courant[moment]=d                       

                else: # Normalement il devrait pas y avoir d'erreur ici mais on sait jamais 
                        assert(decision=='Non')
                               
                        tauxRapide, ok = QtGui.QInputDialog.getDouble(self,'Ton choix', 'Combien t injecteras tu d insuline rapide ?')
                        if ok:
                               dbis[glycemieValue].append(tauxRapide)
                        else:
                               reponse=QtGui.QMessageBox.question(self,'Un probleme est arrive',
                                                          'Je vais devoir quitter, dsl ! Merci de me laisser partir en cliquant sur ok ;)',
                                                          QtGui.QMessageBox.Yes)
                                                     
                               assert(reponse==QtGui.QMessageBox.Yes)
                               QtCore.QCoreApplication.instance().quit()
                               
                        tauxLente, ok = QtGui.QInputDialog.getDouble(self,'Ton choix', 'Combien t injecteras tu d insuline lente ?')
                        if ok:
                              dbis[glycemieValue].append(tauxLente)
                        else: # Idem
                               reponse=QtGui.QMessageBox.question(self,'Un probleme est arrive',
                                                                  'Je vais devoir quitter, dsl ! Merci de me laisser partir en cliquant sur ok ;)',
                                                                  QtGui.QMessageBox.Yes)
                                                             
                               assert(reponse==QtGui.QMessageBox.Yes)
                               QtCore.QCoreApplication.instance().quit()
                        d[moment]=dbis
                        self.simuli.courant[moment]=d
                               

                
                
                
                        
                
                

                
                
                               
        
		
def main():
	app=QtGui.QApplication(sys.argv)
	ex=Application()
	sys.exit(app.exec_())
	
if __name__=='__main__':
	main()
