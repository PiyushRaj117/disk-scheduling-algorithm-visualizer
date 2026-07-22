import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Disk scheduling algorithms
def fcfs(requests, head):
    total = 0
    sequence = []
    for req in requests:
        total += abs(head - req)
        sequence.append(req)
        head = req
    return sequence, total

def sstf(requests, head):
    requests = requests[:]
    total = 0
    sequence = []
    while requests:
        distances = {req: abs(req - head) for req in requests}
        closest = min(distances, key=distances.get)
        total += abs(head - closest)
        sequence.append(closest)
        head = closest
        requests.remove(closest)
    return sequence, total

def scan(requests, head, direction, disk_size=200):
    requests = sorted(requests)
    total = 0
    sequence = []
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    
    if direction == "Left":
        for r in reversed(left):
            total += abs(head - r)
            sequence.append(r)
            head = r
        if left:
            total += head  # move to 0
            head = 0
        for r in right:
            total += abs(head - r)
            sequence.append(r)
            head = r
    else:
        for r in right:
            total += abs(head - r)
            sequence.append(r)
            head = r
        if right:
            total += disk_size - 1 - head
            head = disk_size - 1
        for r in reversed(left):
            total += abs(head - r)
            sequence.append(r)
            head = r
    return sequence, total

# Main GUI App
class DiskSchedulingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disk Scheduling Simulator")
        self.root.geometry("600x500")

        # ---- Tricolor Background using Frames ----
        self.top_frame = tk.Frame(root, bg="#ff9933", height=100, width=600)
        self.middle_frame = tk.Frame(root, bg="#ffffff", height=300, width=600)
        self.bottom_frame = tk.Frame(root, bg="#138808", height=100, width=600)

        self.top_frame.pack(fill=tk.X)
        self.middle_frame.pack(fill=tk.X)
        self.bottom_frame.pack(fill=tk.X)

        # ---- Style for Combobox ----
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox",
                        fieldbackground="white",
                        background="white",
                        foreground="black",
                        font=("Arial", 10))

        # ---- Dynamic Color Label ----
        self.credit_label_left = tk.Label(self.top_frame, text="L P U", 
                                  bg="#ff9933", fg="#00ff00", font=("Arial", 15, "italic"))
        self.credit_label_left.pack(anchor='nw', padx=10, pady=5)
        self.credit_label_left.place(relx=0.0, x=10, y=5, anchor='nw')

        
        self.credit_label = tk.Label(self.top_frame, text="By Piyush, Ankit, Priyesh", 
                                     bg="#ff9933", fg="#00ff00", font=("Arial", 13, "italic"))
        self.credit_label.pack(anchor='ne', padx=10, pady=5)
        self.credit_label.place(relx=1.0, x=-10, y=5, anchor='ne')

        # List of 7 colors in RGB format
        self.colors = [
            "#FFFFFF",  # White
            "#000000",  # Black
            "#33FF57",  # Bright Green
            "#3357FF",  # Bright Blue
            "#4B0082",  # Indigo (Dark Purple)
            "#2F4F4F",  # Dark Slate Gray
            "#A52A2A"   # Brown
        ]
        self.color_index = 0

        # Start changing color of the label
        self.change_color()

        # ---- Widgets on the white (middle) frame ----
        tk.Label(self.middle_frame, text="Enter Requests (space-separated):", 
                 bg="#ffffff", fg="#000000", font=("Arial", 18, "bold")).pack()
        self.req_entry = tk.Entry(self.middle_frame, width=50, bg="white", fg="black", font=("Consolas", 13))
        self.req_entry.pack()

        tk.Label(self.middle_frame, text="Initial Head Position:", 
                 bg="#ffffff", fg="#000000", font=("Arial", 18, "bold")).pack()
        self.head_entry = tk.Entry(self.middle_frame, bg="white", fg="black", font=("Consolas", 13))
        self.head_entry.pack()

        tk.Label(self.middle_frame, text="Algorithm:", 
                 bg="#ffffff", fg="#000000", font=("Arial", 18, "bold")).pack()
        self.algo_choice = ttk.Combobox(self.middle_frame, values=["FCFS", "SSTF", "SCAN"])
        self.algo_choice.pack()

        self.direction_var = tk.StringVar()
        self.direction_frame = tk.Frame(self.middle_frame, bg="#ffffff")
        tk.Label(self.direction_frame, text="Direction:", 
                 bg="#ffffff", fg="black", font=("Arial", 11)).pack(side=tk.LEFT)
        ttk.Combobox(self.direction_frame, textvariable=self.direction_var, values=["Left", "Right"]).pack(side=tk.LEFT)
        self.direction_frame.pack()
        self.direction_frame.pack_forget()  

        self.algo_choice.bind("<<ComboboxSelected>>", self.show_direction_if_needed)

        tk.Button(self.middle_frame, text="Run", command=self.run_simulation, 
                  bg="#0066cc", fg="white", font=("Arial", 11, "bold")).pack(pady=10)

        self.result_label = tk.Label(self.middle_frame, text="", font=("Helvetica", 12), bg="#ffffff", fg="#000")
        self.result_label.pack()

        self.canvas = None

    def show_direction_if_needed(self, event=None):
        algo = self.algo_choice.get()
        if algo == "SCAN":
            self.direction_frame.pack()
        else:
            self.direction_frame.pack_forget()

    def run_simulation(self):
        try:
            requests = list(map(int, self.req_entry.get().split()))
            head = int(self.head_entry.get())
            algo = self.algo_choice.get()

            if not algo:
                messagebox.showerror("Error", "Please select an algorithm.")
                return

            direction = self.direction_var.get() if algo == "SCAN" else None

            if algo == "FCFS":
                sequence, total = fcfs(requests, head)
            elif algo == "SSTF":
                sequence, total = sstf(requests, head)
            elif algo == "SCAN":
                if not direction:
                    messagebox.showerror("Error", "Please select a direction.")
                    return
                sequence, total = scan(requests, head, direction)
            else:
                return

            self.result_label.config(text=f"Sequence: {sequence}\nTotal Movement: {total}")
            self.plot_chart([head] + sequence, algo)

        except Exception as e:
            messagebox.showerror("Error", f"Invalid input:\n{e}")

    def plot_chart(self, data, algo):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(range(len(data)), data, marker='o', color="#0066cc")
        ax.set_title(f"{algo} Disk Scheduling", fontsize=12)
        ax.set_xlabel("Step")
        ax.set_ylabel("Track Number")
        ax.grid(True)

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def change_color(self):
        self.credit_label.config(fg=self.colors[self.color_index])
        self.color_index = (self.color_index + 1) % len(self.colors)
        # Call this function again after 1000 ms (1 second)
        self.root.after(1000, self.change_color)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DiskSchedulingApp(root)
    root.mainloop()
