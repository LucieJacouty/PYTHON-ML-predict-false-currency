import joblib
import os

import numpy as np
import pandas as pd

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from sklearn import preprocessing

root = Tk()
root.geometry("500x500")
root.title("Prédiction de billets")


def get_file():
    global df
    file = filedialog.askopenfilename(title="Select data", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    open_button.config(text=os.path.basename(file),fg="blue")
    if file is not NONE:
        df = pd.read_csv(file)


def check_data():
    global df
    #check if data has missing values
    if df.isnull().values.any() == False:
        pass
    else:
        messagebox.showwarning(title="Error",message="Attention! Il y a des données manquantes.")

    #check if data structure is correct
    correct_columns = ['diagonal','height_left','height_right','margin_low','margin_up','length']
    data_columns = df.columns[0:6].tolist()
    if (correct_columns == data_columns) is False:
        messagebox.showwarning(title="Error",message="Les données n'ont pas la bonne structure.")
    else:
        messagebox.showinfo(title="Result", message="Les données sont correctes.")
   

#import model
imported_model = joblib.load('/Users/Lucie/Jupyter/logreg_model.pkl')


#Prediction function
def billet_predict_logreg():
    global df
    X = df[['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length']]
    X_scaled = preprocessing.StandardScaler().fit_transform(X)
    y = imported_model.predict(X_scaled)
    df['classification'] = y
    predict_label.config(text=df[['id','classification']])


open_button = Button(root, text="Open", command=get_file)
open_button.pack(pady=10)

check_button = Button(root, text="Check data", command=check_data).pack(pady=10)

predict_button = Button(root, text="Predict", command=billet_predict_logreg).pack(pady=10)
predict_label = Label(root, text='')
predict_label.pack(pady=10)


root.mainloop()