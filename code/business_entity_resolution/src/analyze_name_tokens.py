import pandas as pd
from collections import Counter
import re
import unicodedata


def normalize_text(value):
    if pd.isna(value):
        return ""

    value = str(value)
    value = unicodedata.normalize("NFKC", value)
    value = value.lower()

    value = re.sub(r"[^\w\s]", " ", value, flags=re.UNICODE)
    value = re.sub(r"\s+", " ", value).strip()

    return value


def count_tokens(path):
    counts = Counter()

    for chunk in pd.read_csv(
        path,
        sep="\t",
        usecols=["business_name"],
        chunksize=200_000
    ):
        names = chunk["business_name"].fillna("")

        for name in names:
            normalized = normalize_text(name)

            for token in set(normalized.split()):
                if token:
                    counts[token] += 1

    return counts


files = {
    "Source 1": "dataset/train/train_source1.tsv",
    "Source 2": "dataset/train/train_source2.tsv",
    "Source 3": "dataset/train/train_source3.tsv",
}


for name, path in files.items():

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    counts = count_tokens(path)

    print("\nTop 50 most common tokens:")

    for token, count in counts.most_common(50):
        print(f"{token!r}: {count}")