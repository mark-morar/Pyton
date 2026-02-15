import tkinter as tk
import random
import time




def move_button():
    global start_time


    if time.time() - start_time < 30:
        new_x = random.randint(0,500)
        new_y = random.randint(0,400)
        button.place(x=new_x, y=new_y)
        root.after(500,move_button)

    else:
        end_game()

def click():
     global click_count
     click_count += 1
     click_label.config(text=f"score of click {click_count}" )

def end_game():
    button.config(state="disabled")
    click_label.config(text=f"game over! score of click: {click_count}")
    restart_button.pack()


def restart_game():
    global click_count, start_time

    click_count = 0
    start_time = time.time()
    button.config(state="normal")
    restart_button.pack_forget()
    move_button()



click_count = 0
start_time = time.time()

root = tk.Tk()
root.title = ("Click the button")
root.geometry("750x400")

click_label = tk.Label(root, text = f"score of click: {click_count}",
                                     font=("Arial", 14))


click_label.pack()


button = tk.Button(root, text = "click me",
                   font=("Arial", 14),
                   command=click)

button.place(x=250,y=250)

restart_button = tk.Button(root, text="restart the game",
                           font=("Arial", 14),
                           command=restart_game)


move_button()




root.mainloop()

















