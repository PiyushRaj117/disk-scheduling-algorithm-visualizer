# Disk Scheduling Algorithm Visualizer

An interactive **Operating Systems project** developed using **Python**, **Tkinter**, and **Matplotlib** to simulate and visualize classical Disk Scheduling Algorithms.

The application allows users to compare different scheduling algorithms by displaying the disk access sequence, total head movement, and graphical visualization of disk head movement.

---

## Features

- Interactive graphical user interface (GUI)
- Custom disk request input
- Initial head position selection
- Supports multiple disk scheduling algorithms:
  - FCFS (First Come First Serve)
  - SSTF (Shortest Seek Time First)
  - SCAN (Elevator Algorithm)
- Displays:
  - Disk access sequence
  - Total head movement
  - Average seek time
  - System throughput
- Graphical visualization using Matplotlib
- Easy-to-use interface for learning Operating System concepts

---

## Technologies Used

- Python 3.11
- Tkinter
- Matplotlib
- Pillow (PIL)
- Requests

---

## Project Structure

```
disk-scheduling-algorithm-visualizer/
│
├── assets/
│   └── screenshots/
│       ├── home.png
│       ├── fcfs.png
│       └── scan.png
│
├── gui.py
├── requirements.txt
└── README.md
```

---

## Screenshots

### Home Screen

![Home](assets/screenshots/home.png)

### FCFS Algorithm

![FCFS](assets/screenshots/fcfs.png)

### SCAN Algorithm

![SCAN](assets/screenshots/scan.png)

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/disk-scheduling-algorithm-visualizer.git
```

### 2. Navigate to the project folder

```bash
cd disk-scheduling-algorithm-visualizer
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python gui.py
```

---

## Example Input

**Requests**

```
98 183 37 122 14 124 65 67
```

**Initial Head Position**

```
53
```

**Algorithm**

```
SCAN
```

**Direction**

```
Right
```

---

## Output

- Disk access sequence
- Total head movement
- Average seek time
- System throughput
- Graphical visualization of disk head movement

---

## Future Improvements

- LOOK Algorithm
- C-SCAN Algorithm
- C-LOOK Algorithm
- Improved UI Design
- Export simulation results
- Dark mode support

---

## Learning Objectives

This project helps users understand:

- Disk Scheduling Algorithms
- Seek Time Optimization
- Head Movement Analysis
- Operating System Scheduling Techniques
- Algorithm Performance Comparison

---

## Acknowledgements

Developed as an **Operating Systems course project** at **Lovely Professional University (LPU)**.

---

## License

This project is created for educational purposes.
