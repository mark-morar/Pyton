import random

class Astronaut:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 50
        self.morale = 50
        self.alive = True
        self.days_survived = 0

    def explore(self):
        if not self.alive:
            return
        print(f"{self.name} вирушає досліджувати Марс!")
        self.energy -= 15
        self.morale += 10
        if random.random() < 0.2:
            injury = random.randint(5, 20)
            self.health -= injury
            print(f"{self.name} отримав травму! Здоров'я зменшилось на {injury}.")
        self.check_status()

    def repair(self):
        if not self.alive:
            return
        print(f"{self.name} виконує ремонт бази!")
        self.energy -= 20
        self.morale -= 5
        self.check_status()
    def rest(self):
        if not self.alive:
            return
        print(f"{self.name} відпочиває.")
        self.energy += 20
        self.morale += 5
        self.check_status()
    def communicate(self):
        if not self.alive:
            return
        print(f"{self.name} зв'язується із Землею.")
        self.energy -= 10
        self.morale += 15
        self.check_status()
    def check_status(self):
        if self.health <= 0 or self.energy <= 0 or self.morale <= 0:
            self.alive = False
            print(f"{self.name} не вижив...")
    def live_one_day(self):
        if not self.alive:
            return
        self.days_survived += 1
        print(f"День {self.days_survived}: {self.name} виживає на Марсі!")
        action = random.choice([self.explore, self.repair, self.rest, self.communicate])
        action()
        if self.days_survived >= 365:
            print(f"{self.name} успішно вижив рік на Марсі! Перемога!")
            self.alive = False
astro = Astronaut("Олексій")
while astro.alive:
    astro.live_one_day()







class Student:

    def __init__(self,name):
        self.name= name
        self.gladnes = 50
        self.progres = 0
        self.alive = True

    def to_study(self):
        print("time to study")
        self.progres += 0.12
        self.gladnes -= 5

    def to_sleep(self):
        print("go to sleep")
        self.gladnes +=3

    def to_chill(self):
        print("time to chill")
        self.gladnes += 5
        self.progres -= 0.1

    def is_alive(self):
        if self.progres < -0.5:
            print(" i wath except")
            self.alive = False

        elif self.gladnes <= 0:
            print("i have dipraci")
            self.alive = False

        elif self.progres >= 5:
            print("automatic finished")
            self.alive = False


    def end_of_day(self):
        print(f"Gladnes = {self.gladnes}")
        print(f"Progres = {self.progres}")

    def live(self,day):
        print(f"day: {day} - student: {self.name}")
        live_cube = random.randint(1,3)


        if live_cube == 1:
            self.to_sleep()

        elif live_cube == 2:
            self.to_study()

        elif live_cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

nazar = Student("Nazar")

for day in range(365):

    if nazar.alive == False:
        break

    nazar.live(day)

class Entrepreneur:

    def __init__(self,name):
        self.name=name
        self.money = 1000
        self.energy = 50
        self.motivation = 50
        self.alive = True
        self.days = 0

    def work(self):
        if self.energy > 5 and self.motivation > 5:
            earnings = random.randint(200, 500)
            self.money+=earnings
            self.energy-=random.randint(15,20)
            self.motivation-=random.randint(5,10)
        else:
            print(f"{self.name} занадто втомлений або немотивований, щоб працювати.")
        self.check_status()

    def invest(self):
        if self.money >500:
          invest=random.randint(300,700)
          self.money-=invest
          if random.random()<0.5:
            profit=invest*random.randint(2,3)
            self.money+=profit
          else:
             loss = invest * random.randint(1, 2) // 2
             self.money -= loss
             print(f"Інвестиція не вдалася. Втрата: {loss}. Баланс: {self.money}")
        else:
             print("Недостатньо коштів для інвестування.")
        self.check_status()

    def relax(self):
        self.energy = min(100, self.energy + random.randint(15, 25))
        self.motivation = min(100, self.motivation + random.randint(10, 20))
        print(f"{self.name} відпочив. Енергія: {self.energy}, Мотивація: {self.motivation}")
        self.check_status()

    def network(self):
     self.motivation = min(100, self.motivation + random.randint(10, 20))
     if random.random()<0.3:
      bonus=random.randint(500,700)
      self.money+=bonus
      print(f"Нетворкінг приніс бізнес-можливість! Отримано: {bonus}. Баланс: {self.money}")
     else:
      print(f"{self.name} займався нетворкінгом. Мотивація зросла до {self.motivation}.")
      self.check_status()

    def check_status(self):
         if self.money <= 0 or self.energy <= 0 or self.motivation <= 0:
             self.alive = False
             print(f"{self.name} збанкрутував або вигорів. Симуляція завершена.")

    def simulate(self):
        while self.alive and self.days < 365:
            self.days += 1
            print(f"\nДень {self.days}")
            action = random.choice([self.work, self.invest, self.relax, self.network])
            action()
            if self.money >= 50000:
                print(f"{self.name} досяг фінансового успіху! Баланс: {self.money}")
                break
        if self.alive:
         print(f"Симуляція завершена. Підсумок: {self.money} грн за {self.days} днів.")


player = Entrepreneur("Олександр")
player.simulate()








