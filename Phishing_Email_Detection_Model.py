
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample dataset (replace with a larger dataset if available)
data = {
    "email_text": [
        "Congratulations! You have won a free vacation. Click here to claim your prize.",
        "Your account has been compromised. Please verify your login details immediately.",
        "Meeting scheduled at 10 AM tomorrow.",
        "Invoice for your recent purchase attached.",
        "Update your password to avoid account suspension.",
        "Lunch with the team at 1 PM today.",
        "Urgent: Your bank account will be closed unless you confirm your identity."
    ],
    "label": ["Phishing", "Phishing", "Safe", "Safe", "Phishing", "Safe", "Phishing"]
}

df = pd.DataFrame(data)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(df["email_text"], df["label"], test_size=0.3, random_state=42)

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predict
y_pred = model.predict(X_test_vec)

# Evaluate model
print("\nPhishing Email Detection Results:")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Test with new email input
new_email = input("\nEnter an email text to classify: ")
new_email_vec = vectorizer.transform([new_email])
prediction = model.predict(new_email_vec)
print(f"\nThis email is classified as: {prediction[0]}")
