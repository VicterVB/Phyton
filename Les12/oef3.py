class HighScore:
    def __init__(self, naam, scores = {}):
        self.naam = naam
        self.scores = scores 

    def voeg_score_toe(self, naam_speler, score):
        if naam_speler not in self.scores:
            self.scores[naam_speler] = [score]
        else:
            if score > max(self.scores[naam_speler]):
                self.scores[naam_speler].append(score)

    def geef_ranking(self):
        ranking = []
        for naam_speler, scores in self.scores.items():
            for s in scores:
                ranking.append((naam_speler, s))
        ranking.sort(key = lambda x: x[1], reverse = True)
        return ranking
    
    def __str__(self):
        result = f"Dit zijn de resultaten van de highscore {self.naam}:\n"
        ranking = self.geef_ranking()
        for naam_speler, score in ranking:
            result += f"{naam_speler}: {score}\n"
        return result
    


initial_scores = {
    "Steve": [338180],
    "Abc": [555555],
    "XYZ": [123456],
    "Mitch": [150000],
    "Lisa": [200000],
    "Jul": [155555],
    "Milo": [222223],
}

high_score_game = HighScore("ExampleGame", initial_scores)

extra_scores = {
    "Steve": [338180],
    "Abc": [745689],
    "Pipa": [111111],
    "Helo": [989898],
    "Mitch": [550000],
}

for alias, scores in extra_scores.items():
    for score in scores:
        high_score_game.voeg_score_toe(alias, score)

ranking = high_score_game.geef_ranking()

print("Ranking   Alias    highscore")
print("-------   -----    ----------")

for i, (alias, score) in enumerate(ranking, start=1):
    print(f"{i:<9}{alias:<8}{score}")
    