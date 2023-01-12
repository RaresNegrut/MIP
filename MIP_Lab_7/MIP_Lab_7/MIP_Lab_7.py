class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.level = 1

    def describe(self):
        print("<{}:{}, {} HP>".format(self.name,self.level, self.health))

    def take_hit(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def level_up(self):
        self.level = self.level + 1
        self.health = 100


p1 = Player("Bayek", 100)
p1.take_hit(20)
p1.heal(10)
p1.describe()
p1.level_up()
p1.describe()