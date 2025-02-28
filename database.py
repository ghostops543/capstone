import joblib
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import seaborn as sns
import warnings

from sklearn.preprocessing import OrdinalEncoder

warnings.filterwarnings("ignore")
#
#   run this program to initalize the model into a file
#
#
df = pd.read_csv("data set/Autism_Data.arff")

df.replace("?",np.mean,inplace=True)

df.drop("ethnicity", axis=1, inplace = True)
df.drop("relation", axis=1, inplace= True)
df.drop("age", axis=1, inplace=True)
df.drop("age_desc", axis=1, inplace= True)
df.drop("contry_of_res", axis=1, inplace= True)
df.drop("gender", axis= 1, inplace= True)
df.drop("autism", axis = 1, inplace = True)
df.drop("jaundice", axis = 1, inplace = True)
df.drop("used_app_before", axis=1, inplace = True)


autism = ['NO', 'YES']
enc = OrdinalEncoder(categories = [autism])
df['Class/ASD'] = enc.fit_transform(df[['Class/ASD']])

X = df.drop(columns="Class/ASD")
y = df["Class/ASD"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.8, random_state= 11)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
def get_score():
    model_score = model.score(X_test, y_test)
    print(model_score)
def get_matrix():
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)
def get_report():
    clas_report = classification_report(y_test, y_pred)
    print(clas_report)
def predict(data):
    prediction = model.predict(data)
    #print(prediction)
    if np.any(prediction == [1.]):
        return "The machine learning algorithm detects\n that you are likely to have ASD"
    elif np.any(prediction == [0.]):
        return "The machine learning algorithm detects\n that you are not likely to have ASD"
def plots():
    fig , axis = plt.subplots(1,3, figsize=(18,5))
    sns.countplot(x=df['Class/ASD'], data=df, ax=axis[0])
    axis[0].set_title('ASD vs Non ASD')

    sns.scatterplot(data = df, x = df['result'], y = df["Class/ASD"] , ax=axis[1])
    axis[1].set_title('total test score Vs ASD')

    sns.kdeplot(data= df, x = df['result'], ax= axis[2])
    axis[2].set_title('KDE plot')
    plt.tight_layout
    plt.show()








