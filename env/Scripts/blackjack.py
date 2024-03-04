import random
from functools import reduce
 

def create_suit(suit):
    cards = [] 
    for i in range(1,14):
        card = {
            "value":i,
            "suit":suit,
        }
        cards.append(card)
    return cards

def create_deck():
    suits=['Hearts','Clubs','Diamonds','Spades']
    cards=[]
    for i in suits:
        cards.extend(create_suit(i))
    for i in cards:
        num_value= i.get('value')
        card_suit= i.get('suit')
        if num_value == 1:
            i['face'] = f'Ace of {card_suit}'
            i['value'] = 11
        elif num_value == 11:
             i['face'] = f'Jack of {card_suit}'
             i['value'] = 10
        elif num_value == 12:
             i['face'] = f'Queen of {card_suit}'
             i['value'] = 10
        elif num_value == 13:
            i['face'] = f'King of {card_suit}'
            i['value'] = 10
        else:
            i['face'] = f'{num_value} of {card_suit}'
    return cards

def deal(the_deck):
    random.shuffle(the_deck)
    hand = [the_deck.pop(random.randint(1,len(the_deck)-1)),the_deck.pop(random.randint(1,len(the_deck)-1))]
    return hand

def count_hand(hand):
    count = sum(item['value'] for item in hand)
    num_aces = sum(1 for item in hand if item['face'] == 'Ace')

    while count > 21 and num_aces > 0:
        count -= 10 
        num_aces -= 1

    return count


while input('Would You Like to play?').lower()=='yes':
    deck = create_deck()
    user = deal(deck)
    dealer= deal(deck)
    user_count = count_hand(user)
    user_hand_faces = ', '.join(item['face'] for item in user)
    dealer_hand_faces = ', '.join(item['face'] for item in dealer)
    print(f"Your hand {user_hand_faces}: You Score {user_count}")
    print(f"Dealer is showing {dealer[0]['face']}, hidden card: {dealer[0]['value']}")
    if user[0]['value'] +user[1]['value']== 21:
        print('You have BLACK JACK!! You win!!')
    else:
        while  input('Would You Like to Hit?').lower()=='yes':
            user.append(deck.pop(random.randint(1,len(deck)-1)))
            user_count= count_hand(user)
            user_hand_faces = ', '.join(item['face'] for item in user)
            print(f"Your hand { user_hand_faces}: You Score {count_hand(user)}")
            print(f"Dealer is showing {dealer[0]['face']}, hidden card: {dealer[0]['value']}")
            if user_count > 21:
                print(f'You BUSTED! : {user_hand_faces}')
                break
        while count_hand(dealer) < user_count and user_count <=21:
            dealer.append(deck.pop(random.randint(1,len(deck)-1)))
            dealer_hand_faces = ', '.join(item['face'] for item in dealer)
            print( dealer_hand_faces,count_hand(dealer))
        if user_count < count_hand(dealer) and count_hand(dealer) >21:
            print(f'Dealer BUSTED with {count_hand(dealer)} : {dealer_hand_faces}! You win')
        elif user_count > count_hand(dealer) and user_count <= 21:
            print(f'You Won! You had {count_hand(user)} :{user_hand_faces}and Dealer had {count_hand(dealer)} :{dealer_hand_faces}')
        elif user_count == count_hand(dealer):
            print(f'Draw match. You had {user_count} :{user_hand_faces} dealer had {count_hand(dealer)} :{dealer_hand_faces}')
        else:
            dealer_hand_faces = ', '.join(item['face'] for item in dealer)
            print(f'You Lost. Dealer had {count_hand(dealer)}: {dealer_hand_faces} and you had {count_hand(user)}')
else:
    print('Have a great day')