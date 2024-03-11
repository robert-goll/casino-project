import matplotlib.pyplot as plt

probabilities_observed = [68.97, 20.69, 6.897, 3.345, 0, 0]
labels_observed = ['-2', '0', '2', '3', '5', '20']

plt.figure(figsize=(10, 6))
plt.bar(labels_observed, probabilities_observed, color='lightgreen')

plt.title('Observed Probabilities of Sweat Suit Game Outcomes')
plt.xlabel('Tickets Won')
plt.ylabel('Proportion (%)')

plt.tight_layout()
plt.show()