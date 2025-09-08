import time
import pyfiglet
import textwrap
import sys
import random
import re
import os
from utils import loading_config, clear_screen, typewriter, wait_with_dots, birthday_unlocked, play_beep, is_unlocked

user_data = loading_config()

# Try to import winsound for beeps on Windows
try:
    import winsound
except ImportError:
    winsound = None

# -------------------- BOOT SEQUENCE --------------------

def boot(user_data):
    """
    Handles the cinematic boot sequence for PROJECT ILY 3000
    """
    clear_screen()
    typewriter(">>> Initializing Stark Industries Secure Terminal... ", color="\033[96m")
    play_beep(600, 150)
    typewriter(">>> J.A.R.V.I.S. online.", color="\033[96m")
    play_beep(800, 150)
    typewriter(">>> Accessing Stark Industries Database...", color="\033[96m")
    typewriter(">>> Authentication sequence initiated...", color="\033[96m")
    typewriter(f">>> User Detected: {user_data['his_name']}", color="\033[96m")
    wait_with_dots(2)
    typewriter(">>> Identity confirmed.", color="\033[92m")
    typewriter(f">>> Welcome {user_data['his_name']}. Access granted.", color="\033[92m")
    time.sleep(1)
    clear_screen()

    stark = pyfiglet.figlet_format("STARK INDUSTRIES", font='standard')
    banner = pyfiglet.figlet_format("PROJECT ILY-3000", font='slant')
    print("\033[94m" + stark + "\033[0m")
    print("\033[96m" + banner + "\033[0m")
    time.sleep(1)
    typewriter(f">>> Welcome to your birthday mission, {user_data['his_name']}\n", color="\033[93m")


# -------------------- PAUSE --------------------

def pause_return():
    """
    Pause for user to read
    """
    input("\nPress Enter to return to the main menu...")


# -------------------- BIRTHDAY MESSAGES --------------------

def show_birthday_message(user_data):
    clear_screen()
    play_beep()
    intro_lines = [
        f">>> Initializing birthday protocol...",
        f">>> Loading birthday message from {user_data.get('your_name')}...",
        f">>> Target acquired: {user_data.get('his_name')}",
        ">>> Deploying heartfelt transmission...\n"
    ]
    for line in intro_lines:
        typewriter(line, speed=0.05, color="\033[96m")
        time.sleep(0.8)

    msg = textwrap.dedent(f"""
    Happy Birthday, {user_data.get('his_name')}!

    Of all the days I get to spend by your side, today feels more extraordinary than the rest.
    It’s the very first birthday we’re celebrating together, and I can’t begin to explain 
    how grateful I am for you, for the way you light up every room, for your brilliance, 
    your courage, and for the heart that not everyone gets to see, but I’m lucky enough to know.

    I want you to know how deeply I value and love you, and how much I appreciate everything you are,
    both the genius and the man beneath the armor. As you step into another year, 
    I wish you nothing but the best in everything you do. 
    And with you, “the best” has a way of always being extraordinary.

    Here’s to many more birthdays together, 
    each one a reminder that even the strongest men deserve to be loved beyond measure.

    I LOVE YOU
    """)

    for line in msg.splitlines():
        if line.strip():
            typewriter(line.strip(), speed=0.03, color="\033[93m")
            time.sleep(0.4)
        else:
            print()
    typewriter("\n>>> Transmission complete.", speed=0.05, color="\033[92m")
    pause_return()
    clear_screen()


def show_younger_self(user_data):
    clear_screen()
    play_beep()
    intro_lines = [
        f">>> Initializing archival message protocol...",
        f">>> Accessing memory files of {user_data.get('his_name', 'you')}...",
        ">>> Preparing time-capsule transmission..."
    ]
    for line in intro_lines:
        typewriter(line, speed=0.05, max_seconds=10, color="\033[96m")
        for dot in "...":
            sys.stdout.write("\033[93m" + dot + "\033[0m")
            sys.stdout.flush()
            time.sleep(0.5)
        print()
        time.sleep(0.8)

    print()
    msg = textwrap.dedent(f"""\ 
    Hey… it’s me. Or, well… it’s you. The younger version.

    I don’t know everything you’ve been through yet, but I always wondered if we’d make it. 
    If the struggles, the doubts, the restless nights would finally lead somewhere.

    So if you’re hearing this, then I guess… we did it. You made it.
    Keep calm. You’re exactly where you’re supposed to be.

    I may be small now, but I already feel proud of the man you’ve become.
    Every dream I whispered, every hope I held — you carried them here.

    So today, on your birthday, just remember: Take a breath. Smile. You made it.
    And I’ll always be with you.
    """)

    for line in msg.splitlines():
        if line.strip():
            typewriter(line.strip(), speed=0.03, max_seconds=10, color="\033[93m")
            time.sleep(0.5)
        else:
            print()
    typewriter("\n>>> Transmission complete", speed=0.05, color="\033[92m")
    pause_return()
    clear_screen()


