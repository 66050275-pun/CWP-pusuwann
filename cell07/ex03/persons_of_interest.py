#!/usr/bin/env python3

def famous_births(figures):
    sorted_figures = sorted(figures.values(), key=lambda p: p["date_of_birth"])
    for person in sorted_figures:
        name = person["name"]
        date = person["date_of_birth"]
        print(f"{name} is a great scientist born in {date}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)

# Example test command in terminal:
# ./cell07/ex03/persons_of_interest.py
