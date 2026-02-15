import random
from colorama  import Fore, Style


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 50
        self.thirst = 50
        self.food = 2
        self.water = 2

    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.hunger = max(0, self.hunger - 20)
            print(Fore.GREEN + "Ви поїли. Голод зменшився!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "У вас немає їжі!" + Style.RESET_ALL)

    def drink(self):
        if self.water > 0:
            self.water -= 1
            self.thirst = max(0, self.thirst - 20)
            print(Fore.BLUE + "Ви попили. Спрага зменшилася!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "У вас немає води!" + Style.RESET_ALL)

    def rest(self):
        self.health = min(100, self.health + 10)
        print(Fore.YELLOW + "Ви відпочили. Здоров’я покращилось!" + Style.RESET_ALL)

    def explore(self, world):
        print("Ви досліджуєте навколишній світ...")
        world.generate_event(self)

    def status(self):
        print(f"{self.name}: {Fore.RED}Здоров’я: {self.health}{Style.RESET_ALL}, "
              f"{Fore.GREEN}Голод: {self.hunger}{Style.RESET_ALL}, "
              f"{Fore.BLUE}Спрага: {self.thirst}{Style.RESET_ALL}, "
              f"{Fore.YELLOW}Їжа: {self.food}, Вода: {self.water}{Style.RESET_ALL}")

class World:
    def __init__(self):
        self.events = [
            ("Знайдено джерело води!", self.find_water),
            ("Атака дикого звіра!", self.animal_attack),
            ("Ви знайшли їжу!", self.find_food),
            ("Погана погода. Ви промокли та змерзли.", self.bad_weather),
        ]

    def find_water(self, player):
        player.water += 1

    def animal_attack(self, player):
        player.health = max(0, player.health - 20)

    def find_food(self, player):
        player.food += 1

    def bad_weather(self, player):
        player.health = max(0, player.health - 10)

    def generate_event(self, player):
        event, effect = random.choice(self.events)
        print(Fore.MAGENTA + event + Style.RESET_ALL)
        effect(player)


def game():
    name = input("Введіть ім’я гравця: ")
    player = Player(name)
    world = World()

    while player.health > 0:
        player.status()
        action = input("Що ви хочете зробити? (eat/drink/explore/rest/exit): ").strip().lower()

        if action == "eat":
            player.eat()
        elif action == "drink":
            player.drink()
        elif action == "explore":
            player.explore(world)
        elif action == "rest":
            player.rest()
        elif action == "exit":
            print("Дякуємо за гру!")
            break
        else:
            print(Fore.RED + "Невідома команда!" + Style.RESET_ALL)

        if player.health == 0:
            print(Fore.RED + "Ви не вижили... Гра закінчена." + Style.RESET_ALL)
            break

if __name__ == "__main__":
    game()






