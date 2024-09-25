import random

class Player:
    def _init_(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.items = []

    def attack_enemy(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.health -= self.attack
        if enemy.health <= 0:
            print(f"{enemy.name} is defeated!")
        else:
            print(f"{enemy.name} has {enemy.health} health left.")

    def use_item(self, item):
        if item in self.items:
            if item == 'health potion':
                self.health += 20
                print(f"{self.name} uses a health potion and gains 20 health.")
            self.items.remove(item)
        else:
            print("You don't have that item!")

class Enemy:
    def _init_(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_player(self, player):
        print(f"{self.name} attacks {player.name}!")
        player.health -= self.attack
        if player.health <= 0:
            print(f"{player.name} is defeated!")
        else:
            print(f"{player.name} has {player.health} health left.")

class Dungeon:
    def _init_(self, size):
        self.size = size
        self.rooms = [[self.random_room() for _ in range(size)] for _ in range(size)]
        self.player_position = [0, 0]
        self.generate_items()

    def random_room(self):
        return random.choice(['empty', 'enemy', 'puzzle', 'item'])

    def generate_items(self):
        for _ in range(5):
            x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            self.rooms[x][y] = 'item'

    def move_player(self, direction):
        if direction == 'north' and self.player_position[1] > 0:
            self.player_position[1] -= 1
        elif direction == 'south' and self.player_position[1] < self.size - 1:
            self.player_position[1] += 1
        elif direction == 'east' and self.player_position[0] < self.size - 1:
            self.player_position[0] += 1
        elif direction == 'west' and self.player_position[0] > 0:
            self.player_position[0] -= 1
        else:
            print("You can't move in that direction.")
        self.enter_room()

    def enter_room(self):
        x, y = self.player_position
        room = self.rooms[x][y]
        if room == 'enemy':
            enemy = Enemy("Goblin", 50, 5)
            self.fight_enemy(enemy)
        elif room == 'puzzle':
            self.solve_puzzle()
        elif room == 'item':
            self.find_item()
        else:
            print("The room is empty.")

    def fight_enemy(self, enemy):
        while enemy.health > 0 and player.health > 0:
            player.attack_enemy(enemy)
            if enemy.health > 0:
                enemy.attack_player(player)
        if player.health > 0:
            self.rooms[self.player_position[0]][self.player_position[1]] = 'empty'

    def solve_puzzle(self):
        print("You encounter a puzzle!")
        answer = input("What is 5 + 3? ")
        if answer == '8':
            print("You solved the puzzle!")
            self.rooms[self.player_position[0]][self.player_position[1]] = 'empty'
        else:
            print("Incorrect! Try again.")

    def find_item(self):
        item = random.choice(['health potion', 'key', 'sword'])
        print(f"You found a {item}!")
        player.items.append(item)
        self.rooms[self.player_position[0]][self.player_position[1]] = 'empty'


# Game loop
player_name = input("Enter your name: ")
player = Player(player_name)
dungeon = Dungeon(5)

while player.health > 0:
    print(f"You are at position {dungeon.player_position}.")
    direction = input("Which direction do you want to move? (north, south, east, west): ")
    dungeon.move_player(direction)

if player.health <= 0:
    print("Game Over!")
else:
    print("Congratulations! You won!")