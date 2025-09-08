# Helper functions
# clear_screen() - clears terminal
# typewriter(text, speed) - prints text slowly like typing
# wait_with_dots() - shows loading dots animation
# load_config() - reads config.json
# birthday_unlocked() - checks today's date vs birthday (but ignores if dev_mode = true)
import os
import sys
import time
import json
from pathlib import Path
from datetime import datetime, date

# Try to import winsound for beeps on Windows
try:
    import winsound
except ImportError:
    winsound = None


def is_unlocked(cfg):
    """
    Checks if the program should be unlocked.
    Returns True if today's date >= birthday or if dev_mode is True.
    :param cfg: Configuration dictionary from loading_config()
    :return: bool
    """
    if cfg.get("dev_mode", False):
        return True

    try:
        bday = datetime.strptime(cfg["birthday"], "%Y-%m-%d").date()
    except (KeyError, ValueError):
        raise ValueError("`birthday` must be in config.json in YYYY-MM-DD format, e.g., 2025-09-09")

    today = date.today()
    return today >= bday


def clear_screen():
    """
    Clears the terminal screen on Windows, macOS, and Linux.
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def typewriter(text, speed=0.03, max_seconds=10, color="\033[96m"):
    """
    Prints text like a typewriter with optional color and max duration.
    """
    start_time = time.time()
    sys.stdout.write(color)
    for char in text:
        if time.time() - start_time > max_seconds:
            sys.stdout.write("... [skipped]\n")
            sys.stdout.flush()
            break
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\033[0m\n")
    sys.stdout.flush()


def wait_with_dots(seconds=2, interval=0.5):
    """
    Shows a dot-loading animation for 'seconds', printing a dot every 'interval' seconds
    :param seconds: The total duration of the animation in seconds
    :param interval: The delay between printing each dot in seconds
    :return: None
    """
    end_time = time.time() + seconds
    while time.time() < end_time:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write('\n')
    sys.stdout.flush()


def loading_config(path="config.json"):
    """
    Loads configuration from JSON and validates required fields
    :param path: The file path to the JSON configuration file.
    :return: A dict with the relevant information
    """
    cfg_path = Path(path)
    if not cfg_path.exists():
        raise FileExistsError(
            f"Config file not found at {cfg_path.resolve()}. "
            "Create config.json or copy config.example.json"
        )
    try:
        with cfg_path.open("r", encoding="utf-8") as f:
            cfg = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"config.json is not valid JSON: {e}") from e

    required = ["his_name", "your_name", "birthday", "secret_code", "dev_mode"]
    missing = [k for k in required if k not in cfg]
    if missing:
        raise KeyError(f"Missing required config keys: {','.join(missing)}")

    # Basic type checks
    if not isinstance(cfg["his_name"], str) or not cfg["his_name"].strip():
        raise ValueError("`his_name` must be a non-empty string.")
    if not isinstance(cfg["your_name"], str) or not cfg["your_name"].strip():
        raise ValueError("`your_name` must be a non-empty string.")
    if not isinstance(cfg["secret_code"], str) or not cfg["secret_code"].strip():
        raise ValueError("secret_code` must be a non-empty string.")
    if not isinstance(cfg["dev_mode"], bool):
        raise ValueError("`dev_mode` must be true or false.")

    # keep strings tidy
    cfg["his_name"] = cfg["his_name"].strip()
    cfg["your_name"] = cfg["your_name"].strip()
    cfg["secret_code"] = cfg["secret_code"].strip()

    return cfg


def birthday_unlocked(cfg):
    """
    Returns True if dev_mode is true OR if today's date matches the configured birthday.
    :param cfg: A configuration dictionary loaded from 'load_config()'
    :return: True if either; dev_mode is enabled, or today's month and day match the configured birthday.
    """
    if cfg.get("dev_mode", False):
        return True

    # Parse the date string
    try:
        bday = datetime.strptime(cfg["birthday"], "%Y-%m-%d").date()
    except (KeyError, ValueError):
        raise ValueError("`birthday` must be in config.json in YYYY-MM-DD format, (e.g., 2025-05-24)")

    today = date.today()  # uses the machine's timezone
    return (today.month, today.day) == (bday.month, bday.day)


def play_beep(frequency=1000, duration=200):
    """
    Plays a beep sound on Windows, macOS, and Linux terminals.

    :param frequency: Frequency in Hz (Windows only). Default 1000Hz.
    :param duration: Duration in milliseconds (Windows only). Default 200ms.
    :return: None
    """
    if sys.platform == "win32" and winsound:
        # Windows: use winsound
        winsound.Beep(frequency, duration)
    elif sys.platform == "darwin":
        # macOS: play system sound (Glass.aiff or choose another)
        os.system('afplay /System/Library/Sounds/Glass.aiff')
    else:
        # Linux and others: fallback to terminal bell
        print("\a", end='')
