vowels = 0
consonants = 0

for letter in input("enter a word: ").strip().lower():
    if letter in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))

students = {
    "male": ["Tom", "Charlie", "Harry"],
    "female": ["Sara", "Huda", "Samantha", "Emily"]
}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
