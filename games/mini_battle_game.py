import random

def mini_battle_game(player_health, *moves):
    enemy_number = 1  # Track enemies defeated

    while player_health > 0:
        # Step 1: Get new moves from user for each new enemy
        moves_input = input("\nSpecify your moves for this enemy (e.g., punch, heal, defend): ")
        moves = [move.strip() for move in moves_input.split(',') if move.strip()]

        if not moves:
            print("⚠️ No moves entered. Exiting the game.")
            break
        
        # Step 2: Generate a new enemy with fresh health for each encounter
        enemy_health = random.randint(40, 70)
        print(f"\n👾 Enemy {enemy_number} appears with {enemy_health} HP!")

        # Step 3: Player's attack phase
        total_player_damage = 0
        defense_used = False  # Track if defense was used in this turn

        for move in moves:
            if move.lower() == "heal":  # Healing move
                heal_amount = random.randint(5, 15)  # Heal between 5 to 15 HP
                player_health += heal_amount
                print(f"💉 You healed for {heal_amount} HP! Your health is now {player_health}.")
                continue  # Skip further moves for this turn

            if move.lower() == "defend":  # Defense move
                defense_used = True
                print("🛡️ You are preparing to defend against the next enemy attack!")
                continue  # Skip further moves for this turn

            # Determine if the move is physical or magical
            if move.lower() == 'kick':
                move_type = 'physical'
                damage = random.randint(10, 20)
            elif move.lower() == 'fireball':
                move_type = 'magical'
                damage = random.randint(15, 30)
            else:
                move_type = 'physical'
                damage = random.randint(5, 15)

            # Critical hit chance (20%) for magical moves only
            if move_type == 'magical' and random.random() < 0.2:
                damage *= 2
                print(f"🔥 CRITICAL HIT! {move.upper()} ({move_type}) dealt {damage} damage!")
            else:
                print(f"{move.capitalize()} ({move_type}) dealt {damage} damage.")

            enemy_health -= damage
            total_player_damage += damage

            if enemy_health <= 0:
                break  # Stop if enemy defeated

        # Step 4: After attack phase
        print(f"\n➡️ Total damage dealt: {total_player_damage}")

        if enemy_health <= 0:
            print(f"✅ Enemy {enemy_number} defeated!")
        else:
            print(f"⚠️ Enemy survived with {enemy_health} HP!")

        # Step 5: Enemy counter-attack
        enemy_attack = random.randint(10, 25)

        # If defense was used, reduce damage by 50%
        if defense_used:
            enemy_attack = enemy_attack // 2
            print(f"🛡️ Your defense reduced the enemy attack by 50%!")

        player_health -= enemy_attack
        print(f"💥 Enemy attacks you for {enemy_attack} damage!")

        # Step 6: Check player's health
        if player_health <= 0:
            print("\n💀 You were defeated! GAME OVER.")
            break
        else:
            print(f"❤️ You survived with {player_health} HP.")

        # Step 7: Ask player if they want to continue to the next enemy
        choice = input("\nDo you want to move to the next enemy? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\n👋 Thanks for playing! You survived with", player_health, "HP!")
            break

        enemy_number += 1  # Increment the enemy number after each round

# --- Entry point when running from terminal ---

if __name__ == "__main__":
    print("🎮 Welcome to Mini Battle Game!")
    print("Tip: Enter your moves separated by commas (e.g., punch, heal, defend)\n")

    # Step 1: Start game with user-provided moves
    mini_battle_game(100)

# mini_battle_game.py

# This code is a mini battle game where the player can choose any number of moves (* args argument is used) to attack enemies.
# The game generates random enemies with varying health and allows the player to use moves like "punch", "heal", and "defend".


# Action Moves: Punch, Kick, Fireball, Lightning Strike, Slash, Arrow Shot
# Defensive Moves: Heal, Defend, Evade, Dodge Roll
# Healing Moves: Heal, Regeneration, Potion, Bandage
# Special Moves: Critical Strike, Summon, Berserk, Stun
# Status Effect Moves: Poison, Burn, Freeze, Confuse


# The player can heal themselves, defend against enemy attacks, and deal damage to enemies.
# The game includes critical hit chances and allows the player to continue battling until they choose to stop or are defeated.
# The game is interactive and provides feedback on the player's actions, including total damage dealt and remaining health.
# The game is structured to be easy to read and understand, with clear function names and comments explaining each part.