#  Python Bible, Project 5
# Brian Snitzer
# July 25, 2019


films = {
    "Findingn Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,1],
    "Ghostbusters": [12,5]
}

while True:
    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())
# Check user age
        if age >= films[choice][0]:

            # Check the number of seats
            if films[choice][1] > 0:
                print("Enjoy the film.")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out")
        else:
            print("You are too young.")
    else:
        print("We don't have that film.")
