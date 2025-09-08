# PROJECT ILY-3000

**A personalized Iron Man–themed terminal experience and birthday mission.**

This project is a fun, interactive program designed as a heartfelt gift. It combines text-based animations, mini-games, and personalized messages, inspired by Iron Man and J.A.R.V.I.S.

---

## Features

- **Cinematic Boot Sequence:** A dramatic startup sequence simulating Stark Industries’ secure terminal.
- **Birthday Message:** Personalized, typewriter-style message from the sender.
- **Message From Younger Self:** A heartfelt message from “his younger self.”
- **Mini-Games:**

  1. **Energy Stabilization:** Calibrate the Arc Reactor frequency.
  2. **Suit Assembly:** Assemble Iron Man's suit in the correct order.
  3. **Repulsor Target Practice:** Press random keys quickly to test reflexes.
  4. **Shutdown Sequence:** Dramatic, glitchy, and interactive farewell.

---

## Installation

1. **Clone or download the project:**

   ```bash
   git clone <repository_url>
   ```

2. **Ensure Python is installed (Python 3.8+ recommended).**

3. **Install required packages:**

   ```bash
   pip install pyfiglet
   ```

---

## Usage

1. Open a terminal or command prompt.

2. Navigate to the project folder:

   ```bash
   cd path/to/baeshell
   ```

3. Run the program:

   ```bash
   python main.py
   ```

4. Follow the on-screen prompts to:

   - View birthday messages
   - Play mini-games
   - Exit or shutdown the system

---

## Configuration

All personal information is stored in `config.json`. Update the fields:

```json
{
  "his_name": "RecipientName",
  "your_name": "SenderName",
  "birthday": "YYYY-MM-DD",
  "dev_mode": false
}
```

- **his_name:** Recipient’s name
- **your_name:** Sender’s name
- **birthday:** Recipient’s birthday (YYYY-MM-DD)
- **dev_mode:** `true` to unlock birthday features regardless of date

---

## Utilities (`utils.py`)

- `clear_screen()` – Clears the terminal for Windows, macOS, and Linux
- `typewriter(text, speed=0.03, color)` – Prints text slowly like a typewriter, with optional color
- `wait_with_dots(seconds)` – Shows animated loading dots
- `loading_config(path="config.json")` – Loads and validates `config.json`
- `birthday_unlocked(cfg)` – Checks if today matches the birthday or if dev mode is on
- `play_beep(frequency, duration)` – Plays sound effects on Windows, macOS, and Linux

---

## Notes

- Compatible with **Windows, macOS, and Linux** terminals
- Colors and sounds enhance the Iron Man theme
- Designed to be a **personal, interactive birthday experience**

---

## License

This project is intended for **personal use as a gift**.
Feel free to modify and extend it for educational purposes.
