dealer_card = ['2','3','4','5','6','7','8','9','t','a']
hard_totals = ['8','9','t','11','12','13','14','15','16','17']

def play_hand():
    while True:
        hand = input('Hand & Dealer: ')
        hand = hand.split()

        # hard totals
        if hand[0] == '17' or hand[0] == '18' or hand[0] == '19' or hand[0] == '20':
            print('stand')
        elif hand[0] == '11':
            print('double')
        elif hand[0] =='8':
            print('hit')
        elif hand[0] in hard_totals[5:-1]:
            if hand[1] in dealer_card[:5]:
                print('stand')
            else:
                print('hit')
        elif hand[0] == '12':
            if hand[1] in dealer_card[2:5]:
                print('stand')
            else:
                print('hit')
        elif hand[0] == 't':
            if hand[1] in dealer_card[:8]:
                print('double')
            else:
                print('hit')
        elif hand[0] == '9':
            if hand[1] in dealer_card[1:5]:
                print('double')
            else:
                print('hit')
        
        # aces
        elif hand[0] == 'a9':
            print('stand')
        elif hand[0] == 'a8':
            if hand[1] == '6':
                print('double')
            else:
                print('stand')
        elif hand[0] == 'a7':
            if hand[1] in dealer_card[:5]:
                print('double')
            elif hand[1] in dealer_card[5:7]:
                print('stand')
            else:
                print('hit')
        elif hand[0] == 'a6':
            if hand[1] in dealer_card[1:5]:
                print('double')
            else:
                print('hit')
        elif hand[0] == 'a5' or hand[0] == 'a4':
            if hand[1] in dealer_card[2:5]:
                print('double')
            else:
                print('hit')
        elif hand[0] == 'a3' or hand[0] == 'a2':
            if hand[1] in dealer_card[3:5]:
                print('double')
            else:
                print('hit')

        # pairs
        elif hand[0] == 'aa':
            print('split')
        elif hand[0] == 'tt':
            print("don't split")
        elif hand[0] == '88':
            print('split')
        elif hand[0] == '55':
            print("don't split")
        elif hand[0] == '99':
            if hand[1] == dealer_card[5] or hand[1] in dealer_card[8:]:
                print("don't split")
            else:
                print('split')
        elif hand[0] == '77':
            if hand[1] in dealer_card[:6]:
                print('split')
            else:
                print("don't split")
        elif hand[0] == '66':
            if hand[1] in dealer_card[:5]:
                print('split')
            else:
                print("don't split")
        elif hand[0] == '44':
            if hand[1] in dealer_card[3:5]:
                print('split')
            else:
                print("don't split")
        elif hand[0] == '33' or hand[0] == '22':
            if hand[1] in dealer_card[:6]:
                print('split')
            else:
                print("don't split")
        
play_hand()