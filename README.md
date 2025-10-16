<<<<<<< HEAD
# ChessGUI
Chess.com‑style Python chess GUI with Stockfish, analysis, and game review.
=======
# Chess Game with Stockfish AI

A command-line chess game where you can play against the powerful Stockfish chess engine.

## Features
# ChessGUI
Chess.com‑style Python chess GUI with Stockfish, analysis, and game review.

[![Build Windows](https://github.com/malaykasana/ChessGUI/actions/workflows/build-windows.yml/badge.svg)](https://github.com/malaykasana/ChessGUI/actions/workflows/build-windows.yml)

This project includes both a full GUI app (`chess_gui.py`) and a simple command-line game (`main.py`).


### Command-Line Version (main.py)
- ♟ Full chess game implementation with move validation
- 🤖 Play against Stockfish AI engine
- 🎨 Clear command-line board display
- ⚙️ Adjustable AI difficulty (thinking time)
- ↩️ Undo moves
- ✅ Detects checkmate, stalemate, and draw conditions
- 📝 Move input in standard UCI notation (e.g., e2e4)

### GUI Version (chess_gui.py) ✨NEW
- 🎮 **Graphical chess board** with Unicode pieces
- 🖱️ **Click to move** - Intuitive drag-free interface
- 💡 **Legal move highlights** - See where you can move
- 🤖 **AI opponent** with adjustable thinking time
- 🎨 **6 Beautiful themes** - Classic, Blue, Green, Purple, Modern, Dark
- 🔄 **New Game, Undo** buttons
- ⚪⚫ **Choose your color** (White or Black)
- 📊 **Live evaluation bar** - Real-time position analysis
- 💡 **Hint system** - Get best move suggestions from Stockfish
- 💾 **Save/Load PGN** - Export and import games
- 📜 **Move history** - View all moves in the game
- 🔗 **Account integration** - Connect Lichess & Chess.com accounts
- 📊 **Game review mode** - Fetch and analyze your online games
- 🔍 **Move-by-move analysis** - Find blunders, mistakes, and inaccuracies
- ⏮⏭ **Game navigation** - Step through moves with live eval

## Requirements

- Python 3.7+
- Stockfish chess engine installed on your system

## Installation (Sample can be downloaded from releases section.)

### 1. Install Python Dependencies

```powershell
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate

# Install required packages
pip install -r requirements.txt
```

### 2. Install Stockfish Engine

Download and install Stockfish from: https://stockfishchess.org/download/

**Windows:**
- Download the Windows executable
- Extract it to a location (e.g., `C:\Program Files\Stockfish\`)
- Add to PATH or provide the full path when running the game

**Linux:**
```bash
sudo apt-get install stockfish
```

**macOS:**
```bash
brew install stockfish
```

## Usage

### Quick Start

**Command-Line Version:**
```powershell
python main.py
```

**GUI Version (Graphical Interface):**
```powershell
python chess_gui.py
```


### Run with VS Code tasks

- Use the built-in task "Run Chess GUI" to start the app.
- Use the built-in task "Build Windows EXE" to package a distributable.
### Game Setup

When you start the game, you'll be prompted to:
1. Choose your color (white/black)
2. Set AI difficulty (0.5-10 seconds thinking time)
3. Optionally specify a custom Stockfish path

### Making Moves

Enter moves in UCI notation:
- `e2e4` - Move piece from e2 to e4
- `g1f3` - Move knight from g1 to f3
- `e7e8q` - Pawn promotion (to queen)

### Special Commands

- `help` - Display move format help
- `undo` - Take back the last move (yours and AI's)
- `quit` or `exit` - End the game

### Example Game Session

```
Choose your color (white/black) [white]: white
AI difficulty - thinking time in seconds (0.5-10) [1.0]: 1.5

♟ Chess Game - Play against Stockfish ♟
========================================
You are playing as: White
AI difficulty (thinking time): 1.5s

========================================
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
========================================
Turn: White
Legal moves: 20

Your move (e.g., 'e2e4' or 'quit'): e2e4
```

## Project Structure

```
New folder/
├── main.py              # Command-line chess game
├── chess_gui.py         # GUI version with tkinter ✨NEW
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── .gitignore          # Git ignore rules
├── .venv/              # Virtual environment
└── .github/
    └── copilot-instructions.md
```

## Dependencies

- **python-chess** (1.999): Chess game logic and move validation
- **stockfish** (3.28.0): Python wrapper for Stockfish engine
- **requests** (2.31.0): HTTP library for fetching online games

## How to Use New Features

### 💡 Hints
1. Click the **"💡 Hint"** button during your turn
2. The best move will be highlighted in sky blue
3. Click again to hide the hint

### 💾 Save & Load Games
- **Save PGN**: Export your current game to a .pgn file
- **Load PGN**: Import and replay any chess game

### 📊 Game Review
1. Click **"⚙️ Accounts"** to set up your usernames:
   - Enter your Lichess username
   - Enter your Chess.com username
   - Click Save
2. Click **"📊 Review"** to fetch your recent games
3. View game details including opponents, results, and dates

### 🔍 Game Analysis (Review Mode)
1. **Load a PGN file** with "Load PGN" button
2. Use navigation buttons to step through moves:
   - **⏮ Start**: Go to beginning
   - **◀ Prev**: Previous move
   - **Next ▶**: Next move
   - **End ⏭**: Go to end
3. **Watch evaluation bar** change with each move (left side of board)
   - White advantage: Bar goes down (white area)
   - Black advantage: Bar goes up (black area)
   - Center red line = Equal position
4. **Click "🔍 Analyze All Moves"** to get full game analysis:
   - Finds blunders (❌ -2.0 or worse)
   - Finds mistakes (⚠️ -1.0 to -2.0)
   - Finds inaccuracies (?! -0.5 to -1.0)
   - Shows evaluation changes
5. **Learn from mistakes** and improve your game!

### 🎨 Themes
1. Click **"🎨 Theme"** button
2. Choose from 6 beautiful themes:
   - **Classic**: Traditional brown & beige
   - **Blue**: Cool blue tones
   - **Green**: Natural green board
   - **Purple**: Royal purple theme
   - **Modern**: Lichess-style green
   - **Dark**: Dark mode for night play
3. Preview before applying
4. Theme auto-saves for next session

### 📊 Evaluation Bar
- **Left side of board** shows live position evaluation
- **Updates automatically** after each move
- **White advantage**: Bar extends downward (white area grows)
- **Black advantage**: Bar extends upward (black area grows)
- **Equal**: Red line in center
- **Numbers**: +2.0 = White up 2 pawns, -1.5 = Black up 1.5 pawns
- **±∞**: Winning/losing position or mate detected

### 📜 Move History
- Click **"📜 Moves"** to see all moves in the current game
- Moves are displayed in standard algebraic notation (SAN)

## Troubleshooting

### Stockfish Not Found

If you see "Stockfish engine not found":
1. Make sure Stockfish is installed
2. Add Stockfish to your system PATH, or
3. Provide the full path when prompted at startup

### Virtual Environment Issues

Make sure to activate the virtual environment before running:
```powershell
.\venv\Scripts\Activate
```

### Move Format Errors

Use UCI notation: `source_square + destination_square`
- Valid: e2e4, g1f3, a7a8q
- Invalid: e4, Nf3, O-O (use e1g1 for castling)

## Future Enhancements

- [ ] GUI interface with tkinter or pygame
- [ ] Save/load game functionality (PGN format)
- [ ] Multiple difficulty presets
- [ ] Game analysis and move suggestions
- [ ] Opening book integration
- [ ] Time controls and clocks

## License

This project is open source and available for educational purposes.

## Credits

- Chess engine: [Stockfish](https://stockfishchess.org/)
- Python chess library: [python-chess](https://python-chess.readthedocs.io/)

---

Enjoy your game! ♔♕♖♗♘♙
>>>>>>> d8e6fd4 (Initial commit: ChessGUI with GUI, review, Windows build)
