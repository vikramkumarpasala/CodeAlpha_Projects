# Hangman Game (Python)

A simple, interactive console-based Hangman game built with Python. This project was developed as part of a coding task to demonstrate basic logic, loops, and user input handling in Python.

## 🎮 Game Overview

The objective of the game is to guess the hidden word before the "hangman" is fully drawn. You have a limited number of attempts (lives) to guess the correct letters.

## 🚀 Features

*   **Interactive CLI:** Simple command-line interface for an easy user experience.
*   **Dynamic Gameplay:** The game selects a random word from a predefined list.
*   **Visual Progress:** Displays the current state of the word (e.g., `_ _ P _ L _`) and the number of lives remaining.
*   **Input Handling:** Validates user input to ensure only single letters are processed.

## 📋 Requirements

*   **Python 3.x** installed on your system.

## ⚙️ How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/CodeAlpha_Projects.git](https://github.com/your-username/CodeAlpha_Projects.git)
    cd CodeAlpha_Projects/task1
    ```

2.  **Run the script:**
    ```bash
    python hangman.py
    ```

## 🕹️ How to Play

1.  When the game starts, you will see a series of underscores representing the secret word.
2.  Type a single letter and press **Enter**.
3.  If the letter exists in the word, it will appear in the correct position.
4.  If the letter does not exist, you will lose a life.
5.  Continue guessing until you either reveal the full word (Win) or run out of lives (Game Over).

## 📂 Project Structure

```text
task1/
├── hangman.py       # Main game source code
└── README.md        # This file
