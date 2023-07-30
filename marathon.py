import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('./data/marathon.csv')

X = data[['Distance', 'Avg_Pace']]
y = data['Time']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

distance = float(input("Distance of marathon (km): "))
pace = float(input("Run speed (minutes/km): "))

time = model.predict([[distance, pace]])

print("Prediction of time: {:.2f} hours".format(time[0]))