import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn import metrics

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

df = pd.read_csv('color.csv')

x = np.array(df.drop(columns=['name', 'color']))
y = np.array(df['color'])

xTrain, xTest, yTrain, yTest = train_test_split(x, y, train_size=0.7)

def resultados(model, x, y, title):
    yp = model.predict(x)

    print(f"Metricas:\n{metrics.classification_report(y, yp)}")
    print(f"Matriz de confusion:\n{metrics.confusion_matrix(y, yp)}")


######## Decision Tree Classifier
print("\n*** Decision Tree Classifier ***")
model = Pipeline([('scaler', StandardScaler()), ('cla', DecisionTreeClassifier(max_depth=16))])
model.fit(xTrain, yTrain)
pickle.dump(model, open('DTC.sav', 'wb'))

print(f"Train score: {model.score(xTrain, yTrain)}")
print(f"Test score: {model.score(xTest, yTest)}")
resultados(model, x, y, "Decision Tree Classifier")


######## K Neighbors Classifier
print("\n*** K Neighbors Classifier ***")
model = Pipeline([('scaler', StandardScaler()), ('cla', KNeighborsClassifier(n_neighbors=4))])
model.fit(xTrain, yTrain)
pickle.dump(model, open('KNN.sav', 'wb'))

print(f"Train score: {model.score(xTrain, yTrain)}")
print(f"Test score: {model.score(xTest, yTest)}")
resultados(model, x, y, "K Neighbors Classifier")


######## SVM Classifier
print("\n*** SVM Classifier ***")
model = Pipeline([('scaler', StandardScaler()), ('cla', SVC(C=24, kernel='rbf'))])
model.fit(xTrain, yTrain)
pickle.dump(model, open('SVC.sav', 'wb'))

print(f"Train score: {model.score(xTrain, yTrain)}")
print(f"Test score: {model.score(xTest, yTest)}")
resultados(model, x, y, "SVM Classifier")

