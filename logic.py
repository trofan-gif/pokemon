from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.weight = self.get_weight()
        self.height = self.get_height()
        self.hp = self.get_hp()
        self.attack_info = self.get_attack()
        self.hp_random = randint(100,300)
        self.power= randint(10,50)
        #self.info_now = self.get_info_now()
        #self.enemy_power = self.enemy_attack()
        self.last_feed_time = datetime.now()
        

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['showdown']['front_default'])
        else:
            return "https://www.cinemascomics.com/pokemon-explica-por-que-el-pikachu-de-ash-nunca-evoluciona/"
    
    # Метод для получения имени покемона через API
    
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    def get_weight(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['weight'])
        else:
            return "6 кг"
    def get_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['height'])
        else:
            return "0,4 m"
    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][0]["base_stat"])
        else:
            return "35"
    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][1]["base_stat"])
        else:
            return "55"
    def feed(self, feed_interval = 30, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp_random += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp_random}"
        else:
            return f"Следующее время кормления покемона: {current_time-delta_time}"

    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    #def enemy_attack(self,enemy):
        #if enemy.power<self.hp_random:
            #self.hp_random -= enemy.power
        #else:
            #self.hp_random = 0
            #return f"У {self.pokemon_trainer} не осталось хп, создай нового покемона"

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}. Параметры: вес:{self.weight}, рост:{self.height}, ХП: {self.hp_random},сила атаки:{self.power}"


    #def get_info_now(self):
        #f"HP now:{self.hp_random}"

        
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
class Wizard(Pokemon):
    def feed(self, feed_interval=20, hp_increase=30):
        return super().feed(feed_interval, hp_increase)

class Fighter(Pokemon):
    def feed(self, feed_interval=10, hp_increase=10):
        return super().feed(feed_interval, hp_increase)
    def attack(self, enemy):
        super_power = randint(10,20)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "



