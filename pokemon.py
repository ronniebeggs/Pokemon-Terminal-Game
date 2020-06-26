
#class Pokemon:
    #def __init__(self, name, level, type, max_health, current_health, status):
        #self.name = name
        #self.level = level
        #self.type = type
        #self.max_health = max_health
        #self.current_health = current_health
        #self.status = status

    #this method decreases a pokemons health after an attack
    #def lose_health(self, damage):
        #pass


    #def attack(self, type, max_health, current_health, other_pokemon):
        #other_pokemon.current_health = other_pokemon.max_health

char_type = 'fire'
bulb_type = 'grass'
squirt_type = 'water'
#the key is weak to its value
type_advantages = {'water':'grass', 'fire':'water', 'grass':'fire'}
char_weakness = type_advantages.get(char_type)
bulb_weakness = type_advantages.get(bulb_type)
squirt_weakness = type_advantages.get(squirt_type)
#print(char_weakness)


def attack(poke_type, poke_weakness, opponent_type, opponent_weakness):
    damage = 10
    if poke_weakness == opponent_type:
        damage = damage / 2
    elif poke_type == opponent_weakness:
        damage = damage * 2
    else:
        damage = damage
    return damage
char_v_bulb = attack(char_type, char_weakness, bulb_type, bulb_weakness)
#print(char_v_bulb)

char_v_squirt = attack(char_type, char_weakness, squirt_type, squirt_weakness)
#print(char_v_squirt)

char_v_char = attack(char_type, char_weakness, char_type, char_weakness)
#print(char_v_char)

max_health = 40
current_health = max_health
damage = attack(char_type, char_weakness, squirt_type, squirt_weakness)
current_health = current_health - damage
print(current_health)