# -------------------- MINI GAMES --------------------

def energy_stabilization():
    while True:
        clear_screen()
        play_beep()
        typewriter("=== Challenge: Energy Stabilization ===", color="\033[94m")
        typewriter("Arc Reactor frequency must be calibrated to avoid meltdown...", color="\033[96m")
        number = random.randint(100, 999)
        max_attempts = 7
        attempts = max_attempts

        while attempts > 0:
            health = "|" * attempts
            guess = input(f"Enter reactor frequency (100-999), {attempts} attempts left | Stability: {health}: ")

            if not guess.isdigit():
                typewriter("Digits only, sir.", color="\033[91m")
                continue
            guess = int(guess)

            if guess == number:
                typewriter("⚡ Frequency locked! Arc Reactor stabilized! ✅", color="\033[92m")
                play_beep(1200, 200)
                typewriter("System ONLINE. Well done, sir.", color="\033[92m")
                break
            elif abs(guess - number) <= 10:
                typewriter("⚡ Frequency lock almost achieved, sir!", color="\033[93m")
            elif abs(guess - number) <= 50:
                typewriter("Stabilizers responding, recalibrating...", color="\033[93m")
            else:
                typewriter("❄ Frequency unstable. You’re way off, sir.", color="\033[91m")

            attempts -= 1

        else:
            typewriter("⚠️ Warning: Arc Reactor destabilizing...", color="\033[91m")
            play_beep(500, 300)
            typewriter("❌ Calibration failed. Mission compromised, sir.", color="\033[91m")

        typewriter(f"\n>>> The correct frequency was: {number}", color="\033[93m")
        replay = input("\nPlay again? (Y/N): ").strip().lower()
        if replay != 'y':
            return


def suit_assembly():
    while True:
        clear_screen()
        play_beep()
        typewriter("=== Challenge: Suit Assembly ===", color="\033[94m")
        parts = ["HELMET", "ARC REACTOR", "CHEST ARMOR", "GAUNTLETS", "FLIGHT STABILIZERS"]
        shuffled_parts = parts[:]
        random.shuffle(shuffled_parts)

        typewriter("Assemble the suit in the correct order:", color="\033[96m")
        for i, part in enumerate(shuffled_parts, start=1):
            print(f"{i}. {part}")

        attempt = input("\nEnter the sequence of numbers in the correct order (e.g. 3 1 4 2 5): ")
        try:
            attempt_order = [int(x) for x in attempt.split()]
            chosen_parts = [shuffled_parts[i - 1] for i in attempt_order]

            if chosen_parts == parts:
                typewriter("Suit fully assembled. Looking sharp, sir. ✅", color="\033[92m")
                result = True
            else:
                correct_count = sum(1 for a, b in zip(chosen_parts, parts) if a == b)
                typewriter(f"Assembly sequence flawed. {correct_count}/5 parts correct. ⚠️", color="\033[93m")
                result = False
        except:
            typewriter("Invalid input. Autopilot engaged. ⚡", color="\033[91m")
            result = False

        replay = input("\nDo you want to try assembling again? (y/n): ").lower()
        if replay != "y":
            return result


