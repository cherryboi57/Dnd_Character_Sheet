# import race dictionary
# import class dictionary
# import inventory class
import dnd_dice as d

class Player:
#   import race dictionary
#   import classs dictionary
    def __init__(self, n, r, cl):
        self.name = n
        self.race = r
        self.clas = cl
        
        self.ability_scores = {
            "Strength": None,
            "Dexterity": None,
            "Constitution": None,
            "Intelligence": None,
            "Wisdom": None,
            "Charisma": None}
        
        self.base_ability = { 
            "Strength": None,
            "Dexterity": None,
            "Constitution": None,
            "Intelligence": None,
            "Wisdom": None,
            "Charisma": None}
        
        self.ability_mod = {"Strength": None,
            "Dexterity": None,
            "Constitution": None,
            "Intelligence": None,
            "Wisdom": None,
            "Charisma": None}
        
        self.skills = {
            "Acrobatics": None,
            "Animal Handling": None,
            "Arcana": None,
            "Athletics": None,
            "Deception": None,
            "History": None,
            "Insight": None,
            "Intimidation": None,
            "Investigation": None,
            "Medicine": None,
            "Nature": None,
            "Perception": None,
            "Performance": None,
            "Persuasion": None,
            "Religion": None,
            "Sleight of Hand": None,
            "Stealth": None,
            "Survival": None}
        
#       self.inventory = i.Inventory
#       self.rested = True

    def update_stats(self):
        self.ability_scores = {k: self.base_ability.get(k, 0) +
                               self.race.ability_inc.get(k, 0) +
                               self.clas.ability_inc.get(k, 0)
                               for k in set(self.base_ability)}
        self.ability_mod = {
            "Strength": (self.ability_scores["Strength"]-10)/2,
            "Dexterity": (self.ability_scores["Dexterity"]-10)/2,
            "Constitution": (self.ability_scores["Constitution"]-10)/2,
            "Intelligence": (self.ability_scores["Intelligence"]-10)/2,
            "Wisdom": (self.ability_scores["Wisdom"]-10)/2,
            "Charisma": (self.ability_scores["Charisma"]-10)/2}
        self.skills = {
            "Acrobatics": self.ability_mod["Dexterity"],
            "Animal Handling": self.ability_mod["Wisdom"],
            "Arcana": self.ability_mod["Intelligence"],
            "Athletics": self.ability_mod["Strength"],
            "Deception": self.ability_mod["Charisma"],
            "History": self.ability_mod["Intelligence"],
            "Insight": self.ability_mod["Wisdom"],
            "Intimidation": self.ability_mod["Charisma"],
            "Investigation": self.ability_mod["Intelligence"],
            "Medicine": self.ability_mod["Wisdom"],
            "Nature": self.ability_mod["Intelligence"],
            "Perception": self.ability_mod["Wisdom"],
            "Performance": self.ability_mod["Charisma"],
            "Persuasion": self.ability_mod["Charisma"],
            "Religion": self.ability_mod["Intelligence"],
            "Sleight of Hand": self.ability_mod["Dexterity"],
            "Stealth": self.ability_mod["Dexterity"],
            "Survival": self.ability_mod["Wisdom"]}
        

    def set_base_ability(self, st, dex, con, i, wis, cha):
        self.base_ability["Strength"] = st 
        self.base_ability["Dexterity"] = dex
        self.base_ability["Constitution"] = con 
        self.base_ability["Intelligence"] = i 
        self.base_ability["Wisdom"] = wis 
        self.base_ability["Charisma"] = cha 
        self.update_stats()
    
    def skill_check(self, skill, adv = None):
        if adv == 1:
            roll = d.d20.roll_adv()
            return roll + self.skills[skill]
        elif adv == 0:
            roll = d.d20.roll_disadv()
            return roll + self.skills[skill]
        else:
            roll = d.d20.roll()
            return roll + self.skills[skill]
        
    def ability_check(self, skill, adv = None):
        if adv == 1:
            roll = d.d20.roll_adv()
            return roll + self.ability_mod[skill]
        elif adv == 0:
            roll = d.d20.roll_disadv()
            return roll + self.ability_mod[skill]
        else:
            roll = d.d20.roll()
            return roll + self.ability_mod[skill]
    
   
