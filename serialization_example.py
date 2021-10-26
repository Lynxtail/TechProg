import json
import random

class CustomEncoder(json.JSONEncoder):
     def default(self, o):
        if isinstance(o, Protagonist):
             return {'__protagonist__': vars(o)}
        elif isinstance(o, Enemy):
             return {'__enemy__': vars(o)}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}
         

class Creature:
    _name = ''
    _hp = 0
    _mana = 0
    _target = None
    _money = 0
    _equipment = {'head':'',
                'body':'',
                'weapon':''}
    _location = ''

    def __init__(self, name, hp, mana, money, equipment_head, equipment_body, equipment_weapon):
        self._name = name
        self._hp = hp
        self._mana = mana
        self._money = money
        self._equipment['head'] = equipment_head
        self._equipment['body'] = equipment_body
        self._equipment['weapon'] = equipment_weapon
    
    def spawn(self):
        self._location = random.choice(['Village', 'Town', 'Field', 'Inn', 'Ship'])

    def deal_damage(self):
        return round(random.random() * 100)

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, obj):
        self._target = obj
    
class Protagonist(Creature):
    _main_ability_name = ''
    _main_ability_modifier = 0
    def __init__(self, name, hp, mana, money, equipment_head, equipment_body, equipment_weapon, ability):
        super().__init__(name, hp, mana, money, equipment_head, equipment_body, equipment_weapon)
        self._main_ability_name = ability
    
    @property
    def ability_params(self):
        return f'{self._main_ability_name} - +{self._main_ability_modifier} to damage'

    @ability_params.setter
    def ability_params(self, mod):
        self._main_ability_modifier = mod

    def cast_ability(self):
        if self._mana > 0:
            self._mana -= 1
            print(f"{self._name} casts {self._main_ability_name} on {self.target._name}")
            dmg = self.deal_damage()
            if self.target._hp - dmg > 0:
                self.target._hp -= dmg
                print(f'Deal {dmg} to {self.target._name} - now {self.target._name} have {self.target._hp} hit points')
            else:
                self.target._hp = 0
                print(f'Deal {dmg} to {self.target._name} - {self.target._name} has been killed')
        else:
            print(f"{self._name} haven't enough mana!")

    def deal_damage(self):
        return super().deal_damage() + self._main_ability_modifier

class Enemy(Creature):
    
    def punch(self):
        print(f"{self._name} attacks {self.target._name}")
        dmg = self.deal_damage()
        if self.target._hp - dmg > 0:
            self.target._hp -= dmg
            print(f'Deal {dmg} to {self.target._name} - now {self.target._name} have {self.target._hp} hit points')
        else:
            self.target._hp = 0
            print(f'Deal {dmg} to {self.target._name} - {self.target._name} has been killed')

if __name__ == '__main__':
    serialized = []
    henry = Protagonist('Henry', 10, 10, 0, '', 'Old jacket', 'Knife', 'Sneak attack')
    evil_guy = Enemy('Tom', 8, 10, 5, '', 'T-shirt', 'Gun')
    
    evil_guy.target = henry
    henry.target = evil_guy
    evil_guy.punch()
    evil_guy.target = None
    henry.target = None

    # сериализация
    serialized.append(json.dumps(henry, indent=4, cls=CustomEncoder))
    serialized.append(json.dumps(evil_guy, indent=4, cls=CustomEncoder))
    [print(item) for item in serialized]

    # десериализация
    deserialized = map(json.loads, serialized)
    [print(item) for item in deserialized]