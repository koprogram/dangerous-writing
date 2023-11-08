import tkinter as tk
from threading import Timer

# Define the main application class
class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")

        # Configure the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Add a Text widget where the user can type
        self.text_area = tk.Text(self.main_frame, wrap="word")
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.text_area.bind("<Key>", self.reset_timer)  # Bind the key press event to reset the timer

        # Timer that will trigger the deletion of the text
        self.deletion_timer = None
        self.time_limit = 5  # 5 seconds time limit

        # Start the timer when the app runs
        self.reset_timer()

    def reset_timer(self, event=None):
        # If there is an existing timer, cancel it
        if self.deletion_timer is not None:
            self.deletion_timer.cancel()

        # Start a new timer
        self.deletion_timer = Timer(self.time_limit, self.delete_text)
        self.deletion_timer.start()

    def delete_text(self):
        # Clear the Text widget
        self.text_area.delete('1.0', tk.END)

# Create the Tkinter window
root = tk.Tk()

# Set the window size and position
root.geometry("600x400+100+100")

# Create and run the application
app = DangerousWritingApp(root)
root.mainloop()
