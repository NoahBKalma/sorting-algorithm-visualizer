import tkinter as tk
from tkinter import Event, Message, ttk
from random import shuffle
import time

from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge_sort
  

def plot_graph(canvas, curr_list, j, k, step_type):
    '''
    Draws the graph on the canvas and highlights rectangles per step
    '''
    
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

def animate_graph(canvas, algorithm_gen, speed, run_algorithm_button, step_counts):
    '''
    Animates the graph by repeatedly calling the plot_graph function with the current state of the algorithm.
    '''
    
    # Stores ID in case the user wants to quit
    global animation_id

    # Calculate the current speed based on the slider value and convert it to a delay in milliseconds
    curr_speed = 1001 - ((speed.get()))*100

    # Continues until the generator is exhausted
    try:
        curr_list, j, k, step_type = curr_step = next(algorithm_gen)
        plot_graph(canvas, curr_list, j, k, step_type)
        animation_id = canvas.after(curr_speed, animate_graph, canvas, algorithm_gen, speed, run_algorithm_button, step_counts)
        step_counts[0].set(step_counts[0].get() + 1)
        match step_type:
            case "comparison":
                step_counts[1].set(step_counts[1].get() + 1)
            case "swap":
                step_counts[2].set(step_counts[2].get() + 1)
    except StopIteration:
        run_algorithm_button.config(state="active")

def benchmark_algorithm_microseconds(algorithm, arr, repeats=50):
    '''
    Runs the algorithm independently to see time, returns a string with micro- or milli-seconds
    '''

    # Exhaust the generator repeat times
    total=0
    for _ in range(repeats):
        arr_copy = arr.copy()
        start = time.perf_counter()
        for _ in algorithm(arr_copy):
            pass
        end = time.perf_counter()
        total += end-start


    dt = total/repeats
    if dt > .001:
        return f"{round(dt*1000, 1)} milliseconds"
    else:
        return f"{round(dt*1000000, 1)} microseconds"

