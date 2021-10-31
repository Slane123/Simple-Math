import random
import sqlite3
import time
import sys
import tkinter.messagebox as box
from tkinter import *

from Game import game_variables
from Gamemode import game_mode_variables
from Information import user_information
from Leaderboard import leaderboard_values

leaderboard = leaderboard_values
game_mode = game_mode_variables
information = user_information
game = game_variables
window = Tk()

window.title('Simple math')
window.configure(background="#559E54")
c = Canvas(window, width=800, height=550)
c.configure(background="#559E54")
c.pack()

game.time_taken = 0
game.score = 0
game_mode.wrong = 0
game_mode.start = False
game.current_run = True
game.time_taken = 0
counter = 0
valid = True

conn = sqlite3.connect('leaderboard.db')
c1 = conn.cursor()


# c1.execute("CREATE TABLE leaderboard(Name text,Gamemode text,Score integer,Difficulty integer,Time_taken float, "
# "sign integer)")

def reset():
    global c
    c.destroy()
    c = Canvas(window, width=800, height=550)
    c.configure(background="#559E54")
    c.pack()
    select()


def start():
    Label(c, text="Simple Math", bg="#559E54", fg="black",
          font="none 50 bold").place(
        x=10,
        y=20,
    )
    Button(c, bg="#F7DDD4", text="START", width=60, command=reset).place(
        x=10,
        y=100,
    )


def name():
    def print_input():
        user_name = input_field.get()
        if user_name == "":
            box.showerror('ERROR', 'please enter your name')
        elif user_name != "" and len(user_name) <= 30:
            information.name = user_name
            reset()

    Label(c, text="Simple Math", bg="#559E54", fg="black",
          font="none 50 bold").place(
        x=10,
        y=20,
    )
    Label(c,
          text="Enter your username: ",
          bg="#FFAC99",
          fg="black",
          font="none").place(x=300, y=190, width=200)
    c.create_rectangle(150, 150, 650, 350, fill='#FFAC99')
    input_field = Entry(c)
    input_field.place(x=300, y=230, width=190)
    input_field.focus()
    Button(c, text="SUBMIT", bg="#F7DDD4", command=print_input, width=10, height=2).place(x=700, y=500)


def sign():
    def multiplication():
        information.sign = "x"
        reset()

    def subtraction():
        information.sign = "-"
        reset()

    def addition():
        information.sign = "+"
        reset()

    Label(c, text="Simple Math", bg="#559E54", fg="black", font="none 50 bold").place(x=8, y=20)
    Label(c, text="Select a Sign: ", bg="#FFAC99", fg="black", font="none").place(x=290, y=160, width=200)
    Button(c, text="mulitplication (x)", bg="#F7DDD4", command=multiplication, height=2).place(x=113, y=200, width=150)
    Button(c, text="addition (+)", bg="#F7DDD4", command=addition, height=2).place(x=313, y=200, width=150)
    Button(c, text="subtraction (-)", bg="#F7DDD4", command=subtraction, height=2).place(x=513, y=200, width=150)
    c.create_rectangle(100, 150, 700, 300, fill='#FFAC99')


def difficulty():
    def print_input():
        game_difficulty = input_field.get()
        if not game_difficulty.isdigit():
            box.showerror('ERROR', 'Enter a valid difficulty')
        else:
            game_difficulty = int(game_difficulty)
            if information.sign == "x" and 1 <= game_difficulty <= 12:
                information.difficulty = game_difficulty
                reset()
            elif information.sign != "x" and 1 <= game_difficulty <= 100:
                information.difficulty = game_difficulty
                information.difficulty = int(information.difficulty)
                reset()
            else:
                box.showerror('ERROR', 'please enter a valid difficulty')

    Label(c, text="Simple Math", bg="#559E54", fg="black",
          font="none 50 bold").place(x=10, y=20, )
    Label(c, text="Enter your difficulty: ", bg="#FFAC99", fg="black", font="none").place(x=300, y=190, width=200)
    c.create_rectangle(150, 150, 650, 350, fill='#FFAC99')
    input_field = Entry(c)
    input_field.place(x=300, y=230, width=190)
    input_field.focus()
    Button(c, text="SUBMIT", bg="#F7DDD4", command=print_input, width=10, height=2).place(x=700, y=500)

    
def gamemode():
    def fastest_gamemode():
        information.gamemode = "Fastest"
        reset()

    def endless_gamemode():
        information.gamemode = "Endless"
        reset()

    def timed_gamemode():
        information.gamemode = "Timed"
        reset()

    Label(c, text="Simple Math", bg="#559E54", fg="black", font="none 50 bold").place(x=8, y=20)
    Label(c, text="Select a Gamemode: ", bg="#FFAC99", fg="black", font="none").place(x=290, y=160, width=200)
    Button(c, text="Fastest", bg="#F7DDD4", command=fastest_gamemode, height=2).place(x=113, y=200, width=150)
    Button(c, text="Endless", bg="#F7DDD4", command=endless_gamemode, height=2).place(x=313, y=200, width=150)
    Button(c, text="Timed", bg="#F7DDD4", command=timed_gamemode, height=2).place(x=513, y=200, width=150)
    c.create_rectangle(100, 150, 700, 300, fill='#FFAC99')


