# 🚗 Projet Automobile Maroc — Machine Learning

## 👩‍💻 Réalisé par

- **Zineb Zarda**
- **Rajae Boutahri**

## 📌 Description du projet

Ce projet consiste à réaliser une étude complète du marché des voitures d'occasion au Maroc à partir de données collectées depuis le site **Moteur.ma**.

Le projet couvre différentes étapes de Data Science et de Machine Learning :

- Web Scraping des annonces automobiles
- Constitution du dataset
- Nettoyage et préparation des données
- Analyse exploratoire des données (EDA)
- Visualisation des données
- Encodage des variables catégorielles
- Prétraitement des données
- Entraînement de modèles de Machine Learning
- Comparaison des modèles
- Validation des performances
- Optimisation des hyperparamètres
- Segmentation des véhicules avec K-Means
- Analyse et interprétation des résultats

## 🛠️ Technologies utilisées

- Python
- Pandas
- NumPy
- BeautifulSoup
- Requests
- Matplotlib
- Scikit-learn
- XGBoost
- Jupyter Notebook

## 📊 Machine Learning

Plusieurs modèles de régression ont été étudiés :

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

Les performances ont été évaluées à l'aide de :

- MAE
- RMSE
- R²

Une étape d'optimisation des hyperparamètres avec `GridSearchCV` a également été réalisée.

## 🔎 Clustering

La méthode K-Means a été utilisée afin de segmenter les véhicules en différents groupes selon notamment :

- Prix
- Année
- Kilométrage

La méthode du coude (Elbow Method) a été utilisée pour déterminer un nombre approprié de clusters.

## 📁 Structure du projet

```text
Projet_Automobile_Maroc/
│
├── scraping/
│   └── scraping.py
│
├── data/
│   └── cars.csv
│
├── notebooks/
│   └── analyse_modelisation.ipynb
│
└── README.md