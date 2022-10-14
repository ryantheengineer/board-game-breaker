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


# Bird cards might work better as dictionaries. They probably don't need their
# own internal functions
class BirdCard:
    def __init__(self,cards_df_row):
        self.common_name = cards_df_row["Common name"]
        self.scientific_name = cards_df_row["Scientific name"]
        self.color = cards_df_row["Color"]
        self.powercategory = cards_df_row["PowerCategory"]
        self.powertext = cards_df_row["Power text"]
        self.predator = cards_df_row["Predator"]
        self.flocking = cards_df_row["Flocking"]
        
class BirdCardTray:
    def __init__(self, cards_df):
        self.cards_df = cards_df
        self.deck = self.initialize_deck()
        
    def initialize_deck(self):
        # Create the basic list of cards, shuffle, and place cards in tray slots
        deck = [BirdCard(self.cards_df.loc[row]) for row in range(len(cards_df))]
        # shuffle the deck
        
        # draw 3 cards and fill tray
        
        return deck


##### Other functions #####
def prep_card_data(df):
    # Get rid of rows with nan common name
    df = df[df["Common name"].notna()]
    
    df = df.drop(columns=["* (food cost)"], axis=1)
    
    bonus_columns = list(df.columns)
    del bonus_columns[0:27]
    
    boolean_fix_columns = ["Predator", "Flocking", "Bonus card", "Forest",
                           "Grassland", "Wetland", "Straight points power",
                           "Non-environment power", "Power outside env"]
    # Replace 1s and 0s in appropriate columns with True/False
    for boolean_str in boolean_fix_columns:
        df[boolean_str].loc[df[boolean_str] == 0] = False
        df[boolean_str].loc[df[boolean_str] == 1] = True
    
    for i in range(len(df)):
        if np.isnan(df.loc[i,"/ (food cost)"]):
            df.loc[i,"/ (food cost)"] = 0
            
    for bonus_str in bonus_columns:
        for i in range(len(df)):
            if np.isnan(df.loc[i,bonus_str]) or df.loc[i,bonus_str] == 0:
                df.loc[i,bonus_str] = False
            else:
                df.loc[i,bonus_str] = True
                
    return df


if __name__ == "__main__":
    #load bird card data
    cards_df = pd.read_csv('wingspan-card-lists-Core.csv')
    
    cards_df = prep_card_data(cards_df)
    # clean cards_df
    
    
    feeder = Birdfeeder()
    feeder.print_current_dice()
    
    cardtray = BirdCardTray(cards_df)