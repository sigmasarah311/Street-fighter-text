import random
import time

def print_health(p1, p2):
    print(f"\n[HP] Player 1: {p1} | Player 2: {p2}")

def punch():
    return random.randint(5, 15)

def game():
    print("=== STREET FIGHTER: TEXT EDITION ===")
    print("Type 'punch' to attack. First to 0 HP loses.\n")

    p1_hp = 100
    p2_hp = 100

    while p1_hp > 0 and p2_hp > 0:
        # Player 1 turn
        move = input("Player 1's move (punch): ").strip().lower()
        if move == 'punch':
            dmg = punch()
            p2_hp -= dmg
            print(f"Player 1 punches Player 2 for {dmg} damage!")
        else:
            print("Invalid move!")

        if p2_hp <= 0:
            break

        time.sleep(0.5)

        # Player 2 turn
        move = input("Player 2's move (punch): ").strip().lower()
        if move == 'punch':
            dmg = punch()
            p1_hp -= dmg
            print(f"Player 2 punches Player 1 for {dmg} damage!")
        else:
            print("Invalid move!")

        print_health(p1_hp, p2_hp)
        time.sleep(0.5)

    # Game result
    if p1_hp <= 0:
        print("\n🎉 Player 2 WINS!")
    else:
        print("\n🎉 Player 1 WINS!")

if __name__ == "__main__":
    game()
