import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

def start_game():
    print('Start the Game')

    player_one = Player('Mainor')
    player_two = Player('Lucas')
    deck = Deck()
    deck.shuffle()
    total_cards = len(deck.all_cards)
    for i in range(1,total_cards+1):
        card = deck.deal_one()
        if i%2 == 0:
            player_one.add_cards(card)
        else:
            player_two.add_cards(card)

    print(player_one)
    print(player_two)

    winner = ''
    game_on = True
    at_war = False
    war_cars = []
    while game_on:
        if len(player_one.all_cards) == 0:
            winner = player_two
            game_on = False
            break
        if len(player_two.all_cards) == 0:
            winner = player_one
            game_on = False
            break
        p1_card = player_one.remove_one()
        print(f'Player {player_one.name} card is {p1_card} with value {p1_card.value}')
        p2_card = player_two.remove_one()
        print(f'Player {player_two.name} card is {p2_card} with value {p2_card.value}')
        if p1_card.value == p2_card.value:
            at_war = True
            for i in range(1,4):
                if len(player_one.all_cards) > 0:
                    war_cars.append(player_one.remove_one())
                if len(player_two.all_cards) > 0:
                    war_cars.append(player_two.remove_one())
            war_cars_output = ''
            for card in war_cars:
                war_cars_output += f'{card} | '
            print(f'at war!!! cards on war: [{war_cars_output[0:len(war_cars_output)-2]}]')
        elif p1_card.value > p2_card.value:
            player_two.add_cards([p1_card, p2_card])
            if at_war:
                player_two.add_cards(war_cars)
                war_cars = []
                at_war = False
            print(f'Win for {player_one}')
            print(f'Loss for {player_two}')
        else:
            player_one.add_cards([p1_card, p2_card])
            if at_war:
                player_one.add_cards(war_cars)
                war_cars = []
                at_war = False
            print(f'Win for {player_two}')
            print(f'Loss for {player_one}')

        print('------- next round -------')

    if winner != '':
        print(f'{winner.name} IS THE WINNER!!')

    print ('Game Over!')

if __name__ == '__main__':
    start_game()