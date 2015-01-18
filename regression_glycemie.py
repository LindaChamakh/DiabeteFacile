import numpy as np
from sklearn import linear_model

#exemple simple de regression: resolution x*b=y
b = np.array([3,5,7]).transpose()
x = np.array([[1,6,9],   ## 1*3 + 6*5 + 7*9 = 96
              [2,7,7],   ## 2*3 + 7*5 + 7*7 = 90
              [3,4,5]])
y = np.array([96,90,64]).transpose()
clf = linear_model.LinearRegression(fit_intercept=False)
clf.fit([[1,6,9],
         [2,7,7],
         [3,4,5]], [96,90,64])
#print clf.coef_ 


# on a un echantillon de vecteur X de dimension 3 (glycemie avant, inj rapide, inj lente), un echantillon de vecteur Y de dimension 1 (glycemie apres le repas)
# on cherche le coefficient b de dimension 3 tel que X scalaire b (plus un bruit) donne Y
#diabetes=datasets.load_diabetes()

#donnes sur lesquelles on fait la regression lineaire
diabetedata_Xmatin = np.genfromtxt("/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabetedata_Xmatin.txt", delimiter=',')
diabetedata_Ymatin = np.genfromtxt("/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabetedata_Ymatin.txt")

#donnes pour tester la qualite de la regression lineaire
diabetetest_Xmatin = np.genfromtxt("/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabetetest_Xmatin.txt", delimiter=',')
diabetetest_Ymatin = np.genfromtxt("/Users/lindachamakh/Documents/testgit/DiabeteFacile/diabetetest_Ymatin.txt")


reg_diabete=linear_model.LinearRegression(fit_intercept=True, normalize=False)
reg_diabete.fit(diabetedata_Xmatin, diabetedata_Ymatin)

print(reg_diabete.coef_)

#coef de regression nul avec l'insuline lente: pas de relation lineaire avec l'insuline lente

print(reg_diabete.score(diabetetest_Xmatin,diabetetest_Ymatin))
