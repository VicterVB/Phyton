def aantal_chars(tekst):
    aantal = {}
    for i in tekst:
        if i not in aantal:
            aantal[i] = 1
        else:
            aantal[i] +=1
    return aantal

aantal_chars("hottentottententententoonstelling")