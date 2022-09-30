"""

"""

import numpy as np
import pandas as pd
import random


# class Game:
#     # Class made up of players, board, cards, resources, etc.
#
#
#
# class Player:
#     # Class to hold an individual player's cards and available resources
#
######## BUILDING UP DICE AND BIRDFEEDER FROM THE GROUND UP ####################
class FoodDie:
    sides = ["Seed", "Invertebrate", "Fish", "Fruit", "Rodent", "Seed or Invertebrate"]

    def __init__(self,sideup=None,infeeder=None):
        if sideup is None:
            sideup = random.choice(FoodDie.sides)
        self.sideup = sideup
        # print(self.sideup)

        if infeeder is None:
            infeeder = True
        self.infeeder = infeeder

    def rollfood(self):
        self.sideup = random.choice(FoodDie.sides)
        print(self.sideup)


class Birdfeeder:
    def __init__(self, die1=None, die2=None, die3=None, die4=None, die5=None, dice=None, foodinfeeder=None, foodoutfeeder=None):
        # "Invertebrate", "Fish", "Fruit", "Rodent", "Seed or Invertebrate"]
        self.die1 = FoodDie()
        self.die2 = FoodDie()
        self.die3 = FoodDie()
        self.die4 = FoodDie()
        self.die5 = FoodDie()
        # FIX: other methods might work better if a list of dice is iterable

        if dice is None:
            dice = [self.die1, self.die2, self.die3, self.die4, self.die5]
        self.dice = dice

        if foodinfeeder is None:
            _ = self.countinfeeder()
            
        if foodoutfeeder is None:
            _ = self.countoutfeeder()

    def countinfeeder(self):
        # Count the current food in the feeder (can be immediately after a roll
        # or just to check)
        # foodinfeeder = [0, 0, 0, 0, 0, 0]
        foodinfeeder = {"Seed":0, "Invertebrate":0, "Fish":0, "Fruit":0, "Rodent":0, "Seed or Invertebrate":0}
        for i in range(len(self.dice)):
            if self.dice[i].infeeder is True:
                foodinfeeder[self.dice[i].sideup] += 1

        self.foodinfeeder = foodinfeeder

        return foodinfeeder

    def countoutfeeder(self):
        # Count the current food outside the feeder (can be immediately after a
        # roll or just to check)
        foodoutfeeder = {"Seed":0, "Invertebrate":0, "Fish":0, "Fruit":0, "Rodent":0, "Seed or Invertebrate":0}
        
        for i in range(len(self.dice)):
            if self.dice[i].infeeder is False:
                foodoutfeeder[self.dice[i].sideup] += 1
        
        self.foodoutfeeder = foodoutfeeder

        return foodoutfeeder

    def rollalldice(self):
        # Roll all dice into the birdfeeder
        for i in range(len(self.dice)):
            self.dice[i].infeeder = True
            self.dice[i].rollfood()

    def rolloutfeeder(self):
        # Roll only the dice that are out of the feeder
        foodoutfeeder = {"Seed":0, "Invertebrate":0, "Fish":0, "Fruit":0, "Rodent":0, "Seed or Invertebrate":0}

        for i in range(len(self.dice)):
            if self.dice[i].infeeder is False:
                self.dice[i].rollfood()

                foodoutfeeder = self.countoutfeeder()

        return foodoutfeeder
    
    def print_current_dice(self):
        # Print all the dice in the feeder and then all the dice out of the feeder
        print("Dice currently in the feeder:")
        print(self.foodinfeeder)
        print("\nDice currently out of the feeder:")
        print(self.foodoutfeeder)

##################### BUILDING UP PLAYER BOARD FROM THE GROUND UP ##############
# How to best build the player board? Should there be a class for a card space
# that would contain the default action, the environment, the cost, etc.? Or
# should that be coded directly into a larger player board class?


class BirdCard:
    def __init__(self,name,pts,category,habitats):
        self.name = name
        self.pts = pts
        self.category = category
        self.habitats = habitats



if __name__ == "__main__":
    feeder = Birdfeeder()
    feeder.print_current_dice()