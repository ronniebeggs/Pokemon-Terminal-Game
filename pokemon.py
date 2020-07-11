import random

#creates type dis/advantes for fire, water, and grass types
type_advantages = {
'grass':['water', 'ground', 'rock'], 'water':['fire', 'ground', 'rock'], 'fire':['grass', 'ice'],
'electric':['flying', 'water'], 'flying':['grass'], 'ground':['fire', 'electric', 'rock'],
'ice':['flying', 'ground', 'grass'], 'rock':['flying', 'fire', 'ice'], 'normal':[]
}
type_disadvantages = {
'water':['grass', 'electric'], 'fire':['water', 'ground', 'rock'], 'grass':['fire', 'flying', 'ice'],
'electric':['ground'], 'flying':['electric', 'rock', 'ice'], 'ground':['grass', 'water', 'ice'],
'ice':['rock', 'fire'], 'rock':['ground', 'water', 'grass'], 'normal':[]
 }

flamethrower = [90, 'fire', "Flamethrower"]
giga_drain = [75, 'grass', "Giga Drain"]
aqua_tail = [90, 'water', "Aqua Tail"]
sky_attack = [100, 'flying', "Sky Attack"]
fly = [90, 'flying', "Fly"]
discharge = [80, 'electric', "Discharge"]
dig = [80, 'ground', "Dig"]
ice_beam = [90, 'ice', "Ice Beam"]
stone_edge = [100, 'rock', "Stone Edge"]
body_slam = [85, 'normal', "Body Slam"]
slash = [70, 'normal', "Slash"]
solar_beam = [120, 'grass', "Solar Beam"]

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
        return "the {type} type pokemon {name}, with {hp} hit points remaining".format(type=self.type, name=self.name, hp=self.current_health)

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
            #sets each modifier at 1
            critical = 1
            stab = 1
            typeadv = 1
            crit_random = random.randint(1, 20)
            #finds the info about the move
            power = move[0]
            movetype = move[1]
            #changes the modifiers based on type mathcups, criticals, and stab
            if crit_random == 6:
                critical = 2
            if self.type == movetype:
                stab = 1.5
            if movetype in opposing_pokemon.weakness:
                typeadv = 2
            elif movetype in opposing_pokemon.advantage:
                typeadv = 0.5
            #multiplies damage by the modifier and rounds the result
            modifier = stab * critical * typeadv
            unrounded_damage = (((((2 * self.level / 5) + 2) * power * self.attackst / opposing_pokemon.defensest) / 50) + 2) * modifier
            damage = round(unrounded_damage, 0)
            print("{my_poke} attacked {oppo_poke} for {damage} damage.".format(my_poke=self.name, oppo_poke=opposing_pokemon.name, damage=damage))
            #prints the restult of the type matchup
            if typeadv == 2:
                print("It's Super Effective!")
            elif typeadv == 0.5:
                print("It's Not Very Effective!")
            opposing_pokemon.lose_health(damage)


#creates subclasses for each pokemon including base stats and a move list
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

class Pidgeot(Pokemon):
    def __init__(self, level, base_hp, base_attack, base_defense, base_speed, move_list):
        super().__init__("Pidgeot", 'flying', base_hp, level)
        self.attackst = (2*base_attack) + 5
        self.defensest = (2*base_defense) + 5
        self.speedst = (2*base_speed) + 5
        self.move_list = move_list

class Jolteon(Pokemon):
    def __init__(self, level, base_hp, base_attack, base_defense, base_speed, move_list):
        super().__init__("Jolteon", 'electric', base_hp, level)
        self.attackst = (2*base_attack) + 5
        self.defensest = (2*base_defense) + 5
        self.speedst = (2*base_speed) + 5
        self.move_list = move_list

