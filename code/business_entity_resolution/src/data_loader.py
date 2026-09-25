import pandas as pd

train_s1 = pd.read_csv(
    "dataset/train/train_source1.tsv",
    sep="\t"
)

train_s2 = pd.read_csv(
    "dataset/train/train_source2.tsv",
    sep="\t"
)

train_s3 = pd.read_csv(
    "dataset/train/train_source3.tsv",
    sep="\t"
)

ground_truth = pd.read_csv(
    "dataset/train/train_ground_truth.tsv",
    sep="\t"
)

print("Source 1:", train_s1.shape)
print("Source 2:", train_s2.shape)
print("Source 3:", train_s3.shape)
print("Ground Truth:", ground_truth.shape)

print("\nSource 1 columns:")
print(train_s1.columns.tolist())

print("\nGround Truth columns:")
print(ground_truth.columns.tolist())