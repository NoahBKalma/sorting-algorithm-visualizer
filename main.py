import tkinter as tk
from tkinter import ttk
from random import shuffle

from Algorithms.bubble_sort import bubble_sort
from Algorithms.insertion_sort import insertion_sort
from Algorithms.selection_sort import selection_sort
from Algorithms.merge_sort import merge_sort
  

def plot_graph(canvas, curr_list, j, k, step_type):
    
    # Resets the canvas
    canvas.delete("all")
        
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    rect_width = canvas_width / len(curr_list)
    
    for i in range(len(curr_list)):
        
        # Calculate the size and position of rectangle
        rect_height = (curr_list[i] / max(curr_list)) * canvas_height
        x1 = i * rect_width
        x2 = (i+1) * rect_width
        y1 = canvas_height - rect_height
        y2 = canvas_height
        
        # Draws rectangles with colors corresponding to use in current step
        if step_type == "comparison" and (i == j or i == k):
            canvas.create_rectangle(x1, y1, x2, y2, fill="green")
        elif step_type == "swap" and (i == j or i == k):
            canvas.create_rectangle(x1, y1, x2, y2, fill="red")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")

def animate_graph(canvas, algorithm_gen, speed):
    '''
    Animates the graph by repeatedly calling the plot_graph function with the current state of the algorithm.
    '''
    
    # Calculate the current speed based on the slider value and convert it to a delay in milliseconds
    curr_speed = 1001 - ((speed.get())**2)*10

    # Continues until the generator is exhausted
    try:
        curr_list, j, k, step_type = curr_step = next(algorithm_gen)
        plot_graph(canvas, curr_list, j, k, step_type)
        canvas.after(curr_speed, animate_graph, canvas, algorithm_gen, speed)
    except StopIteration:
        pass

def main():

    # Create the main window
    root = tk.Tk()
    root.title("Sorting Algorithm Visualizer")
    
    # Set the window size
    root.geometry("700x600")
    
    # Create and pack the title
    title = ttk.Label(root, text="Sorting Algorithm Visualizer", font=("Ariel Rounded MT Bold", 16))
    title.pack()
    
    # Create and pack the algorithm selector
    algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort"]
    selected_algorithm = tk.StringVar()

    algorithm_dropdown = ttk.Combobox(root, values=algorithms, textvariable=selected_algorithm, state="readonly", width=20)
    algorithm_dropdown.set("Algorithms")
    algorithm_dropdown.pack()
    
    # Create Canvas for the algorithms to be drawn on
    canvas = tk.Canvas(root, width=600, height=400, bg="gray")    
    canvas.pack()
    
    # Create frame to house the options for the algorithm
    options_frame = tk.Frame(root)
    options_frame.pack()
    
    # Create slider for speed change
    speed_slider = tk.Scale(options_frame, from_=1, to=10, orient=tk.HORIZONTAL, label="Animation Speed", length=200)
    speed_slider.set(1)
    speed_slider.grid(row=0,column=4, padx=10, pady=10)
       
    # Add input box for array size
    array_size_label = ttk.Label(options_frame, text="Array Size:", font=("Arial", 11))
    array_size_label.grid(row=0,column=2, padx=(10,0), pady=10)
    
    array_size = tk.Entry(options_frame, width=10, font=("Arial", 11))
    array_size.grid(row=0,column=3, padx=10, pady=10)
    
    # Create button to run algorithm
    run_algorithm_button = tk.Button(options_frame, text="Run Algorithm", font=("Arial", 11), command=lambda: run_algorithm(array_size.get()))
    run_algorithm_button.grid(row=0,column=1, padx=10, pady=10)
    
    # Create button to quit current algorithm
    quit_algorithm_button = tk.Button(options_frame, text="Quit Algorithm", font=("Arial", 11))
    quit_algorithm_button.grid(row=0,column=0, padx=10, pady=10)
    
    # Function to run the selected algorithm
    def run_algorithm(list_size):
        '''
        Runs the selected algorithm by creating a generator with a randomly shuffled list of the specified size.
        '''
        
        # Creates the shuffled list as long as the input is valid, otherwise returns 1
        try:
            list_to_sort = list(range(1, int(list_size)+1))
        except ValueError:
            return 1
        shuffle(list_to_sort)
                
        # Chooses which algorithm to run 
        match selected_algorithm.get():
            case "Bubble Sort":
                print("Running Bubble Sort")
                bubble_sort_gen = bubble_sort(list_to_sort)
                canvas.after(int(speed_slider.get()), animate_graph, canvas, bubble_sort_gen, speed_slider)
            case "Selection Sort":
                print("Running Selection Sort")
                selection_sort_gen = selection_sort(list_to_sort)
                canvas.after(int(speed_slider.get()), animate_graph, canvas, selection_sort_gen, speed_slider)
            case "Insertion Sort":
                print("Running Insertion Sort")
                insertion_sort_gen = insertion_sort(list_to_sort)
                canvas.after(int(speed_slider.get()), animate_graph, canvas, insertion_sort_gen, speed_slider)
            case "Merge Sort":
                print("Running Merge Sort")
                merge_sort_gen = merge_sort(list_to_sort)
                canvas.after(int(speed_slider.get()), animate_graph, canvas, merge_sort_gen, speed_slider)
    
    # Create title for selected algorithm
    selected_algorithm_title = ttk.Label(root, text="Selected Algorithm: " + selected_algorithm.get())
    selected_algorithm_title.config(font=("Ariel Rounded MT Bold", 12))
    selected_algorithm_title.pack()

    # Function to update the selected algorithm title when the user selects an algorithm
    def algorithm_changed(*args):
        print("Changed algorithm to", selected_algorithm.get())
        selected_algorithm_title.config(text="Selected Algorithm: " + selected_algorithm.get())
        
    # Runs the algorithm_changed function when the user selects an algorithm
    selected_algorithm.trace_add("write", algorithm_changed)

    # Start the GUI event loop
    root.mainloop()
    
if __name__ == "__main__":
    main()