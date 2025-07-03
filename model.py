from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import joblib

df = pd.read_csv("weather.csv")
df_model = df

# Drop date column for modeling
df_model = df.drop(columns=["date"])

# Encode target labels
le = LabelEncoder()
df_model["weather_encoded"] = le.fit_transform(df_model["weather"])

# Features and target
X = df_model.drop(columns=["weather", "weather_encoded"])
y = df_model["weather_encoded"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=le.classes_)

# Save the model and label encoder
joblib.dump(clf, "weather_model.pkl")
joblib.dump(le, "label_encoder.pkl")

print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(report)
