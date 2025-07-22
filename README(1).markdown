# Roulette CLI Game

A command-line interface (CLI) implementation of a Roulette game written in Python. Players can place bets, spin the roulette wheel, and manage their balance, with data persisted in a JSON file. The game supports various bet types with realistic payouts and probabilities, and features a dynamic spinning animation.

## Features

- **Player Management**: Add players with an initial balance, stored in `players.json`.
- **Bet Types**: Supports multiple bet types including odd/even, black/red, high/low, dozen, column, six number, four number, three number, two number, and single number bets.
- **Roulette Wheel**: Simulates a standard European roulette wheel with 37 numbers (0–36) and a visual spinning effect.
- **Payout System**: Implements realistic payouts (e.g., 35:1 for single number, 1:1 for odd/even).
- **Interactive CLI**: User-friendly prompts for bet placement and game interaction.
- **Help Table**: Displays bet types, payouts, probabilities, and descriptions.
- **Rich Console Output**: Colorful output for numbers, win/loss messages, and game status using the `rich` library.

## Requirements

- Python 3.6+
- Required packages:
  - `prettytable` (for help table display)
  - `rich` (for enhanced console output)

Install dependencies using:
```bash
pip install prettytable rich
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/roulette-cli-game.git
   cd roulette-cli-game
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python roulette.py
   ```

## Usage

### Interactive Mode
Run the game without arguments to enter interactive mode:
```bash
python roulette.py
```
- Enter your player name and starting balance (if new).
- Choose a bet type (e.g., `1` for odd/even).
- Specify your bet choice and amount.
- Watch the roulette wheel spin and see the result.

### Command-Line Arguments
The game supports the following commands:

1. **Add a Player**:
   ```bash
   python roulette.py add-player --name <player_name> --balance <initial_balance>
   ```
   Example:
   ```bash
   python roulette.py add-player --name Alice --balance 1000
   ```

2. **Play a Game**:
   ```bash
   python roulette.py play --name <player_name> --bet-type <bet_type> --amount <amount> --choice <choice>
   ```
   Example (betting on a single number):
   ```bash
   python roulette.py play --name Alice --bet-type "one number" --amount 100 --choice 17
   ```

3. **Show Help Table**:
   ```bash
   python roulette.py help-table
   ```
   Displays a table of bet types, payouts, probabilities, and descriptions.

### Bet Types
| Bet Type       | Payout | Probability | Description                                      |
|----------------|--------|-------------|--------------------------------------------------|
| odd/even       | 1:1    | 48.65%      | Bet on all odd or even numbers                   |
| black/red      | 1:1    | 48.65%      | Bet on all red or all black numbers              |
| high/low       | 1:1    | 48.65%      | Bet on 1–18 (low) or 19–36 (high)                |
| Dozen          | 2:1    | 32.43%      | Bet on 1st (1–12), 2nd (13–24), or 3rd (25–36) dozen |
| Column         | 2:1    | 32.43%      | Bet on one of the three vertical columns         |
| six number     | 5:1    | 16.22%      | Bet on two adjacent rows (six numbers)           |
| four number    | 8:1    | 10.81%      | Bet on four numbers that meet at one corner      |
| three number   | 11:1   | 8.11%       | Bet on a row of three consecutive numbers        |
| two number     | 17:1   | 5.41%       | Bet on two adjacent numbers                      |
| one number     | 35:1   | 2.70%       | Bet on a single number                           |

### Example Commands
- Bet on red:
  ```bash
  python roulette.py play --name Alice --bet-type "black/red" --amount 50 --choice red
  ```
- Bet on the first dozen:
  ```bash
  python roulette.py play --name Alice --bet-type Dozen --amount 50 --choice 1
  ```
- Bet on a single number (17):
  ```bash
  python roulette.py play --name Alice --bet-type "one number" --amount 50 --choice 17
  ```

## File Structure
- `roulette.py`: Main game script containing all logic.
- `players.json`: Stores player names and balances (created automatically).
- `requirements.txt`: Lists required Python packages.

## Notes
- Player data is saved in `players.json` and persists between sessions.
- The roulette wheel animation uses a dynamic sleep time for a realistic spinning effect.
- Invalid inputs (e.g., insufficient balance, invalid bet type) are handled with clear error messages.
- The game uses a standard European roulette wheel layout (37 numbers, single zero).

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.