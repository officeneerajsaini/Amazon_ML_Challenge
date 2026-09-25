import pandas as pd
from collections import Counter


def analyze_names(path):
    lengths = Counter()
    examples = []

    for chunk in pd.read_csv(
        path,
        sep="\t",
        usecols=["business_name"],
        chunksize=200_000
    ):
        names = chunk["business_name"].fillna("").astype(str)

        for name in names:
            tokens = name.split()

            lengths[len(tokens)] += 1

            if len(examples) < 20 and name.strip():
                examples.append(name)

    return lengths, examples


files = {
    "Source 1": "dataset/train/train_source1.tsv",
    "Source 2": "dataset/train/train_source2.tsv",
    "Source 3": "dataset/train/train_source3.tsv",
}


for name, path in files.items():

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    lengths, examples = analyze_names(path)

    print("\nName token count distribution:")

    for token_count, frequency in sorted(lengths.items()):
        print(token_count, "tokens:", frequency)

    print("\nExample names:")

    for example in examples[:10]:
        print(example)