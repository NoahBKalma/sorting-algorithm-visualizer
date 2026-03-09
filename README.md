# Sorting Algorithm Visualizer

A Python GUI application that visually demonstrates how different sorting algorithms work.  
The program uses Tkinter to animate sorting operations step-by-step, highlighting comparisons and swaps in real time.

This tool is useful for learning how common sorting algorithms behave and for visually understanding their performance differences.


## Features

- Visualize multiple sorting algorithms
- Adjustable animation speed
- Customizable array size
- Step-by-step visualization of:
  - Comparisons
  - Swaps
- Benchmark timing for each algorithm


## Implemented Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort

Each algorithm is implemented in the `algorithms/` folder and designed as a generator that yields intermediate steps for visualization.


## Requirements

- Python 3.10+
- Tkinter (included with most Python installations)


## Installation/Usage

### 1. Clone the repository

```bash
git clone https://github.com/NoahBKalma/sorting-algorithm-visualizer
```

### 2. Run the main application

```bash
python main.py
```

### Steps:
- Select a sorting algorithm
- Enter an array size
- Adjust the speed slider
- Click Run Algorithm

- Keybinds:
  - Escape Key: Quit algorithm
  - Enter Key: Run algorithm
  - Left Arrow Key: Decrease speed
  - Right Arrow Key: Increase speed