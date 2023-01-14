import tkinter as tk
from tkinter import messagebox
import time
from random_words import RandomWords

characters_typed = 1
correct_counter = 0
tocni_zborovi = 0
correct_wpm = 0
timeleft = 60
cnt = True
timer_started = False
index = 0
labels = []
cnt = True




def start_timer():
    global start_time, timer_started, timeleft, cnt
    if not timer_started:
        start_time = time.time()
        timeleft = 60
        timer_started = True
        if cnt:
            count_time()
            cnt = False
def check_word(event):
    global words, index, labels, correct_counter, original_text, tocni_zborovi, characters_typed
    entered_word = entry.get()
    # print(original_text[index + correct_counter])
    if entered_word == original_text[index + correct_counter]:
        characters_typed += len(entered_word)
        labels[correct_counter].config(fg="black", bg="green")
        tocni_zborovi += 1
    else:
        labels[correct_counter].config(fg="black", bg="red")
    if correct_counter == 9:
        for labeli in labels:
            labeli.destroy()
            correct_counter = 0
        index += 10
        create_labels()
    else:
        correct_counter += 1
    entry.delete(0, tk.END)


def create_labels():
    global labels, original_text, index
    labels = []
    for i in range(10):
        # print(index)
        label = tk.Label(root, text=original_text[i+index], font=("Arial", 16))
        label.grid(row=0, column=i)
        labels.append(label)
    

def restart():
    global original_text, index, words, timer_started, labels, correct_counter, tocni_zborovi, characters_typed, lbl_time
    # Generate a new list of 100 words
    words = rw.random_words(count=100)
    words = [' '.join(words[i:i+10]) for i in range(0, len(words), 10)]
    random_text = '\n'.join(words)
    original_text = random_text.split()
    index = 0
    correct_counter = 0
    tocni_zborovi = 0
    characters_typed = 0
    timer_started = False
    timeleft = 60
    lbl_time.config(text="Time left: " + str(timeleft))
    for labeli in labels:
        labeli.destroy()
    entry.bind("<Key>", start_and_count)
    create_labels()



def start_and_count(event):
    if timer_started == False:
        start_timer()
    entry.bind("<Return>", check_word)
    


def count_time():
    global timeleft, lbl_time
    if timeleft > 0:
        timeleft -= 1
        lbl_time.config(text="Time left: " + str(timeleft))
        lbl_time.after(1000, count_time)

    else:
        check_typing()


def check_typing():
    global start_time, tocni_zborovi, characters_typed
    end_time = time.time()
    elapsed_time = end_time - start_time
    messagebox.showinfo("Results", "Correct CPM : {}\n WPM : {}\n".format(characters_typed / (elapsed_time/60), tocni_zborovi/(elapsed_time/60)))
    # entry.config(state="disabled")



root = tk.Tk()
root.title("Typing Test")
root.geometry('900x400')

rw = RandomWords()
words = rw.random_words(count=100)
words = [' '.join(words[i:i+10]) for i in range(0, len(words), 10)]
random_text = '\n'.join(words)
original_text = random_text.split()

create_labels()

entry = tk.Entry(root)
entry.bind("<Key>", start_and_count)
entry.grid(row=1, column=5)
restart_button = tk.Button(root, text = "Restart", command = restart)
restart_button.grid(row=2, column=5)
lbl_time = tk.Label(root, text="Time left: " + str(timeleft))
lbl_time.grid(row=3, column=5)

root.mainloop()