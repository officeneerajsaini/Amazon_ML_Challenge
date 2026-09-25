import pandas as pd

files = {
    "Source 1": "dataset/train/train_source1.tsv",
    "Source 2": "dataset/train/train_source2.tsv",
    "Source 3": "dataset/train/train_source3.tsv",
    "Ground Truth": "dataset/train/train_ground_truth.tsv",
}

for name, path in files.items():
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    df = pd.read_csv(path, sep="\t", nrows=5)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.to_string(index=False))