import dnd_race as r
import dnd_passive_traits as pt

Dwarf = r.Race("Dwarf")
Dwarf.ability_inc["Constitution"] = Dwarf.ability_inc["Constitution"] + 2
Dwarf.age_adult = 50
Dwarf.lifespan = 350
Dwarf.size = "4-5ft (Medium)"
Dwarf.speed = 25
Dwarf.languages = {"Dwarvish", "Common"}

dark_vision = pt.Passive_Trait("Dark Vision", Dwarf)
dark_vision.description = '''. Accustomed to life underground, you have
    superior vision in dark and dim conditions. You can see
    in dim light within 60 feet of you as if it were bright light,
    and in darkness as if it were dim light. You can’t discern
    color in darkness, only shades of gray.'''
    
dwarven_resilience = pt.Passive_Trait("Dwarven Resilliance", Dwarf)
dwarven_resilience.description = '''You have advantage on saving
    throws against poison, and you have resistance against
    poison damage'''
# how to integrate this?
    
dwarven_combat_training = pt.Passive_Trait("Dwarven Combat Training", Dwarf)
dwarven_combat_training.description = '''You have proficiency with
    the battleaxe, handaxe, light hammer, and warhammer.'''
# add to proficiencies dictionary
    
stonecutting = pt.Passive_Trait("Stonecutting", Dwarf)
stonecutting.description = '''Whenever you make an Intelligence
    (History) check related to the origin of stonework, you are
    considered proficient in the History skill and add double
    your proficiency bonus to the check, instead of your normal proficiency bonus.'''
# proooobably not gonna try and encode this lol but thats what roll_adv is for


Hill_Dwarf = r.SubRace("Hill Dwarf", Dwarf)
Hill_Dwarf.ability_inc["Strength"] = Hill_Dwarf.ability_inc["Strength"] + 2

dwarven_armor_training = pt.Passive_Trait("Dwarven Armor Training", Hill_Dwarf)
dwarven_armor_training.description = "You have proficiency with light and medium armor."
# add to proficiencies dictionary