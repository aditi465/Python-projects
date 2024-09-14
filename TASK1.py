import tkinter as tk
from random import randint
from PIL import Image,ImageTk

#main window 
window = tk.Tk()
window.title("Rock paper sicssors")
window.configure(background="#478778")


#Pictures
rock_img =ImageTk.PhotoImage(Image.open("rock user.png"))      
paper_img =ImageTk.PhotoImage(Image.open("paper user .png"))
scissor_img =ImageTk.PhotoImage(Image.open("scissor user.png"))
rock_img_comp =ImageTk.PhotoImage(Image.open("Rock.png"))
paper_img_comp =ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_img_comp =ImageTk.PhotoImage(Image.open("scissor.png"))

#insert picture
user_label =tk.Label(window,image=scissor_img,bg="black")
comp_label = tk.Label(window,image=scissor_img_comp,bg="black")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=5)


#sources
playerScore = tk.Label(window,text=0,font=100,bg="black",fg="white")
computerScore =tk.Label(window,text=0,font=100,bg="black",fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicarors
user_indicator = tk.Label(window,font=50,text="USER",bg="black",fg="white")
comp_indicator=tk.Label(window,font=50,text="COMPUTER",bg="black",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)


#messages

msg =tk.Label(window,font=50,bg="black",fg="white")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
   msg['text'] = x

#update score
def updateUserscore():
   score = int(playerScore["text"] )
   score +=1
   playerScore["text"]= str(score)

def updateCompscore(): 
  score = int(computerScore["text"] )
  score +=1
  computerScore["text"]= str(score) 


#check winner
def checkWinner(player,computer):
  if player == computer:
     updateMessage("Its a tie!!!")
  elif player == "rock":
     if computer == "paper":
        updateMessage("Computer wins!!!")
        updateCompscore()
     else:
         updateMessage("Player wins!!!")
         updateUserscore()
  elif player == "paper":
     if computer == "scisssor":
        updateMessage("Player wins!!!")
        updateCompscore()
     else:
        updateMessage("Computer wins!!!")
        updateUserscore()  
  elif  player == "scissor":
      if computer == "rock":
        updateMessage("Computer wins!!!")
        updateCompscore()
      else:
        updateMessage("Player wins!!!")
        updateUserscore() 
  else:
      pass    

   
#update choices

choices = ["rock","paper","scissor"]
def updateChoice(x):

    #for computer
    compChoice = choices[randint(0, 2)]
    #my_list = list(compChoice)
    if compChoice =="rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice =="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

        checkWinner(x,compChoice)

    #for user
    if x=="rock":
      user_label.configure(image=rock_img)
    elif x=="paper":
      user_label.configure(image=paper_img)
    else:
      user_label.configure(image=scissor_img) 

      checkWinner(x,compChoice)
#buttons
rock = tk.Button(window,width=20,height=2,text="ROCK",bg="green",fg="white",command = lambda:updateChoice("rock")).grid(row=2,column=1)
paper = tk.Button(window,width=20,height=2,text="PAPER",bg="red",fg="white",command = lambda:updateChoice("paper")).grid(row=2,column=2)
sicssor = tk.Button(window,width=20,height=2,text="SCISSOR",bg="Blue",fg="Black",command = lambda:updateChoice("scissor")).grid(row=2,column=3)


window.mainloop()