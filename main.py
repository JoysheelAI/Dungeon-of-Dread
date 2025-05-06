import pygame
pygame.mixer.init()

def play_sound(file):
    try:
        sound = pygame.mixer.Sound(file)
        sound.play()
    except Exception as e:
        print(f"❌ Sound error: {e}")


from pyfiglet import figlet_format
from rich.console import Console
from rich.progress import Progress
import time as t

console = Console()

with Progress() as progress:
    task = progress.add_task("[green]Spawning Dungeon...", total=100)
    while not progress.finished:
        t.sleep(0.02)
        progress.update(task, advance=2)

console.print(figlet_format("DUNGEON OF DREAD", font="starwars"), style="bold magenta")


console.print("\n🌌 [bold cyan]Welcome, brave soul, to the Dungeon of Dread![/bold cyan]")
console.print("[yellow]Legends whisper of lost treasures, cursed code, and bugs that haunt devs forever...[/yellow]")
console.print(f"[magenta]But today, YOU enter. With nothing but your wits, and a keyboard blessed by the Python gods.[/magenta]")

play_sound("sounds/intro.mp3")


import random as rd
import time as t
from colorama import init, Fore, Style
init(autoreset=True)

# status
player_name = input("Enter your name, chosen one: ")
health = 100
bugzilla_health = 100
potions_left = 3  
damage_taken = [10, 15, 30]
bugzilla_damage_taken = [10, 15, 30]

# welcome message
print(Fore.CYAN + "\n🌌 Welcome, brave soul, to the Dungeon of Dread! 🌌")
print(Fore.YELLOW + "Legends whisper of lost treasures, cursed code, and bugs that haunt devs forever...")
print(Fore.MAGENTA + f"But today, YOU enter. With nothing but your wits, and a keyboard blessed by the Python gods. 🐍🛡️")
print(Style.BRIGHT + Fore.GREEN + f"Prepare yourself... {player_name}. The battle begins now. ⚔️💻")

# choices
def fight():
    global bugzilla_health
    print("🗡️ You raise your mighty keyboard and prepare to DESTROY Bugzilla!")
    t.sleep(1)
    attack_to_bugzilla = rd.choice(bugzilla_damage_taken)
    bugzilla_health -= attack_to_bugzilla
    print(f"💥 You dealt {attack_to_bugzilla} damage! Bugzilla's health is now: {max(bugzilla_health, 0)}")

def run():
    print("🏃‍♂️ You yeet yourself out of the dungeon. No shame in living to code another day!")

def use_potion():
    global health, potions_left
    print("🧪 You sip the Debug Potion. It tastes like coffee and regret... with a hint of burnt dreams.")
    t.sleep(1)

    if potions_left <= 0:
        print("🚫 Outta potions, my dude. You're gonna have to raw dog this bug fight.")
        return

    if health < 100:
        health = 100
        potions_left -= 1
        print(f"✨ Health fully restored! Potions left: {potions_left}")
    else:
        print("📛 Bro, your health is already THICC. Save that potion for when you're actually dying 💀")

def taunt():
    print("😏 You mock Bugzilla: 'Your code doesn’t even compile, loser!'")

# bugzilla's attack
def bugzilla_attack():
    global health
    play_sound("sounds/roar.mp3")
    t.sleep(1)
    damage = rd.choice(damage_taken)
    health -= damage
    print(f"🪲 Bugzilla hisses and launches a syntax error at you! You took {damage} damage.")
    print(f"🩸 Your health is now: {max(health, 0)}")

# user choice
def choice():
    choices = {
        "fight": fight,
        "run": run,
        "potion": use_potion,
        "taunt": taunt
    }

    try:
        user_choice = input(Fore.LIGHTWHITE_EX + f"\nWhat do you want to do, {player_name}? (fight/run/potion/taunt): ").lower()
        if user_choice not in choices:
            raise ValueError
        else:
            choices[user_choice]()

            if user_choice == "run":
                return "ran"
            elif user_choice == "fight":
                if bugzilla_health > 0:
                    bugzilla_attack()
            
            # After each turn
            print(Fore.CYAN + f"\n💖 {player_name}'s Health: {max(health, 0)} | 🪲 Bugzilla's Health: {max(bugzilla_health, 0)}")

    except ValueError:
        print(Fore.RED + f"🚨 INVALID COMMAND, {player_name}. Try: fight / run / potion / taunt 🧠💥")

# start game
def start_game():
    while health > 0 and bugzilla_health > 0:
        result = choice()
        if result == "ran":
            print(Fore.BLUE + f"\n🧍 You walk away, {player_name}. Bugzilla cackles in the shadows... but you live. For now.")
            break

    if health <= 0:
        play_sound("sounds/lose.mp3")
        print(Fore.RED + "\n💀 You have fallen in battle. Bugzilla corrupted your soul with legacy code...")
    elif bugzilla_health <= 0:
        play_sound("sounds/win.mp3")
        print(Fore.GREEN + f"\n🎉 YOU DID IT, {player_name.upper()}! Bugzilla has been squashed. Time to commit and push 🧑‍💻✨")



def play_again():
    while True:
        try:
            start_choice = input(f"\n{player_name}, do you wanna play again? (yes/no): ").lower()
            if start_choice == "yes":
                # Reset game state
                global health, bugzilla_health
                health = 100
                bugzilla_health = 100
                start_game()
            elif start_choice == "no":
                print(f"\n👋 Farewell, {player_name}. May your syntax always be correct.")
                break
            else:
                raise ValueError
        except ValueError:
            print(f"🛑 Invalid choice, {player_name}. Type 'yes' or 'no'. No semicolons allowed either 😤")


start_game()

play_again()



        

