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
'fighting':['flying', 'psychic', 'fairy'], 'steel':['fighting', 'ground', 'fire'], 'psychic':['dark', 'bug', 'ghost'], 'poison':['ground', 'psychic'],
'bug':['flying', 'rock', 'fire'], 'dragon':['ice', 'dragon', 'fairy'], 'dark':['fighting', 'bug', 'fairy'], 'fairy':['poison', 'steel'],
'ghost':['ghost', 'dark'], '':[]
 }

#move power, type, name, category
flamethrower = [90, 'fire', "Flamethrower", 1]
fire_punch = [75, 'fire', "Fire Punch", 0]
giga_drain = [75, 'grass', "Giga Drain", 1]
solar_beam = [120, 'grass', "Solar Beam", 1]
energy_ball = [90, 'grass', "Energy Ball", 1]
aqua_tail = [90, 'water', "Aqua Tail", 0]
dive = [80, 'water', "Dive", 0]
sky_attack = [120, 'flying', "Sky Attack", 0]
fly = [90, 'flying', "Fly", 0]
thunderbolt = [90, 'electric', "Thunderbolt", 1]
earthquake = [100, 'ground', "Earthquake", 0]
stone_edge = [100, 'rock', "Stone Edge", 0]
ice_beam = [90, 'ice', "Ice Beam", 1]
avalanche = [60, 'ice', "Avalanche", 0]
body_slam = [85, 'normal', "Body Slam", 0]
slash = [70, 'normal', "Slash", 0]
strength = [80, 'normal', "Strength", 0]
dragon_claw = [80, 'dragon', "Dragon Claw", 0]
sludge_bomb = [90, 'poison', "Sludge Bomb", 1]
poison_jab = [80, 'poison', "Poison Jab", 0]
u_turn = [70, 'bug', "U-Turn", 0]
shadow_ball = [80, 'ghost', "Shadow Ball", 1]
steel_wing = [70, 'steel', "Steel Wing", 0]
psychic = [90, 'psychic', "Psychic", 1]
dazzling_gleam = [80, 'fairy', "Dazzling Gleam", 1]
dynamic_punch = [100, 'fighting', "Dynamic Punch", 0]
brick_break = [75, 'fighting', "Brick Break", 0]
throat_chop = [80, 'dark', "Throat Chop", 0]
bite = [60, 'dark', "Bite", 0]
protect = [None, 'normal', "Protect", 2]
recover = [None, 'normal', "Recover", 2]
rest = [None, 'normal', "Rest", 2]

