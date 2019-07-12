# Brian Snitzer
# July 12, 2019

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma",
                "Fred", "George", "Harry"]

print(len(known_users))

while True:
    print("Hi! My name is Travis.")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}. Name recognized".format(name))
        remove = input("Would you like to be removed?  (y/n)").strip().lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("Okey Dokey")

    else:
        print("Hmm, I don't think I've met you yet {}.".format(name))
        add_me = input("Would you like to be added? (y/n)").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("Nice to meet you anyway.")
