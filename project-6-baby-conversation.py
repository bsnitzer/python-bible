# Python Bible
# Brian Snitzer
# July 25, 2019

from random import choice

questions = [
    "Why is the sky blue?: ",
    "What is the moon made of?: ",
    "What happened to the dinosaurs?: "
    ]

question= choice(questions)
answer = input(question).strip().lower()
breakout = "just because"
while answer != breakout:
    answer = input("Why?: ").strip().lower()
