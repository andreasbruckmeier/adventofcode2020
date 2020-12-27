class Player:

    def __init__(self, cards):
        self.cards = cards
        self.history = []

    def get_slice_of_deck(self, number):
        return self.cards[:number]

    def is_out_of_cards(self):
        return len(self.cards) == 0

    def draw(self):
        if not self.cards:
            return None
        self.history.append('-'.join(str(x) for x in self.cards))
        max_card = self.cards[0]
        self.cards.remove(max_card)
        return max_card

    def remaining(self):
        return len(self.cards)

    def is_replay(self):
        return '-'.join(str(x) for x in self.cards) in self.history

    def take_win(self, cards):
        self.cards += cards

    def get_score(self):
        score = 0
        mult = 1
        for i in range(len(self.cards) -1, -1, -1):
            score += mult * self.cards[i]
            mult += 1
        
        return score

def combat_task1(player1, player2, level = 0):

    player1 = Player(player1)
    player2 = Player(player2)

    while True:
        card_player_1 = player1.draw()
        card_player_2 = player2.draw()
        if card_player_1 > card_player_2:
            player1.take_win([card_player_1,card_player_2])
        else:
            player2.take_win([card_player_2,card_player_1])
        if player1.is_out_of_cards():
            return player2.get_score()
        if player2.is_out_of_cards():
            return player1.get_score()

def combat_task2(player1, player2, level = 0):

    player1 = Player(player1)
    player2 = Player(player2)

    while True:

        if player1.is_replay() or player2.is_replay():
            return True

        card_player_1 = player1.draw()
        card_player_2 = player2.draw()

        # one play has not enough cards on Player
        if player1.remaining() < card_player_1 or player2.remaining() < card_player_2:
            if card_player_1 > card_player_2:
                player1.take_win([card_player_1,card_player_2])
            else:
                player2.take_win([card_player_2,card_player_1])
        else:
            res = combat_task2(player1.get_slice_of_deck(card_player_1), \
                               player2.get_slice_of_deck(card_player_2), level + 1)
            if not res:
                player2.take_win([card_player_2,card_player_1])
            else:
                player1.take_win([card_player_1,card_player_2])

        if player1.is_out_of_cards():
            return player2.get_score() if level == 0 else False
        if player2.is_out_of_cards():
            return player1.get_score() if level == 0 else True

p1 = [31,24,5,33,7,12,30,22,48,14,16,26,18,45,4,42,25,20,46,21,40,38,34,17,50]
p2 = [1,3,41,8,37,35,28,39,43,29,10,27,11,36,49,32,2,23,19,9,13,15,47,6,44]

print("Task 1 result: {}".format(combat_task1(p1.copy(), p2.copy())))
print("Task 2 result: {}".format(combat_task2(p1.copy(), p2.copy())))
