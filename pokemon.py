import random
import time
import sys
def delayed_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    time.sleep(0.50)

#creates type dis/advantes for fire, water, and grass types
type_advantages = {
'grass':['water', 'ground', 'rock'], 'water':['fire', 'ground', 'rock'], 'fire':['grass', 'ice', 'bug', 'steel'],
'electric':['flying', 'water'], 'flying':['grass', 'fighting', 'bug'], 'ground':['fire', 'electric', 'rock', 'poison', 'steel'],
'ice':['flying', 'ground', 'grass', 'dragon'], 'rock':['flying', 'fire', 'ice', 'bug'], 'normal':[], 'fighting':['normal', 'rock', 'ice', 'steel', 'dark'],
'steel':['rock', 'ice', 'fairy'], 'psychic':['fighting', 'poison'], 'poison':['grass', 'fairy'], 'bug':['grass', 'psychic', 'dark'],
'dragon':['dragon'], 'dark':['ghost', 'psychic'], 'fairy':['fighting', 'dragon', 'dark'], 'ghost':['ghost', 'psychic'], '':[]
}
type_disadvantages = {
'water':['grass', 'electric'], 'fire':['water', 'ground', 'rock'], 'grass':['fire', 'flying', 'ice', 'poison', 'bug'],
'electric':['ground'], 'flying':['electric', 'rock', 'ice'], 'ground':['grass', 'water', 'ice'],
'ice':['rock', 'fire', 'fighting', 'steel'], 'rock':['ground', 'water', 'grass', 'fighting', 'steel'], 'normal':['fighting'],
'fighting':['flying'], 'steel':['fighting', 'ground', 'fire'], 'psychic':['dark', 'bug', 'ghost'], 'poison':['ground', 'psychic'],
'bug':['flying', 'rock', 'fire'], 'dragon':['ice', 'dragon', 'fairy'], 'dark':['fighting', 'bug', 'fairy'], 'fairy':['poison', 'steel'],
'ghost':['ghost', 'dark'], '':[]
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
    def __init__(self, name, types, base_hp, base_attack, base_defense, base_speed, move_list, level=5):
        self.name = name
        self.level = level
        self.types = types
        self.max_health = 110 + (2*base_hp)
        self.current_health = self.max_health
        self.knocked_out = False
        self.weakness = type_disadvantages.get(types[0]) + type_disadvantages.get(types[1])
        self.advantage = type_advantages.get(types[0]) + type_advantages.get(types[1])
        self.attackst = (2*base_attack) + 5
        self.defensest = (2*base_defense) + 5
        self.speedst = (2*base_speed) + 5
        self.move_list = move_list

    def __repr__(self):
        #printing a pokemon displays its name, type, level, and its hit points
        return "the {type1} type pokemon {name}, with {hp} hit points remaining".format(type1=self.types[0], name=self.name, hp=self.current_health)

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
            print("\n{} has fainted.".format(self.name))

    def revive(self):
        #checks to make sure that the pokemon is knocked out before reviving it
        if self.current_health <= 0 and self.knocked_out == True:
            self.knocked_out = False
            self.current_health += (self.max_health / 2)
            print("\n{name} was revived!".format(name=self.name))

    def attack(self, opposing_pokemon, move):
        #checks to see if the pokemon is able to attack the opponent
        if self.knocked_out == True:
            print("\nThis pokemon has fainted and is unable to attack!")
        else:
            #sets each modifier at 1
            critical = 1
            stab = 1
            typeadv = 1
            sametype = 1
            crit_random = random.randint(1, 20)
            #finds the info about the move
            power = move[0]
            movetype = move[1]
            movename = move[2]
            #changes the modifiers based on type mathcups, criticals, and stab
            if movetype in opposing_pokemon.types:
                sametype = 0.5
            if crit_random == 6:
                critical = 2
            if movetype in self.types:
                stab = 1.5
            if movetype in opposing_pokemon.weakness:
                typeadv = 2
            elif movetype in opposing_pokemon.advantage:
                typeadv = 0.5
            #multiplies damage by the modifier and rounds the result
            modifier = stab * critical * typeadv * sametype
            unrounded_damage = (((((2 * self.level / 5) + 2) * power * self.attackst / opposing_pokemon.defensest) / 50) + 2) * modifier
            damage = round(unrounded_damage, 0)
            print("\n{trainerpoke} attacked {oppo_poke} using {movename}!".format(trainerpoke=self.name, oppo_poke=opposing_pokemon.name, movename=movename))
            print("-{damage} hp".format(damage=damage))
            #prints the restult of the type matchup
            if critical == 2:
                print("Critical Hit!")
            if typeadv == 2:
                print("It's Super Effective!")
            elif typeadv == 0.5:
                print("It's Not Very Effective!")
            opposing_pokemon.lose_health(damage)


class Trainer:
    def __init__(self, pokemon_list, potions, max_potions, revives, trainer_name):
        self.pokemon_list = pokemon_list
        self.potions = potions
        self.max_potions = max_potions
        self.revives = revives
        self.trainer_name = trainer_name
        self.current_pokemon = 0
        self.lost_fight = False

    def __repr__(self):
        #lists off the trainers pokemon and shows which one is currently in battle
        print("{trainer} has the following pokemon:".format(trainer=self.trainer_name))
        for pokemon in self.pokemon_list:
            print(pokemon)
        print("{pokemon} is currently in battle.".format(pokemon=self.pokemon_list[self.current_pokemon].name))

    def find_bars(self):
        bar_increments = (self.pokemon_list[self.current_pokemon].max_health / 20)
        num_of_bars = round(int(self.pokemon_list[self.current_pokemon].current_health / bar_increments), 0)
        bars = ""
        for i in range(num_of_bars):
            bars += "="
        lenbars = len(bars)
        whitespace_bars = 20 - lenbars
        if lenbars < 20:
            for i in range(whitespace_bars):
                bars += " "
        print("{pokemon_name} \t|{bars}|".format(bars=bars, pokemon_name=self.pokemon_list[self.current_pokemon].name))

    def open_bag(self, raw_choice, bag_decision):
        #makes sure that the trainer has enough potions before using them, then increases the health of the current pokemon
        potion = 50
        pokemon_choice = raw_choice - 1
        if bag_decision == 3:
            if self.pokemon_list[pokemon_choice].knocked_out == True:
                self.pokemon_list[pokemon_choice].revive()
                self.revives -= 1
            else:
                print("\nYou are unable to use a revive on a pokemon that is still alive!")
        else:
            if self.pokemon_list[pokemon_choice].current_health == self.pokemon_list[pokemon_choice].max_health:
                print("\nYou are unable to use a potion on a pokemon with max health!")
            else:
                if bag_decision == 1 and self.potions > 0:
                    print("\n{trainer} used a potion on {pokemon}.".format(trainer=self.trainer_name, pokemon=self.pokemon_list[pokemon_choice].name))
                    max_current_diff = (self.pokemon_list[pokemon_choice].max_health - self.pokemon_list[pokemon_choice].current_health)
                    if max_current_diff < potion:
                        self.pokemon_list[pokemon_choice].gain_health(max_current_diff)
                    else:
                        self.pokemon_list[pokemon_choice].gain_health(potion)
                    self.potions -= 1
                elif bag_decision == 1 and self.potions == 0:
                    print("\nYou don't have any potions left!")
                if bag_decision == 2 and self.max_potions > 0:
                    print("\n{trainer} used a max potion on {pokemon}.".format(trainer=self.trainer_name, pokemon=self.pokemon_list[pokemon_choice].name))
                    max_current_diff = (self.pokemon_list[pokemon_choice].max_health - self.pokemon_list[pokemon_choice].current_health)
                    self.pokemon_list[pokemon_choice].gain_health(max_current_diff)
                    self.max_potions -= 1
                elif bag_decision == 2 and self.max_potions == 0:
                    print("\nYou don't have any potions left!")

    def attack_opposing_trainer(self, other_trainer, move):
        #finds the current pokemon and its opponent
        opposing_pokemon = other_trainer.pokemon_list[other_trainer.current_pokemon]
        my_pokemon = self.pokemon_list[self.current_pokemon]
        #makes sure the active pokemon has the move in its list, and attacks with it
        if move in self.pokemon_list[self.current_pokemon].move_list:
            my_pokemon.attack(opposing_pokemon, move)
        else:
            print("\nThis pokemon doesn't have that move!")

    def switch_active_pokemon(self, new_active):
        #checks to make sure that the new_active value can be applied to the pokemon_list
        if new_active < len(self.pokemon_list) and new_active >= 0:
            #checks if the the pokemon is knocked out
            if self.pokemon_list[new_active].knocked_out:
                print("\n{pokemon} is knocked out! It is unable to enter the battle!".format(pokemon=self.pokemon_list[new_active].name))
            #checks whether the pokemon is already in battle
            elif self.current_pokemon == new_active:
                print("\n{pokemon} is already in battle!".format(pokemon=self.pokemon_list[new_active].name))
            #switches in the new pokemon
            else:
                print("{old_active} was switched out.".format(old_active=self.pokemon_list[self.current_pokemon].name))
                print("{new_active} has entered the battle!".format(new_active=self.pokemon_list[new_active].name))
                self.current_pokemon = new_active


charizard = Pokemon("Charizard", ['fire', 'flying'], 80, 84, 78, 100, [flamethrower, fly], 100)
venusaur = Pokemon("Venusaur", ['grass', 'poison'], 78, 82, 83, 80, [giga_drain, solar_beam], 100)
blastoise = Pokemon("Blastoise", ['water', ''], 79, 83, 100, 78, [aqua_tail, ice_beam], 100)
pidgeot = Pokemon("Pidgeot", ['flying', 'normal'], 83, 80, 75, 101, [sky_attack, slash], 100)
jolteon = Pokemon("Jolteon", ['electric', ''], 65, 65, 60, 130, [discharge, body_slam], 100)
nidoking = Pokemon("Nidoking", ['ground', 'poison'], 81, 102, 77, 85, [dig, stone_edge], 100)
dragonite = Pokemon("Dragonite", ['dragon', 'flying'], 91, 134, 95, 80, [], 100)
gengar = Pokemon("Gengar", ['ghost', 'poison'], 60, 65, 60, 110, [], 100)
alakazam = Pokemon("Alakazam", ['psychic', ''], 55, 50, 45, 120, [], 100)
machamp = Pokemon("Machamp", ['fighting', ''], 90, 130, 80, 55, [], 100)
magneton = Pokemon("Magneton", ['electric', 'steel'], 50, 60, 95, 70, [], 100)

player1 = Trainer([pidgeot, blastoise, nidoking], 2, 1, 1, "Red")
cpu = Trainer([venusaur, jolteon, charizard], 0, 3, 0, "Steven")


def start_fight(trainer, other_trainer):
    #introduces the battle and the current pokemon
    print("\n{opponent} would like to battle! \n{opponent} sent out {other_pokemon}. \nYou sent {my_pokemon}.".format(opponent=other_trainer.trainer_name, other_pokemon=other_trainer.pokemon_list[other_trainer.current_pokemon], my_pokemon=trainer.pokemon_list[trainer.current_pokemon]))
    #creates a for loop that continues until either trainer loses
    end_fight = False
    while end_fight == False:
        current_list_pokemon = "\nList of Pokemon: \n1. {poke1} \t{poke1current}/{poke1max} \n2. {poke2} \t{poke2current}/{poke2max} \n3. {poke3} \t{poke3current}/{poke3max}".format(poke1=trainer.pokemon_list[0].name,
        poke2=trainer.pokemon_list[1].name, poke3=trainer.pokemon_list[2].name, poke1current=trainer.pokemon_list[0].current_health,
        poke2current=trainer.pokemon_list[1].current_health, poke3current=trainer.pokemon_list[2].current_health,
        poke1max=trainer.pokemon_list[0].max_health, poke2max=trainer.pokemon_list[1].max_health, poke3max=trainer.pokemon_list[2].max_health)
        #checks to see if the current pokemon has fainted - if so, forces you to switch pokemon
        if trainer.pokemon_list[trainer.current_pokemon].knocked_out == True:
            #makes sure that the user makes a valid decision
            options = (1, 2, 3)
            while trainer.pokemon_list[trainer.current_pokemon].knocked_out == True:
                print("\nCurrent Pokemon has fainted. Must be switched out.")
                print(current_list_pokemon)
                switch_decision = int(input("Switch to: "))
                if switch_decision not in options:
                    print("\n*Not a valid option! Try again!")
                trainer.switch_active_pokemon(switch_decision - 1)

        #if cpu current pokemon has fainted, it forces it to switch out
        #if one of the cpu's pokemon is super effective against trainer1, it switches to that one
        if other_trainer.pokemon_list[other_trainer.current_pokemon].knocked_out == True:
            trainer_weaknesses = trainer.pokemon_list[trainer.current_pokemon].weakness
            for pokemon in other_trainer.pokemon_list:
                if pokemon.types[0] in trainer_weaknesses and pokemon.knocked_out == False:
                    pokeindex = other_trainer.pokemon_list.index(pokemon)
                    other_trainer.switch_active_pokemon(pokeindex)
                    break
                elif pokemon.types[1] in trainer_weaknesses and pokemon.knocked_out == False:
                    pokeindex = other_trainer.pokemon_list.index(pokemon)
                    other_trainer.switch_active_pokemon(pokeindex)
                    break
                #if none of the cpus pokemon are super effective against trainer1, it makes a random switch to any pokemon that hasn't fainted
                elif pokemon.types not in trainer_weaknesses and pokemon.knocked_out == False:
                    pokeindex = other_trainer.pokemon_list.index(pokemon)
                    other_trainer.switch_active_pokemon(pokeindex)
                    break

        print("\n----------POKEMON BATTLE----------\n")
        trainer.find_bars()
        other_trainer.find_bars()

        #gives you an attack, use potion, or switch pokemon option
        valid_option = False
        while valid_option == False:
            options = (1, 2, 3)
            print("\n1. Attack \n2. Bag \n3. Switch Pokemon")
            user_decision = int(input("What will you do: "))
            if user_decision in options:
                valid_option = True
            else:
                print("\n*Not a valid option! Try Again!")

        #gives you the attack options and executes them
        if user_decision == 1:
            print("\n1. {first_move} \n2. {second_move}".format(first_move=trainer.pokemon_list[trainer.current_pokemon].move_list[0][2], second_move=trainer.pokemon_list[trainer.current_pokemon].move_list[1][2]))
            attack_decision = int(input("Which attack will you use: "))
            options = (1, 2)
            if attack_decision not in options:
                valid_option = False
                while valid_option == False:
                    print("\n*Not a valid option! Try Again!")
                    print("\n1. {first_move} \n2. {second_move}".format(first_move=trainer.pokemon_list[trainer.current_pokemon].move_list[0][2], second_move=trainer.pokemon_list[trainer.current_pokemon].move_list[1][2]))
                    attack_decision = int(input("Which attack will you use: "))
                    if attack_decision in options:
                        valid_option = True
        #opens bag to choose between potions and revives
        if user_decision == 2:
            print("\n1. Potion \t {potions} \n2. Max Potion \t {max_potions} \n3. Revive \t {revives}".format(potions=trainer.potions, max_potions=trainer.max_potions, revives=trainer.revives))
            bag_decision = int(input("Use: "))
            if bag_decision not in options:
                valid_option = False
                while valid_option == False:
                    print("\n*Not a valid option! Try Again!")
                    print("\n1. Potion \n2. Max Potion \n3. Revive")
                    user_decision = int(input("Use: "))
                    if user_decision in options:
                        valid_option = True
            print(current_list_pokemon)
            pokemon_choice = int(input("On which pokemon: "))
            if bag_decision not in options:
                valid_option = False
                while valid_option == False:
                    print("\n*Not a valid option! Try Again!")
                    print(current_list_pokemon)
                    user_decision = int(input("On which pokemon: "))
                    if user_decision in options:
                        valid_option = True
        #gives you the switch pokemon option
        elif user_decision == 3:
            print(current_list_pokemon)
            switch_decision = int(input("Switch to: "))
            options = (1, 2, 3)
            #checks to see if the decision is valid, if not, they are forced to change it
            if switch_decision not in options:
                valid_option = False
                while valid_option == False:
                    print("\n*Not a valid option! Try Again!")
                    print(current_list_pokemon)
                    switch_decision = int(input("Switch to: "))
                    if switch_decision in options:
                        valid_option = True

        other_trainer_usepotion = False
        other_trainer_attack = False
        if other_trainer.pokemon_list[other_trainer.current_pokemon].knocked_out == False:
            #if cpu current pokemon's health is below 1/4 of the max, it will use a potion - else: will attack with random decision
            if (other_trainer.pokemon_list[other_trainer.current_pokemon].current_health <= (other_trainer.pokemon_list[other_trainer.current_pokemon].max_health / 4)) and other_trainer.pokemon_list[other_trainer.current_pokemon].knocked_out == False:
                if other_trainer.max_potions > 0:
                    potion_or_attack = random.randint(1, 3)
                    if potion_or_attack == 2:
                        other_trainer_usepotion = True
                    else:
                        other_trainer_attack = True
                else:
                    other_trainer_attack = True
            else:
                other_trainer_attack = True

        #performs use_potions and switches at the beginning of a turn
        trainer_dont_attack = False
        if user_decision == 2:
            trainer.open_bag(pokemon_choice, bag_decision)
            trainer_dont_attack = True
        if user_decision == 3:
            trainer.switch_active_pokemon(switch_decision - 1)
            trainer_dont_attack = True
        if other_trainer_usepotion == True:
            other_trainer.open_bag(other_trainer.current_pokemon + 1, 2)

        #compares speed of current pokemon to determine who attacks first
        #if their speed is equal, trainer1 attacks first
        if trainer.pokemon_list[trainer.current_pokemon].speedst >= other_trainer.pokemon_list[other_trainer.current_pokemon].speedst:
            if user_decision == 1 and trainer_dont_attack == False:
                trainer.attack_opposing_trainer(cpu, trainer.pokemon_list[trainer.current_pokemon].move_list[(attack_decision - 1)])

            #checks to make sure that the current pokemon hasn't fainted
            if other_trainer.pokemon_list[other_trainer.current_pokemon].knocked_out == False:
                #checks to see if a potion was used
                if other_trainer_attack == True and other_trainer_usepotion == False:
                    #randomly decides which attack the cpu will use
                    opponent_decision = random.randint(1, len(other_trainer.pokemon_list[other_trainer.current_pokemon].move_list))
                    other_trainer.attack_opposing_trainer(trainer, other_trainer.pokemon_list[other_trainer.current_pokemon].move_list[opponent_decision - 1])

        else:
            #checks to see if a potion was used, determining whether the cpu will attack
            if other_trainer_attack == True and other_trainer_usepotion == False:
                #randomly decides which attack the cpu will use
                opponent_decision = random.randint(1, len(other_trainer.pokemon_list[other_trainer.current_pokemon].move_list))
                other_trainer.attack_opposing_trainer(trainer, other_trainer.pokemon_list[other_trainer.current_pokemon].move_list[opponent_decision - 1])

            #makes sure the currnet pokemon is alive, and hasn't already used a potion
            if trainer.pokemon_list[trainer.current_pokemon].knocked_out == False and trainer_dont_attack == False:
                trainer.attack_opposing_trainer(cpu, trainer.pokemon_list[trainer.current_pokemon].move_list[(attack_decision - 1)])

        #if all pokemon have fainted on either side, the fight ends
        faint_counter = 0
        for pokemon in trainer.pokemon_list:
            if pokemon.knocked_out == True:
                faint_counter += 1
        if faint_counter == len(trainer.pokemon_list):
            trainer.lost_fight = True
            end_fight = True
        faint_counter = 0
        for pokemon in other_trainer.pokemon_list:
            if pokemon.knocked_out == True:
                faint_counter += 1
        if faint_counter == len(other_trainer.pokemon_list):
            other_trainer.lost_fight = True
            end_fight = True

    #displays winning or losing messages at the end of a battle, and randomly decides the prize money
    earnings = random.randint(200, 1000)
    if trainer.lost_fight == True:
        print("\nYou blacked out and paid your opponent ${earnings}....".format(earnings=earnings))
    if other_trainer.lost_fight == True:
        print("\n{trainer} has defeated {other_trainer}! \n{trainer} got ${earnings} for winning!".format(trainer=trainer.trainer_name, other_trainer=other_trainer.trainer_name, earnings=earnings))
    return "Thanks for Playing!"

print(start_fight(player1, cpu))
