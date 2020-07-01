
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
        print("{name} just used a potion and gained {potion} hit points!".format(name=self.name, potion=amount))
        return self.current_health

    def lose_health(self, amount):
        #takes an amount of damage and applies it to the pokemon
        self.current_health -= amount
        print("{name} just got hit and lost {damage} hit points!".format(name=self.name, damage=amount))
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
