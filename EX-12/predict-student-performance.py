# Install dependencies
# pip install pandas scikit-learn matplotlib seaborn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
url = 'student-mat.csv'
data = pd.read_csv(url, sep=';')
# Create binary target (pass/fail)
data['pass'] = (data['G3'] >= 10).astype(int)
# Select features
features = ['studytime', 'failures', 'absences']
X = data[features]
y = data['pass']
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
# Prediction
y_pred = model.predict(X_test)
# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
# Feature Importance Plot
importance = model.feature_importances_
sns.barplot(x=features, y=importance)
plt.title("Feature Importance")
plt.show()