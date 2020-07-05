#creates type dis/advantes for fire, water, and grass types
type_advantages = {'grass':'water', 'water':'fire', 'fire':'grass'}
type_disadvantages = {'water':'grass', 'fire':'water', 'grass':'fire'}

class Pokemon:

    def __init__(self, name, type, level=5):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level * 4
        self.current_health = level * 4
        self.knocked_out = False
        self.weakness = type_disadvantages.get(type)
        self.advantage = type_advantages.get(type)

    def __repr__(self):
        #printing a pokemon displays its name, type, level, and its hit points
        return "The {type} type, level {level} {name} has {hp} hit points remaining.".format(type=self.type, level=self.level, name=self.name, hp=self.current_health)

    def gain_health(self, amount):
        #takes a health potion and applies the health to the pokemon
        self.current_health += amount
        print("{name} now has {health} health!".format(name=self.name, health=self.current_health))
        return self.current_health

    def lose_health(self, amount):
        #takes an amount of damage and applies it to the pokemon
        self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0
            self.knock_out()
        else:
            print("{name} now has {health} health.".format(name=self.name, health=self.current_health))
            return self.current_health

    def knock_out(self):
        #if the pokemons health is less than or equal to zero, the pokemon is knocked out
        if self.current_health <= 0:
            self.knocked_out = True
            print("{} has fainted.".format(self.name))

    def revive(self):
        #checks to make sure that the pokemon is knocked out before reviving it
        if self.current_health <= 0 and self.knocked_out == True:
            self.knocked_out = False
            self.current_health += (self.max_health / 2)
            print("{name} was revived and has returned to the battle!".format(name=self.name))

    def attack(self, opponent_poke):
        #checks to see if the pokemon is able to attack the opponent
        if self.knocked_out == True:
            return "This pokemon has fainted and is unable to attack!"
        else:
            damage = self.max_health / 3
            #determines damage if it's a not very effective matchup
            if self.weakness == opponent_poke.type:
                matchup_damage = damage / 2
                print("{my_poke} attacked {oppo_poke} for {damage} damage.".format(my_poke=self.name, oppo_poke=opponent_poke.name, damage=matchup_damage))
                print("It's Not Very Effective!")
                opponent_poke.lose_health(matchup_damage)
            #determines damage if it's a supereffective matchup
            elif self.advantage == opponent_poke.type:
                matchup_damage = damage * 2
                print("{my_poke} attacked {oppo_poke} for {damage} damage.".format(my_poke=self.name, oppo_poke=opponent_poke.name, damage=matchup_damage))
                print("It's Super Effective!")
                opponent_poke.lose_health(matchup_damage)
            #determines damage if it's a neutral matchup
            else:
                matchup_damage = damage
                print("{my_poke} attacked {oppo_poke} for {damage} damage.".format(my_poke=self.name, oppo_poke=opponent_poke.name, damage=matchup_damage))
                opponent_poke.lose_health(matchup_damage)

class Charizard(Pokemon):
    def __init__(self, level=5):
        super().__init__("Charizard", 'fire', level)

class Venusaur(Pokemon):
    def __init__(self, level=5):
        super().__init__("Venusaur", 'grass', level)

class Blastoise(Pokemon):
    def __init__(self, level=5):
        super().__init__("Blastoise", 'water', level)

class Combusken(Pokemon):
    def __init__(self, level=5):
        super().__init__("Combusken", 'fire', level)

class Sceptile(Pokemon):
    def __init__(self, level=5):
        super().__init__("Sceptile", 'grass', level)

class Swampert(Pokemon):
    def __init__(self, level=5):
        super().__init__("Swampert", 'water', level)

class Trainer:

    def __init__(self, pokemon_list, potions, trainer_name):
        self.pokemon_list = pokemon_list
        self.potions = potions
        self.trainer_name = trainer_name
        self.current_pokemon = 0

    def __repr__(self):
        #lists off the trainers pokemon and shows which one is currently in battle
        print("{trainer} has the following pokemon:".format(trainer=self.trainer_name))
        for pokemon in self.pokemon_list:
            print(pokemon)
        return "{pokemon} is currently in battle.".format(pokemon=self.pokemon_list[self.current_pokemon].name)

    def use_potion(self):
        #makes sure that the trainer has enough potions before using them, then increases the health of the current pokemon
        potion = 20
        if self.potions > 0:
            print("{trainer} used a potion on {pokemon}.".format(trainer=self.trainer_name, pokemon=self.pokemon_list[self.current_pokemon].name))
            self.pokemon_list[self.current_pokemon].gain_health(potion)
            self.potions -= 1
        else:
            print("You don't have any potions left!")
        print('-----')

    def attack_opposing_trainer(self, other_trainer):
        #finds the current pokemon and its opponent, and attacks the opponent
        opposing_pokemon = other_trainer.pokemon_list[other_trainer.current_pokemon]
        my_pokemon = self.pokemon_list[self.current_pokemon]
        my_pokemon.attack(opposing_pokemon)
        print('-----')

    def switch_active_pokemon(self, new_active):
        #checks to make sure that the new_active value can be applied to the pokemon_list
        if new_active < len(self.pokemon_list) and new_active >= 0:
            #checks if the the pokemon is knocked out
            if self.pokemon_list[new_active].knocked_out:
                print("This {pokemon} is knocked out! It is unable to enter the battle!".format(pokemon=self.pokemon_list[new_active].name))
            #checks whether the pokemon is already in battle
            elif self.current_pokemon == new_active:
                print("This pokemon is already in battle!")
            #switches in the new pokemon
            else:
                print("{old_active} was switched out.".format(old_active=self.pokemon_list[self.current_pokemon].name))
                print("{new_active} has entered the battle!".format(new_active=self.pokemon_list[new_active].name))
                self.current_pokemon = new_active
            print('-----')

charizard = Charizard(36)
venusaur = Venusaur(32)
blastoise = Blastoise(36)
combusken = Combusken(36)
sceptile = Sceptile(32)
swampert = Swampert(36)


red = Trainer([charizard, venusaur, blastoise], 3, "Red")
steven = Trainer([combusken, sceptile, swampert], 3, "Steven")

print(red)
print(steven)

print('-----')
red.attack_opposing_trainer(steven)
steven.switch_active_pokemon(2)
red.attack_opposing_trainer(steven)
steven.attack_opposing_trainer(red)
red.use_potion()
steven.attack_opposing_trainer(red)
red.switch_active_pokemon(0)
red.switch_active_pokemon(1)
charizard.revive()
print(charizard.current_health)
