"""
Chess Game with Stockfish AI
A command-line chess game where you can play against the Stockfish engine.
"""

import chess
import chess.engine
import sys
import os
from pathlib import Path


class ChessGame:
    def __init__(self, stockfish_path=None):
        """Initialize the chess game with Stockfish engine."""
        self.board = chess.Board()
        self.engine = None
        
        # Try to find Stockfish executable
        if stockfish_path and os.path.exists(stockfish_path):
            self.engine_path = stockfish_path
        else:
            # Common Stockfish locations
            possible_paths = [
                "stockfish\\stockfish-windows-x86-64-avx2.exe",  # Local project folder
                "stockfish\\stockfish.exe",
                "stockfish.exe",  # Windows in PATH
                "stockfish",  # Unix in PATH
                "/usr/bin/stockfish",  # Linux
                "/usr/local/bin/stockfish",  # macOS
                r"C:\Program Files\Stockfish\stockfish.exe",
            ]
            
            self.engine_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    self.engine_path = path
                    break
                elif path in ["stockfish", "stockfish.exe"]:
                    self.engine_path = path
                    break
        
        if self.engine_path:
            try:
                self.engine = chess.engine.SimpleEngine.popen_uci(self.engine_path)
                print(f"✓ Stockfish engine loaded from: {self.engine_path}\n")
            except Exception as e:
                print(f"⚠ Warning: Could not load Stockfish engine: {e}")
                print("You can still play, but won't have an AI opponent.\n")
        else:
            print("⚠ Stockfish engine not found. Install it or provide the path.")
            print("Download from: https://stockfishchess.org/download/\n")
    
    def display_board(self):
        """Display the current board state."""
        print("\n" + "="*40)
        print(self.board)
        print("="*40)
        print(f"Turn: {'White' if self.board.turn else 'Black'}")
        print(f"Legal moves: {self.board.legal_moves.count()}")
        print()
    
    def get_player_move(self):
        """Get and validate a move from the player."""
        while True:
            try:
                move_str = input("Your move (e.g., 'e2e4' or 'quit'): ").strip().lower()
                
                if move_str in ['quit', 'exit', 'q']:
                    return None
                
                if move_str == 'help':
                    print("\nMove format: starting_square + ending_square")
                    print("Examples: e2e4, g1f3, e7e8q (pawn promotion to queen)")
                    print("Special: 'quit' to exit, 'undo' to take back move\n")
                    continue
                
                if move_str == 'undo' and len(self.board.move_stack) > 0:
                    self.board.pop()
                    if len(self.board.move_stack) > 0:  # Undo AI move too
                        self.board.pop()
                    print("✓ Last move undone\n")
                    return 'undo'
                
                move = chess.Move.from_uci(move_str)
                
                if move in self.board.legal_moves:
                    return move
                else:
                    print("✗ Illegal move! Try again.")
                    
            except ValueError:
                print("✗ Invalid format! Use format like 'e2e4' or type 'help'")
    
    def get_stockfish_move(self, time_limit=1.0):
        """Get the best move from Stockfish engine."""
        if not self.engine:
            print("✗ Stockfish engine not available!")
            return None
        
        print("🤔 Stockfish is thinking...")
        result = self.engine.play(self.board, chess.engine.Limit(time=time_limit))
        return result.move
    
    def check_game_over(self):
        """Check if the game is over and display result."""
        if self.board.is_checkmate():
            winner = "Black" if self.board.turn else "White"
            print(f"\n🏆 Checkmate! {winner} wins!")
            return True
        elif self.board.is_stalemate():
            print("\n🤝 Stalemate! Game is a draw.")
            return True
        elif self.board.is_insufficient_material():
            print("\n🤝 Draw due to insufficient material.")
            return True
        elif self.board.is_fifty_moves():
            print("\n🤝 Draw due to fifty-move rule.")
            return True
        elif self.board.is_repetition():
            print("\n🤝 Draw due to threefold repetition.")
            return True
        
        if self.board.is_check():
            print("⚠ Check!")
        
        return False
    
    def play(self, player_color='white', difficulty=1.0):
        """Main game loop."""
        print("\n♟ Chess Game - Play against Stockfish ♟")
        print("=" * 40)
        print(f"You are playing as: {player_color.capitalize()}")
        print(f"AI difficulty (thinking time): {difficulty}s")
        print("\nCommands: type 'help' for move format, 'quit' to exit, 'undo' to take back")
        
        player_is_white = (player_color.lower() == 'white')
        
        while not self.board.is_game_over():
            self.display_board()
            
            # Player's turn
            if self.board.turn == chess.WHITE and player_is_white:
                move = self.get_player_move()
                if move is None:
                    print("\n👋 Thanks for playing!")
                    break
                if move == 'undo':
                    continue
                self.board.push(move)
                
            # AI's turn
            elif self.board.turn == chess.BLACK and not player_is_white:
                move = self.get_player_move()
                if move is None:
                    print("\n👋 Thanks for playing!")
                    break
                if move == 'undo':
                    continue
                self.board.push(move)
            
            # Stockfish's turn
            else:
                if not self.engine:
                    print("✗ Cannot continue without Stockfish engine!")
                    break
                    
                ai_move = self.get_stockfish_move(difficulty)
                if ai_move:
                    self.board.push(ai_move)
                    print(f"✓ Stockfish played: {ai_move}\n")
                else:
                    print("✗ Stockfish couldn't find a move!")
                    break
            
            # Check game status
            if self.check_game_over():
                self.display_board()
                break
        
        # Cleanup
        if self.engine:
            self.engine.quit()
    
    def close(self):
        """Clean up resources."""
        if self.engine:
            self.engine.quit()


def main():
    """Main entry point."""
    print("\n" + "="*50)
    print("    ♔ CHESS GAME WITH STOCKFISH AI ♔")
    print("="*50)
    
    # Get player preferences
    print("\nSetup:")
    color = input("Choose your color (white/black) [white]: ").strip().lower()
    if color not in ['white', 'black']:
        color = 'white'
    
    difficulty = input("AI difficulty - thinking time in seconds (0.5-10) [1.0]: ").strip()
    try:
        difficulty = float(difficulty)
        difficulty = max(0.5, min(10.0, difficulty))
    except ValueError:
        difficulty = 1.0
    
    # Optional: specify custom Stockfish path
    custom_path = input("Stockfish path (press Enter to auto-detect): ").strip()
    if not custom_path:
        custom_path = None
    
    # Start game
    game = ChessGame(stockfish_path=custom_path)
    
    try:
        game.play(player_color=color, difficulty=difficulty)
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    finally:
        game.close()


if __name__ == "__main__":
    main()
