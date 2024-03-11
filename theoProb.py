import matplotlib.pyplot as plt

probabilities = [0.75, 0.115, 0.039, 0.039, 0.039, 0.019]
labels = ['Losing Two Tickets', 'Breaking Even', 'Winning Two Tickets', 'Winning Three Tickets', 'Winning 5 Tickets', 'Winning Twenty Tickets']

plt.figure(figsize=(10, 6))
plt.bar(labels, probabilities, color='skyblue')

plt.title('Theoretical Probabilities of Sweat Suit Game Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Probability')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
