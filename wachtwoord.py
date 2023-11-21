import random

def generate_password():
    uppercase = "ZSFRTGYHJKPLMWXCVB"
    lowercase = "azertyuopqsfghjkwxcbn"
    numbers = "123456789"
    punctuation = ["*", "?", "!", "+"]
    
    hoofd = random.choice(uppercase)
    klein = random.choice(lowercase)
    klein2 = random.choice(lowercase)
    klein3 = random.choice(lowercase)
    get = random.choice(numbers)
    get2 = random.choice(numbers)
    get3 = random.choice(numbers)
    teken = random.choice(punctuation)
    
    password = f"{hoofd}{klein}{klein2}{klein3}{teken}{get}{get2}{get3}"
    return password

aantal = int(input("Geef een aantal paswoorden: "))
for i in range(aantal):
    print(generate_password())
