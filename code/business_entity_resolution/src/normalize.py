import re
import unicodedata


def normalize_text(value):
    if value is None:
        return ""

    if not isinstance(value, str):
        return ""

    value = unicodedata.normalize("NFKC", value)

    value = value.lower()

    value = value.replace("&", " and ")

    value = re.sub(r"[^\W_]", lambda m: m.group(0), value, flags=re.UNICODE)

    value = re.sub(r"\s+", " ", value).strip()

    return value


def normalize_name(value):
    return normalize_text(value)


def normalize_address(value):
    return normalize_text(value)

#temp
# if __name__ == "__main__":
#     examples = [
#         "ABC Corporation Pvt. Ltd.",
#         "ABC Corp. Pvt Ltd",
#         "Success International School Private Limited",
#         "सुप्रीम इलेक्ट्रॉनिक्स",
#     ]

#     for x in examples:
#         print(x)
#         print(" -> ", normalize_name(x))
#         print()

if __name__ == "__main__":
    examples = [
        "सुप्रीम इलेक्ट्रॉनिक्स",
        "ಕನ್ನಡ ಕಂಪನಿ",
        "ABC Corporation Pvt. Ltd."
    ]

    for x in examples:
        result = normalize_name(x)

        print("Original :", repr(x))
        print("Normalized:", repr(result))
        print()