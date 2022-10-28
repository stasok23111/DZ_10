import json


def load_candidates(filename):
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_by_pk(pk):
    return data[pk - 1]


def get_by_skills(name_skill):
    candidates = []
    for i in data:
        if name_skill.lower() in i["skills"].lower():
            candidates.append(i)
    return candidates


file_name = "candidates.json"
data = load_candidates(file_name)

print(get_by_skills("python"))
