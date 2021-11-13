class Race:
    def __init__(self, name = None):
        self.name = name
        self.ability_inc = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0}
        self.age_adult = None
        self.lifespan = None
        self.size = None
        self.speed = None
        self.languages = None
        self.hp_modifier = 0
        
    def info(self):
        print("Race: " + self.name)
        
        print("Ability Score Increase: ")
        for a in self.ability_inc.keys():
            if self.ability_inc[a] != 0:
                print('   ' + a + ": +" + str(self.ability_inc[a]))
        print("Age of Adulthood: " + str(self.age_adult))
        print("Lifespan: " + str(self.lifespan) +" years")
        print("Size: " + self.size)
        print("Speed: " + str(self.speed) + "ft")
        print("Languages Known: " + ' '.join(self.languages))

class SubRace(Race):
    def __init__(self, name, race):
        self.race = race.name
        self.subrace = name
        self.ability_inc = race.ability_inc
        self.age_adult = race.age_adult
        self.lifespan = race.lifespan
        self.size = race.size
        self.speed = race.speed
        self.languages = race.languages