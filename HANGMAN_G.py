import tkinter as tk
from tkinter import messagebox
import random
import string
import os

# Dictionary of words and their hints
word_dict = {
    "PYTHON": "A popular programming language",
    "HANGMAN": "Classic guessing game",
    "COMPUTER": "Electronic device for processing data",
    "PROGRAMMING": "Writing code",
    "DEVELOPER": "A person who writes software",
    "KEYBOARD": "Input device with keys",
    "MOUSE": "Used to point and click",
    "MONITOR": "Displays computer output",
    "LAPTOP": "Portable computer",
    "PRINTER": "Produces physical documents",
    "SOFTWARE": "Programs and operating systems",
    "HARDWARE": "Physical components of a computer",
    "INTERNET": "Global network",
    "ROUTER": "Connects networks",
    "MODEM": "Device that connects to internet",
    "BROWSER": "Used to access websites",
    "GOOGLE": "Popular search engine",
    "WEBSITE": "Collection of web pages",
    "DATABASE": "Organized data storage",
    "NETWORK": "Interconnected computers",
    "FIREWALL": "Protects against unauthorized access",
    "ANTIVIRUS": "Protects from malware",
    "BACKUP": "Copy of data for recovery",
    "CLOUD": "Online data storage",
    "EMAIL": "Electronic message",
    "SPAM": "Unwanted email",
    "PASSWORD": "Used to authenticate user",
    "LOGIN": "Accessing a system",
    "BIT": "Smallest data unit",
    "BYTE": "8 bits",
    "GIGABYTE": "Around 1 billion bytes",
    "TERABYTE": "Around 1000 gigabytes",
    "PROCESSOR": "CPU, brain of the computer",
    "MEMORY": "Temporarily stores data",
    "STORAGE": "Long-term data saving",
    "USB": "Universal Serial Bus",
    "HDMI": "Video/audio interface",
    "VIRUS": "Malicious software",
    "MALWARE": "General term for bad software",
    "SPYWARE": "Secretly monitors user",
    "PHISHING": "Tricks users into revealing info",
    "ENCRYPTION": "Protecting data by encoding",
    "DECRYPTION": "Converting back encoded data",
    "SCRIPT": "Small program",
    "FUNCTION": "Reusable block of code",
    "LOOP": "Repeats a set of instructions",
    "CONDITIONAL": "Performs logic like if-else",
    "DEBUGGING": "Fixing code errors",
    "ALGORITHM": "Set of instructions",
    "VARIABLE": "Stores a value in programming",
    "OBJECT": "Instance in OOP",
    "CLASS": "Blueprint in OOP",
    "MODULE": "Reusable Python file",
    "PACKAGE": "Collection of modules",
    "GITHUB": "Code hosting platform",
    "REPOSITORY": "Project storage in Git",
    "TERMINAL": "Command line interface",
    "SHELL": "Command interpreter",
    "LINUX": "Popular open-source OS",
    "WINDOWS": "Microsoft operating system",
    "MACOS": "Apple's operating system",
    "ANDROID": "Google's mobile OS",
    "IOS": "Apple's mobile OS",
    "APP": "Application software",
    "FRAMEWORK": "Code structure for development",
    "LIBRARY": "Reusable code collection",
    "PYGAME": "Python game dev library",
    "DJANGO": "Python web framework",
    "FLASK": "Lightweight Python web framework",
    "NUMPY": "Python math library",
    "PANDAS": "Python data analysis library",
    "MATPLOTLIB": "Python plotting library",
    "SCIPY": "Scientific Python tools",
    "TENSORFLOW": "ML framework",
    "KERAS": "Deep learning API",
    "NEURAL": "Network for deep learning",
    "DATA": "Information",
    "BIGDATA": "Very large datasets",
    "AI": "Artificial Intelligence",
    "ML": "Machine Learning",
    "DL": "Deep Learning",
    "MODEL": "Trained ML structure",
    "TRAINING": "Learning from data",
    "PREDICTION": "Estimating outcomes",
    "ACCURACY": "Correctness measure",
    "LOSS": "Model error measurement",
    "GRADIENT": "Slope of error",
    "OPTIMIZER": "Improves model performance",
    "ACTIVATION": "Function in neural nets",
    "RELU": "Popular activation function",
    "SIGMOID": "Squashes values 0-1",
    "SOFTMAX": "Outputs probability",
    "CROSSVALIDATION": "Model evaluation technique",
    "FEATURE": "Input to model",
    "LABEL": "Output in supervised learning",
    "SUPERVISED": "Learning with labels",
    "UNSUPERVISED": "Learning without labels",
    "CLUSTERING": "Grouping similar data",
    "CLASSIFICATION": "Label prediction",
    "REGRESSION": "Numerical prediction",
    "ABSTRACTION": "OOP principle that hides implementation details",
    "AGILE": "Software development methodology",
    "ASYNC": "Non-blocking execution model",
    "BANDWIDTH": "Amount of data transmitted in a given time",
    "BINARY": "Base-2 numeral system",
    "BITCOIN": "Popular cryptocurrency",
    "BLOCKCHAIN": "Distributed digital ledger",
    "BOOLEAN": "Data type with true or false",
    "BOOT": "Starting a computer",
    "BUG": "Error in a program",
    "CACHE": "Temporary storage for fast access",
    "CAPTCHA": "Test to distinguish humans from bots",
    "CDN": "Delivers web content closer to users",
    "CLI": "Command-line interface",
    "COMPILE": "Convert code to machine language",
    "COMPRESSION": "Reducing data size",
    "COOKIE": "Small piece of data stored by browser",
    "CYBERSECURITY": "Protection of computer systems",
    "DATAFRAME": "2D labeled data structure in pandas",
    "DATAMINING": "Extracting patterns from data",
    "DEFRAGMENT": "Reorganize data on a disk",
    "DNS": "Translates domain names to IP",
    "DOM": "Document Object Model in web development",
    "DOS": "Older disk-based operating system",
    "DRIVER": "Software to control hardware",
    "DYNAMIC": "Executed at runtime",
    "EMULATOR": "Imitates another system",
    "ETHERNET": "Wired network protocol",
    "EXCEL": "Spreadsheet software by Microsoft",
    "EXCEPTION": "Error event in programming",
    "EXPONENTIAL": "Rapid increase rate",
    "FIBONACCI": "Mathematical sequence",
    "FIREBASE": "Google mobile development platform",
    "FIRMWARE": "Software for hardware control",
    "FLIPFLOP": "Basic memory circuit",
    "FLOP": "Floating point operation",
    "FORMAT": "Prepare a storage medium",
    "FRONTEND": "Client-side part of a web app",
    "FTP": "File transfer protocol",
    "FULLSTACK": "Frontend and backend development",
    "FUNCTIONAL": "Programming paradigm using functions",
    "GATEWAY": "Network point connecting two networks",
    "GIGAHERTZ": "Frequency unit for processors",
    "GIT": "Version control system",
    "HASH": "Function that maps data to values",
    "HEXADECIMAL": "Base-16 numeral system",
    "HOST": "Computer on a network",
    "HTML": "Markup language for web pages",
    "HTTP": "Protocol for web communication",
    "HTTPS": "Secure version of HTTP",
    "IDE": "Integrated development environment",
    "INDEX": "Database pointer for fast access",
    "INPUT": "Data provided to a system",
    "INSTANCE": "Specific object of a class",
    "INTERFACE": "Shared boundary across systems",
    "IP": "Internet Protocol address",
    "ITERATOR": "Object that enables looping",
    "JAVA": "Object-oriented programming language",
    "JAVASCRIPT": "Scripting language for web",
    "JQUERY": "JavaScript library",
    "JSON": "Data format based on key-value pairs",
    "KERNEL": "Core part of an OS",
    "KEY": "Identifier in key-value pair",
    "KEYFRAME": "Defines motion in animation",
    "LATENCY": "Delay before data transfer",
    "LAYER": "Level in a neural network",
    "LEARNINGRATE": "Controls speed of training",
    "LINKEDLIST": "Linear data structure",
    "LOADBALANCER": "Distributes network traffic",
    "LOCALE": "Language and region settings",
    "LOGIC": "Fundamentals of computation",
    "MAC": "Media Access Control address",
    "MACHINE": "Mechanical or electrical device",
    "MAGNETIC": "Data storage using magnetism",
    "MAINFRAME": "Powerful large computer",
    "MATRIX": "2D array structure",
    "MEMCACHE": "Memory caching system",
    "MERGE": "Combine data or branches",
    "METADATA": "Data about data",
    "METHOD": "Function inside a class",
    "MICROCHIP": "Integrated circuit",
    "MICROPROCESSOR": "Central processing unit",
    "MINING": "Extracting cryptocurrency or data",
    "MOBILE": "Portable computing device",
    "MODULATION": "Varying a wave to encode data",
    "MONITORING": "Observing system performance",
    "MOTHERBOARD": "Main circuit board",
    "MULTITHREADING": "Executing multiple threads",
    "NANOSECOND": "One billionth of a second",
    "NATURAL": "Derived from real-world data",
    "NAVIGATION": "Moving between pages",
    "NEURALNET": "Brain-inspired model",
    "NODE": "Basic unit in data structure or network",
    "NORMALIZATION": "Data scaling method",
    "OBJECTIVE": "Goal in ML or AI",
    "OCR": "Optical character recognition",
    "OFFLINE": "Not connected to the internet",
    "ONLINE": "Connected to the internet",
    "OPENCV": "Computer vision library",
    "OPERATING": "System software controlling hardware",
    "OPTICAL": "Relating to light",
    "OUTPUT": "Produced result",
    "OVERFLOW": "Exceeding storage limits",
    "PACKAGE": "Bundled code module"
}


