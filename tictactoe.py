# FOR THIS GAME WE NEED TO INSTALL pygame MODULE
# FOR DOING THIS OPEN Command Prompt and type:
# pip install pygame (with internet connection)
# I already installed it so it is saying that requirement already satisfied
# NOW WE WILL USE PYGAME MODULE

from tkinter import *
from pygame import *
import tkinter.messagebox as msg
import random


# ================================ PLAYING WITH COMPUTER ===================================== #
def __play_comp__():
    game_computer = Toplevel(root)
    game_computer.focus_force()
    width, height = 900, 600
    g_w = ((game_computer.winfo_screenwidth() // 2) - (width // 2))
    g_h = ((game_computer.winfo_screenheight() // 2) - (height // 2))
    game_computer.geometry(f"{width}x{height}+{g_w}+{g_h}")
    game_computer.resizable(0, 0)
    game_computer.title("TIC-TAC-TOE")
    game_computer.iconbitmap("files/ico.ico")
    game_computer.configure(bg="#EEEEEE")

    # ===================== FUNCTIONS OF GAME WINDOW (PLAYER VS COMPUTER) ====================== #
    def winner():
        # CONDITION IF USER WINS THE GAME:
        if l1['text'] == l4['text'] == l7['text'] == "  X  " or l2['text'] == l5['text'] == l8['text'] == "  X  " or \
           l3['text'] == l6['text'] == l9['text'] == "  X  " or l1['text'] == l2['text'] == l3['text'] == "  X  " or \
           l4['text'] == l5['text'] == l6['text'] == "  X  " or l7['text'] == l8['text'] == l9['text'] == "  X  " or \
           l1['text'] == l5['text'] == l9['text'] == "  X  " or l3['text'] == l5['text'] == l7['text'] == "  X  ":
            msg.showinfo("Well Done!", f"{player1.get()} won this game by defeating Computer ", parent=game_computer)
            l1['text'] = l2['text'] = l3['text'] = l4['text'] = l5['text'] = l6['text'] = l7['text'] = l8['text']\
                = l9['text'] = "       "

        # CONDITION IF BOT WINS THE GAME:
        elif l1['text'] == l4['text'] == l7['text'] == "  O  " or l2['text'] == l5['text'] == l8['text'] == "  O  " or \
                l3['text'] == l6['text'] == l9['text'] == "  O  " or l1['text'] == l2['text'] == l3['text'] == "  O  " or \
                l4['text'] == l5['text'] == l6['text'] == "  O  " or l7['text'] == l8['text'] == l9['text'] == "  O  " or \
                l1['text'] == l5['text'] == l9['text'] == "  O  " or l3['text'] == l5['text'] == l7['text'] == "  O  ":
            msg.showinfo("Try Again!", f"Computer won this game by defeating {player1.get()}", parent=game_computer)
            l1['text'] = l2['text'] = l3['text'] = l4['text'] = l5['text'] = l6['text'] = l7['text'] = l8['text']\
                = l9['text'] = "       "

        # CONDITION IF TIE BETWEEN THEN:
        elif l1['text'] != "       " and l2['text'] != "       " and l3['text'] != "       " and \
                l4['text'] != "       " and l5['text'] != "       " and l6['text'] != "       " and \
                l7['text'] != "       " and l8['text'] != "       " and l9['text'] != "       ":
            msg.showinfo("Better Luck Next Time!", f"It is a tie between {player1.get()} and Random Bot", parent=game_computer)
            l1['text'] = l2['text'] = l3['text'] = l4['text'] = l5['text'] = l6['text'] = l7['text'] = l8['text'] \
                = l9['text'] = "       "

    def bot_move():
        chance = random.choice(chances)  # CHOICE IS USED TO PICK ONE ItEM FROM A LIST
        if chance.cget('text') == "       ":
            chance.config(text="  O  ")
            
        else:
            for x in range(len(chances)):
                if chances[x].cget('text') == "       ":
                    bot_move()
                    break
        p_name.config(fg="blue")
        c_name.config(fg="black")

    def whose_move(event):
        if move.get() == 1:
            p_name.config(fg="black")
            c_name.config(fg="blue")
            event.widget.config(text="  X  ")
            
            move.set(0)
        if move.get() == 0:
            game_computer.after(400, bot_move)
            move.set(1)
        winner()

    def check_space(event):
        if event.widget.cget('text') == "       ":
            whose_move(event)

    # ================================ CANVAS GAME CREATION LAYOUT ==================================== #
    canvas = Canvas(game_computer, height=510, width=660, bg="#8A2BE2", bd=0)

    # ================ VERTICAL LINES ===================== #
    canvas.create_line(219, 0, 219, 510)
    canvas.create_line(220, 0, 220, 510)
    canvas.create_line(221, 0, 221, 510)
    canvas.create_line(439, 0, 439, 510)
    canvas.create_line(440, 0, 440, 510)
    canvas.create_line(441, 0, 441, 510)

    # ================ HORIZONTAL LINES ===================== #
    canvas.create_line(0, 169, 660, 169)
    canvas.create_line(0, 170, 660, 170)
    canvas.create_line(0, 171, 660, 171)
    canvas.create_line(0, 339, 660, 339)
    canvas.create_line(0, 340, 660, 340)
    canvas.create_line(0, 341, 660, 341)

    # =================== CIRCLE AND CROSS ==================== #

    # ========== 1st ROW ========== #
    square_1 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l1 = Label(square_1, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l1.pack(padx=1, pady=1.5, fill=Y)
    square_1.place(x=6, y=6)

    square_2 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l2 = Label(square_2, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l2.pack(padx=1, pady=1.5, fill=Y)
    square_2.place(x=226, y=6)

    square_3 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l3 = Label(square_3, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l3.pack(padx=1, pady=1.5, fill=Y)
    square_3.place(x=446, y=6)

    # ========= 2nd ROW ========= #
    square_4 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l4 = Label(square_4, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l4.pack(padx=1, pady=1.5, fill=Y)
    square_4.place(x=6, y=176)

    square_5 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l5 = Label(square_5, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l5.pack(padx=1, pady=1.5, fill=Y)
    square_5.place(x=226, y=176)

    square_6 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l6 = Label(square_6, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l6.pack(padx=1, pady=1.5, fill=Y)
    square_6.place(x=446, y=176)

    # ========= 3rd ROW ========= #
    square_7 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l7 = Label(square_7, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l7.pack(padx=1, pady=1.5, fill=Y)
    square_7.place(x=6, y=346)

    square_8 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l8 = Label(square_8, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l8.pack(padx=1, pady=1.5, fill=Y)
    square_8.place(x=226, y=346)

    square_9 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l9 = Label(square_9, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l9.pack(padx=1, pady=1.5, fill=Y)
    square_9.place(x=446, y=346)

    l1.bind('<Button>', check_space)
    l2.bind('<Button>', check_space)
    l3.bind('<Button>', check_space)
    l4.bind('<Button>', check_space)
    l5.bind('<Button>', check_space)
    l6.bind('<Button>', check_space)
    l7.bind('<Button>', check_space)
    l8.bind('<Button>', check_space)
    l9.bind('<Button>', check_space)

    # LIST Variable of the above labels #
    chances = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

    canvas.place(x=(width / 2) - (660 / 2), y=(height / 2) - (510 / 2))

    # ========================== PLAYER NAME =========================== #
    p_name = Label(game_computer, text=player1.get(), font="Corbel 20 bold", bg="#EEEEEE", anchor=W, fg="red")
    p_name.pack(side=LEFT, anchor=NW, padx=5)

    c_name = Label(game_computer, text="Random Bot", font="Corbel 20 bold", bg="#EEEEEE", anchor=W)
    c_name.pack(side=RIGHT, anchor=NE, padx=5)

    


# ========================= ASKING FOR PLAYER NAME IN COMPUTER MODE ================================== #
def __computer__():
    mode.destroy()

    # ================== ALL FUNCTIONS OF THIS WINDOW ================= #
    def __comp_condition__(event=""):
        computer.destroy()
        if player1.get() == "":
            msg.showerror("Error", "Please check that you have entered the name of player.")
            player1.set("")
            __computer__()
        else:
            __play_comp__()

    def _comp_quit_():
        player1.set("")
        player2.set("")
        computer.destroy()
        __game_type__()

    computer = Toplevel(root)
    computer.focus_force()
    w, h = 700, 400
    s_w, s_h = (computer.winfo_screenwidth() // 2 - (w // 2)), (computer.winfo_screenheight() // 2 - (h // 2))
    computer.geometry(f"{w}x{h}+{s_w}+{s_h}")
    computer.title("PLAYER VS COMPUTER")
    computer.iconbitmap("files/ico.ico")
    computer.resizable(0, 0)
    computer.e1 = PhotoImage(file="files/e1.png")  # e is short form of Entry Widget
    computer.e2 = PhotoImage(file="files/e2.png")  # e is short form of Entry Widget
    computer.submit = PhotoImage(file="files/submit.png")
    computer.configure(bg="#8A2BE2")

    # ============================ LAYOUT ====================================== #
    canvas_1 = Canvas(computer, height=6, width=766)
    canvas_1.create_line(0, 1, 766, 1)
    canvas_1.create_line(0, 2, 766, 2)
    canvas_1.create_line(0, 3, 766, 3)
    canvas_1.create_line(0, 4, 766, 4)
    canvas_1.pack()

    heading = Label(computer, text="Enter The Name Of Player", font="Courier 33 bold", pady=5)
    heading.pack(fill=X)

    canvas_2 = Canvas(computer, height=6, width=766)
    canvas_2.create_line(0, 1, 766, 1)
    canvas_2.create_line(0, 2, 766, 2)
    canvas_2.create_line(0, 3, 766, 3)
    canvas_2.create_line(0, 4, 766, 4)
    canvas_2.pack()

    frame1 = Frame(computer, bg="#8A2BE2")
    p_1 = Label(frame1, text="Player's Name:", font="Courier 20 bold", pady=25, bg="#8A2BE2", padx=10)
    p_1.pack(side=LEFT, anchor=W)

    l1 = Label(frame1, image=computer.e1, bg="#8A2BE2")
    l1.pack(side=RIGHT, anchor=E)

    global e1
    player1.set("")

    e1 = Entry(frame1, textvariable=player1, bg="#8A2BE2", font="Courier 25 bold", width=15, relief=FLAT)
    e1.place(x=323, y=23)
    frame1.pack(fill=X, pady=10)

    frame2 = Frame(computer, bg="#8A2BE2")
    p_2 = Label(frame2, text="Computer Name:", font="Courier 20 bold", pady=25, bg="#8A2BE2", padx=10)
    p_2.pack(side=LEFT, anchor=W)

    l2 = Label(frame2, image=computer.e1, bg="#8A2BE2")
    l2.pack(side=RIGHT, anchor=E)

    global e2
    player1.set("")

    e2 = Label(frame2, text="Random Bot", bg="#8A2BE2", font="Courier 25 bold", width=15, relief=FLAT, anchor=W)
    e2.place(x=323, y=23)
    frame2.pack(fill=X, pady=10)

    btn_submit = Button(computer, image=computer.submit, bg="#8A2BE2", bd=0, command=__comp_condition__)
    computer.bind('<Return>', __comp_condition__)
    btn_submit.pack(side=RIGHT, anchor=SE, padx=10, pady=10)

    btn_quit = Button(computer, image=root.exit_btn, bd=0, bg="#8A2BE2", command=_comp_quit_)
    btn_quit.pack(side=LEFT, anchor=SW, padx=10, pady=10)
    


# ============================= GAME AREA FOR 2 PLAYERS ==================================== #

def __play_friend__():
    game_friend = Toplevel(root)
    game_friend.focus_force()
    width, height = 900, 600
    g_w = ((game_friend.winfo_screenwidth() // 2) - (width // 2))
    g_h = ((game_friend.winfo_screenheight() // 2) - (height // 2))
    game_friend.geometry(f"{width}x{height}+{g_w}+{g_h}")
    game_friend.resizable(0, 0)
    game_friend.title("TIC-TAC-TOE")
    game_friend.iconbitmap("files/ico.ico")
    game_friend.configure(bg="#EEEEEE")

    # =============================== FUNCTION OF GAME AREA (P vs P) ===================================== #
    def winner():
        # CONDITION IF PLAYER 1 WINS THE GAME:
        if l1['text'] == l4['text'] == l7['text'] == "  X  " or l2['text'] == l5['text'] == l8['text'] == "  X  " or \
           l3['text'] == l6['text'] == l9['text'] == "  X  " or l1['text'] == l2['text'] == l3['text'] == "  X  " or \
           l4['text'] == l5['text'] == l6['text'] == "  X  " or l7['text'] == l8['text'] == l9['text'] == "  X  " or \
           l1['text'] == l5['text'] == l9['text'] == "  X  " or l3['text'] == l5['text'] == l7['text'] == "  X  ":
            msg.showinfo("Well Done!", f"{player1.get()} won this game by defeating {player2.get()}", parent=game_friend)
            l1['text'] = l2['text'] = l3['text'] = l4['text'] = l5['text'] = l6['text'] = l7['text'] = l8['text']\
                = l9['text'] = "       "

        # CONDITION IF PLAYER 2 WINS THE GAME:
        elif l1['text'] == l4['text'] == l7['text'] == "  O  " or l2['text'] == l5['text'] == l8['text'] == "  O  " or \
                l3['text'] == l6['text'] == l9['text'] == "  O  " or l1['text'] == l2['text'] == l3['text'] == "  O  " or \
                l4['text'] == l5['text'] == l6['text'] == "  O  " or l7['text'] == l8['text'] == l9['text'] == "  O  " or \
                l1['text'] == l5['text'] == l9['text'] == "  O  " or l3['text'] == l5['text'] == l7['text'] == "  O  ":
            msg.showinfo("Well Done!", f"{player2.get()} won this game by defeating {player1.get()}", parent=game_friend)
            l1['text'] = l2['text'] = l3['text'] = l4['text'] = l5['text'] = l6['text'] = l7['text'] = l8['text']\
                = l9['text'] = "       "

        # CONDITION IF TIE BETWEEN THEM:
        elif l1['text'] != "       " and l2['text'] != "       " and l3['text'] != "       " and \
                l4['text'] != "       " and l5['text'] != "       " and l6['text'] != "       " and \
                l7['text'] != "       " and l8['text'] != "       " and l9['text'] != "       ":
            msg.showinfo("Better Luck Next Time!", f"It is a tie between {player1.get()} and {player2.get()}", parent=game_friend)
            l1['text'] = l2['text'] = l3['text'] = l4['text'] = l5['text'] = l6['text'] = l7['text'] = l8['text'] \
                = l9['text'] = "       "

    def which_p_move(event):
        if move.get() == 1:
            event.widget.config(text="  X  ")
            
            p_name1.config(fg="black")
            p_name2.config(fg="red")
            move.set(0)
        elif move.get() == 0:
            event.widget.config(text="  O  ")
          
            p_name1.config(fg="red")
            p_name2.config(fg="black")
            move.set(1)
        winner()

    def check_empty_space(event):
        if event.widget.cget('text') == "       ":
            which_p_move(event)

    # ================================ CANVAS GAME CREATION LAYOUT ==================================== #
    canvas = Canvas(game_friend, height=510, width=660, bg="#8A2BE2", bd=0)

    # ================ VERTICAL LINES ===================== #
    canvas.create_line(219, 0, 219, 510)
    canvas.create_line(220, 0, 220, 510)
    canvas.create_line(221, 0, 221, 510)
    canvas.create_line(439, 0, 439, 510)
    canvas.create_line(440, 0, 440, 510)
    canvas.create_line(441, 0, 441, 510)

    # ================ HORIZONTAL LINES ===================== #
    canvas.create_line(0, 169, 660, 169)
    canvas.create_line(0, 170, 660, 170)
    canvas.create_line(0, 171, 660, 171)
    canvas.create_line(0, 339, 660, 339)
    canvas.create_line(0, 340, 660, 340)
    canvas.create_line(0, 341, 660, 341)

    # =================== CIRCLE AND CROSS ==================== #

    # ========== 1st ROW ========== #
    square_1 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l1 = Label(square_1, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l1.pack(padx=1, pady=1.5, fill=Y)
    square_1.place(x=6, y=6)

    square_2 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l2 = Label(square_2, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l2.pack(padx=1, pady=1.5, fill=Y)
    square_2.place(x=226, y=6)

    square_3 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l3 = Label(square_3, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l3.pack(padx=1, pady=1.5, fill=Y)
    square_3.place(x=446, y=6)

    # ========= 2nd ROW ========= #
    square_4 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l4 = Label(square_4, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l4.pack(padx=1, pady=1.5, fill=Y)
    square_4.place(x=6, y=176)

    square_5 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l5 = Label(square_5, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l5.pack(padx=1, pady=1.5, fill=Y)
    square_5.place(x=226, y=176)

    square_6 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l6 = Label(square_6, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l6.pack(padx=1, pady=1.5, fill=Y)
    square_6.place(x=446, y=176)

    # ========= 3rd ROW ========= #
    square_7 = Frame(canvas, width=190, height=160, bg="#8A2BE2")
    l7 = Label(square_7, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l7.pack(padx=1, pady=1.5, fill=Y)
    square_7.place(x=6, y=346)

    square_8 = Frame(canvas, width=190, height=160, bg="#9370DB")
    l8 = Label(square_8, text="       ", font="Corbel 93 bold", bg="#8A2BE2")  # 7 EMPTY SPACES
    l8.pack(padx=1, pady=1.5, fill=Y)
    square_8.place(x=226, y=346)

    square_9 = Frame(canvas, width=190, height=160, bg="#9370DB")
    l9 = Label(square_9, text="       ", font="Corbel 93 bold", bg="#9370DB")  # 7 EMPTY SPACES
    l9.pack(padx=1, pady=1.5, fill=Y)
    square_9.place(x=446, y=346)

    l1.bind('<Button>', check_empty_space)
    l2.bind('<Button>', check_empty_space)
    l3.bind('<Button>', check_empty_space)
    l4.bind('<Button>', check_empty_space)
    l5.bind('<Button>', check_empty_space)
    l6.bind('<Button>', check_empty_space)
    l7.bind('<Button>', check_empty_space)
    l8.bind('<Button>', check_empty_space)
    l9.bind('<Button>', check_empty_space)

    canvas.place(x=(width / 2) - (660 / 2), y=(height / 2) - (510 / 2))

    # ========================== PLAYER'S NAME =========================== #
    p_name1 = Label(game_friend, text=player1.get(), font="Corbel 20 bold", bg="#EEEEEE", anchor=W, fg="red")
    p_name1.pack(side=LEFT, anchor=NW, padx=5)

    p_name2 = Label(game_friend, text=player2.get(), font="Corbel 20 bold", bg="#EEEEEE", anchor=W)
    p_name2.pack(side=RIGHT, anchor=NE, padx=5)




def __condition__(event=""):
    players.destroy()
    if player1.get() == "" or player2.get() == "":
        msg.showerror("Error", "Please check that you have entered the name of players.")
        player1.set("")
        player2.set("")
        __players__()
    else:
        __play_friend__()


def _quit_():
    player1.set("")
    player2.set("")
    players.destroy()
    __game_type__()


# =============================== PLAY WITH FRIENDS WINDOW ====================================== #
def __players__():
    global players
    mode.destroy()
    players = Toplevel(root)
    players.focus_force()
    w, h = 700, 400
    s_w, s_h = (players.winfo_screenwidth() // 2 - (w // 2)), (players.winfo_screenheight() // 2 - (h // 2))
    players.geometry(f"{w}x{h}+{s_w}+{s_h}")
    players.title("PLAYER VS PLAYER")
    players.iconbitmap("files/ico.ico")
    players.resizable(0, 0)
    players.e1 = PhotoImage(file="files/e1.png")  # e is short form of Entry Widget
    players.e2 = PhotoImage(file="files/e2.png")  # e is short form of Entry Widget
    players.submit = PhotoImage(file="files/submit.png")
    players.configure(bg="#8A2BE2")

    # ============================ LAYOUT ====================================== #
    canvas_1 = Canvas(players, height=6, width=766)
    canvas_1.create_line(0, 1, 766, 1)
    canvas_1.create_line(0, 2, 766, 2)
    canvas_1.create_line(0, 3, 766, 3)
    canvas_1.create_line(0, 4, 766, 4)
    canvas_1.pack()

    heading = Label(players, text="Enter The Name Of Players", font="Courier 33 bold", pady=5)
    heading.pack(fill=X)

    canvas_2 = Canvas(players, height=6, width=766)
    canvas_2.create_line(0, 1, 766, 1)
    canvas_2.create_line(0, 2, 766, 2)
    canvas_2.create_line(0, 3, 766, 3)
    canvas_2.create_line(0, 4, 766, 4)
    canvas_2.pack()

    frame1 = Frame(players, bg="#8A2BE2")
    p_1 = Label(frame1, text="Player's Name:", font="Courier 20 bold", pady=25, bg="#8A2BE2", padx=10)
    p_1.pack(side=LEFT, anchor=W)

    l1 = Label(frame1, image=players.e1, bg="#8A2BE2")
    l1.pack(side=RIGHT, anchor=E)

    global e1
    player1.set("")

    e1 = Entry(frame1, textvariable=player1, bg="#8A2BE2", font="Courier 25 bold", width=15, relief=FLAT)
    e1.place(x=323, y=23)
    frame1.pack(fill=X, pady=10)

    frame2 = Frame(players, bg="#8A2BE2")
    p_2 = Label(frame2, text="Player's Name:", font="Courier 20 bold", pady=25, bg="#8A2BE2", padx=10)
    p_2.pack(side=LEFT, anchor=W)

    l2 = Label(frame2, image=players.e1, bg="#8A2BE2")
    l2.pack(side=RIGHT, anchor=E)

    global e2
    player1.set("")

    e2 = Entry(frame2, textvariable=player2, bg="#8A2BE2", font="Courier 25 bold", width=15, relief=FLAT)
    e2.place(x=323, y=23)
    frame2.pack(fill=X, pady=10)

    btn_submit = Button(players, image=players.submit, bg="#8A2BE2", bd=0, command=__condition__)
    players.bind('<Return>', __condition__)
    btn_submit.pack(side=RIGHT, anchor=SE, padx=10, pady=10)

    btn_quit = Button(players, image=root.exit_btn, bd=0, bg="#8A2BE2", command=_quit_)
    btn_quit.pack(side=LEFT, anchor=SW, padx=10, pady=10)



# =============================== GAME TYPE FUNCTIONS ========================================= #
def __game_type__():
    global mode
    mode = Toplevel(root)
    mode.focus_force()
    w, h = 766, 400
    s_w, s_h = (mode.winfo_screenwidth() // 2 - (w // 2)), (mode.winfo_screenheight() // 2 - (h // 2))
    mode.geometry(f"{w}x{h}+{s_w}+{s_h}")
    mode.title("CHOOSE THE GAME")
    mode.iconbitmap('files/ico.ico')
    mode.resizable(0, 0)
    mode.computer = PhotoImage(file="files/computer.png")
    mode.friend = PhotoImage(file="files/friend.png")

    # ================== FUNCTIONS FOR MODE WINDOW ==================== #
    def __exit_mode__():
      
        mode.destroy()

    # ========================= LAYOUT ================================ #
    canvas_1 = Canvas(mode, height=6, width=766)
    canvas_1.create_line(0, 1, 766, 1)
    canvas_1.create_line(0, 2, 766, 2)
    canvas_1.create_line(0, 3, 766, 3)
    canvas_1.create_line(0, 4, 766, 4)
    canvas_1.pack()

    head = Label(mode, text="Play With Computer Or Friend", font="Courier 33 bold", pady=5)
    head.pack(fill=X)

    canvas_2 = Canvas(mode, height=6, width=766)
    canvas_2.create_line(0, 1, 766, 1)
    canvas_2.create_line(0, 2, 766, 2)
    canvas_2.create_line(0, 3, 766, 3)
    canvas_2.create_line(0, 4, 766, 4)
    canvas_2.pack()

    btn1 = Button(mode, image=mode.computer, bd=0, command=__computer__)
    btn1.pack(pady=10)

    btn2 = Button(mode, image=mode.friend, bd=0, command=__players__)
    btn2.pack(pady=10)

    btn3 = Button(mode, image=root.exit_btn, bd=0, command=__exit_mode__)
    btn3.pack(side=RIGHT, anchor=E, pady=5, padx=5)



# ============================= MAIN WINDOW ===================================== #

root = Tk()
mixer.init()

# ======================================= FUNCTIONS ============================================ #



# EXIT COMMAND #
def ___exit___():
    root.destroy()


m_width, m_height = 700, 360
s_width = ((root.winfo_screenwidth() // 2) - (m_width // 2))
s_height = ((root.winfo_screenheight() // 2) - (m_height // 2))
root.geometry(f'{m_width}x{m_height}+{s_width}+{s_height}')
root.title("TIC TAC TOE")
root.resizable(0, 0)
root.iconbitmap("files/ico.ico")
root.heading = PhotoImage(file="files/background.png")
root.play_btn = PhotoImage(file="files/play.png")
root.exit_btn = PhotoImage(file="files/exit.png")


# VARIABLES #
pop = IntVar(root, 1)
musical = IntVar(root, 1)
move = IntVar(root, 1)
player1 = StringVar()
player2 = StringVar()

# =============================== LAYOUT ================================== #
lbl = Label(root, image=root.heading)
lbl.pack(pady=10)

play = Button(root, image=root.play_btn, bd=0, relief=FLAT, command=__game_type__)
play.pack(pady=10)


exited = Button(root, image=root.exit_btn, bd=0, relief=FLAT, command=___exit___)
exited.pack(anchor=S, side=RIGHT, padx=3, pady=3)



root.mainloop()
