from random import shuffle
from time import sleep
from random import choice

# ♡ ♢ ♧ ♤


def deck():
    cards = [(2, '2♡'), (2, '2♤'), (3, '3♡'), (3, '3♤'), (4, '4♡'), (4, '4♤'),
             (5, '5♡'), (5, '5♤'), (6, '6♡'), (6, '6♤'), (7, '7♡'), (7, '7♤'),
             (8, '8♡'), (8, '8♤'), (9, '9♡'), (9, '9♤'), (10, '10♡'), (10,
                                                                       '10♤'),
             (10, 'Jack♡'), (10, 'Jack♤'), (10, 'Queen♡'), (10, 'Queen♤'),
             (10, 'King♡'), (10, 'King♤'), (11, 'Ace♡'), (11, 'Ace♤'),
             (2, '2♢'), (2, '2♧'), (3, '3♢'), (3, '3♧'), (4, '4♢'), (4, '4♧'),
             (5, '5♢'), (5, '5♧'), (6, '6♢'), (6, '6♧'), (7, '7♢'), (7, '7♧'),
             (8, '8♢'), (8, '8♧'), (9, '9♢'), (9, '9♧'), (10, '10♢'), (10,
                                                                       '10♧'),
             (10, 'Jack♢'), (10, 'Jack♧'), (10, 'Queen♢'), (10, 'Queen♧'),
             (10, 'King♢'), (10, 'King♧'), (11, 'Ace♢'), (11, 'Ace♧')]
    shuffle(cards)
    return cards


def main():

    wins = 0
    loses = 0
    ties = 0

    text = ''
    while text != 'quit':

        card_format = []
        player_hand = []
        cards = deck()
        first_player = cards.pop()
        second_player = cards.pop()

        card_format.append(first_player[1])
        card_format.append(second_player[1])

        player_hand.append(first_player[0])
        player_hand.append(second_player[0])

        first_dealer = cards.pop()
        second_dealer = cards.pop()

        print('Wins: {}\nLoses: {}\nStandoffs: {}'.format(wins, loses, ties))
        print(
            '\n---------------------------------------------------------------\n'
        )

        print('Dealing cards...')
        sleep(3)
        text = ''
        while text != 'quit':

            print('Your hand: {}'.format(card_format))
            print('Dealer\'s hand: {}, *'.format(first_dealer[1]))

            if (first_player[0] + second_player[0] == 21) and (
                    first_dealer[0] + second_dealer[0] == 21):
                print('Dealer is revealing his hole card...')
                sleep(2)
                print('Dealer\'s hand: {}, {}'.format(first_dealer[1],
                                                     second_dealer[1]))
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
                print('Dealer\'s hand: {}, {}'.format(first_dealer[1],
                                                     second_dealer[1]))
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
                card_format.append(third_player[1])
                print(
                    '\n---------------------------------------------------------------\n'
                )
                if first_player[0] + second_player[0] + third_player[0] > 21:
                    print('You busted!')
                    print(
                        '\n---------------------------------------------------------------\n'
                    )
                    loses += 1
                    break

                else:
                    continue

            elif text == '2':
                total = 0
                for card in range(len(player_hand)):
                    total += player_hand[card]

                if total > first_dealer[0] + second_dealer[0]:
                    print('Dealer is revealing his hole card...')
                    sleep(2)
                    print('Dealer\'s hand: {}, {}'.format(
                        first_dealer[1], second_dealer[1]))
                    print('You win!')
                    print(
                        '\n---------------------------------------------------------------\n'
                    )
                    wins += 1
                    player_hand.clear()
                    break

                elif total < first_dealer[0] + second_dealer[0]:
                    print('Dealer is revealing his hole card...')
                    sleep(2)
                    print('Dealer\'s hand: {}, {}'.format(
                        first_dealer[1], second_dealer[1]))
                    print('You lose!')
                    print(
                        '\n---------------------------------------------------------------\n'
                    )
                    loses += 1
                    player_hand.clear()
                    break

                elif total == first_dealer[0] + second_dealer[0]:
                    print('Dealer is revealing his hole card...')
                    sleep(2)
                    print('Dealer\'s hand: {}, {}'.format(
                        first_dealer[1], second_dealer[1]))
                    print('Standoff!')
                    print(
                        '\n---------------------------------------------------------------\n'
                    )
                    ties += 1
                    player_hand.clear()
                    break

            elif text == 'quit':
                break

            else:
                print('Invalid Choice!')


if __name__ == '__main__':
    main()