score_file = "hangman_scores.txt"

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f8ff")

        # Canvas for drawing hangman
        self.canvas = tk.Canvas(root, width=200, height=250, bg="white", highlightthickness=2)
        self.canvas.pack(pady=10)

        # Load score
        self.score = self.load_score()

        # Score label
        self.label_score = tk.Label(root, text=f"Score: Wins - {self.score['wins']}, Losses - {self.score['losses']}", 
                                    font=("Helvetica", 12), bg="#f0f8ff")
        self.label_score.pack()

        # Title
        self.label_title = tk.Label(root, text="🎯 Hangman Game 🎯", font=("Helvetica", 20, "bold"), bg="#f0f8ff")
        self.label_title.pack(pady=10)

        # Word display
        self.word_display = tk.Label(root, font=("Helvetica", 24), bg="#f0f8ff")
        self.word_display.pack(pady=10)

        # Hint display
        self.label_hint = tk.Label(root, text="", font=("Helvetica", 12, "italic"), fg="gray", bg="#f0f8ff")
        self.label_hint.pack(pady=5)

        # Used letters
        self.label_used = tk.Label(root, text="Used Letters: ", font=("Helvetica", 12), bg="#f0f8ff")
        self.label_used.pack()

        # Entry box
        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.pack()

        # Buttons
        self.guess_btn = tk.Button(root, text="Guess", command=self.guess_letter, bg="#d1e7dd", font=("Helvetica", 12))
        self.guess_btn.pack(pady=5)

        self.reset_btn = tk.Button(root, text="New Game", command=self.reset_game, bg="#e2e3e5", font=("Helvetica", 12))
        self.reset_btn.pack(pady=5)

        self.reset_game()

    def load_score(self):
        if not os.path.exists(score_file):
            return {"wins": 0, "losses": 0}
        with open(score_file, "r") as f:
            data = f.read().split(',')
            return {"wins": int(data[0]), "losses": int(data[1])}

    def save_score(self):
        with open(score_file, "w") as f:
            f.write(f"{self.score['wins']},{self.score['losses']}")

    def draw_hangman(self):
        self.canvas.delete("all")
        # Scaffold (always visible)
        self.canvas.create_line(20, 230, 180, 230, width=2)  # base
        self.canvas.create_line(50, 230, 50, 20, width=2)    # pole
        self.canvas.create_line(50, 20, 130, 20, width=2)    # top
        self.canvas.create_line(130, 20, 130, 50, width=2)   # rope

        if self.lives >= 1:
            self.canvas.create_oval(110, 50, 150, 90, width=2)  # head
        if self.lives >= 2:
            self.canvas.create_line(130, 90, 130, 150, width=2)  # body
        if self.lives >= 3:
            self.canvas.create_line(130, 100, 110, 130, width=2)  # left arm
            self.canvas.create_line(130, 100, 150, 130, width=2)  # right arm
        if self.lives >= 4:
            self.canvas.create_line(130, 150, 110, 190, width=2)  # left leg
        if self.lives >= 5:
            self.canvas.create_line(130, 150, 150, 190, width=2)  # right leg

    def get_display_word(self):
        return ' '.join([letter if letter in self.used_letters else '_' for letter in self.word])

    def guess_letter(self):
        entry = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if len(entry) != 1 or entry not in string.ascii_uppercase:
            messagebox.showwarning("Invalid Input", "Please enter a single valid letter.")
            return

        if entry in self.used_letters:
            messagebox.showinfo("Duplicate", f"You already guessed '{entry}'.")
            return

        self.used_letters.append(entry)

        if entry in self.word:
            self.word_letters.discard(entry)
        else:
            self.lives -= 1

        self.word_display.config(text=self.get_display_word())
        self.label_used.config(text=f"Used Letters: {' '.join(self.used_letters)}")
        self.draw_hangman()

        if self.lives == 3:
            self.label_hint.config(text=f"Hint: {word_dict[self.word]}")
        if len(self.word_letters) == 0:
            self.score["wins"] += 1
            self.save_score()
            messagebox.showinfo("Victory", f"You won! The word was '{self.word}'")
            self.reset_game()
        elif self.lives == 0:
            self.score["losses"] += 1
            self.save_score()
            messagebox.showinfo("Game Over", f"You lost! The word was '{self.word}'")
            self.reset_game()

    def reset_game(self):
        self.word = random.choice(list(word_dict.keys()))
        self.word_letters = set(self.word)
        self.used_letters = []
        self.lives = 6
        self.label_hint.config(text="")
        self.word_display.config(text=self.get_display_word())
        self.label_used.config(text="Used Letters: ")
        self.label_score.config(text=f"Score: Wins - {self.score['wins']}, Losses - {self.score['losses']}")
        self.draw_hangman()

# Start the game
root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
