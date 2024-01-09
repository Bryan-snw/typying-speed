from tkinter import *
from random import choice
from words import words_list

# ---------------------------- VARIABLE ------------------------------- #
BACKGROUND = "#332941"
second = 60
num_word = 0
words = []
correct_words = 0


# ---------------------------- FUNCTION ------------------------------- #
def reset():
    global second, num_word, words, correct_words
    # reset variable
    second = 60
    num_word = 0
    correct_words = 0

    word_input.delete(0, END)

    # Enable Input for word and unbind the key
    word_input.config(state="normal")
    # Binding key for input
    word_input.bind("<space>", on_key_press)

    # Remove Score Label
    score_label.grid_remove()

    reset_btn.grid_remove()

    # start time again
    start_time()


def start_time():
    global words
    # Choose random array from words list
    words = choice(words_list)

    words_label.config(bg='white')

    # removing start button
    start_btn.grid_remove()

    # Showing label for word
    words_label.config(text=f"{words[num_word]} {words[num_word + 1]} {words[num_word + 2]} {words[num_word + 3]} "
                            f"{words[num_word + 4]}")
    words_label.grid(column=0, row=2)

    # showing input for word
    word_input.grid(column=0, row=3, pady=(20, 10))
    word_input.focus()

    # calling update_time after 1 second
    window.after(1000, update_timer)


def update_timer():
    global second, correct_words
    second -= 1

    if second < 10:
        time = f'00:0{second}'
    else:
        time = f'00:{second}'

    # change the label words
    timer_label.config(text=time)

    # if the time still on then
    if second > 0:
        # Call the function again recursion
        window.after(1000, update_timer)
    else:
        # disable Input for word and unbind the key
        word_input.config(state="disabled")
        word_input.unbind("<space>")

        # Showing Score Label
        score_label.config(text=f'Correct Word Count: {correct_words} WPM')
        score_label.grid(column=0, row=5)

        # Showing reset Button
        reset_btn.grid(column=0, row=6)


def on_key_press(event):
    global words, num_word, correct_words

    input_text = word_input.get().strip()

    if words[num_word] == input_text:
        words_label.config(bg='#A2FF86')
        correct_words += 1
    else:
        words_label.config(bg='#FF6D60')

    word_input.delete(0, END)
    num_word += 1
    words_label.config(text=f"{words[num_word]} {words[num_word + 1]} {words[num_word + 2]} {words[num_word + 3]} "
                            f"{words[num_word + 4]}")


# ---------------------------- UI DESIGN ------------------------------- #
window = Tk()
window.config(bg="#332941", padx=40, pady=40)
window.title("Typing Speed Test")
# Set the window size
window_width = 750
window_height = 400

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Set the window geometry
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Heading
title_label = Label(text='Typing Test Speed', bg=BACKGROUND, fg='white', font=('flash rogers', 38, 'bold'))
title_label.grid(column=0, row=0)

# Timer Label
timer_label = Label(text="00:00", bg=BACKGROUND, fg="white", font=('arial', 42), pady=10)
timer_label.grid(column=0, row=1, sticky='nsew')

# Words Label
words_label = Label(text="", font=('arial', 18), width=45)

# Input/Entry
word_input = Entry(width=50, font=('arial', 16), justify='center')

# Binding key for input
word_input.bind("<space>", on_key_press)

# Score Label
score_label = Label(text="", font=('arial', 16, 'bold'), bg=BACKGROUND, fg='white',  pady=10)

# Button
start_btn = Button(text="Start", width=60, font=12, borderwidth=2, command=start_time)
start_btn.grid(column=0, row=2, sticky='nsew')

# Button
reset_btn = Button(text="Play Again", width=60, font=12, borderwidth=2, command=reset)

# # shadow so the design doesn't change
shadow = Label(text="", width=60, font=12, bg=BACKGROUND, relief="flat")
shadow.grid(column=0, row=8, sticky='nsew')

window.mainloop()
