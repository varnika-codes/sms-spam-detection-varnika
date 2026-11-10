# import pandas as pd

# # Load dataset
# sms = pd.read_csv(
#     "data/SMSSpamCollection",
#     sep="\t",
#     header=None,
#     names=["label", "message"]
# )

# # Display first 5 records
# print(sms.head())


import pandas as pd

# Step 3: Load dataset
sms = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Display first 5 records
# print("--- First 5 Records ---")
# print(sms.head())

# # Step 4: Inspect and understand the dataset
# print("\n--- A. Total SMS ---")
# print("Total SMS:", len(sms))

# print("\n--- B. Dataset Shape (Rows, Columns) ---")
# print(sms.shape)

# print("\n--- C. Dataset Info ---")
# print(sms.info())

# print("\n--- D. First 10 Records ---")
# print(sms.head(10))

# print("\n--- D. Last 10 Records ---")
# print(sms.tail(10))

# print("\n--- E. Unique Labels ---")
# print(sms["label"].unique())

# print("\n--- F. Class Counts ---")
# print(sms["label"].value_counts())

# print("\n--- G. Class Percentages ---")
# print(sms["label"].value_counts(normalize=True) * 100)

# print(sms.isnull().sum())

# print("Duplicate records:", sms.duplicated().sum())

# duplicates = sms[sms.duplicated(keep=False)]

# print(duplicates.head(10))

# sms = sms.drop_duplicates().reset_index(drop=True)

# print("Dataset shape after removing duplicates:", sms.shape)

def clean_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove leading and trailing spaces
    text = text.strip()

    # Remove extra spaces
    text = " ".join(text.split())

    return text


sms["message"] = sms["message"].apply(clean_text)

print(sms.head())

print("\nDataset Shape:")
print(sms.shape)

print("\nMissing Values:")
print(sms.isnull().sum())

print("\nLabel Distribution:")
print(sms["label"].value_counts())

print("\nDuplicate Records:")
print(sms.duplicated().sum())

print(sms["label"].value_counts())