# 🎰 Coin Machine

A command-line slot machine game built in Python — Week 2 project on Python

## How it works

The player starts with **100 coins** and bets any amount each turn. Three random food symbols are drawn, and winnings are calculated based on the result.

| Result | Payout |
|---|---|
| 3 identical symbols | **x5** the bet  |
| 2 identical symbols | **x3** the bet  |
| No match | Lose the bet  |

## Symbols

🍕 🥨 🥖 🍥 🍩 🍪 🥐 🧀 🥫 🍙 🥟 🍣

## How to run

```bash
python jackpot.py
```

## Example

```
============= WELCOME TO THE COIN MACHINE =============
How much do you want to bet ? 20
🍕  🍕  🥖
You got 2 same symboles.
You win 60 coins !
=========== COIN MACHINE ===========
Coins = 140
```

## Input validation

The program handles all edge cases :
- Non-integer input → error message, ask again
- Negative bet → rejected
- Bet higher than available coins → rejected
- Bet 0 → exits the game
- 0 coins left → game over

## Python concepts practiced

- `while` loop for the game cycle
- `if / elif / else` for win conditions
- `break` and `continue` for flow control
- `try / except` for input validation
- `random.choice()` from the `random` module
- Functions with parameters and return values

## Author

Eva — [github.com/evaguia](https://github.com/evaguia)
