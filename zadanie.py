shopping_dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "pietruszka"]
}
shopping_dict = {key: [ele.capitalize() for ele in shopping_dict[key]] for key in shopping_dict}
new_dict = dict((key.capitalize(), value) for key, value in shopping_dict.items())
for key, value in new_dict.items():
    print(f"Idę do {key} i kupuję tam {value}")
count = sum(map(len, new_dict.values()))
print(f"W sumie kupuję {count} produktów")