def reset_game_window():
    global c
    c.delete(ALL)
    c.destroy()
    c = Canvas(window, width=800, height=550)
    c.configure(background="#559E54")
    c.pack()
    gamemode_select()


def game_window():
    def print_input():
        response = input_field.get()
        if not response.isdigit():
            box.showerror('ERROR', 'please enter a valid answer')
        else:
            game.response = response
            game.response = int(game.response)
            if game.response == game.answer:
                game.score += 1
            else:
                game_mode.wrong += 1
            reset_game_window()

    Label(c, text=f"Score: {game.score}", font="none 10 bold").place(x=730, y=10)
    Label(c, text=game.equation, bg="white", fg="black", font="none 70 bold").place(x=200, y=175)
    c.create_rectangle(80, 120, 720, 370, fill='white')
    input_field = Entry(c)
    input_field.place(x=300, y=390, width=190)
    input_field.focus()
    Button(c, text="SUBMIT", bg="#F7DDD4", command=print_input, width=10, height=2).place(x=700, y=500)


def equation():
    num1 = random.randint(1, information.difficulty)
    num2 = random.randint(1, information.difficulty)
    game.equation = f"{str(num1)} {information.sign} {str(num2)} = ?"
    if information.sign == "x":
        answer = (num1 * num2)
    elif information.sign == "+":
        answer = (num1 + num2)
    else:
        answer = (num1 - num2)

    game.answer = answer
    game_window()


def gamemode_select():
    if information.gamemode == "Timed":
        timed()
    elif information.gamemode == "Fastest":
        fastest()
    else:
        endless()


def timed():
    if not game_mode.start:
        game_mode.time = time.time() + 30
        game_mode.start = True
    if time.time() < game_mode.time:
        equation()
    else:
        select()


def fastest():
    if not game_mode.start:
        game_mode.time = time.time()
        game_mode.start = True
        game_mode.count = 1
    for i in range(game_mode.count):
        if game.score == 10:
            game_mode.count = 0
            select()
        else:
            duration = time.time() - game_mode.time
            game.time_taken = round(duration, 2)
            equation()


def endless():
    if not game_mode.start:
        game_mode.count = 1
        game_mode.start = True
    for i in range(game_mode.count):
        if game_mode.wrong != 0:
            game_mode.count = 0
            select()
        else:
            equation()


def percentage_answer():
    def close():
        sys.exit()
    if game.score != 0:
        percentage = game.score / (game.score + game_mode.wrong)
        percentage = percentage * 100
        percentage = round(percentage)
    else:
        percentage = 0
    Label(c, text="Simple Math", bg="white", fg="black", font="none 50 bold").place(x=200, y=70)
    if information.gamemode != "Fastest":
        Label(c, text=f"You scored: {game.score}", bg="white", fg="black", font="none 20 bold").place(x=80, y=150)
    else:
        Label(c, text=f"You had a time of: {game.time_taken}s", bg="white", fg="black", font="none 20 bold") \
            .place(x=80, y=150)
    Label(c, text=f"You achieved: {percentage}% correct", bg="white", fg="black", font="none 20 bold").place(x=80, y=200)
    Label(c, text="Would you like to submit?", bg="white", fg="black", font="none 20 bold").place(x=230, y=300)
    Button(c, text="SUBMIT", bg="#F7DDD4", width=10, command=reset).place(x=650, y=450)
    Button(c, text=" Exit ", bg="#F7DDD4", width=10, command=close).place(x=75, y=450)
    c.create_rectangle(50, 50, 750, 400, fill='white')


def database():
    # Inserting into leaderboard
    c1.execute(
        "INSERT INTO leaderboard VALUES (:Name, :Gamemode, :Score, :Difficulty, :Time_taken, :sign)",
        {'Name': information.name, 'Gamemode': information.gamemode, 'Score': game.score,
         'Difficulty': information.difficulty, 'Time_taken': game.time_taken, 'sign': information.sign})
    conn.commit()

    def sqlfastest():
        # Selecting into leaderboard
        leaderboard.name = []
        leaderboard.time_taken = []
        c1.execute("SELECT Name FROM leaderboard WHERE Gamemode =:Gamemode AND Difficulty=:Difficulty AND sign=:sign",
                   {'Gamemode': information.gamemode, 'Difficulty': information.difficulty, 'sign': information.sign})
        leaderboard.name = c1.fetchall()
        c1.execute(
            "SELECT Time_taken FROM leaderboard WHERE Gamemode =:Gamemode AND Difficulty=:Difficulty AND sign=:sign",
            {'Gamemode': information.gamemode, 'Difficulty': information.difficulty, 'sign': information.sign})
        leaderboard.time_taken = c1.fetchall()

        reset()

    def sqlscore():
        # Selecting into leaderboard

        c1.execute("SELECT Name FROM leaderboard WHERE Gamemode =:Gamemode AND Difficulty=:Difficulty AND sign=:sign",
                   {'Gamemode': information.gamemode, 'Difficulty': information.difficulty, 'sign': information.sign})
        leaderboard.name = c1.fetchall()
        c1.execute("SELECT Score FROM leaderboard WHERE Gamemode =:Gamemode AND Difficulty=:Difficulty AND sign=:sign",
                   {'Gamemode': information.gamemode, 'Difficulty': information.difficulty, 'sign': information.sign})
        leaderboard.score = c1.fetchall()

        reset()

    if information.gamemode == "Fastest":
        sqlfastest()
    else:
        sqlscore()


