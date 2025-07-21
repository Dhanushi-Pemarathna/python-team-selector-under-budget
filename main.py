import json
from itertools import product

class Candidate:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{self.name} ({self.salary})"

class Position:
    def __init__(self, title):
        self.title = title
        self.candidates = []

    def add_candidate(self, name, salary):
        self.candidates.append(Candidate(name, salary))

class TeamSelector:
    def __init__(self, positions, budget):
        self.positions = positions
        self.budget = budget

    def select_best_team(self):
        best_team = None
        best_total = -1
        all_options = [p.candidates for p in self.positions]

        for combo in product(*all_options):
            total = sum(c.salary for c in combo)
            if total <= self.budget and total > best_total:
                best_total = total
                best_team = combo

        return best_team, best_total

# Load from dictionary (after reading JSON)
def load_positions_from_dict(data):
    positions = []
    for title, candidates in data.items():
        pos = Position(title)
        for name, salary in candidates:
            pos.add_candidate(name, salary)
        positions.append(pos)
    return positions
