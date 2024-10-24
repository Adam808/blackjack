from tkinter import *
from tkinter import ttk

# hard totals
def sixteen():
    hand.set('16')
def fifteen():
    hand.set('15')
def fourteen():
    hand.set('14')
def thirteen():
    hand.set('13')
def twelve():
    hand.set('12')
def eleven():
    hand.set('11')
def ten():
    hand.set('10')
def nine():
    hand.set('9')

#soft totals
def a9():
    hand.set('a9')
def a8():
    hand.set('a8')
def a7():
    hand.set('a7')
def a6():
    hand.set('a6')
def a5():
    hand.set('a5')
def a4():
    hand.set('a4')
def a3():
    hand.set('a3')
def a2():
    hand.set('a2')

# pairs
def aces():
    hand.set('aa')
def tens():
    hand.set('tt')
def nines():
    hand.set('99')
def eights():
    hand.set('88')
def sevens():
    hand.set('77')
def sixes():
    hand.set('66')
def fives():
    hand.set('55')
def fours():
    hand.set('44')
def threes():
    hand.set('33')
def twos():
    hand.set('22')

# dealer's hand
def dAce():
    dealer.set('a')
def dTen():
    dealer.set('10')
def dNine():
    dealer.set('9')
def dEight():
    dealer.set('8')
def dSeven():
    dealer.set('7')
def dSix():
    dealer.set('6')
def dFive():
    dealer.set('5')
def dFour():
    dealer.set('4')
def dThree():
    dealer.set('3')
def dTwo():
    dealer.set('2')

dealer_card = ['2','3','4','5','6','7','8','9','10','a']
hard_totals = ['9','10','11','12','13','14','15','16']

def play_hand():

    hand.get()
    dealer.get()
        
    # hard totals
    if hand.get() == '11':
        action.set('double')
    elif hand.get() in hard_totals[4:]:
        if dealer.get() in dealer_card[:5]:
            action.set('stand')
        else:
            action.set('hit')
    elif hand.get() == '12':
        if dealer.get() in dealer_card[2:5]:
            action.set('stand')
        else:
            action.set('hit')
    elif hand.get() == '10':
        if dealer.get() in dealer_card[:8]:
            action.set('double')
        else:
            action.set('hit')
    elif hand.get() == '9':
        if dealer.get() in dealer_card[1:5]:
            action.set('double')
        else:
            action.set('hit')
    
    # aces
    elif hand.get() == 'a9':
        action.set('stand')
    elif hand.get() == 'a8':
        if dealer.get() == '6':
            action.set('double')
        else:
            action.set('stand')
    elif hand.get() == 'a7':
        if dealer.get() in dealer_card[:5]:
            action.set('double')
        elif dealer.get() in dealer_card[5:7]:
            action.set('stand')
        else:
            action.set('hit')
    elif hand.get() == 'a6':
        if dealer.get() in dealer_card[1:5]:
            action.set('double')
        else:
            action.set('hit')
    elif hand.get() == 'a5' or hand == 'a4':
        if dealer.get() in dealer_card[2:5]:
            action.set('double')
        else:
            action.set('hit')
    elif hand.get() == 'a3' or hand == 'a2':
        if dealer.get() in dealer_card[3:5]:
            action.set('double')
        else:
            action.set('hit')

    # pairs
    elif hand.get() == 'aa':
        action.set('split')
    elif hand.get() == 'tt':
        action.set("don't split")
    elif hand.get() == '88':
        action.set('split')
    elif hand.get() == '55':
        action.set("don't split")
    elif hand.get() == '99':
        if dealer.get() == dealer_card[5] or dealer.get() in dealer_card[8:]:
            action.set("don't split")
        else:
            action.set('split')
    elif hand.get() == '77':
        if dealer.get() in dealer_card[:6]:
            action.set('split')
        else:
            action.set("don't split")
    elif hand.get() == '66':
        if dealer.get() in dealer_card[:5]:
            action.set('split')
        else:
            action.set("don't split")
    elif hand.get() == '44':
        if dealer.get() in dealer_card[3:5]:
            action.set('split')
        else:
            action.set("don't split")
    elif hand.get() == '33' or hand == '22':
        if dealer.get() in dealer_card[:6]:
            action.set('split')
        else:
            action.set("don't split")

# gui
root = Tk()
root.title('Basic Strategy')

