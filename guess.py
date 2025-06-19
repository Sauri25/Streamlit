import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("Salary_dataset.csv")
df.drop(columns="Unnamed: 0", inplace=True)
# print(df.info())
X = df.drop(columns="Salary")
y = df["Salary"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=43
)
model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print(r2)

# Save model to file
joblib.dump(model, "salary_model.pkl")
print("Model saved as salary_model.pkl")
