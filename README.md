import tkinter as tk
from tkinter import Toplevel, messagebox

# Function to open the football stats entry window
def open_football_stats_window():
    open_stats_window("football")

# Function to open the boys basketball stats entry window
def open_boys_basketball_stats_window():
    open_stats_window("boys basketball")

# Function to open the girls basketball stats entry window
def open_girls_basketball_stats_window():
    open_stats_window("girls basketball")

# Function to open the stats entry window
def open_stats_window(sport):
    # Create a new window for stats entry
    stats_window = Toplevel(root)
    stats_window.title(f"{sport.capitalize()} Stats")
    stats_window.geometry("600x300") 

    if sport == "football":
        create_football_stats_window(stats_window)
    elif sport == "boys basketball" or sport == "girls basketball":
        create_basketball_stats_window(stats_window)
    else:
        error_label = tk.Label(stats_window, text="Sport not supported.")
        error_label.pack(pady=10)

# Function to create football stats window
def create_football_stats_window(window):
    player_label = tk.Label(window, text="Player Name: ")
    player_label.pack()
    player_entry = tk.Entry(window)
    player_entry.pack()

    goals_label = tk.Label(window, text="Catching Attempts: ")
    goals_label.pack()
    goals_entry = tk.Entry(window)
    goals_entry.pack()

    assists_label = tk.Label(window, text="Rushing Attempts: ")
    assists_label.pack()
    assists_entry = tk.Entry(window)
    assists_entry.pack()

    assists_label = tk.Label(window, text="Touchdowns: ")
    assists_label.pack()
    assists_entry = tk.Entry(window)
    assists_entry.pack()

    # Function to display football stats
    def display_football_stats():
        player = player_entry.get()
        goals = goals_entry.get()
        assists = assists_entry.get()

        if not player or not goals or not assists:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        result_label.config(text=f"Player: {player}\nGoals: {goals}\nAssists: {assists}")

    display_button = tk.Button(window, text="Display Stats", command=display_football_stats)
    display_button.pack(pady=10)

    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

# Function to create basketball stats window
def create_basketball_stats_window(window):
    player_label = tk.Label(window, text="Player Name: ")
    player_label.pack()
    player_entry = tk.Entry(window)
    player_entry.pack()
    
    shots_taken_label = tk.Label(window, text="Shots Taken: ")
    shots_taken_label.pack()
    shots_taken_entry = tk.Entry(window)
    shots_taken_entry.pack()

    points_label = tk.Label(window, text="Points: ")
    points_label.pack()
    points_entry = tk.Entry(window)
    points_entry.pack()

    rebounds_label = tk.Label(window, text="Rebounds: ")
    rebounds_label.pack()
    rebounds_entry = tk.Entry(window)
    rebounds_entry.pack()

    assists_label = tk.Label(window, text="Assists: ")
    assists_label.pack()
    assists_entry = tk.Entry(window)
    assists_entry.pack()

    # Function to display basketball stats
    def display_basketball_stats():
        player = player_entry.get()
        shots_taken = shots_taken_entry.get()
        points = points_entry.get()
        rebounds = rebounds_entry.get()
        assists = assists_entry.get()

        if not player or not shots_taken or not points or not rebounds or not assists:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        result_label.config(text=f"Player: {player}\nShots Taken: {shots_taken}\nPoints: {points}\nRebounds: {rebounds}\nAssists: {assists}")

    display_button = tk.Button(window, text="Display Stats", command=display_basketball_stats)
    display_button.pack(pady=10)

    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

# Function to exit the application
def exit_application():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Sport Selection")

# Create a label for the title
title_label = tk.Label(root, text="Select Sport", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create buttons for sport selection
football_button = tk.Button(root, text="Football", command=open_football_stats_window)
football_button.pack(pady=5)

boys_basketball_button = tk.Button(root, text="Boys Basketball", command=open_boys_basketball_stats_window)
boys_basketball_button.pack(pady=5)

girls_basketball_button = tk.Button(root, text="Girls Basketball", command=open_girls_basketball_stats_window)
girls_basketball_button.pack(pady=5)

# Create exit button
exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.pack(pady=5)

# Run the application
root.mainloop()
