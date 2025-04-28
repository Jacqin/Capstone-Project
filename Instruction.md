# Tic Tac Toe Game

## Overview
This project implements a classic Tic Tac Toe game where players can compete against an AI opponent. The game features a clean, modern interface and intelligent game logic.

## Core Functionality
- Interactive game board with visual feedback
- AI opponent with strategic decision-making
- Win/draw detection
- Score tracking
- Responsive design for various screen sizes

## Technical Stack
- **Backend**: Flask (Python)
- **Game Logic**: Python
- **Frontend**: HTML5, CSS3, JavaScript
- **Templates**: Jinja2 (Flask)

## Project Structure
```
tic-tac-toe/
├── app.py              # Main Flask application
├── game_logic.py       # Game rules and AI logic
├── static/
│   ├── css/           # Stylesheets
│   └── js/            # JavaScript files
└── templates/
    └── index.html     # Main game interface
```

## Setup Instructions
1. Ensure Python 3.x is installed on your system
2. Install required dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://localhost:5000`

## Game Rules
- Players take turns placing their mark (X or O) on the 3x3 grid
- The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins
- If all squares are filled without a winner, the game is a draw

## Features
- Clean, intuitive user interface
- Real-time game state updates
- AI opponent with varying difficulty levels
- Score tracking across multiple games
- Mobile-responsive design