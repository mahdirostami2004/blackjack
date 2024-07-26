from random import *
import tkinter as tk
from tkinter import messagebox,font
import time
 
def main_window():
    global balance
    balance = 5000
    # cards={"heart":(1,2,3,4,5,6,7,8,9,10,"J","Q","K"),"dimond":}
    global black_card
    black_card="🂠"
    global play_cards
    play_cards={
    "🂮":10,'🂭':10,"🂫":10,'🂪':10,'🂩':9,'🂨':8,'🂧':7,'🂦':6,'🂥':5,'🂤':4,'🂣':3,'🂢':2,'🂡':1,
    '🂾':10,'🂽':10,'🂻':10,'🂺':10,'🂹':9,'🂸':8,'🂷':7,'🂶':6,'🂵':5,'🂴':4,'🂳':3,'🂲':2,'🂱':1,
    '🃎':10,'🃍':10,'🃋':10,'🃊':10,'🃉':9,'🃈':8,'🃇':7,'🃆':6,'🃅':5,'🃄':4,'🃃':3,'🃂':2,'🃁':1,
    '🃞':10,'🃝':10,'🃛':10,'🃚':10,'🃙':9,'🃘':8,'🃗':7,'🃖':6,'🃕':5,'🃔':4,'🃓':3,'🃒':2,'🃑':1}
    #defining functons 
    
    
    
    import random
    res = random.choice(list(play_cards.items()))
    

    
   
    global bet
    bet =0

    def tendoller():
        global bet
        bet+=10
        l1.config(text=f"PLACE YOUR BET :{bet} $",font=("Arial",50),foreground="purple").grid()

    def hundereddoller():
        global bet
        bet+=100
        l1.config(text=f"PLACE YOUR BET :{bet} $",font=("Arial",50),foreground="purple").grid()

    def fiftydoller():
        global bet
        bet+=50
        l1.config(text=f"PLACE YOUR BET :{bet} $",font=("Arial",50),foreground="purple").grid()


    def openNewWindow():
        global newWindow
        newWindow = tk.Toplevel(window)
        newWindow.title("BLACK JACK")
        newWindow.geometry("1920x1080")
        newWindow.configure(bg=("green"))
        global player_hand,dealer_hand,dealer_score,player_score
        #creating two random cards for each player in the biganing of the game
        
        def randcard():
            begin = random.choice(list(play_cards.items()))
            return begin
        global p_card1,p_card2,d_card1,d_card12     
        p_card1=randcard()
        p_card2=randcard()
        d_card1=randcard()
        d_card2=randcard()
        
        
        player_hand=[]
        dealer_hand=[]
        player_score=p_card2[1]+p_card1[1]
        dealer_score=d_card2[1]+d_card1[1]
      
        
        def blackjack():
            if player_score==21:
                messagebox.showinfo("","BLACK JACK !!!")
                reset_game()
            elif dealer_score==21:
                messagebox.showinfo("","BLACK JACK !!!")
                reset_game()
        blackjack()
       
        # Define the game functions
        def new_card():
            global player_hand, player_score,dealer_hand,dealer_score
            card2=random.choice(list(play_cards.items()))
            card = random.choice(list(play_cards.items()))
            dealer_hand.append(card2)
            player_hand.append(card)
            player_score += card[1]
            dealer_score  += card2[1]

        def dealer_card():
            global dealer_hand, dealer_score
            card = random.choice(list(play_cards.items()))
            dealer_hand.append(card)
            dealer_score += card[1]

        bgd = tk.PhotoImage(file = "./images/cc.png") 
        labelbdg= tk.Label( root, image = bgd) 
        labelbdg.place(x = 0, y = 0) 

        def stand():
          
            global dealer_score
            dealer_show.config(text=f"DEALER :{dealer_score} >>>>> {d_card2[0]}  {d_card1[0]}{', '.join([card[0] for card in dealer_hand])}")
            if dealer_score > 21:
                messagebox.showinfo("MATCH ", "YOU WON!")
                reset_game()
                newWindow.destroy()
            elif 21 > dealer_score > player_score:
                messagebox.showinfo("MATCH ", "DEALER WON!")
                reset_game()
                newWindow.destroy()
            elif dealer_score < player_score < 21:
                messagebox.showinfo("MATCH ", "YOU WON!")
                reset_game()
                newWindow.destroy()
            elif dealer_score == player_score:
               new_card()
            while dealer_score < 21:
                dealer_card()
                
        def reset_game():
            global player_hand, player_score, dealer_score,dealer_hand
            player_hand = []
            dealer_hand = []
            player_score = 0
            dealer_score = 0
        def hit():
            global player_hand, player_score
            new_card()
            dealer_show.config(text=f"DEALER :{dealer_score} >>>>>> {d_card2[0]}  {d_card1[0]}{', '.join([card[0] for card in dealer_hand])}")
            your_show.config(text=f"YOU :{player_score} >>>>>> {p_card1[0]}{p_card2[0]} {', '.join([card[0] for card in player_hand])}")
            if player_score > 21:
                messagebox.showinfo("MATCH ", "YOU BUSTED!")
                reset_game()
                newWindow.destroy()
            elif dealer_score>21 :
                messagebox.showinfo("MATCH ", "DEALER BUSTED!")
                reset_game()
                newWindow.destroy()
            elif dealer_score==21 :
                messagebox.showinfo("MATCH ", "DEALER WON!")
                reset_game()
                newWindow.destroy()
            elif player_score==21:
                messagebox.showinfo("MATCH ", "YOU WON!")
                reset_game()
                newWindow.destroy()
            elif dealer_score==player_score:
                hit()
            elif dealer_score > player_score:
                messagebox.showinfo("MATCH ", "DEALER WON!")
                reset_game()
                newWindow.destroy()
            elif dealer_score < player_score:
                messagebox.showinfo("MATCH ", "YOU WON!")
                reset_game()
                newWindow.destroy()
           
            
        your_show = tk.Label(newWindow, text=f"YOU :{player_score} >>>>>> {p_card1[0]}{p_card2[0]} ", font=("Arial", 50,"bold"), background="green", foreground="white")
        your_show.grid(row=1)
        dealer_show=tk.Label(newWindow, text=f"DEALER :  >>>>>> {black_card}{d_card1[0]}", font=("Arial", 50,"bold"), background="green", foreground="white")
        dealer_show.grid(row=2)
            
        stand_image = tk.PhotoImage(file=r"./images/stand.png")
        img6 = stand_image.subsample(5, 5)
        hit_button = tk.Button(newWindow, text="Stand", image=img6, command=stand)
        hit_button.grid(row=3,column=1,padx=10)
        hit_image = tk.PhotoImage(file=r"./images/hit.png")
        img5 = hit_image.subsample(5, 5)
        hit_button = tk.Button(newWindow, text="Stand", image=img5, command=hit)
        hit_button.grid(row=3,column=2,padx=10)
                
        global your_cards
        your_cards=tk.Label(newWindow,text=" ")
        newWindow.configure(bg=("green"))
        global ti
        ti=15
        global second
        second= tk.Label(newWindow, text=f"you have {ti} second to make your decide   ", font=("Arial",32,"bold"),foreground="purple",background="red")
        second.pack(pady=20)
                
        def times_up():
            global ti
            if ti > 0:
                second.config(text=f"You have <{ti}> seconds to make your decision")
                ti-= 1
                second.after(1000, times_up)  # Call this method again after 1000 ms (1 second)
            else:
                messagebox.showwarning("Time Countdown", "Time's up!")
                        
                newWindow.destroy()  # Close the window
            
            newWindow.mainloop()
        times_up()
        bga = tk.PhotoImage(file = "./images/cc.png") 
        labelbga= tk.Label( root, image = bga) 
        labelbga.place(x = 0, y = 0) 

    #tk settings
    global window
    window = tk.Toplevel(root)

    window.title("BLACK JACK")
    window.configure(bg=("green"))

    #buttons and labels
    l1=tk.Label(window,text="PLACE YOUR BET :  ",font=("Arial",50),foreground="blue")
    l1.grid(row=0,column=0)

    l2=tk.Label(window,text=f"YOUR BALANCE : {balance}$ ",font=("Arial",50),foreground="darkcyan")
    l2.grid(row=1,column=0)
    #time lable
        
    #bets buttons
    photo1= tk.PhotoImage(file = r"./images/10.png") 
    photo2 = tk.PhotoImage(file = r"./images/fifty.png") 
    photo3 = tk.PhotoImage(file = r"./images/100.png") 
    deal= tk.PhotoImage(file = r"./images/deal.png") 


    smaller_image1 = photo1.subsample(5, 5)   
    smaller_image2 = photo2.subsample(5, 5)
    smaller_image3 = photo3.subsample(5, 5)
    smaller_image4 = deal.subsample(5, 5)

    # here, image option is used to 
    # set image on button   
    tk.Button(window, text = '10$',image=smaller_image1,borderwidth=0,command=tendoller).grid(row=0,column=1)
    tk.Button(window,text="100$",image=smaller_image2,borderwidth=0,command=hundereddoller).grid(row=0,column=2)
    tk.Button(window,text="50$",image=smaller_image3,command=fiftydoller).grid(row=0,column=3,)
    tk.Button(window,text="deal",image=smaller_image4,command=openNewWindow).grid(row=4,column=2)
    bg = tk.PhotoImage(file = "./images/cc.png") 
    labelbg= tk.Label( root, image = bg) 
    labelbg.place(x = 0, y = 0)
    window.mainloop()
   

global root
root = tk.Tk()
root.title("Blackjack Introduction")
root.configure(background="green")  




#background image  
bg = tk.PhotoImage(file = "./images/cc.png") 
labelbg= tk.Label( root, image = bg) 
labelbg.place(x = 0, y = 0) 


custom_font = font.Font(family="Arial", size=24, weight="bold")

# Create a label
l0=tk.Label(root,text="HELLO THERE",font=custom_font, fg="white", bg="green")
l0.grid()
l1 = tk.Label(root, text='''Players receive all cards face up and the dealer's first card is face up and the second is face down.
              The object of the game is to get closer to 21 than the dealer without going over 21. 
              If a hand goes over 21, it is called a "bust" or "break" and the wager is lost.
              In Blackjack, Jacks, Queens, Kings and 10s count as 10.''', font=custom_font, fg="white", bg="green", wraplength=800)
l1.grid(row=1, column=0, padx=20, pady=20)

# Create a button
button = tk.Button(root, text="OK", font=custom_font, fg="white", bg="green", command=main_window)
button.grid(row=2, column=0, pady=20)

# Start the main loop
root.mainloop()
