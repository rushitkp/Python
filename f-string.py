# letter="Hey my name is {0} and I am from {1}"
# country="India"
# name="Rk"
# letter.format(name,country)
# print(letter.format(name,country))

# print(f"Hey my name is {name} and I am from {country}")
# print(f"{2*45,20+30}")
# print(type(f"{2*45,20+30}"))

letter="Hey My Name is {0} And I Am From {1}"
name="Rushit"
country="India"
letter.format(name,country)
print(letter.format(name,country))

txt="Rk"
country="India"
print(f"Hello my name is {txt} and I come from {country}")

txt="for only {price:.2f} dollars"
print(txt.format(price=49.099999))
