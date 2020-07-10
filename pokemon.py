import random
#creates type dis/advantes for fire, water, and grass types
type_advantages = {'grass':'water', 'water':'fire', 'fire':'grass'}
type_disadvantages = {'water':'grass', 'fire':'water', 'grass':'fire'}

flamethrower = [90, 'fire']
giga_drain = [75, 'grass']
aqua_tail = [90, 'water']

class Pokemon:

    def __init__(self, name, type, base_hp, level=5):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = 110 + (2*base_hp)
        self.current_health = self.max_health
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

    def attack(self, opposing_pokemon, move):
        #checks to see if the pokemon is able to attack the opponent
        if self.knocked_out == True:
            print("This pokemon has fainted and is unable to attack!")

        else:
            critical = 1
            stab = 1
            typeadv = 1
            crit_random = random.randint(1, 20)

            power = move[0]
            movetype = move[1]

            if crit_random == 6:
                critical = 2
            if self.type == movetype:
                stab = 1.5
            if movetype == opposing_pokemon.weakness:
                typeadv = 2
            elif movetype == opposing_pokemon.advantage:
                typeadv = 0.5

            modifier = stab * critical * typeadv
            unrounded_damage = (((((2 * self.level / 5) + 2) * power * self.attackst / opposing_pokemon.defensest) / 50) + 2) * modifier
            damage = round(unrounded_damage, 0)

            print("{my_poke} attacked {oppo_poke} for {damage} damage.".format(my_poke=self.name, oppo_poke=opposing_pokemon.name, damage=damage))

            if typeadv == 2:
                print("It's Super Effective!")
            elif typeadv == 0.5:
                print("It's Not Very Effective!")

            opposing_pokemon.lose_health(damage)


class Charizard(Pokemon):
    def __init__(self, level, base_hp, base_attack, base_defense, base_speed, move_list):
        super().__init__("Charizard", 'fire', base_hp, level)
        self.attackst = (2*base_attack) + 5
        self.defensest = (2*base_defense) + 5
        self.speedst = (2*base_speed) + 5
        self.move_list = move_list


class Venusaur(Pokemon):
    def __init__(self, level, base_hp, base_attack, base_defense, base_speed, move_list):
        super().__init__("Venusaur", 'grass', base_hp, level)
        self.attackst = (2*base_attack) + 5
        self.defensest = (2*base_defense) + 5
        self.speedst = (2*base_speed) + 5
        self.move_list = move_list


class Blastoise(Pokemon):
    def __init__(self, level, base_hp, base_attack, base_defense, base_speed, move_list):
        super().__init__("Blastoise", 'water', base_hp, level)
        self.attackst = (2*base_attack) + 5
        self.defensest = (2*base_defense) + 5
        self.speedst = (2*base_speed) + 5
        self.move_list = move_list


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
        print("{pokemon} is currently in battle.".format(pokemon=self.pokemon_list[self.current_pokemon].name))
        return "-----"

    def use_potion(self):
        #makes sure that the trainer has enough potions before using them, then increases the health of the current pokemon
        potion = 20
        if self.pokemon_list[self.current_pokemon].current_health == self.pokemon_list[self.current_pokemon].max_health:
            print("You are unable to use a potion on a pokemon with max health!")
            print("-----")
        else:
            if self.potions > 0:
                print("{trainer} used a potion on {pokemon}.".format(trainer=self.trainer_name, pokemon=self.pokemon_list[self.current_pokemon].name))
                max_current_diff = (self.pokemon_list[self.current_pokemon].max_health - self.pokemon_list[self.current_pokemon].current_health)
                if max_current_diff < potion:
                    self.pokemon_list[self.current_pokemon].gain_health(max_current_diff)
                else:
                    self.pokemon_list[self.current_pokemon].gain_health(potion)
                self.potions -= 1
            else:
                print("You don't have any potions left!")
            print('-----')

    def attack_opposing_trainer(self, other_trainer, move):
        #finds the current pokemon and its opponent, and attacks the opponent
        opposing_pokemon = other_trainer.pokemon_list[other_trainer.current_pokemon]
        my_pokemon = self.pokemon_list[self.current_pokemon]

        if move in self.pokemon_list[self.current_pokemon].move_list:
            my_pokemon.attack(opposing_pokemon, move)
            print('-----')

        else:
            print("This pokemon doesn't have that move!")
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


charizard = Charizard(100, 80, 84, 78, 100, [flamethrower])
venusaur = Venusaur(100, 78, 82, 83, 80, [giga_drain])
blastoise = Blastoise(100, 79, 83, 100, 78, [aqua_tail])

red = Trainer([charizard], 3, "Red")
steven = Trainer([venusaur, blastoise], 3, "Steven")

print(red)
print(steven)

red.attack_opposing_trainer(steven, flamethrower)
steven.attack_opposing_trainer(red, giga_drain)
red.attack_opposing_trainer(steven, flamethrower)
steven.switch_active_pokemon(1)
steven.attack_opposing_trainer(red, aqua_tail)
