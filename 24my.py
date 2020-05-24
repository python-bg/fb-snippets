text = str(input())

pre_mapping = {'zh': 'ж', 'ts': 'ц', 'ch': 'ч', 'sh': 'ш', 'шt': 'щ', 'yu': 'ю', 'ya': 'я', "6t": "щ", "1o": "ьо",
               "dй": "дь", "jй": "жь", "жй": "жь", "zй": "зь", "kй": "кь", "lй": "ль", "mй": "мь", "nй": "нь",
               "pй": "пь", "rй": "рь", "sй": "сь", "tй": "ть", "fй": "фь", "cй": "ць", "чй": "чь", "шй": "шь",
               "щй": "щь"}

mapping = {'a': 'а', 'b': 'б', 'w': 'в', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'j': 'ж', 'z': 'з', 'i': 'и', 'y': 'й',
           'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф',
           'h': 'х', 'c': 'ц', '4': 'ч', '6': 'ш', '1': 'ъ', 'q': 'я'}

for latin, cyrillic in pre_mapping.items():
    text = text.replace(latin, cyrillic)
    text = text.replace(latin.upper(), cyrillic.upper())
    text = text.replace(latin.capitalize(), cyrillic.capitalize())

for latin, cyrillic in mapping.items():
    text = text.replace(latin, cyrillic)
    text = text.replace(latin.upper(), cyrillic.upper())

print(text)
