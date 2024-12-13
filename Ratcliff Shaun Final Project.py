import tkinter as tk
from tkinter import Toplevel, messagebox, Canvas
from PIL import Image, ImageTk  # Importing Pillow for image handling

# Callback functions for sport buttons
def sport_callback(sport):
    """
    Callback function for sport buttons.
    Opens the stats window for the selected sport.
    """
    print(f"{sport.capitalize()} Callback")
    open_stats_window(sport)

# Function to open the stats entry window
def open_stats_window(sport):
    """
    Opens a new window for stats entry based on the selected sport.
    Adjusts window size for basketball stats.
    """
    stats_window = Toplevel(root)  # Create a new top-level window
    stats_window.title(f"{sport.capitalize()} Stats")  # Set the window title

    # Adjust window size based on the sport
    if sport in ["boys basketball", "girls basketball"]:
        stats_window.geometry("1000x1000")  # Larger size for basketball windows
    else:
        stats_window.geometry("1000x1000")  # Default size for football

    # Call the appropriate function to create the stats window
    if sport == "football":
        create_football_stats_window(stats_window, sport)
    elif sport in ["boys basketball", "girls basketball"]:
        create_basketball_stats_window(stats_window, sport)
    else:
        error_label = tk.Label(stats_window, text="Sport not supported.")
        error_label.pack(pady=10)

# Function to create football stats window
def create_football_stats_window(window, sport):
    """
    Creates the football stats entry window with input fields and display button.
    """
    # Create and pack the player name label and entry
    player_label = tk.Label(window, text="Player Name: ")
    player_label.pack()
    player_entry = tk.Entry(window)
    player_entry.pack()

    # Create and pack the catching attempts label and entry
    catching_attempts_label = tk.Label(window, text="Catching Attempts: ")
    catching_attempts_label.pack()
    catching_attempts_entry = tk.Entry(window)
    catching_attempts_entry.pack()

    # Create and pack the rushing attempts label and entry
    rushing_attempts_label = tk.Label(window, text="Rushing Attempts: ")
    rushing_attempts_label.pack()
    rushing_attempts_entry = tk.Entry(window)
    rushing_attempts_entry.pack()

    # Create and pack the touchdowns label and entry
    touchdowns_label = tk.Label(window, text="Touchdowns: ")
    touchdowns_label.pack()
    touchdowns_entry = tk.Entry(window)
    touchdowns_entry.pack()

    # Function to display football stats
    def display_football_stats():
        """
        Displays the entered football stats in a label.
        """
        player = player_entry.get()  # Get player name
        catching_attempts = catching_attempts_entry.get()  # Get catching attempts
        rushing_attempts = rushing_attempts_entry.get()  # Get rushing attempts
        touchdowns = touchdowns_entry.get()  # Get touchdowns

        # Check if all fields are filled out
        if not player or not catching_attempts or not rushing_attempts or not touchdowns:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        # Display the stats in the result label
        result_label.config(text=f"Player: {player}\nCatching Attempts: {catching_attempts}\nRushing Attempts: {rushing_attempts}\nTouchdowns: {touchdowns}")

    # Create the display button
    display_button = tk.Button(window, text="Display Stats", command=display_football_stats)
    display_button.pack(pady=10)

    # Create the result label
    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

    # Load and display an image for football
    if sport.lower() == "football":
        load_image(window, r"C:\\Users\\srat\\OneDrive\\Documents\\football.png")

    # Add exit button
    exit_button = tk.Button(window, text="Exit", command=window.destroy)
    exit_button.pack(pady=5)

# Load and display an image
def load_image(window, image_path):
    """
    Loads and displays an image in the given window.
    """
    try:
        image = Image.open(image_path)  # Open the image file
        image = image.resize((100, 100), Image.Resampling.LANCZOS)  # Resize the image
        photo = ImageTk.PhotoImage(image)  # Convert to PhotoImage

        # Create a canvas and display the image
        canvas = Canvas(window, width=100, height=100)
        canvas.pack(pady=10)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo  # Keep a reference to avoid garbage collection
    except Exception as e:
        messagebox.showerror("Image Error", f"Failed to load image: {e}")

# Function to create basketball stats window
def create_basketball_stats_window(window, sport):
    """
    Creates the basketball stats entry window with input fields and display button.
    """
    # Create the player name label and entry
    player_label = tk.Label(window, text="Player Name: ")
    player_label.pack()
    player_entry = tk.Entry(window)
    player_entry.pack()
    
    # Create the shots taken label and entry
    shots_taken_label = tk.Label(window, text="Shots Taken: ")
    shots_taken_label.pack()
    shots_taken_entry = tk.Entry(window)
    shots_taken_entry.pack()

    # Create the points label and entry
    points_label = tk.Label(window, text="Points: ")
    points_label.pack()
    points_entry = tk.Entry(window)
    points_entry.pack()

    # Create and pack the rebounds label and entry
    rebounds_label = tk.Label(window, text="Rebounds: ")
    rebounds_label.pack()
    rebounds_entry = tk.Entry(window)
    rebounds_entry.pack()

    # Create and pack the assists label and entry
    assists_label = tk.Label(window, text="Assists: ")
    assists_label.pack()
    assists_entry = tk.Entry(window)
    assists_entry.pack()

    # Function to display basketball stats
    def display_basketball_stats():
        """
        Displays the entered basketball stats in a label.
        """
        player = player_entry.get()  # Get player name
        shots_taken = shots_taken_entry.get()  # Get shots taken
        points = points_entry.get()  # Get points
        rebounds = rebounds_entry.get()  # Get rebounds
        assists = assists_entry.get()  # Get assists

        # Check if all fields are filled out
        if not player or not shots_taken or not points or not rebounds or not assists:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        # Display the stats in the result label
        result_label.config(text=f"Player: {player}\nShots Taken: {shots_taken}\nPoints: {points}\nRebounds: {rebounds}\nAssists: {assists}")

    # Create the display button
    display_button = tk.Button(window, text="Display Stats", command=display_basketball_stats)
    display_button.pack(pady=10)

    # Create the result label
    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

    # Load and display an image for boys basketball
    if sport.lower() == "boys basketball":
        load_image(window, r"C:\\Users\\srat\\OneDrive\\Documents\\Boy basketball player.jpg")

    # Add exit button for both boys and girls basketball
    exit_button = tk.Button(window, text="Exit", command=window.destroy)
    exit_button.pack(pady=5)

# Function to handle exit button callback
def on_exit():
    """
    Handles the exit button callback.
    Performs cleanup actions and closes the application.
    """
    print("Exiting the application...")  # Print exit message
    root.destroy()  # Destroy the main window

# Create the main window
root = tk.Tk()
root.title("Sport Selection")  # Set the window title

# Create a label for the title
title_label = tk.Label(root, text="Select Sport", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create buttons for sport selection
football_button = tk.Button(root, text="Football", command=lambda: sport_callback("football"))
football_button.pack(pady=5)

boys_basketball_button = tk.Button(root, text="Boys Basketball", command=lambda: sport_callback("boys basketball"))
boys_basketball_button.pack(pady=5)

girls_basketball_button = tk.Button(root, text="Girls Basketball", command=lambda: sport_callback("girls basketball"))
girls_basketball_button.pack(pady=5)

# Create exit button
exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack(pady=5)

# Run the application
root.mainloop()