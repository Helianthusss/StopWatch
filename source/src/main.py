import tkinter as tk
from tkinter import *
import time
import threading

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")
        
        self.time_var = tk.StringVar()
        self.time_var.set("00:00:0")
        self.time_label = tk.Label(self.master, textvariable=self.time_var, font=("Helvetica", 80))
        self.time_label.pack()
        
        self.start_time = None
        self.is_running = False
        
        self.start_button = tk.Button(self.master, text="Start", command=self.start)
        self.start_button.pack(side="left", padx=10, pady=10)
        
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(side="left", padx=10, pady=10)
        self.stop_button.configure(state="disabled")
        
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", padx=10, pady=10)
        self.reset_button.configure(state="disabled")
        
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(side="left", padx=10, pady=10)
        
    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            self.start_button.configure(state="disabled")
            self.stop_button.configure(state="normal")
            self.reset_button.configure(state="disabled")
            self.update_clock()
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            self.start_button.configure(state="normal")
            self.stop_button.configure(state="disabled")
            self.reset_button.configure(state="normal")
    
    def reset(self):
        self.is_running = False
        self.start_time = None
        self.time_var.set("00:00.0")
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.reset_button.configure(state="disabled")
    
    def update_clock(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(elapsed_time, 60)
            minutes, seconds = int(minutes), int(seconds)
            milliseconds = int((elapsed_time - int(elapsed_time)) * 10)
            self.time_var.set(f"{minutes:02}:{seconds:02}.{milliseconds:01}")
            self.master.after(100, self.update_clock)
    
root = tk.Tk()
app = Stopwatch(root)
root.mainloop()