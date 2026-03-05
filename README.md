# Sorting Algorithm Visualizer

A Python GUI application that visually demonstrates how different sorting algorithms work.  
The program uses **Tkinter** to animate sorting operations step-by-step, highlighting comparisons and swaps in real time.

This tool is useful for learning how common sorting algorithms behave and for visually understanding their performance differences.

---

## Features

- Visualize multiple sorting algorithms
- Adjustable animation speed
- Customizable array size
- Step-by-step visualization of:
  - Comparisons
  - Swaps
- Benchmark timing for each algorithm

---

## Implemented Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort

Each algorithm is implemented in the `algorithms/` folder and designed as a **generator** that yields intermediate steps for visualization.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/NoahBKalma/sorting-algorithm-visualizer
cd sorting-visualizer