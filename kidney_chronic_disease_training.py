# -*- coding: utf-8 -*-
"""kidney-chronic-disease-training

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lnkvlmNbztQfBL_A3NbBZjpescHhrzAd
"""

import keras   #Imports

from keras.models import Sequential
model = Sequential()   #Model Creation

from keras.layers import Dense

import pandas as pd

dt = pd.read_csv('/content/kidney_disease.csv')   #Data Loading
dt.head()

dt = dt.dropna()

for i in dt.columns:
  if dt[i].dtype == 'object':
    dt[i] = dt[i].astype('category').cat.codes

dt.corr()

dt = dt.drop(['su','ba','wc','rc','cad'],axis=1)

dt.tail(1)

"""row-col"""

x = dt.iloc[:,0:-1]   #Feature Selection
y = dt['classification']

x

from sklearn.model_selection import train_test_split   #Data Split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

print(x.shape,y.shape,x_train.shape,x_test.shape,y_train.shape,y_test.shape)

model.add(Dense(units=20,activation='relu', input_shape=(x_train.shape[1],)))  #Model Architecture

model.add(Dense(units=10,activation='relu'))

model.add(Dense(units=1,activation='sigmoid'))

model.build(input_shape=(None,20))

model.summary()

"""Model Compilation and Training"""

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=50,batch_size=10,steps_per_epoch=x_train.shape[0]//10)

y_pred = model.predict(x_test)

y_pred = (y_pred > 0.5).astype(int)

from sklearn.metrics import accuracy_score  #Evaluation
accuracy_score(y_test,y_pred)

model.save('kidney.h5')

x_train

x_train.columns

