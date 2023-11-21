class LoopWedstrijd:
    def __init__(self, naam_weds, lijst_naam = [], lijst_tijden = []):
        self.naam_weds = naam_weds
        self.lijst_naam = lijst_naam
        self.lijst_tijden = lijst_tijden
        self.dict = dict(zip(self.lijst_naam, self.lijst_tijden))

    def geef_winnaar(self):
        laagste_tijd = float("inf")
        winnaar = ""
        for i in self.dict:
            value = self.dict[i]
            if float(value) < float(laagste_tijd):
                laagste_tijd = value
                winnaar = str(i)
            elif float(value) == float(laagste_tijd):
                winnaar += " / " + str(i)
        return winnaar
    
    def voeg_prestatie_toe(self, atleet, prestatie):
        if atleet not in self.lijst_naam:
            self.lijst_naam.append(atleet)
            self.lijst_tijden.append(prestatie)
        else:
            index = self.lijst_naam.index(atleet)
            self.lijst_tijden[index] += prestatie

        self.dict = dict(zip(self.lijst_naam, self.lijst_tijden))

    def __str__(self):
        result = f"Dit zijn de resultaten van de loopwedstrijd {self.naam_weds}:\n"
        for atleet in self.dict:
            result += f"{atleet}: {self.dict[atleet]} seconden\n"
        return(result)
    
deelnemers = ["Peter", "Kristien", "Thomas", "Evert-Jan"]
tijden = ["12.5", "14.8", "13.2", "12.2"]

wedstrijd = LoopWedstrijd("OdiseeRun", deelnemers, tijden)

print(wedstrijd)
print(wedstrijd.geef_winnaar())

nieuwe_atleet = input("Welke atleet wil je toevoegen? ")
tijd_nieuwe_atleet = input("Welke tijd heeft hij/zij gelopen? ")

wedstrijd.voeg_prestatie_toe(nieuwe_atleet, tijd_nieuwe_atleet)

print(wedstrijd)
print(wedstrijd.geef_winnaar())