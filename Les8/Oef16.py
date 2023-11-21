def zoekertje(tekst):
    klinkers = "aeiouAEIOU"
    woorden = tekst.split()
    resultaat = []

    for woord in woorden:
        ingekort_woord = ""
        eerste_klinker_gevonden = False

        for letter in woord:
            if letter in klinkers:
                if not eerste_klinker_gevonden:
                    ingekort_woord += letter
                    eerste_klinker_gevonden = True
            else:
                ingekort_woord += letter

        resultaat.append(ingekort_woord)

    ingekorte_tekst = " ".join(resultaat)
    return ingekorte_tekst

originele_tekst = "Appartement Te Huur, 3 slaapkamers, ruime inkom,\ntuin en garage."
resultaat = zoekertje(originele_tekst)
print(resultaat)