import random
class Hider:
    # The hider class is
    def __init__(self):

        self.hider_location = random.randint(1, 1000)
        self.distance = [0, 0]#[current, last]

    def get_hint(self):
        if self.distance[-1] == 0:
            return 'Yahaha you found me!'

        elif self.distance[-1] > self.distance[-2]:
            return 'Getting Colder.'

        elif self.distance[-1] < self.distance[-2]:
            return 'Getting Warmer!'


    def watch(self, location):
        current_distance = abs(self.hider_location - location)
        self.distance.append(current_distance)
        
        