class Nidoking(Pokemon):
    def __init__(self, level, base_hp, base_attack, base_defense, base_speed, move_list):
        super().__init__("Nidoking", 'ground', base_hp, level)
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
        self.lost_fight = False

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
        #finds the current pokemon and its opponent
        opposing_pokemon = other_trainer.pokemon_list[other_trainer.current_pokemon]
        my_pokemon = self.pokemon_list[self.current_pokemon]
        #makes sure the active pokemon has the move in its list, and attacks with it
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

    def lose_fight(self, other_trainer):
        faint_counter = 0
        for pokemon in range(len(self.pokemon_list - 1)):
            if self.pokemon_list[pokemon].knocked_out == True:
                faint_counter += 1
        if faint_counter == len(self.pokemon_list):
            print("You blacked out and paid your opponent $682.")
            lose_fight = True



charizard = Charizard(100, 80, 84, 78, 100, [flamethrower, fly])
venusaur = Venusaur(100, 78, 82, 83, 80, [giga_drain, solar_beam])
blastoise = Blastoise(100, 79, 83, 100, 78, [aqua_tail, ice_beam])
pidgeot = Pidgeot(100, 83, 80, 75, 101, [sky_attack, slash])
jolteon = Jolteon(100, 65, 65, 60, 130, [discharge, body_slam])
nidoking = Nidoking(100, 81, 102, 77, 85, [dig, stone_edge])

trainer1 = Trainer([pidgeot, blastoise, nidoking], 3, "Red")
cpu = Trainer([venusaur, jolteon, charizard], 3, "Steven")


def start_fight(trainer, other_trainer):
    #introduces the battle and the current pokemon
    print("{opponent} would like to battle! \n{opponent} sent out {pokemon}.".format(opponent=other_trainer.trainer_name, pokemon=other_trainer.pokemon_list[other_trainer.current_pokemon]))
    print("You sent {pokemon}.".format(pokemon=trainer.pokemon_list[trainer.current_pokemon]))
    #creates a for loop that continues until either trainer loses
    while trainer.lost_fight == False or other_trainer.lostfight == False:
        #checks to see if the current pokemon has fainted - if so, forces you to switch pokemon
        if trainer.pokemon_list[trainer.current_pokemon].knocked_out == True:
            print("Current List of Pokemon: \n1. {poke_1} \n2. {poke_2} \n3. {poke_3} \n-----".format(poke_1=trainer.pokemon_list[0].name, poke_2=trainer.pokemon_list[1].name, poke_3=trainer.pokemon_list[2].name))
            switch_decision1 = int(input())
            trainer.switch_active_pokemon(switch_decision1 - 1)
        #gives you an attack, use potion, or switch pokemon option
        print("What will you do? \n1. Attack \n2. Use Potion \n3. Switch Pokemon \n-----")
        user_decision1 = int(input())
        #checks to see if the input is valid and allows you to redo your input
        if user_decision1 > 3:
            print("Not an option! Try Again!")
            user_decision1 = int(input())
        #gives you the attack options and executes them
        if user_decision1 == 1:
            print("Which attack will you use? \n1. {first_move} \n2. {second_move} \n-----".format(first_move=trainer.pokemon_list[trainer.current_pokemon].move_list[0][2], second_move=trainer.pokemon_list[trainer.current_pokemon].move_list[1][2]))
            attack_decision1 = int(input())
            trainer.attack_opposing_trainer(cpu, trainer.pokemon_list[trainer.current_pokemon].move_list[(attack_decision1 - 1)])
        #gives you the use potion option
        elif user_decision1 == 2:
            trainer.use_potion()
        #gives you the switch pokemon option
        elif user_decision1 == 3:
            print("Current List of Pokemon: \n1. {poke_1} \n2. {poke_2} \n3. {poke_3} \n-----".format(poke_1=trainer.pokemon_list[0].name, poke_2=trainer.pokemon_list[1].name, poke_3=trainer.pokemon_list[2].name))
            switch_decision1 = int(input())
            trainer.switch_active_pokemon(switch_decision1 - 1)



print(start_fight(trainer1, cpu))
