
class Pokemon:
    type_advantages = {'water':'grass', 'fire':'water', 'grass':'fire'}

    def __init__(self, name, level, type, current_health, status):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level * 2
        self.current_health = current_health
        self.status = status

    def attack(type, opponent_type):
        poke_weakness = type_advantages.get(self.type)
        damage = 10
        if poke_weakness == opponent_type:
            damage = damage / 2
        elif poke_type == opponent_weakness:
            damage = damage * 2
        else:
            damage = damage
        return damage

    def lose_health():
        max_health = 40
        current_health = max_health
        damage = attack(char_type, char_weakness, squirt_type, squirt_weakness)
        current_health = current_health - damage
        return current_health

    def poke_status():
        if self.current_health <= 0:
            self.status = 0
            print("{} has fainted.".format(self.name))

char_type = 'fire'
bulb_type = 'grass'
squirt_type = 'water'
#the key is weak to its value
type_advantages = {'water':'grass', 'fire':'water', 'grass':'fire'}
char_weakness = type_advantages.get(char_type)
bulb_weakness = type_advantages.get(bulb_type)
squirt_weakness = type_advantages.get(squirt_type)
#print(char_weakness)

#instantiate char
char = Pokemon('Charmander', 5, 'fire', 10, 1)


#char_v_bulb = attack(char_type, char_weakness, bulb_type, bulb_weakness)
#print(char_v_bulb)

#char_v_squirt = attack(char_type, char_weakness, squirt_type, squirt_weakness)
#print(char_v_squirt)

#char_v_char = attack(char_type, char_weakness, char_type, char_weakness)
#print(char_v_char)
