#%%
def ampm(tijd):
    if tijd.endswith("AM"):
        tijd2 = tijd[:-2]
        if tijd2 != "12":
            tijd2 = 0
        return f"{tijd2}u"
    elif tijd.endswith("PM"):
        tijd2 = tijd[:-2]
        if tijd2 != "12":
            tijd2 = (int(tijd2)) + 12
        return f"{tijd2}u"
    elif tijd.endswith("u"):
        tijd2 = tijd[:-1]
        if tijd2 == "0":
            tijd2 = 12
            aanduiding = "AM"
        elif int(tijd2) >= 1 and int(tijd2) <= 11:
            tijd2 = tijd2
            aanduiding = "AM"
        elif tijd2 == "12":
            tijd2 = tijd
            aanduiding = "PM"
        elif int(tijd2) >= 13 and int(tijd2) <= 23:
            tijd2 = (int(tijd2)) - 12
            aanduiding = "PM"
        else:
            print("Er klopt iets niet :) ")
            aanduiding = ""
    return f"{tijd2}{aanduiding}"    

ampm("23u")
# %%