class Pokemon:
    def __init__(self, name, types, base_hp, base_attack, base_defense, base_spatk, base_spdef, base_speed, move_list, level=100):
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
        self.sp_attackkst = (2*base_spatk) + 5
        self.sp_defensest = (2*base_spdef) + 5
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
            crit_random = random.randint(1, 30)
            #finds the info about the move
            power = move[0]
            movetype = move[1]
            movename = move[2]
            movecategory = move[3]
            #changes the modifiers based on type mathcups, criticals, and stab
            if movetype in opposing_pokemon.types:
                sametype = 0.5
            if crit_random == 6:
                critical = 2
            if movetype in self.types:
                stab = 1.3
            #cycles through opponent pokemon weakness' and advantages and creates a value depending on the frequency of the movetype
            type_counter = 0
            for type in opposing_pokemon.weakness:
                if movetype == type:
                    type_counter += 1
            for type in opposing_pokemon.advantage:
                if movetype == type:
                    type_counter -= 1
            #changes the type dis/advantage multiplier depending on the previous value
            if type_counter == -2:
                typeadv = 0.25
            elif type_counter == -1:
                typeadv = 0.5
            elif type_counter == 0:
                typeadv = 1
            elif type_counter == 1:
                typeadv = 2
            else:
                typeadv = 4
            #multiplies damage by the modifier and rounds the result
            modifier = stab * critical * typeadv * sametype
            if movecategory == 0:    #physical move
                unrounded_damage = (((((2 * self.level / 6) + 2) * power * self.attackst / opposing_pokemon.defensest) / 50) + 2) * modifier
            elif movecategory == 1:     #special move
                unrounded_damage = (((((2 * self.level / 6) + 2) * power * self.sp_attackkst / opposing_pokemon.sp_defensest) / 50) + 2) * modifier
            else:
                unrounded_damage = 0
                print("Special Move")
            damage = round(unrounded_damage, 0)
            print("\n{trainerpoke} attacked {oppo_poke} using {movename}!".format(trainerpoke=self.name, oppo_poke=opposing_pokemon.name, movename=movename))
            print("-{damage} hp".format(damage=damage))
            #prints the restult of the type matchup
            if critical == 2:
                print("Critical Hit!")
            if typeadv == 2 or typeadv == 4:
                print("It's Super Effective!")
            elif typeadv == 0.5 or typeadv == 0.25:
                print("It's Not Very Effective!")
            opposing_pokemon.lose_health(damage)

    def special_case_move(self, opposing_pokemon, move):
        pass



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

    def check_validity(self, input_choices, input_text, options):
        valid_option = False
        while valid_option == False:
            print(input_choices)
            try:
                decision = int(input(input_text))
            except:
                print("\n*Decision must be an Integer!")
                continue
            if decision in options:
                valid_option = True
            else:
                print("\n*Not a valid option! Try Again!")
                continue
        lst1.append(decision)

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
        print("{pokemon_name}   \t   |{bars}|".format(bars=bars, pokemon_name=self.pokemon_list[self.current_pokemon].name))

    def find_pokemon_remaining(self):
        pokemon_remaining = 0
        pokeball_icon = "("
        for index, pokemon in enumerate(self.pokemon_list):
            if pokemon.knocked_out == False:
                pokemon_remaining += 1
                pokeball_icon += "o"
            else:
                pokeball_icon += "ø"
            if index == (len(self.pokemon_list) - 1):
                break
            pokeball_icon += ":"
        pokeball_icon += ")"
        return self.trainer_name + " - " + pokeball_icon

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
            elif self.pokemon_list[pokemon_choice].knocked_out == True:
                print("\nYou are unable to use a potion on a pokemon that has fainted!")
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
                print("\n{old_active} was switched out.".format(old_active=self.pokemon_list[self.current_pokemon].name))
                print("{new_active} has entered the battle!".format(new_active=self.pokemon_list[new_active].name))
                self.current_pokemon = new_active


#instantiates each pokemon with stats, moves, types, and name
charizard = Pokemon("Charizard", ['fire', 'flying'], 78, 84, 78, 109, 85, 100, [flamethrower, fly, steel_wing])
venusaur = Pokemon("Venusaur", ['grass', 'poison'], 80, 82, 83, 100, 100, 80, [giga_drain, solar_beam, sludge_bomb])
blastoise = Pokemon("Blastoise", ['water', ''], 79, 83, 100, 85, 105, 78, [aqua_tail, ice_beam, bite])
pidgeot = Pokemon("Pidgeot", ['flying', 'normal'], 83, 80, 75, 70, 70, 101, [sky_attack, slash, u_turn])
jolteon = Pokemon("Jolteon", ['electric', ''], 65, 65, 60, 110, 95, 130, [thunderbolt, body_slam, shadow_ball])
nidoking = Pokemon("Nidoking", ['ground', 'poison'], 81, 102, 77, 85, 75, 85, [earthquake, stone_edge, poison_jab])
dragonite = Pokemon("Dragonite", ['dragon', 'flying'], 91, 134, 95, 100, 100, 80, [dragon_claw, sky_attack, fire_punch])
gengar = Pokemon("Gengar", ['ghost', 'poison'], 60, 65, 60, 130, 75, 110, [sludge_bomb, shadow_ball, giga_drain])
alakazam = Pokemon("Alakazam", ['psychic', ''], 55, 50, 45, 135, 95, 120, [psychic, dazzling_gleam, recover])
machamp = Pokemon("Machamp", ['fighting', ''], 90, 130, 80, 65, 85, 55, [dynamic_punch, strength, throat_chop])
snorlax = Pokemon("Snorlax", ['normal', ''], 160, 110, 65, 65, 110, 30, [body_slam, brick_break, rest])
cloyster = Pokemon("Cloyster", ['water', 'ice'], 50, 95, 180, 85, 45, 70, [avalanche, dive, protect])
#instantiates both trainers with pokemon lists, and potion counts
player1 = Trainer([blastoise, venusaur, charizard, pidgeot, machamp, nidoking], 2, 1, 1, "Red")
cpu = Trainer([dragonite, gengar, jolteon, snorlax, alakazam, cloyster], 0, 3, 0, "Blue")


