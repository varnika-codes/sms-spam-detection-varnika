import pandas as pd

# Load all datasets
cleaned = pd.read_csv("data/sms_cleaned.csv")
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

# Dataset sizes
print("CLEANED DATASET:", cleaned.shape)
print("TRAIN DATASET:", train.shape)
print("TEST DATASET:", test.shape)

# Label distribution
print("\nCleaned Dataset Distribution:")
print(cleaned["label"].value_counts())

print("\nTraining Dataset Distribution:")
print(train["label"].value_counts())

print("\nTesting Dataset Distribution:")
print(test["label"].value_counts())

# Check missing values
print("\nMissing Values in Training:")
print(train.isnull().sum())

print("\nMissing Values in Testing:")
print(test.isnull().sum())

# Check duplicate records
print("\nDuplicates in Cleaned Dataset:")
print(cleaned.duplicated().sum())

# Check for overlap between train and test
overlap = set(train["message"]) & set(test["message"])

print("\nTrain-Test Message Overlap:", len(overlap))

print("\nDataset verification completed!")