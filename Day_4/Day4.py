import os
import sys


class card:
    # initialize each card with it´s original image and it´s transposed image
    def __init__(self, matrix, transposed):
        self.matrix = matrix  # to check rows
        self.transposed = transposed  # to check columns


cards = []  # list of card objects
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()

    calls = lines[0].strip().split(",")

    i = 2
    while i < len(lines):
        matrix = []
        for j in range(5):
            line = lines[i+j].strip().split()
            matrix.append(line)
        # transpose each card-matrix
        transposed = list(map(list, zip(*matrix)))
        cards.append(card(matrix, transposed))
        i += 6

    winner = False
    for call in calls:
        for c in cards:
            for i in range(5):
                # check if called value is in the card matrix
                if call in c.matrix[i]:
                    c.matrix[i].remove(call)
                # check if called value is in the transposed card matrix
                if call in c.transposed[i]:
                    c.transposed[i].remove(call)
                # if a row of matrix or the transposed matrix is empty, we have a winning card
                if len(c.matrix[i]) == 0 or len(c.transposed[i]) == 0:
                    winning_card = c.matrix
                    last_call = call
                    winner = True
                    break
            if winner:
                break
        if winner:
            break

    # sum up the ramining card values
    sum = 0
    for i in range(len(winning_card)):
        for j in range(len(winning_card[i])):
            sum += int(winning_card[i][j])

    result = int(last_call)*sum
    print(result)
