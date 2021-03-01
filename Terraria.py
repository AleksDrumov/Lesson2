import random
def main_code():
    HP_player = 100
    #Все название монстров - настоящие айди(в майне)
    damage_to_player = 0
    damage_skeleton = 15
    damage_spider = 40
    damage_zombie = 5
    range_damage = range(1,21)
    range_mob = range(1,4)
    range_random_damage = random.choice(range_damage)
    range_random_mob = random.choice(range_mob)
    if range_random_mob == 1:
        damage_to_player = damage_skeleton * range_random_damage
    if range_random_mob == 2:
        damage_to_player = damage_spider * range_random_damage
    if range_random_mob == 3:
        damage_to_player = damage_zombie * range_random_damage
    remaining_HP = HP_player - damage_to_player
    if remaining_HP > 0:
        print('У тебя осталось',remaining_HP)
    else:
        print('You DIE')
or_3d_or_2d = input('3d или 2d?')
if or_3d_or_2d == '3д':
    print("Minecraft(он раньше(2009))")
    a = input('Играть?')
    if a == 'да':
        main_code()
    else:
        print('За что?(((((')
if or_3d_or_2d == '2д':
    print('Terraria(она позже(20011))')
    b = input('Играть?')
    if b == 'да':
        main_code()
    else:
        print('За что?(((((')





