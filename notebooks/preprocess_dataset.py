import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Load original dataset
sms = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

print("Original dataset:", sms.shape)

# 2. Remove missing values
sms = sms.dropna(subset=["label", "message"]).copy()

# 3. Standardize labels
sms["label"] = sms["label"].str.strip().str.lower()

# 4. Clean SMS text
def clean_text(text):
    text = text.lower()
    text = text.strip()
    text = " ".join(text.split())
    return text

sms["message"] = sms["message"].apply(clean_text)

# 5. Remove empty messages
sms = sms[sms["message"] != ""].copy()

# 6. Validate labels
print("\nUnique labels:", sms["label"].unique())

# 7. Check messages with conflicting labels
conflicts = sms.groupby("message")["label"].nunique()
conflicts = conflicts[conflicts > 1]

print("\nMessages with conflicting labels:", len(conflicts))

# 8. Remove exact duplicate rows
print("\nDuplicates before removal:", sms.duplicated().sum())

sms = sms.drop_duplicates().reset_index(drop=True)

print("Duplicates after removal:", sms.duplicated().sum())

# 9. Final dataset summary
print("\nFinal Dataset Shape:", sms.shape)

print("\nFinal Label Distribution:")
print(sms["label"].value_counts())

print("\nFinal Label Percentages:")
print(sms["label"].value_counts(normalize=True) * 100)

# 10. Save cleaned dataset
sms.to_csv("data/sms_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")