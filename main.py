from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([
    [25, 6.0, 1],
    [30, 7.5, 3],
    [22, 5.5, 0],
    [28, 6.5, 2],
    [35, 8.0, 5],
    [40, 7.0, 4]
])
y = np.array([0, 1, 0, 1, 1, 1])

model = LinearRegression()
model.fit(X, y)

age = int(input('Enter your age: '))
IELTS = float(input('Enter your IELTS score: '))
experience = int(input('How many years of experience do you have?: '))

new_condidate = np.array([[age, float(IELTS), experience]])
prediction = model.predict(new_condidate)

def accepted_or_no(prediction):
  if round(prediction[0]) == 1:
    return 'You have been hired..'
  else:
    return 'You were not hired.'

print(accepted_or_no(prediction))
