"""
Test script to verify Chess.com API connectivity
"""
import requests
import json

def test_chesscom_api(username):
    """Test Chess.com API with the given username."""
    
    print(f"Testing Chess.com API for user: {username}")
    print("="*60)
    
    # Normalize username
    username = username.lower().strip()
    print(f"Normalized username: {username}\n")
    
    # Headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json'
    }
    
    try:
        # Test 1: Check if user exists
        print("Test 1: Checking if user profile exists...")
        profile_url = f"https://api.chess.com/pub/player/{username}"
        response = requests.get(profile_url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            print(f"❌ FAILED: User '{username}' not found!")
            print("   Please verify the username is correct.")
            return False
        elif response.status_code == 200:
            profile = response.json()
            print(f"✓ SUCCESS: Found user '{profile.get('username', username)}'")
            print(f"   Player ID: {profile.get('player_id', 'N/A')}")
            print(f"   Name: {profile.get('name', 'N/A')}")
        else:
            print(f"⚠ Warning: Unexpected status code: {response.status_code}")
        
        print()
        
        # Test 2: Get game archives
        print("Test 2: Fetching game archives...")
        archives_url = f"https://api.chess.com/pub/player/{username}/games/archives"
        response = requests.get(archives_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        archives = response.json()
        archive_list = archives.get('archives', [])
        
        if not archive_list:
            print("⚠ No game archives found. This account may not have played any games.")
            return True
        
        print(f"✓ SUCCESS: Found {len(archive_list)} months of games")
        print(f"   Latest month: {archive_list[-1]}")
        print()
        
        # Test 3: Get games from latest month
        print("Test 3: Fetching games from latest month...")
        latest_url = archive_list[-1]
        response = requests.get(latest_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        games_data = response.json()
        games = games_data.get('games', [])
        
        print(f"✓ SUCCESS: Found {len(games)} games in latest month")
        
        if games:
            print("\nLast 3 games:")
            for i, game in enumerate(games[-3:], 1):
                print(f"\n  Game {i}:")
                print(f"    White: {game.get('white', {}).get('username', 'Unknown')}")
                print(f"    Black: {game.get('black', {}).get('username', 'Unknown')}")
                print(f"    Result: {game.get('white', {}).get('result', '?')} vs {game.get('black', {}).get('result', '?')}")
                if 'url' in game:
                    print(f"    URL: {game['url']}")
        
        print("\n" + "="*60)
        print("✅ ALL TESTS PASSED! Chess.com API is working correctly.")
        return True
        
    except requests.exceptions.ConnectionError as e:
        print(f"\n❌ CONNECTION ERROR: {e}")
        print("   Your internet connection may be unstable.")
        print("   Try checking your network connection.")
        return False
    
    except requests.exceptions.Timeout:
        print("\n❌ TIMEOUT ERROR: Chess.com API is not responding")
        print("   The server may be slow or your connection is poor.")
        return False
    
    except requests.exceptions.HTTPError as e:
        print(f"\n❌ HTTP ERROR: {e}")
        print(f"   Status code: {response.status_code}")
        return False
    
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {type(e).__name__}")
        print(f"   Details: {e}")
        return False


if __name__ == "__main__":
    # Test with the username from settings
    import os
    
    settings_file = "chess_settings.json"
    
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            settings = json.load(f)
            username = settings.get('chesscom_username', '')
            
            if username:
                print(f"Found username in settings: {username}\n")
                test_chesscom_api(username)
            else:
                print("No Chess.com username found in settings!")
                print("Please enter your username:")
                username = input("> ").strip()
                if username:
                    test_chesscom_api(username)
    else:
        print("Settings file not found!")
        print("Please enter your Chess.com username:")
        username = input("> ").strip()
        if username:
            test_chesscom_api(username)
