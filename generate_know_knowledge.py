import json


countries = ['austria', 'denmark', 'finland', 'france', 'greece', 'ireland', 'italy', 'netherlands', 'poland', 'romania','spain', 'sweden', 'switzerland', 'united kingdom', 'portugal', 'ukraine']

resp = []

for country in countries:
    with open(f'files/{country}.json', 'r') as f:
        data = json.load(f)
    for single_note in data:
        resp.append(f"In {country.capitalize()}: {single_note['note']}")

with open('knowledge.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(resp, ensure_ascii=False))
