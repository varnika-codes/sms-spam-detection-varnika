import pandas as pd
from sklearn.model_selection import train_test_split

# Load cleaned dataset
sms = pd.read_csv("data/sms_cleaned.csv")

# Separate features and labels
X = sms["message"]
y = sms["label"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Display results
print("Total records:", len(sms))
print("Training records:", len(X_train))
print("Testing records:", len(X_test))

print("\nTraining distribution:")
print(y_train.value_counts())

print("\nTesting distribution:")
print(y_test.value_counts())

# Save training dataset
train_data = pd.DataFrame({
    "label": y_train,
    "message": X_train
})

train_data.to_csv("data/train.csv", index=False)

# Save testing dataset
test_data = pd.DataFrame({
    "label": y_test,
    "message": X_test
})

test_data.to_csv("data/test.csv", index=False)

print("\nTrain and test datasets saved successfully!")