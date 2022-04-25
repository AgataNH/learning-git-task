shopping_dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
shopping_dict = {key: [ele.capitalize() for ele in shopping_dict[key]] for key in shopping_dict}
new_dict = dict((key.capitalize(), value) for key, value in shopping_dict.items())