import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arr1 = random.sample(range(100), 10)

def bubble_sort_steps(arr):
    steps = []
    print("Arr chưa sort:", arr)
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(arr.copy())
                swapped = True
            if not swapped:
                break
        return steps

def visualize_sort_bubble(arr):
    steps = bubble_sort_steps(arr)
    fig, ax = plt.subplots()
    ax.set_title("Step by step bubble sort")
    bar_rects = ax.bar(range(len(arr)), align="edge", color="blue")
    ax.set_xlim(0,len(arr))
    ax.set_ylim(0,max(arr) + 5)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_bars (frame):
        for rect, val in zip(bar_rects, steps [frame]): # chieu cao cua cot
                rect.set_height(val)
        text.set_text(f"Step {(frame + 1):02}/ {len(steps)}")
        return bar_rects
# tao animation
    ani = animation. FuncAnimation (fig, update_bars, frames=len (steps), interval=1000, repeat=False)
# hien thi do thi
    plt.show()
#test
visualize_sort_bubble(arr1)  
    