from random import shuffle
from time import sleep
from random import choice

# ♡ ♢ ♧ ♤


def deck():
    cards = [(2, '[2♡]'), (2, '[2♤]'), (3, '[3♡]'), (3, '[3♤]'), (4, '[4♡]'),
             (4, '[4♤]'), (5, '[5♡]'), (5, '[5♤]'), (6, '[6♡]'), (6, '[6♤]'),
             (7, '[7♡]'), (7, '[7♤]'), (8, '[8♡]'), (8, '[8♤]'), (9, '[9♡]'),
             (9, '[9♤]'), (10, '[10♡]'), (10, '[10♤]'), (10, '[J♡]'),
             (10, '[J♤]'), (10, '[Q♡]'), (10, '[Q♤]'), (10, '[K♡]'), (10,
                                                                      '[K♤]'),
             (11, '[A♡]'), (11, '[A♤]'), (2, '[2♢]'), (2, '[2♧]'), (3, '[3♢]'),
             (3, '[3♧]'), (4, '[4]♢'), (4, '[4♧]'), (5, '[5♢]'), (5, '[5♧]'),
             (6, '[6♢]'), (6, '[6♧]'), (7, '[7]♢'), (7, '[7♧]'), (8, '[8♢]'),
             (8, '[8♧]'), (9, '[9♢]'), (9, '[9♧]'), (10, '[10♢]'),
             (10, '[10♧]'), (10, '[J♢]'), (10, '[J♧]'), (10, '[Q♢]'),
             (10, '[Q♧]'), (10, '[K♢]'), (10, '[K♧]'), (11, '[A♢]'), (11,
                                                                      '[A♧]')]
    shuffle(cards)
    return cards


def hand_value(hand):
    aces = []
    non_aces = []
    if 11 in hand:
        for card in hand:
            if card == 11:
                aces.append(card)
            else:
                non_aces.append(card)
        for card in aces:
            if sum(aces) + sum(non_aces) > 21:
                aces.remove(card)
                non_aces.append(1)
            else:
                non_aces.append(card)
                aces.remove(card)
        hand = non_aces
        return hand
    else:
        return hand


def cards_in_hand(format):
    hands = ''
    for cards in format:
        hands += cards
    return hands


def main():

    wins = 0
    loses = 0
    ties = 0

    text = ''
    while text != 'quit':

        player_cards = []
        player_hand = []
        cards = deck()

        first_dealer = cards.pop()
        first_player = cards.pop()
        second_dealer = cards.pop()
        second_player = cards.pop()

        player_cards.append(first_player[1])
        player_cards.append(second_player[1])

        player_hand.append(first_player[0])
        player_hand.append(second_player[0])

        dealer_hand = []
        dealer_cards = []

        dealer_hand.append(first_dealer[0])
        dealer_hand.append(second_dealer[0])

        dealer_cards.append(first_dealer[1])
        dealer_cards.append(second_dealer[1])

        print('Wins: {}\nLoses: {}\nStandoffs: {}'.format(wins, loses, ties))
        print(
            '\n---------------------------------------------------------------\n'
        )

        print(
            'Dealer must draw to 16, and stand on all 17\'s\nDealing cards...')
        sleep(3)
        text = ''
        while text != 'quit':

            card_format = cards_in_hand(player_cards)
            dealer_format = cards_in_hand(dealer_cards)
            print('Your hand: {}'.format(card_format))
            print('Dealer\'s hand: {}, *'.format(dealer_cards[0]))
            player_hand = hand_value(player_hand)

            if (first_player[0] + second_player[0] == 21) and (
                    first_dealer[0] + second_dealer[0] == 21):
                print('Dealer is revealing his hole card...')
                sleep(2)
                print('Dealer\'s hand: {}, {}'.format(dealer_format))
                print('Standoff!')
                print(
                    '\n---------------------------------------------------------------\n'
                )
                ties += 1
                break

            elif first_player[0] + second_player[0] == 21:
                print('Player has BLACKJACK!')
                print(
                    '\n---------------------------------------------------------------\n'
                )
                wins += 1

                break

            elif first_dealer[0] + second_dealer[0] == 21:
                print('Dealer is revealing his hole card...')
                print('Dealer\'s hand: {}, {}'.format(dealer_format))
                print('Dealer has BLACKJACK!')
                print(
                    '\n---------------------------------------------------------------\n'
                )
                sleep(1)
                loses += 1

                break

            #choices = ['1', '2']
            text = input('Hit or stand?\n"1": hit\n"2": stand\n').strip()
            #text = choice(choices)
            if text == '1':
                print('Dealing card...')
                sleep(2)
                third_player = cards.pop()
                player_hand.append(third_player[0])
                player_cards.append(third_player[1])
                print(
                    '\n---------------------------------------------------------------\n'
                )

                player_hand = hand_value(player_hand)

                total = 0
                for card in range(len(player_hand)):
                    total += player_hand[card]

                if total > 21:
                    print('Your hand: {}'.format(card_format))
                    print('You busted!')
                    print(
                        '\n---------------------------------------------------------------\n'
                    )
                    sleep(1)
                    loses += 1
                    break

                else:
                    continue

            elif text == '2':
                total = 0
                for card in range(len(player_hand)):
                    total += player_hand[card]

                print('Dealer is revealing his hole card...')
                sleep(2)
                print('Dealer\'s hand: {}'.format(dealer_format))

                while True:
                    # for num in range(len(dealer_hand)):
                    dealer_total = sum(dealer_hand)
                    if dealer_total <= 16:
                        print('Dealer is drawing a card...')
                        sleep(2)
                        third_dealer = cards.pop()
                        dealer_total += third_dealer[0]
                        dealer_hand.append(third_dealer[0])
                        dealer_cards.append(third_dealer[1])
                        dealer_format = cards_in_hand(dealer_cards)
                        print('Dealer\'s hand: {}'.format(dealer_format))
                        continue
                    else:
                        break

                if dealer_total > 21:
                    print('Dealer busted!\nYou win!')
                    print(
                        '\n---------------------------------------------------------------\n'
                    )
                    wins += 1
                    break

                elif total > dealer_total:
                    print('You win!')
                    print(
                        '\n---------------------------------------------------------------\n'
                    )
                    wins += 1
                    break

                elif total < dealer_total:
                    print('You lose!')
                    print(
                        '\n---------------------------------------------------------------\n'
                    )
                    loses += 1
                    break

                elif total == dealer_total:
                    print('Standoff!')
                    print(
                        '\n---------------------------------------------------------------\n'
                    )
                    ties += 1
                    break

            elif text == 'quit':
                break

            else:
                print('Invalid Choice!')
                print(
                    '\n---------------------------------------------------------------\n'
                )


if __name__ == '__main__':
    main()
