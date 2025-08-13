import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



# load data set
data = pd.read_csv("experience_salary.csv")

X = data[["YearExperience"]]
y = data[["Salary"]]


model = LinearRegression()
model.fit(X, y)

data["PredictedSalary"] = model.predict(X)

print(f"Model Coefficient (slope) {round(float(model.coef_[0]), 2)}")
print(f"Model Intercept (base salary) {round(float(model.intercept_), 2)}")


plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, data["PredictedSalary"], color="red", label="Regression line")
plt.xlabel("Year of experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

