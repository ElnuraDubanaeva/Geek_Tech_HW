from enum import Enum
from random import randint, choice

round_number = 0
class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    STEAL = 5

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        chosen_hero = choice(heroes)
        self.__defence = chosen_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super(Boss, self).__str__() + f' defence: {self.defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super(Hero, self).__init__(name, health, damage)
        if not isinstance(ability, SuperAbility):
            raise ValueError('Value for attribute ability must be of type SuperAbility')
        else:
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = randint(1, 3)
        boss.health -= self.damage * coefficient
        print(f'Warrior hits critically: {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super(Magic, self).__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        n = randint(1, 3)
        for el in heroes:
            el.damage *= n
        print(f'Magic increases the attack of each heroes for {n} times')


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super(Witcher, self).__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.damage = 0

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0:
                hero.health = self.health
                self.health = 0
                print(f' Witcher gave live to {hero.name}')
                break


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super(Hacker, self).__init__(name, health, damage, SuperAbility.STEAL)


    def apply_super_power(self, boss, heroes):
        global round_number
        if round_number % 2 == 1:
            n = randint(10, 100)
            boss.health -= n
            for el in heroes:
                el.health += n
                print(f'Hacker took {n} from boss and gave it to {el.name} ')
                break

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super(Medic, self).__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_power(self, boss, heroes):
        saved_damage = boss.damage // 5
        self.health += saved_damage
        boss.health -= saved_damage
        print(f'Berserk saved {saved_damage}')





def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def print_statistics(boss, heroes):
    print(f'ROUND {round_number} -----------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if boss.defence != hero.ability and hero.health > 0:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss("Surtur", 1000, 50)
    warrior = Warrior("Spartak", 270, 1)
    doc = Medic("Merlin", 250, 5, 15)
    magic = Magic("Harry Potter", 2, 20)
    berserk = Berserk("Tor", 280, 15)
    assistant = Medic("Stajer", 290, 10, 5)
    witcher = Witcher('Witch', 340, 45)
    hacker = Hacker('Hacker', 200, 40)
    heroes_list = [warrior, doc, magic, berserk, assistant, witcher, hacker]

    print_statistics(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
