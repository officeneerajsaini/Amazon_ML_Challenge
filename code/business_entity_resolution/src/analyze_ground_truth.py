import pandas as pd

gt = pd.read_csv(
    "dataset/train/train_ground_truth.tsv",
    sep="\t"
)

# Count how many matched IDs each S1 has
def count_matches(value):
    if pd.isna(value) or str(value).strip() == "":
        return 0

    return len(str(value).split(","))


gt["match_count"] = gt["matched_entity_ids"].apply(count_matches)

print("Total S1 entities:", len(gt))

print("\nMatch count distribution:")
print(gt["match_count"].value_counts().sort_index())

print("\nBasic statistics:")
print(gt["match_count"].describe())

print("\nSingletons / zero matches:")
print((gt["match_count"] == 0).sum())

print("\nEntities with multiple matches:")
print((gt["match_count"] > 1).sum())

print("\nMaximum matches for one S1:")
print(gt["match_count"].max())