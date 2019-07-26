# Python Bible - Coin
# Brian Snitzer
# July 26, 2019
import random


class Coin:
    def __init__(self, rare =False, clean =True, heads =True, **kwargs):

        for key,value in kwargs.items():
            setattr(self, key, value)

        self.rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

        def rust(self):
            self.color = self.rusty_color

        def clean(self):
            self.color = self.clean_color

        def flip(self):
            heads_options = [True, False]
            choice = random.choice(heads_options)
            self.heads = choice

        def __del__(self):
            print("Coin spent.")


class Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickess": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)