def start_fight(trainer, other_trainer):
    #introduces the battle and the current pokemon
    print("\n{opponent} would like to battle! \n{opponent} sent out {other_pokemon}. \nYou sent {my_pokemon}.".format(opponent=other_trainer.trainer_name, other_pokemon=other_trainer.pokemon_list[other_trainer.current_pokemon], my_pokemon=trainer.pokemon_list[trainer.current_pokemon]))
    #creates a for loop that continues until either trainer loses
    end_fight = False
    while end_fight == False:

        #saves list of pokemon to a variable to be used multiple times
        current_list_pokemon = "\nList of Pokemon: \n1. {poke1} \t{poke1current}/{poke1max} \n2. {poke2} \t{poke2current}/{poke2max} \n3. {poke3} \t{poke3current}/{poke3max} \n4. {poke4} \t{poke4current}/{poke4max} \n5. {poke5} \t{poke5current}/{poke5max} \n6. {poke6} \t{poke6current}/{poke6max}".format(
        poke1=trainer.pokemon_list[0].name, poke1current=trainer.pokemon_list[0].current_health, poke1max=trainer.pokemon_list[0].max_health,
        poke2=trainer.pokemon_list[1].name, poke2current=trainer.pokemon_list[1].current_health, poke2max=trainer.pokemon_list[1].max_health,
        poke3=trainer.pokemon_list[2].name, poke3current=trainer.pokemon_list[2].current_health, poke3max=trainer.pokemon_list[2].max_health,
        poke4=trainer.pokemon_list[3].name, poke4current=trainer.pokemon_list[3].current_health, poke4max=trainer.pokemon_list[3].max_health,
        poke5=trainer.pokemon_list[4].name, poke5current=trainer.pokemon_list[4].current_health, poke5max=trainer.pokemon_list[4].max_health,
        poke6=trainer.pokemon_list[5].name, poke6current=trainer.pokemon_list[5].current_health, poke6max=trainer.pokemon_list[5].max_health
        )


        #CPU AND USER PRE-ROUND SWITCHES IF POKEMON HAS FAINTED:
        #checks to see if the current pokemon has fainted - if so, forces you to switch pokemon
        if trainer.pokemon_list[trainer.current_pokemon].knocked_out == True:
            #makes sure that the user makes a valid decision
            options = range(len(trainer.pokemon_list))
            while trainer.pokemon_list[trainer.current_pokemon].knocked_out == True:
                #if user input is not in a list of options, they are given the option to redo their input until it's valid
                print("\nCurrent Pokemon has fainted. Must be switched out.")
                print(current_list_pokemon)
                switch_decision = int(input("Switch to: "))
                if switch_decision not in options:
                    print("\n*Not a valid option! Try again!")
                trainer.switch_active_pokemon(switch_decision - 1)
        #if cpu current pokemon has fainted, it's forced to switch out
        if other_trainer.pokemon_list[other_trainer.current_pokemon].knocked_out == True:
            #takes a list of the trainer's weaknesses and loops through pokemon list to find a super effective matchup
            trainer_weaknesses = trainer.pokemon_list[trainer.current_pokemon].weakness
            find_othertrainer_switch = False
            for pokeindex, pokemon in enumerate(other_trainer.pokemon_list):
                #checks if either type of iterated pokemon creates a super effective matchup
                if pokemon.types[0] in trainer_weaknesses and pokemon.knocked_out == False:
                    other_trainer.switch_active_pokemon(pokeindex)
                    find_othertrainer_switch = True
                    break
                elif pokemon.types[1] in trainer_weaknesses and pokemon.knocked_out == False:
                    other_trainer.switch_active_pokemon(pokeindex)
                    find_othertrainer_switch = True
                    break
            #if they can't find a good matchup, it randomly choses an alive pokemon to switch in
            if find_othertrainer_switch == False:
                current_fainted = True
                while current_fainted == True:
                    random_switch = random.randint(1, len(other_trainer.pokemon_list))
                    if other_trainer.pokemon_list[random_switch - 1].knocked_out == True:
                        continue
                    else:
                        current_fainted = False
                other_trainer.switch_active_pokemon(random_switch - 1)


        #BEGINNING OF TURN:
        print("\n----------POKEMON BATTLE----------")
        print("{trainer1pokemon} \t {trainer2pokemon}\n".format(trainer1pokemon=trainer.find_pokemon_remaining(), trainer2pokemon=other_trainer.find_pokemon_remaining()))
        trainer.find_bars()
        other_trainer.find_bars()


        #CPU DECISION MAKING PROCESS:
        other_trainer_usepotion = False
        other_trainer_attack = False
        #if cpu current pokemon's health is below 1/4 of the max, it will use a potion
        potion_or_attack = random.randint(1, 3)
        if (other_trainer.pokemon_list[other_trainer.current_pokemon].current_health <= (other_trainer.pokemon_list[other_trainer.current_pokemon].max_health / 4)) and potion_or_attack == 2:
            if other_trainer.max_potions > 0:
                other_trainer_usepotion = True
        else:
            #takes each current cpu moves and tries to find one that has an advantage against the opponent
            other_trainer_attack = True
            find_supereffective_move = False
            for move_index, move in enumerate(other_trainer.pokemon_list[other_trainer.current_pokemon].move_list):
                if move[1] in trainer.pokemon_list[trainer.current_pokemon].weakness:
                    opponent_decision = move_index
                    find_supereffective_move = True
                    break
            #randomly choses an attack if it can't find an advantageous move
            if find_supereffective_move == False:
                opponent_decision = random.randint(1, len(other_trainer.pokemon_list[other_trainer.current_pokemon].move_list)) - 1


        #USER DECISION MAKING PROCESS:
        #starts by creating a loop that allows a back button to function
        #if the user inputs '0', it will restart the loop allowing the user to redo their decisions
        back_input = 0
        confirmed_option = False
        first_back = True
        while confirmed_option == False:
            back_button_pressed = False
            if first_back == False:
                print("<<< Back")
            print("----------------------------------")
            #gives you an attack, use potion, or switch pokemon option
            valid_option = False
            basic_options = (1, 2, 3)
            while valid_option == False:
                print("\n1. Attack \n2. Bag \n3. Switch Pokemon")
                try:
                    user_decision = int(input("What will you do: "))
                except:
                    print("\n*Decision must be an Integer!")
                    continue
                if user_decision in basic_options:
                    valid_option = True
                else:
                    print("\n*Not a valid option! Try Again!")
                    continue
            #gives you the attack options and executes them
            if user_decision == 1:
                print("")
                move_options = range(1, len(trainer.pokemon_list[trainer.current_pokemon].move_list) + 1)
                print(len(trainer.pokemon_list[trainer.current_pokemon].move_list) + 1)
                valid_option = False
                while valid_option == False:
                    for move_number, move in enumerate(trainer.pokemon_list[trainer.current_pokemon].move_list):
                        print(f"{move_number + 1}. {move[2]}")
                    try:
                        attack_decision = int(input("Which attack will you use: "))
                    except:
                        print("\n*Decision must be an Integer!")
                        continue
                    if attack_decision in move_options:
                        valid_option = True
                    elif attack_decision == back_input:
                        back_button_pressed = True
                        break
                    else:
                        print("\n*Not a valid option! Try Again!")
                        continue
            #opens bag to choose between potions and revives
            if user_decision == 2:
                bag_options = (1, 2, 3)
                valid_option = False
                while valid_option == False:
                    print(f"\n1. Potion \t {trainer.potions} \n2. Max Potion \t {trainer.max_potions} \n3. Revive \t {trainer.revives}")
                    try:
                        bag_decision = int(input("What item will you use: "))
                    except:
                        print("\n*Decision must be an Integer!")
                        continue
                    if bag_decision in bag_options:
                        valid_option = True
                    elif bag_decision == back_input:
                        back_button_pressed = True
                        break
                    else:
                        print("\n*Not a valid option! Try Again!")
                        continue
                pokeitem_options = range(1, len(trainer.pokemon_list) + 1)
                valid_option = False
                while valid_option == False:
                    print(current_list_pokemon)
                    try:
                        pokemon_choice = int(input("Use item on which pokemon: "))
                    except:
                        print("\n*Decision must be an Integer!")
                        continue
                    if pokemon_choice in pokeitem_options:
                        valid_option = True
                    elif pokemon_choice == back_input:
                        back_button_pressed = True
                        break
                    else:
                        print("\n*Not a valid option! Try Again!")
                        continue
            #gives you the switch pokemon option
            elif user_decision == 3:
                pokeswitch_options = range(1, len(trainer.pokemon_list) + 1)
                valid_option = False
                while valid_option == False:
                    print(current_list_pokemon)
                    try:
                        switch_decision = int(input("Switch pokemon: "))
                    except:
                        print("\n*Decision must be an Integer!")
                        continue
                    if switch_decision in pokeswitch_options:
                        valid_option = True
                    elif switch_decision == back_input:
                        back_button_pressed = True
                        break
                    else:
                        print("\n*Not a valid option! Try Again!")
                        continue
            if back_button_pressed == True:
                first_back = False
                continue
            confirmed_option = True


        #EXECUTION OF CPU AND USER DECISIONS:
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
                    #decides which attack the cpu will use depending on previous code
                    other_trainer.attack_opposing_trainer(trainer, other_trainer.pokemon_list[other_trainer.current_pokemon].move_list[opponent_decision])

        else:
            #checks to see if a potion was used, determining whether the cpu will attack
            if other_trainer_attack == True and other_trainer_usepotion == False:
                #randomly decides which attack the cpu will use
                other_trainer.attack_opposing_trainer(trainer, other_trainer.pokemon_list[other_trainer.current_pokemon].move_list[opponent_decision])
            #makes sure the currnet pokemon is alive, and hasn't already used a potion
            if trainer.pokemon_list[trainer.current_pokemon].knocked_out == False and trainer_dont_attack == False:
                trainer.attack_opposing_trainer(cpu, trainer.pokemon_list[trainer.current_pokemon].move_list[(attack_decision - 1)])


        #CHECKS WHETHER THE ROUND HAS ENDED:
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


    #END OF BATTLE MESSAGES:
    #displays winning or losing messages at the end of a battle, and randomly decides the prize money
    earnings = random.randint(200, 1000)
    if trainer.lost_fight == True:
        print("\nYou blacked out and paid your opponent ${earnings}....".format(earnings=earnings))
    if other_trainer.lost_fight == True:
        print("\n{trainer} has defeated {other_trainer}! \n{trainer} got ${earnings} for winning!".format(trainer=trainer.trainer_name, other_trainer=other_trainer.trainer_name, earnings=earnings))
    return "Thanks for Playing!"


print(start_fight(player1, cpu))

#blastoise = "blastoise"
#charizard = "charizard"

#current_list_pokemon = f"\nList of Pokemon: \n1. {blastoise} \n2. {charizard}"
#switch_input = "Switch pokemon: "
#pokeswitch_options = (1, 2)
#lst1 = []

#print(check_validity(current_list_pokemon, switch_input, pokeswitch_options))

#decision = lst1[0]
