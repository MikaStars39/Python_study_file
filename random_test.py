class Dice:
    def roll(self):
        import random
        dice_number = [1, 2, 3, 4, 5, 6]
        result = (random.choice(dice_number), random.choice(dice_number))
        return result
