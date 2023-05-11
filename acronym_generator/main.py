data = input("Please enter the strings of word to generate Acronyms: ").split()

acronyms = []


for _ in data:
    a = _.strip()[0]
    acronyms.append(a.upper())

print("".join(acronyms))