def bubblesort():
    if information.gamemode != "Fastest":
        # sorting list to produce leaderboard
        for i in range(len(leaderboard.name)):
            for pass_num in range(len(leaderboard.score) - 1, 0, -1):
                for i in range(pass_num):
                    if leaderboard.score[i] < leaderboard.score[i + 1]:
                        leaderboard.score[i], leaderboard.score[i + 1] = leaderboard.score[i + 1], leaderboard.score[i]
                        leaderboard.name[i], leaderboard.name[i + 1] = leaderboard.name[i + 1], leaderboard.name[i]

    else:
        # sorting list to produce leaderboard
        for i in range(len(leaderboard.name)):
            for pass_num in range(len(leaderboard.time_taken) - 1, 0, -1):
                for i in range(pass_num):
                    if leaderboard.time_taken[i] > leaderboard.time_taken[i + 1]:
                        leaderboard.time_taken[i], leaderboard.time_taken[i + 1] = leaderboard.time_taken[i + 1], \
                                                                                   leaderboard.time_taken[i]
                        leaderboard.name[i], leaderboard.name[i + 1] = leaderboard.name[i + 1], leaderboard.name[i]
    reset()


def leaderboard():
    Label(c, text="Leaderboard", bg="#559E54", fg="black", font="none 50 bold").place(x=10, y=2)
    c.create_rectangle(10, 100, 748, 475, fill='white')

    def close():
        sys.exit()

    Label(c, text="Rank", bg="white", fg="black", relief="solid", borderwidth=1, font="none 12 bold", width=5,
          height=1) \
        .place(x=10, y=70)
    Label(c, text="Username", bg="white", fg="black", relief="solid", borderwidth=1, font="none 12 bold", width=60,
          height=1) \
        .place(x=62, y=70)

    try:
        for i in range(10):
            # if str(leaderboard.name[i])[2:-3] == information.name:
            # colour = "light blue"
            if (i % 2) == 0:
                colour = "white"
            else:
                colour = "light gray"
            Label(c, text=f"{str(leaderboard.name[i])[2:-3]}", relief="solid", borderwidth=1, font="none 20 bold",
                  bg=colour, width=31, height=1).place(x=60, y=(i * 40) + 100)
            Label(c, text=f"{i + 1}.", relief="solid", borderwidth=1, font="none 20 bold",
                  bg=colour, width=3, height=1).place(x=10, y=(i * 40) + 100)
            if information.gamemode != "Fastest":
                Label(c, text=f"{str(leaderboard.score[i])[1:-2]}", relief="solid", borderwidth=1, font="none 20 bold",
                      bg=colour, width=10, height=1).place(x=575, y=(i * 40) + 100)
                Label(c, text="Score", bg="white", fg="black", relief="solid", borderwidth=1, font="none 12 bold",
                      width=17, height=1).place(x=575, y=70)

            elif information.gamemode == "Fastest":
                Label(c, text=f"{str(leaderboard.time_taken[i])[1:-2]}", relief="solid", borderwidth=1,
                      font="none 20 bold", bg=colour, width=10, height=1).place(x=575, y=(i * 40) + 100)
                Label(c, text="Time", bg="white", fg="black", relief="solid", borderwidth=1, font="none 12 bold",
                      width=17, height=1).place(x=575, y=70)

    except:
        pass
    Button(c, text="Exit", bg="#F7DDD4", command=close, width=10, height=2).place(x=700, y=500)


def select():
    global counter
    counter = counter + 1
    if counter == 1:
        start()
    elif counter == 2:
        name()
    elif counter == 3:
        sign()
    elif counter == 4:
        difficulty()
    elif counter == 5:
        gamemode()
    elif counter == 6:
        gamemode_select()
    elif counter == 7:
        percentage_answer()
    elif counter == 8:
        database()
    elif counter == 9:
        bubblesort()
    elif counter == 10:
        leaderboard()


select()

window.mainloop()
