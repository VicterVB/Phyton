class MeetGegevens:
    def __init__(self, meetgegevens):
        self.meetgegevens = meetgegevens

    def zijn_alle_elementen_verschillend(self):
        return len(set(self.meetgegevens)) == len(self.meetgegevens)

    def bepaal_kleinste_positief_verschil(self):
        if not self.zijn_alle_elementen_verschillend():
            return "Niet alle elementen zijn verschillend, dus het kleinste positieve verschil kan niet bepaald worden."

        gesorteerd_meetgegevens = sorted(self.meetgegevens)
        kleinste_verschil = float("inf")

        for i in range(len(gesorteerd_meetgegevens) - 1):
            verschil = gesorteerd_meetgegevens[i + 1] - gesorteerd_meetgegevens[i]
            if verschil < kleinste_verschil:
                kleinste_verschil = verschil

        return kleinste_verschil

    def __str__(self):
        return str(self.meetgegevens)

# Testprogramma
meetwaarden = [1,2,4,8]
meet_object = MeetGegevens(meetwaarden)
if meet_object.zijn_alle_elementen_verschillend():
    print("Alle meetgegevens zijn verschillend")
else:
    print("Niet alle meetwaarden zijn verschillend")
print(meet_object.bepaal_kleinste_positief_verschil())
print("Meetwaarden:", meet_object)