def main():

    # Create the main window
    root = tk.Tk()
    root.title("Sorting Algorithm Visualizer")
    root.resizable(False, False)

    # Set focus on whatever is pressed
    def set_focus(event):
        try:
            event.widget.focus_set()
        except AttributeError:
            return
    root.bind_all("<Button-1>", set_focus)

    # Set the window size
    root_width = 1000
    root_height = 720
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{root_width}x{root_height}+{int(screen_width/2 - root_width/2)}+{int(screen_height/2 - root_height/2 - 16)}")
    
    # Create and pack the title
    title = ttk.Label(root, text="Sorting Algorithm Visualizer", font=("Arial Rounded MT Bold", 24))
    title.pack(pady=(15,0))
    
    # Create and pack the algorithm selector
    algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort"]
    selected_algorithm = tk.StringVar()

    algorithm_dropdown = ttk.Combobox(root, values=algorithms, textvariable=selected_algorithm, state="readonly")
    algorithm_dropdown.set("Algorithms")
    algorithm_dropdown.config(font=("Arial Rounded MT", 14), width=20, justify="center")
    algorithm_dropdown.pack(pady=10)
    
    # Create frame for current algorithm info
    algorithm_info_frame = tk.Frame(root)
    algorithm_info_frame.pack()

    # Create variable to count steps and their type
    step_counts = [tk.IntVar(),tk.IntVar(),tk.IntVar()] # [total, comparisons, swaps]

    # Create frame for total step count display
    total_steps_frame = tk.Frame(algorithm_info_frame, borderwidth=1, relief="solid")
    total_steps_frame.grid(column=0, row=0)

    # Add label to total step count frame
    ttk.Label(total_steps_frame, text="Total Steps",  font=("Arial Rounded MT", 14)).pack()

    # Add total step count to the frame
    total_steps_display = ttk.Label(total_steps_frame, textvariable=step_counts[0], font=("Arial Rounded MT", 12))
    total_steps_display.pack(padx=10, pady=5)
    total_steps_display.config(padding=(50,5))

    # Create frame for comparison display
    comparison_frame = tk.Frame(algorithm_info_frame, borderwidth=1, relief="solid")
    comparison_frame.grid(column=1, row=0, padx=5)

    # Add label to comparison frame
    ttk.Label(comparison_frame, text="Comparisons",  font=("Arial Rounded MT", 14)).pack()

    # Add comparison count to the frame
    comparison_display = ttk.Label(comparison_frame, textvariable=step_counts[1], font=("Arial Rounded MT", 12))
    comparison_display.pack(padx=10, pady=5)
    comparison_display.config(padding=(50,5))

    # Create frame for swap display
    swap_frame = tk.Frame(algorithm_info_frame, borderwidth=1, relief="solid")
    swap_frame.grid(column=2, row=0, padx=(0,5))

    # Add label to swap frame
    ttk.Label(swap_frame, text="Swaps",  font=("Arial Rounded MT", 14)).pack()

    # Add swap count to the frams
    swap_display = ttk.Label(swap_frame, textvariable=step_counts[2], font=("Arial Rounded MT", 12))
    swap_display.pack(padx=10, pady=5)
    swap_display.config(padding=(50,5))

    # Create frame for time display
    time_frame = tk.Frame(algorithm_info_frame, borderwidth=1, relief="solid")
    time_frame.grid(column=3, row=0)

    # Add label to time frame
    time_complexity = tk.StringVar(value = f"Time Complexity: ")
    ttk.Label(time_frame, textvariable=time_complexity,  font=("Arial Rounded MT", 14)).pack()

    time = tk.StringVar(value="000.0 microseconds")

    # Add time to the frame
    time_display = ttk.Label(time_frame, textvariable=time, font=("Arial Rounded MT", 12))
    time_display.pack(padx=40, pady=10)

    # Create Canvas for the algorithms to be drawn on
    canvas = tk.Canvas(root, width=650, height=400, bg="gray") 
    canvas.config(highlightthickness=0)   
    canvas.pack(pady=(10,0))
    
    # Create frame to house the options for the algorithm
    options_frame = tk.Frame(root)
    options_frame.pack()
    
    # Create frame to house speed slider
    speed_slider_frame = tk.Frame(options_frame)
    speed_slider_frame.grid(row=0,column=4, padx=10, pady=(10,0))

    # Create label for speed slider
    speed_slider_label = tk.Label(speed_slider_frame, text = "Speed Slider", font=("Arial Rounded MT", 13))
    speed_slider_label.pack(pady=(5,0))

    # Create slider for speed change
    speed_slider = tk.Scale(speed_slider_frame, from_=1, to=10, orient=tk.HORIZONTAL, length=200, width=20)
    speed_slider.set(1)
    speed_slider.config(highlightthickness=0)
    speed_slider.pack()
       
    # Add input box for array size
    array_size_label = ttk.Label(options_frame, text="Array Size:", font=("Arial Rounded MT", 13))
    array_size_label.grid(row=0,column=2, padx=(10,0), pady=(10,2))
    
    array_size = tk.Entry(options_frame, width=10, font=("Arial Rounded MT", 13))
    array_size.grid(row=0,column=3, padx=10, pady=(10,0), ipady=4)
    
    # Create button to run algorithm
    run_algorithm_button = tk.Button(options_frame, text="Run Algorithm", font=("Arial Rounded MT", 13), command=lambda: run_algorithm(array_size.get()))
    run_algorithm_button.config(width=15, height=2, justify="center")
    run_algorithm_button.grid(row=0,column=1, padx=10, pady=(10,0))
    
    # Create button to quit current algorithm
    quit_algorithm_button = tk.Button(options_frame, text="Quit Algorithm", font=("Arial Rounded MT", 13), command=lambda: quit_algorithm())
    quit_algorithm_button.config(width=15, height=2, justify="center")
    quit_algorithm_button.grid(row=0,column=0, padx=10, pady=(10,0))

    # Funcion to cancel animation
    def quit_algorithm():
        global animation_id
        try:
            if animation_id is not None:
                canvas.after_cancel(animation_id)
                animation_id = None
                run_algorithm_button.config(state="active")
        except NameError:
            user_message.config(text="Nothing to quit")

    # Function to run the selected algorithm
    def run_algorithm(list_size):
        '''
        Runs the selected algorithm by creating a generator with a randomly shuffled list of the specified size.
        '''

        # Resets step counts for new algorithm
        for count in step_counts:
            count.set(0)

        # Resets the user message
        user_message.config(text="")

        # Creates the shuffled list as long as the input is valid, otherwise displays message and exits
        try:
            list_to_sort = list(range(1, int(list_size)+1))
        except ValueError:
            print("Error in list size")
            user_message.config(text="Invalid Array Size")
            return
        shuffle(list_to_sort)
                
        # Disables run button to prevent multiple graphs animating at once
        run_algorithm_button.config(state="disabled")

        # Chooses which algorithm to run 
        match selected_algorithm.get():
            case "Bubble Sort":
                time.set(benchmark_algorithm_microseconds(bubble_sort, list_to_sort))
                print(f"Running Bubble Sort: {time.get()}")
                bubble_sort_gen = bubble_sort(list_to_sort)
                canvas.after(int(speed_slider.get()), animate_graph, canvas, bubble_sort_gen, speed_slider, run_algorithm_button, step_counts)
            case "Selection Sort":
                time.set(benchmark_algorithm_microseconds(selection_sort, list_to_sort))
                print(f"Running Selection Sort: {time.get()}")
                selection_sort_gen = selection_sort(list_to_sort)
                canvas.after(int(speed_slider.get()), animate_graph, canvas, selection_sort_gen, speed_slider, run_algorithm_button, step_counts)
            case "Insertion Sort":
                time.set(benchmark_algorithm_microseconds(insertion_sort, list_to_sort))
                print(f"Running Insertion Sort: {time.get()}")
                insertion_sort_gen = insertion_sort(list_to_sort)
                canvas.after(int(speed_slider.get()), animate_graph, canvas, insertion_sort_gen, speed_slider, run_algorithm_button, step_counts)
            case "Merge Sort":
                time.set(benchmark_algorithm_microseconds(merge_sort, list_to_sort))
                print(f"Running Merge Sort: {time.get()}")
                merge_sort_gen = merge_sort(list_to_sort)
                canvas.after(int(speed_slider.get()), animate_graph, canvas, merge_sort_gen, speed_slider, run_algorithm_button, step_counts)
            case _:
                # Re-enables run button if nothing selected
                run_algorithm_button.config(state="active")
                # Gives user message to choose algorithm
                user_message.config(text="Choose Algorithm")
    
    # Create title for selected algorithm
    user_message = ttk.Label(root, text="")
    user_message.config(font=("Arial Rounded MT", 12), foreground="red")
    user_message.pack(pady=(10,0))

    # Function to update the selected algorithm title when the user selects an algorithm
    def algorithm_changed(*args):
        print("Changed algorithm to", selected_algorithm.get())
        user_message.config(text="")
        match selected_algorithm.get():
            case "Bubble Sort":
                time_complexity.set("Time Complexity: O(n\u00B2)")
            case "Selection Sort":
                time_complexity.set("Time Complexity: O(n\u00B2)")
            case "Insertion Sort":
                time_complexity.set("Time Complexity: O(n\u00B2)")
            case "Merge Sort":
                time_complexity.set("Time Complexity: O(nlog(n))")
        
    # Runs the algorithm_changed function when the user selects an algorithm
    selected_algorithm.trace_add("write", algorithm_changed)

    # Start the GUI event loop
    root.mainloop()
    
if __name__ == "__main__":
    main()