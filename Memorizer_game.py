from tkinter import *
import time
import random


main_screen = Tk()   # create a GUI window 
main_screen.geometry("1300x550")
main_screen.configure(bg='greenyellow')
li=[[],[]]
for i in range(2):
    for j in range(3):
        li[i].append(random.randint(0,9))
print(li)

count=0
count2=0
ans=0

def start():
    global count
    global ans
    if count==5:
        
        
        inputrow.configure(state="normal")
        inputcol.configure(state="normal")
        element1.configure(text="*")
        element2.configure(text="*")
        element3.configure(text="*")
        element4.configure(text="*")
        element5.configure(text="*")
        element6.configure(text="*")
       
        val.configure(state="normal")
        startgame.configure(text="Game started")
        curr_time.after(1000,start)
    if count==65:
        inputrow.configure(state="disable")
        inputcol.configure(state="disable")
        val.configure(state="disable")
        curr_time.config(text = "Time's up")
        ansright="Correct Answers : " + str(ans)
        answrong="Wrong/Unanswered Answers : "+ str(6-ans)
        answer.configure(text=ansright)
        answrng.configure(text=answrong)
        button.configure(state="disable")
        return
    
    count=count+1
    curr_time.config(text = count)
    curr_time.after(1000,start)

def check():
    global li
    global ans
    row=int(inputrow.get())
    col=int(inputcol.get())
    vval=int(val.get())
    print(row)
    for i in li:
        if vval==li[row][col]:
            ans=ans+1
            answer.configure(text="Correct")
            print("sdf")
            break
        else:
             answer.configure(text="Incorrect")
             print("sdf")
             break
    

main_screen.title("Memorizer Game")

curr =Label(main_screen, font ='arial 15 bold', width="30",text = 'Timer : ', fg = 'gray25',bg='greenyellow')
curr.grid(column = 0, row = 1)

curr_time =Label(main_screen, font ='arial 15 bold', width="10",text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.grid(column = 1, row = 1)
start()

      

row =Label(main_screen, font ='arial 15 bold', width="15",text = 'Enter Row : ', fg = 'gray25')
row.grid(column = 0, row = 2)
inputrow = Entry(main_screen,width = 25,bg = "light yellow",font ='arial 15 bold',state='disabled') 
inputrow.grid(column = 1, row = 2)


col =Label(main_screen, font ='arial 15 bold', width="15",text = 'Enter Column : ', fg = 'gray25')
col.grid(column = 0, row = 3)
inputcol = Entry(main_screen,width = 25,font ='arial 15 bold',bg = "light yellow",state='disabled') 
inputcol.grid(column = 1, row = 3)
val = Entry(main_screen,width = 25,font ='arial 15 bold',bg = "light yellow",state='disabled') 
val.grid(column = 1, row = 4)

startgame =Label(main_screen, font ='arial 15 bold', width="20",text = 'Memorize ', fg = 'gray25',bg ='papaya whip')
startgame.grid(column = 0, row = 8)


element1=Label(main_screen, font ='arial 15 bold', width="10",text = li[0][0], fg = 'gray25',bg ='mintcream')
element1.grid(column = 3, row = 2,padx=30, pady=10)
element2=Label(main_screen, font ='arial 15 bold', width="10",text = li[0][1], fg = 'gray25',bg ='mintcream')
element2.grid(column = 4, row = 2,padx=10, pady=10)
element3=Label(main_screen, font ='arial 15 bold', width="10",text = li[0][2], fg = 'gray25',bg ='mintcream')
element3.grid(column = 5, row = 2,padx=10, pady=10)
element4=Label(main_screen, font ='arial 15 bold', width="10",text = li[1][0], fg = 'gray25',bg ='mintcream')
element4.grid(column = 3, row = 3,padx=10, pady=10)
element5=Label(main_screen, font ='arial 15 bold', width="10",text = li[1][1], fg = 'gray25',bg ='mintcream')
element5.grid(column = 4, row = 3,padx=10, pady=10)
element6=Label(main_screen, font ='arial 15 bold', width="10",text = li[1][2], fg = 'gray25',bg ='mintcream')
element6.grid(column = 5, row = 3,padx=10, pady=10)
answer=Label(main_screen, font ='arial 15 bold', width="30",text = " ", fg = 'gray25',bg ='greenyellow')
answer.grid(column = 0, row = 5,padx=10, pady=10)
answrng=Label(main_screen, font ='arial 15 bold', width="39",text = " ", fg = 'gray25',bg ='greenyellow')
answrng.grid(column = 0, row = 6,padx=10, pady=10)
instruct=Label(main_screen, font ='arial 15 bold', width="42",text = "Memorize Time: 5s Attempt Time :60s", fg = 'gray25',bg ='greenyellow')
instruct.grid(column = 0, row = 9,padx=10, pady=10)

button = Button(main_screen,text = 'Check',font ='arial 15 bold', width="10",command=check)
button.grid(column = 0, row = 7,padx=10, pady=10)

 

main_screen.mainloop() # start the GUI
