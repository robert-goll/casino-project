import random
import matplotlib.pyplot as plt
from collections import Counter

def sim_game(guess_suit, guess_num):
    card_suit = random.randint(1, 4)
    card_num = random.randint(1, 13)

    correct_suit = (guess_suit == card_suit)
    diff = min((guess_num - card_num) % 13, (card_num - guess_num) % 13)

    if not correct_suit:
        return -2
    else:
        if diff == 0:
            return 20
        elif diff == 1:
            return 5
        elif diff == 2:
            return 3
        elif diff == 3:
            return 2
        else:
            return 0


def sim_multi_games(num_rounds, guess_num, guess_suit, initial_tickets):
    total_tickets = 0
    for _ in range(num_rounds):
        outcome = sim_game(guess_num, guess_suit)
        total_tickets += outcome
    final_tickets = initial_tickets - total_tickets
    return final_tickets

num_simulations = 1000000
house_tickets_post_sims = []

for _ in range(num_simulations):
    guess_num = random.randint(1, 13)
    guess_suit = random.randint(1, 4)
    initial_tickets = 50
    final_tickets = sim_multi_games(30, guess_num, guess_suit, initial_tickets)
    house_tickets_post_sims.append(final_tickets)

frequency_counter = Counter(house_tickets_post_sims)
total_simulations = sum(frequency_counter.values())

plt.hist(house_tickets_post_sims, bins=20, edgecolor='black')
plt.xlabel('Final amount of tickets for the casino after 30 simulations')
plt.ylabel('Frequency')
plt.title('Distribution of Average Casino Tickets after 1,000,000 Simulations')
plt.show()

print("Value   Frequency   Percentage")
for value, frequency in frequency_counter.items():
    percentage = (frequency / num_simulations) * 100
    print(f"{value:<8} {frequency:<12} {percentage:.3f}%")
