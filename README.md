# Création d'un algorithme de détection de faux billets 

Projet Openclassrooms - Formation Data Analyst  

Objectif : pour lutter contre le faux-monnayage, créer un modèle capable d'identifier, à partir de plusieurs données numériques de dimension d'un billet, les faux et les vrais billets

Contenu :
- Data : données utilisées (2 datasets, le 2nd pour tester l'algorithme final)
- Code : notebook jupyter regroupant toutes les étapes de la création du modèle prédictif  
- Script App : script d'application permettant d'appliquer le modèle (réalisé avec Tkinter)    


## Code

Utilisation des librairies : Numpy, Pandas, Matplotlib, Seaborn, Statsmodel, Scikit-learn et Imbalanced-learn  

### Préparation des données et analyse descriptive : 

Import d'un dataset comprenant des vrais et faux billets labellisés  

Vérification des données (total, uniques, doublons)   
Vérification du nombre de vrais et faux billets dans le dataset  
Vérification de la distribution de chaque variable numérique  
Vérification des corrélations 2 à 2 avec corr()  

### Régression linéaire pour remplacer les valeurs nulles 

Réalisé avec scikit-learn et statsmodel  

Valeurs nulles dans "margin_low"

Séparation des données train/test :
- Train : toutes les données sans valeurs nulles 
- Test : toutes les données où il y a des valeurs nulles  

Entrainement d'un modèle de régression linéaire multiple sur le train set  
Prédiction sur le test set
-> Score R2 relativement bas  

Réalisation de cross validation et test de différents modèles de régression linéaire (ridge, lasso, elasticnet)  
-> Pas meilleurs que la régression linéaire classique

Remplacer les valeurs nulles par les données prédites  

### ACP et K-means  

Réalisés afin de comprendre les liens entre les variables et les individus  

ACP, étudier les liens entre les variables : on détermine 2 composantes, soit 1 plan factoriel  
Réalisation du cercle de corrélation  

K-means, étudier les liens entre les individus : choix de 3 clusters  
Clustering identifie bien les vrais et faux billets  

### Régression logistique  

Séparation des données en train/test avec train_test_split  
Normalisation des données  

Entrainement de la régression logistique sur le train set  
Prédictions sur le test set   
Vérifications de la qualité du modèle : 
- Matrice de confusion 
- Courbe ROC 
- Learning Curve 

Vérification de la possibilité d'une meilleure prédiction avec l'oversampling (-> Non)  

### Prédictions avec centroïdes k-means  

Normalisation des données  
Séparation des données en train/test avec train_test_split  

Nouveau k-means réalisé sur le train set   
Utilisation des centroïdes pour prédire sur le test set   
-> Un peu moins bon que la régression logistique  

### Algorithme de prédiction

Création de la fonction de prédiction  


## Script App

Création d'une application avec Tkinter 

Permets : 
- D'ouvrir un fichier/dataset 
- De vérifier que la forme du fichier/dataset corresponde bien au modèle entraîné (forme, pas de valeurs nulles)  
- D'afficher l'identification vrai/faux pour chaque billet
