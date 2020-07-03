
class Pokemon:
    #creates type dis/advantes for fire, water, and grass types
    type_advantages = {'grass':'water', 'water':'fire', 'fire':'grass'}
    type_disadvantages = {'water':'grass', 'fire':'water', 'grass':'fire'}

    def __init__(self, name, level=5, type, status):
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
        return "{} type, level {} {} has {} hit points remaining.".format(self.type, self.level, self.name, self.current_health)

    def gain_health(self, amount):
        #takes a health potion and applies the health to the pokemon
        self.current_health += amount
        print("{name} now has {health} health!".format(name=self.name, health=self.current_health))
        return self.current_health

    def lose_health(self, amount):
        #takes an amount of damage and applies it to the pokemon
        self.current_health -= amount
        print("{name} was attacked and lost {damage} hit points! {name} now has {health} health.".format(name=self.name, damage=amount, health=self.current_health))
        return self.current_health

    def knocked_out(self):
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
            damage = (self.max_health / 3)
            #determines damage if it's a not very effective matchup
            if self.weakness == opponent_poke.type:
                matchup_damage = damage / 2
                opponent_poke.lose_health(matchup_damage)
                print("It's Not Very Effective!")
                print("{my_poke} attacked {oppo_poke} for {damage} damage.".format(my_poke=self.name, oppo_poke=opponent_poke.name, damage=matchup_damage))
            #determines damage if it's a supereffective matchup
            elif self.advantage == opponent_poke.type:
                matchup_damage = damage * 2
                opponent_poke.lose_health(matchup_damage)
                print("It's Super Effective!")
                print("{my_poke} attacked {oppo_poke} for {damage} damage.".format(my_poke=self.name, oppo_poke=opponent_poke.name, damage=matchup_damage))
            #determines damage if it's a neutral matchup
            else:
                matchup_damage = damage
                opponent_poke.lose_health(matchup_damage)
                print("{my_poke} attacked {oppo_poke} for {damage} damage.".format(my_poke=self.name, oppo_poke=opponent_poke.name, damage=matchup_damage))

class Trainer:

    def __init__(self, pokemon_list, potions, trainer_name):
        self.pokemon_list = pokemon_list
        self.potions = potions
        self.trainer_name = trainer_name
        self.current_pokemon = 0

    def __repr__(self):
        #lists off the trainers pokemon and shows which one is currently in battle
        print("{trainer} has the following pokemon:".format(trainer=self.trainer_name))
        for pokemon in pokemon_list:
            print(pokemon)
        return "{pokemon} is currently in battle.".format(pokemon=self.pokemon_list[self.current_pokemon].name)

    def use_potion(self):
        #makes sure that the trainer has enough potions before using them, then increases the health of the current pokemon
        potion = self.max_health * .40
        if self.potions > 0:
            print("{trainer} used a potion on {pokemon}.".format(trainer=self.trainer_name, pokemon=self.current_pokemon))
            self.current_pokemon.gain_health(potion)
            self.potions -= 1
        else:
            print("You don't have any potions left!")

    def attack_opposing_trainer(self, other_trainer):
        #finds the current pokemon and its opponent, and attacks the opponent
        opposing_pokemon = other_trainer.pokemon_list[other_trainer.current_pokemon]
        my_pokemon = self.pokemon_list[self.current_pokemon]
        my_pokemon.attack(opposing_pokemon)

    def switch_active_pokemon(self, new_active):
        #checks to make sure that the new_active value can be applied to the pokemon_list
        if new_active < len(self.pokemon_list) and new_active >= 0:
            #checks if the the pokemon is knocked out
            if self.pokemon_list[new_active].knocked_out:
                print("{pokemon} is knocked out! It's unable to enter the battle!".format(pokemon=self.pokemon_list[new_active].name))
            #checks whether the pokemon is already in battle
            elif self.current_pokemon == new_active:
                print("This pokemon is already in battle!")
            #switches in the new pokemon
            else:
                print("{new_active} has entered the battle!".format(new_active=self.current_pokemon[new_active].name))
                self.current_pokemon = new_active