frame1 = ttk.Frame(root, padding='2 2 2 2')
frame1.grid(column=0, row=0, sticky=(N, W, E, S))
frame2 = ttk.Frame(root, padding='2 2 2 2')
frame2.grid(column=1, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

action = StringVar(root, 'action')
hand = StringVar(root, 'hand')
dealer = StringVar(root, 'dealer')

ttk.Label(frame1, text='Hard Totals').grid(column=0, row=0, sticky=W)
ttk.Button(frame1, text='16', command=sixteen).grid(column=0, row=1, sticky=W)
ttk.Button(frame1, text='15', command=fifteen).grid(column=1, row=1, sticky=W)
ttk.Button(frame1, text='14', command=fourteen).grid(column=2, row=1, sticky=W)
ttk.Button(frame1, text='13', command=thirteen).grid(column=0, row=2, sticky=W)
ttk.Button(frame1, text='12', command=twelve).grid(column=1, row=2, sticky=W)
ttk.Button(frame1, text='11', command=eleven).grid(column=2, row=2, sticky=W)
ttk.Button(frame1, text='10', command=ten).grid(column=0, row=3, sticky=W)
ttk.Button(frame1, text='9', command=nine).grid(column=1, row=3, sticky=W)

ttk.Label(frame1, text='Soft Totals').grid(column=0, row=4)
ttk.Button(frame1, text='A9', command=a9).grid(column=0, row=5, sticky=W)
ttk.Button(frame1, text='A8', command=a8).grid(column=1, row=5, sticky=W)
ttk.Button(frame1, text='A7', command=a7).grid(column=2, row=5, sticky=W)
ttk.Button(frame1, text='A6', command=a6).grid(column=0, row=6, sticky=W)
ttk.Button(frame1, text='A5', command=a5).grid(column=1, row=6, sticky=W)
ttk.Button(frame1, text='A4', command=a4).grid(column=2, row=6, sticky=W)
ttk.Button(frame1, text='A3', command=a3).grid(column=0, row=7, sticky=W)
ttk.Button(frame1, text='A2', command=a2).grid(column=1, row=7, sticky=W)

ttk.Label(frame1, text='Pairs').grid(column=0, row=8, sticky=W)
ttk.Button(frame1, text='AA', command=aces).grid(column=0, row=9, sticky=W)
ttk.Button(frame1, text='TT', command=tens).grid(column=1, row=9, sticky=W)
ttk.Button(frame1, text='99', command=nines).grid(column=2, row=9, sticky=W)
ttk.Button(frame1, text='88', command=eights).grid(column=0, row=10, sticky=W)
ttk.Button(frame1, text='77', command=sevens).grid(column=1, row=10, sticky=W)
ttk.Button(frame1, text='66', command=sixes).grid(column=2, row=10, sticky=W)
ttk.Button(frame1, text='55', command=fives).grid(column=0, row=11, sticky=W)
ttk.Button(frame1, text='44', command=fours).grid(column=1, row=11, sticky=W)
ttk.Button(frame1, text='33', command=threes).grid(column=2, row=11, sticky=W)
ttk.Button(frame1, text='22', command=twos).grid(column=0, row=12, sticky=W)

ttk.Label(frame2, text='Dealer Card').grid(column=0, row=0, sticky=W)
ttk.Button(frame2, text='A', command=dAce).grid(column=0, row=1, sticky=W)
ttk.Button(frame2, text='10', command=dTen).grid(column=1, row=1, sticky=W)
ttk.Button(frame2, text='9', command=dNine).grid(column=2, row=1, sticky=W)
ttk.Button(frame2, text='8', command=dEight).grid(column=0, row=2, sticky=W)
ttk.Button(frame2, text='7', command=dSeven).grid(column=1, row=2, sticky=W)
ttk.Button(frame2, text='6', command=dSix).grid(column=2, row=2, sticky=W)
ttk.Button(frame2, text='5', command=dFive).grid(column=0, row=3, sticky=W)
ttk.Button(frame2, text='4', command=dFour).grid(column=1, row=3, sticky=W)
ttk.Button(frame2, text='3', command=dThree).grid(column=2, row=3, sticky=W)
ttk.Button(frame2, text='2', command=dTwo).grid(column=0, row=4, sticky=W)



ttk.Label(frame2, text='Player:').grid(column=0, row=5)
ttk.Label(frame2, textvariable=hand).grid(column=1, row=5)
ttk.Label(frame2, text='Dealer:').grid(column=0, row=6)
ttk.Label(frame2, textvariable=dealer).grid(column=1, row=6)

ttk.Button(frame2, text='Play', command=play_hand).grid(column=0, row=7, sticky=W)
ttk.Label(frame2, textvariable=action).grid(column=1, row=7)


root.attributes('-topmost', True)

for child in frame1.winfo_children():
    child.grid_configure(padx=2, pady=2)

for child in frame2.winfo_children():
    child.grid_configure(padx=2, pady=2)

root.mainloop()