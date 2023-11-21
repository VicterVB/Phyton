#%%
def geldige_parameter (parameter):
    waarde = parameter.startswith("?") and parameter.isupper()
    return waarde 

invoer_parameter = input("Geef je parameter: ")
uitvoer = geldige_parameter(invoer_parameter)

string = "Dit is een correcte parameter" if uitvoer == True else "Dit is geen correcte parameter"
print(string)
#%%
def zoek_parameter(template):
    start_parameter = template.find("?")
    einde_parameter = template.find(" ", start_parameter)

    parameter_woord = template[start_parameter + 1 : einde_parameter].isupper()
    parameter = template[start_parameter : einde_parameter]
    uitkomst = parameter if parameter_woord == True else False
    return uitkomst

template1 = """Beste ?NAAM ik ben er even niet,
ik zal je bericht zo snel mogelijk beantwoorden.
groeten, 
Katja"""

print(zoek_parameter(template1))

# %%
def personaliseer_template(template, waarde):
    def zoek_parameter(template_1):
        start_parameter = template_1.find("?")
        einde_parameter = template_1.find(" ", start_parameter)

        parameter_woord = template_1[start_parameter + 1 : einde_parameter].isupper()
        parameter = template_1[start_parameter : einde_parameter]
        uitkomst = parameter if parameter_woord == True else False
        return uitkomst
    nieuwe_template = template.replace(zoek_parameter(template), waarde)
    return nieuwe_template

#template1 = input("Vul een template in: ")
template1 = """Beste ?NAAM ik ben er even niet,
ik zal je bericht zo snel mogelijk beantwoorden.
groeten, 
Katja"""
waarde_invoer = input("Vul een waarde in: ")
print(personaliseer_template(template1, waarde_invoer))
# %%
def personaliseer_template(template):
    einde_parameter = 0
    nieuwe_template_2 = ""
    einde_parameter_1 = 0

    while einde_parameter < len(template):
        def zoek_parameter(template_1):
            start_parameter = template_1.find("?", einde_parameter_1)
            einde_parameter = template_1.find(" ", start_parameter)
            einde_parameter_1 = einde_parameter

            parameter_woord = template_1[start_parameter + 1 : einde_parameter].isupper()
            parameter = template_1[start_parameter : einde_parameter]
            uitkomst = parameter if parameter_woord == True else False
            return uitkomst, einde_parameter
        template_leeg = zoek_parameter(template[einde_parameter:])[0]
        einde_parameter = int(zoek_parameter(template)[1])
        waarde = input(f"Wat is de waarde voor de parameter {template_leeg}")
        nieuwe_template = template.replace(template_leeg, waarde)[einde_parameter: len(template)]
        nieuwe_template_2 = nieuwe_template_2 + nieuwe_template
    return nieuwe_template_2

template2 = "Beste ?ONTVANGER ik geniet momenteel van een welverdiende vakantie, Ik ben terug op ?DATUM grtjs ?AFZENDER Odisee campus Gent."

personaliseer_template(template2)


# %%

# %%
