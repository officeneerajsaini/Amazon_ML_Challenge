import pandas as pd
from collections import Counter


def count_countries(path):
    counts = Counter()

    for chunk in pd.read_csv(
        path,
        sep="\t",
        usecols=["country"],
        chunksize=200_000
    ):
        values = chunk["country"].fillna("").astype(str).str.strip()

        counts.update(values)

    return counts


files = {
    "Source 1": "dataset/train/train_source1.tsv",
    "Source 2": "dataset/train/train_source2.tsv",
    "Source 3": "dataset/train/train_source3.tsv",
}


for name, path in files.items():
    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    counts = count_countries(path)

    print("Number of unique country values:", len(counts))

    print("\nTop 20 countries:")
    for country, count in counts.most_common(20):
        print(repr(country), ":", count)