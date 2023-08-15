import tkinter as tk
import time
import threading
import random

class SpeedTyping:
    #Creating a constructor
    def __init__(self):
        self.prompt = tk.Tk()
        self.prompt.title("Speed typing test")
        self.prompt.geometry("800x400")
        self.text = open("text.txt", "r").read().split("\n")
        self.frame = tk.Frame(self.prompt)
        #Creating a label named sample_label
        self.sample_label = tk.Label(self.frame, text=random.choice(self.text), font=("Helvetica", 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        #Creating a text box named input_entry
        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        #Adding the function to start automatically if the key is pressed
        self.input_entry.bind("<KeyRelease>", self.start)
        #Creating a label named speed_label for the timer
        self.speed_label = tk.Label(self.frame, text="Speed:\n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM", font=("Helvetica", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        #Creating a reset button
        self.reset_button = tk.Button(self.frame, text="Reset",bg="dark gray", command=self.reset, font=("Helvetica", 24))
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        self.frame.pack(expand=True)
        #Adding a boolean to know that the app is started or not
        self.counter = 0
        self.running = False
        self.prompt.mainloop()
    #Defining the start function with parameters
    def start(self, event):
        if not self.running:
            if event.keycode not in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text')[:-1]:
            self.running = False
            self.input_entry.config(fg="green")
    #Defining the time function in a different thread
    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM")
    #Defining the reset function
    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM")
        self.sample_label.config(text=random.choice(self.text))
        self.input_entry.delete(0, tk.END)
#Created an instance of Speedtyping class and start the application
SpeedTyping()