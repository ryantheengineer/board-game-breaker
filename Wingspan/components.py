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
            # foodinfeeder = {"Seed":0, "Invertebrate":0, "Fish":0, "Fruit":0, "Rodent":0, "Seed or Invertebrate":0}
            # # foodinfeeder = [0, 0, 0, 0, 0, 0]
            # # for i in range(len(dice)):
            # #     if self.dice[i].infeeder is True:
            # #         if self.dice[i].sideup == "Seed":
            # #             foodinfeeder[0] += 1
            # #         elif self.dice[i].sideup == "Invertebrate":
            # #             foodinfeeder[1] += 1
            # #         elif self.dice[i].sideup == "Fish":
            # #             foodinfeeder[2] += 1
            # #         elif self.dice[i].sideup == "Fruit":
            # #             foodinfeeder[3] += 1
            # #         elif self.dice[i].sideup == "Rodent":
            # #             foodinfeeder[4] += 1
            # #         elif self.dice[i].sideup == "Seed or Invertebrate":
            # #             foodinfeeder[5] += 1
            # #         else:
            # #             print("There's a problem with the code")
            # for i in range(len(dice)):
            #     if self.dice[i].infeeder is True:
            #         foodinfeeder[self.dice[i].sideup] += 1
            #         self.foodinfeeder = foodinfeeder

    def countinfeeder(self):
        # Count the current food in the feeder (can be immediately after a roll
        # or just to check)
        # foodinfeeder = [0, 0, 0, 0, 0, 0]
        foodinfeeder = {"Seed":0, "Invertebrate":0, "Fish":0, "Fruit":0, "Rodent":0, "Seed or Invertebrate":0}
        for i in range(len(self.dice)):
            if self.dice[i].infeeder is True:
                foodinfeeder[self.dice[i].sideup] += 1
        # for i in range(len(self.dice)):
        #     if self.dice[i].infeeder is True:
        #         if self.dice[i].sideup == "Seed":
        #             foodinfeeder[0] += 1
        #         elif self.dice[i].sideup == "Invertebrate":
        #             foodinfeeder[1] += 1
        #         elif self.dice[i].sideup == "Fish":
        #             foodinfeeder[2] += 1
        #         elif self.dice[i].sideup == "Fruit":
        #             foodinfeeder[3] += 1
        #         elif self.dice[i].sideup == "Rodent":
        #             foodinfeeder[4] += 1
        #         elif self.dice[i].sideup == "Seed or Invertebrate":
        #             foodinfeeder[5] += 1
        #         else:
        #             print("There's a problem with the code")
        self.foodinfeeder = foodinfeeder

        return foodinfeeder

    def countoutfeeder(self):
        # Count the current food outside the feeder (can be immediately after a
        # roll or just to check)
        foodoutfeeder = {"Seed":0, "Invertebrate":0, "Fish":0, "Fruit":0, "Rodent":0, "Seed or Invertebrate":0}
        
        for i in range(len(self.dice)):
            if self.dice[i].infeeder is False:
                foodoutfeeder[self.dice[i].sideup] += 1

        # for i in range(len(self.dice)):
        #     if self.dice[i].infeeder is False:
        #         if self.dice[i].sideup == "Seed":
        #             foodoutfeeder[0] += 1
        #         elif self.dice[i].sideup == "Invertebrate":
        #             foodoutfeeder[1] += 1
        #         elif self.dice[i].sideup == "Fish":
        #             foodoutfeeder[2] += 1
        #         elif self.dice[i].sideup == "Fruit":
        #             foodoutfeeder[3] += 1
        #         elif self.dice[i].sideup == "Rodent":
        #             foodoutfeeder[4] += 1
        #         elif self.dice[i].sideup == "Seed or Invertebrate":
        #             foodoutfeeder[5] += 1
        #         else:
        #             print("There's a problem with the code")
        
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

##################### BUILDING UP PLAYER BOARD FROM THE GROUND UP ##############
# How to best build the player board? Should there be a class for a card space
# that would contain the default action, the environment, the cost, etc.? Or
# should that be coded directly into a larger player board class?