def repulsor_target_practice(rounds=5, base_time_limit=2.0):
    while True:
        clear_screen()
        play_beep()
        typewriter("=== Challenge: Repulsor Target Practice ===", color="\033[94m")
        typewriter("Objective: Hit the correct target key as fast as possible.\n", color="\033[96m")
        time.sleep(2)
        score = 0
        for i in range(rounds):
            time_limit = max(0.8, base_time_limit - (i * 0.2))
            target = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            typewriter(f"Target {i + 1}: {target}", color="\033[93m")
            start = time.perf_counter()
            entry = input("Your input: ").upper().strip()
            elapsed = time.perf_counter() - start

            if entry == target and elapsed <= time_limit:
                typewriter("⚡ Perfect shot! Lightning fast.", color="\033[92m")
                play_beep(1200, 150)
                score += 2
            elif entry == target:
                typewriter("✅ Hit confirmed but a bit slow.", color="\033[93m")
                score += 1
            else:
                typewriter("❌ Missed target. Keep steady.", color="\033[91m")

        accuracy = (score / (rounds * 2)) * 100
        typewriter(f"\nTraining complete. Accuracy: {accuracy:.1f}%", color="\033[93m")
        result = accuracy >= 60
        if result:
            typewriter("System calibration successful. Repulsors online. ✅", color="\033[92m")
        else:
            typewriter("Calibration failed. Repulsors unstable. ❌", color="\033[91m")

        replay = input("\nDo you want to retry target practice? (y/n): ").lower()
        if replay != "y":
            return result


# -------------------- GAMES MENU --------------------

def games_menu():
    while True:
        clear_screen()
        typewriter("=== Iron Man Protocol: Games Menu ===", color="\033[94m")
        print("1. Energy Stabilization")
        print("2. Suit Assembly Order")
        print("3. Repulsor Target Practice")
        print("4. Return to Main Menu")
        choice = input("Select a game: ")

        if choice == "1":
            energy_stabilization()
        elif choice == "2":
            suit_assembly()
        elif choice == "3":
            repulsor_target_practice()
        elif choice == "4":
            break
        else:
            typewriter("Invalid choice, sir.", color="\033[91m")

        input("\nPress ENTER to return to the games menu...")


# -------------------- SHUTDOWN --------------------

def shutdown():
    clear_screen()
    typewriter("System shutting down...", speed=0.03, color="\033[94m")
    wait_with_dots(2)
    glitch_text = ["G..oo..d..b...y..e...", "GoOdByE", "GOODBYE"]
    for line in glitch_text:
        print("\033[91m" + line + "\033[0m")
        time.sleep(0.2)
        clear_screen()
        play_beep()
        play_beep()
    typewriter("Goodbye. PROJECT ILY-3000 signing off.", speed=0.03, color="\033[94m")
    wait_with_dots(0.8)


# -------------------- MAIN MENU --------------------

def show_menu(user_data):
    clear_screen()
    try:
        while True:
            typewriter("======================================", speed=0.02, color="\033[96m")
            typewriter("        PROJECT ILY-3000 MAIN MENU", speed=0.02, color="\033[96m")
            typewriter("======================================", speed=0.02, color="\033[96m")
            print()

            typewriter(f"1. Birthday Message from {user_data.get('your_name')}", speed=0.02, color="\033[93m")
            typewriter("2. A Message From Your Younger Self", speed=0.02, color="\033[93m")
            typewriter("3. Mission Challenge", speed=0.02, color="\033[93m")
            typewriter("4. System Shutdown", speed=0.02, color="\033[93m")

            choice = input("\n>>> Select an option (1-4): ").strip().lower()
            if choice in ("1", "birthday", "message"):
                show_birthday_message(user_data)
            elif choice in ("2", "younger", "younger self", "younger_self"):
                show_younger_self(user_data)
            elif choice in ("3", "mission", "game", "play", "mini-game", "minigame"):
                games_menu()
            elif choice in ("4", "shutdown", "exit", "quit"):
                shutdown()
                break
            else:
                typewriter("Invalid selection. Please choose 1-4.", speed=0.02, color="\033[91m")
                wait_with_dots(1)
                clear_screen()

    except (KeyboardInterrupt, EOFError):
        typewriter("\nReceived interrupt — shutting down safely...", speed=0.02, color="\033[91m")
        wait_with_dots(1)
        shutdown()

user_data = loading_config()
# Lock program until birthday if dev_mode is False
if not is_unlocked(user_data):
    clear_screen()
    typewriter(">>> Access Denied: Birthday features are locked until your special day.", speed=0.03)
    typewriter(f">>> Birthday unlock date: {user_data['birthday']}", speed=0.03)
    play_beep()
    play_beep()
    play_beep()
    wait_with_dots(2)
    exit()  # Exit the program

boot(user_data)
time.sleep(2)
show_menu(user_data)