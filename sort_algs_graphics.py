"""Sorting Algorithms Visualizer Personal Project"""
from button import *
from heap import *
import pygame
import sys
import random

pygame.font.init()

screen_width = 1024
screen_height = 500

# Initialize font.
font = pygame.font.SysFont("comicsansms", 20)

# Initialize screen.
screen = pygame.display.set_mode((screen_width, screen_height + 180))

# Initialize clock.
clock = pygame.time.Clock()

# Title.
pygame.display.set_caption("Sorting Algorithms Visualizer")

# Boolean variable to run the program in the while loop.
run = True

# Boolean variable to determine if visualization has stopped.
stop_visual = False

# Min and max length of array.
min_arr_length = 2
max_arr_length = 550

# Initial array length
arr_length = min_arr_length

# Min and max execution speed (measured in milliseconds).
# The lower the number, the faster the speed.
# The higher the number, the lower the speed.
max_speed = 1
min_speed = 250

# Initial speed of execution.
speed = min_speed

# Initialize array.
arr = [0] * arr_length

arr_distance = (screen_width / arr_length)
arr_width = arr_distance - 1

# Colors.
orange = (255, 102, 0)
blue = (46, 24, 255)
red = (224, 0, 0)
green = (0, 255, 68)
white = (255, 255, 255)
black = (0, 0, 0)

arr_clr = [orange] * arr_length
clrs = [orange, blue, red, green]

# Button controls.
increase_length_button = button(green, 30, 4, 30, 30, ' + ')
decrease_length_button = button(green, 30, 68, 30, 30, ' - ')

generate_new_arr_button = button(green, 179, 4, 175, 25, 'Generate New Array')
stop_visualization_button = button(green, 179, 68, 175, 25, 'Stop Visualization')

mergesort_button = button(green, 500, 4, 105, 25, 'Mergesort')
quicksort_button = button(green, 500, 37, 105, 25, 'Quicksort')
heapsort_button = button(green, 500, 70, 105, 25, 'Heapsort')

selection_sort_button = button(green, 680, 4, 119, 25, 'Selection Sort')
bubblesort_button = button(green, 680, 37, 119, 25, 'Bubblesort')
insertion_sort_button = button(green, 680, 70, 119, 25, 'Insertion Sort')

odd_even_sort_button = button(green, 860, 4, 122, 25, 'Odd-Even Sort')
cocktail_sort_button = button(green, 860, 37, 122, 25, 'Cocktail Sort')
comb_sort_button = button(green, 860, 70, 122, 25, 'Comb Sort')

# Stores each button in a list.
buttons = [increase_length_button, decrease_length_button, generate_new_arr_button,
           stop_visualization_button, mergesort_button, quicksort_button, heapsort_button,
           selection_sort_button, bubblesort_button, insertion_sort_button, odd_even_sort_button,
           cocktail_sort_button, comb_sort_button]


# Generate new Array.
def generate_arr(n):
    """ Generates an array of length n."""
    for i in range(n):
        arr_clr[i] = clrs[0]
        arr[i] = random.randrange(1, max_arr_length)
    all_same = all(elem == arr[0] for elem in arr)
    if not all_same:
        while arr == sorted(arr):
            random.shuffle(arr)


generate_arr(arr_length)


def refill():
    screen.fill(white)
    draw()
    pygame.display.update()
    pygame.time.delay(speed)


# Implementation of Mergesort Algorithm
# ---------------------------------------------------------------------------------------
def merge(arr, left, middle, right):
    """
    Divides an array into two parts,
    and merges them together.
    """
    i = left
    j = middle + 1
    temp = []
    pygame.event.pump()

    while i <= middle and j <= right:
        if stop_visual:            # Stops the visual.
            return None
        arr_clr[i] = clrs[1]
        arr_clr[j] = clrs[1]
        refill()
        arr_clr[i] = clrs[0]
        arr_clr[j] = clrs[0]
        if arr[i] < arr[j]:         # Determines if left element is less than right element.
            temp.append(arr[i])     # Adds the left element to the 'temp' array.
            i += 1                  # Increments i.
        else:
            temp.append(arr[j])     # Otherwise, if right element is less than left element,
            j += 1                  # add right element to the 'temp' array and increment j.

    while i <= middle:              # Adds any remaining elements from the left part of
        arr_clr[i] = clrs[1]        # 'arr' to the 'temp' array.
        refill()
        arr_clr[i] = clrs[0]
        temp.append(arr[i])
        i += 1

    while j <= right:               # Adds any remaining elements from the right part of
        arr_clr[j] = clrs[1]        # 'arr' to the 'temp' array.
        refill()
        arr_clr[j] = clrs[0]
        temp.append(arr[j])
        j += 1

    j = 0
    for i in range(left, right + 1):    # Adds the elements from the temp array back into arr.
        pygame.event.pump()
        arr[i] = temp[j]
        j += 1
        arr_clr[i] = clrs[2]
        refill()
        if right - left == len(arr) - 2:
            arr_clr[i] = clrs[0]
        else:
            arr_clr[i] = clrs[3]


def mergesort(arr, left, right):
    """Uses the mergesort algorithm to sort an array of integers."""
    middle = (left + right) // 2
    if left < right:
        mergesort(arr, left, middle)
        mergesort(arr, middle + 1, right)
        merge(arr, left, middle, right)

# ---------------------------------------------------------------------------------------


# Implementation of Quicksort Algorithm
# ---------------------------------------------------------------------------------------
def partition(arr, low, high):
    """Partitions an array of integers by using a pivot."""
    pygame.event.pump()
    pivot = arr[high]
    arr_clr[high] = clrs[1]
    i = low - 1
    for j in range(low, high):
        if stop_visual:
            return None
        arr_clr[j] = clrs[2]        # change color to red.
        refill()
        arr_clr[high] = clrs[1]     # change color to blue.
        arr_clr[j] = clrs[0]        # Change color of current element to orange.
        arr_clr[i] = clrs[0]        # Change color of smaller element to orange.

        # Determines whether or not current element is smaller than the pivot.
        if arr[j] < pivot:
            i = i + 1
            arr_clr[i] = clrs[2]
            arr[i], arr[j] = arr[j], arr[i]

    refill()
    arr_clr[i] = clrs[0]
    arr_clr[high] = clrs[0]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Returns the partitioning index.
    return(i + 1)


def quicksort(arr, left, right):
    """Uses the quicksort algorithm to sort an array of integers."""
    if left < right:
        pi = partition(arr, left, right)    # Gets the partitioning index of the array
        if pi is None:
            return None
        quicksort(arr, left, pi - 1)        # Recursively sort elements before partition
        refill()
        for i in range(0, pi + 1):          # Changes the colors of each element to green.
            arr_clr[i] = clrs[3]
        if (pi + 1 == (len(arr) - 1)) and all(clr == clrs[3] for clr in arr_clr[:len(arr_clr) - 1]):
            arr_clr[-1] = clrs[3]
        quicksort(arr, pi + 1, right)       # Recursively sort elements after partition.

# ---------------------------------------------------------------------------------------


# Implementation of heapsort algorithm
# ---------------------------------------------------------------------------------------
def max_heapify(arr, heap_size, cur_index):
    """Modifies the heap to satisfy max-heap properties."""
    l = left_child(cur_index)             # Gets position of left child of current node.
    r = right_child(cur_index)            # Gets position of right child of current node.
    largest = cur_index

    if stop_visual:
        return None

    # Determines if left child of a current node exists
    # and is greater than the current node.
    if l < heap_size and arr[l] > arr[largest]:
        largest = l

    # Determines if right child of a current node exists
    # and is greater than the current node.
    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    # Changes the current node, if needed.
    if largest != cur_index:
        arr_clr[largest] = clrs[1]
        arr_clr[cur_index] = clrs[1]
        arr[largest], arr[cur_index] = arr[cur_index], arr[largest]
        refill()
        arr_clr[largest] = clrs[0]
        arr_clr[cur_index] = clrs[0]
        max_heapify(arr, heap_size, largest)


def build_max_heap(arr):
    """Builds a max-heap representation of the array."""
    heap_size = arr_length
    for i in range(parent(heap_size), -1, -1):
        pygame.event.pump()
        max_heapify(arr, heap_size, i)


def heapsort(arr):
    """Uses the heapsort algorithm to sort an array of integers."""
    build_max_heap(arr)
    heap_size = arr_length
    for i in range(heap_size - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        arr_clr[i] = clrs[3]
        if stop_visual:
            return None
        refill()
        max_heapify(arr, i, 0)

# ---------------------------------------------------------------------------------------


# Implementation of selection sort algorithm
# ---------------------------------------------------------------------------------------
def selection_sort(arr):
    """
    Uses the selection sort algorithm
    to sort an array of integers.
    """
    pygame.event.pump()
    # iterate through all elements of the array.
    for i in range(arr_length - 1):
        min_index = i
        for j in range(i + 1, arr_length):
            if stop_visual:
                return None
            if arr[j] < arr[min_index]:
                min_index = j

        arr_clr[min_index] = clrs[1]
        refill()
        arr_clr[min_index] = clrs[0]

        # Swaps the found minimum element with
        # the element in its current iteration
        # of index i.
        arr[i], arr[min_index] = arr[min_index], arr[i]

        arr_clr[i] = clrs[1]            # change color of current index element to blue.
        refill()
        arr_clr[i] = clrs[0]            # change color of current index element to orange.
        arr_clr[min_index] = clrs[3]    # change color of found minimum element to green.

        arr_clr[min_index] = clrs[0]    # change color of found minimum element to orange.
        arr_clr[i] = clrs[1]            # change color of found minimum element to blue.
        refill()
        arr_clr[i] = clrs[3]            # change color of current index element to green.
    all_same = all(color == clrs[3] for color in arr_clr[:-1])
    if all_same:
        arr_clr[-1] = clrs[3]           # change color of last element to green.

# ---------------------------------------------------------------------------------------


# Implementation of bubblesort algorithm
# ---------------------------------------------------------------------------------------
def bubblesort(arr):
    """
    Uses the bubblesort algorithm
    to sort an array of integers.
    """
    pygame.event.pump()
    # Iterate through all elements in the array.
    for i in range(arr_length):
        for j in range(arr_length - i - 1):
            if stop_visual:
                return None
            # Determines if current element
            # is greater than its next element.
            if arr[j] > arr[j + 1]:
                # Swaps the current element with
                # the element next to it.
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

            arr_clr[j] = clrs[2]        # changes color of current element to red.
            arr_clr[j] = clrs[3]        # changes color of current element to green.
            refill()
            arr_clr[j + 1] = clrs[0]    # changes color of next element orange.

            arr_clr[j + 1] = clrs[2]    # changes color of next element to red.
            refill()
            arr_clr[j + 1] = clrs[3]    # changes color of next element to green.
            arr_clr[j] = clrs[0]        # changes color of next element to orange.

    arr_clr[0] = clrs[3]                # changes color of first element to green.

# ---------------------------------------------------------------------------------------


# Implementation of Insertion Sort algorithm
# ---------------------------------------------------------------------------------------
def insertion_sort(arr):
    """
    Uses the insertion sort algorithm to sort an
    array of integers.
    """
    for i in range(1, arr_length):
        if stop_visual:
            return None
        pygame.event.pump()
        refill()

        # Selects the first unsorted element in the array.
        key = arr[i]
        arr_clr[i] = clrs[1]        # set color of element to blue.
        j = i - 1

        # Shifts all the elements to the right to
        # create the position for the unsorted element.
        while j >= 0 and arr[j] > key:
            arr_clr[j] = clrs[1]    # set color of element to blue.
            arr[j+1] = arr[j]
            refill()
            arr_clr[j] = clrs[3]    # set color of element to green.
            j = j - 1

        # Inserts the unsorted element to the correct position.
        arr[j + 1] = key

    for i in range(arr_length):
        arr_clr[i] = clrs[3]

# ---------------------------------------------------------------------------------------


# Implementation of odd-even sort algorithm
# ---------------------------------------------------------------------------------------
def odd_even_sort(arr):
    """
    Uses the odd-even sort algorithm
    to sort an array of integers.
    """
    # Initializes the boolean 'isSorted' to False.
    isSorted = False

    while isSorted is False:
        isSorted = True
        pygame.event.pump()

        # Goes through the odd indexed elements of
        # the array and checks if swapping is needed
        # between two elements.
        for i in range(1, arr_length - 1, 2):
            if stop_visual:
                return None
            arr_clr[i] = clrs[2]            # changes color of current element to red.
            arr_clr[i+1] = clrs[2]          # changes color of next element to red.
            refill()
            if arr[i] > arr[i + 1]:         # determines if current element is greater than the next element.
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + 1] = clrs[0]    # changes color of next element to orange.
                isSorted = False
            else:                           # determines if current element is less than or equal to the next element.
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + 1] = clrs[0]    # changes color of next element to orange.

        # Goes through the even indexed elements of
        # the array and checks if swapping is needed
        # between two elements.
        for i in range(0, arr_length - 1, 2):
            if stop_visual:
                return None
            arr_clr[i] = clrs[2]            # changes color of current element to red.
            arr_clr[i + 1] = clrs[2]        # changes color of next element to red.
            refill()
            if arr[i] > arr[i + 1]:         # determines if current element is greater than the next element.
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + 1] = clrs[0]    # changes color of next element to orange.
                isSorted = False
            else:                           # determines if current element is less than or equal to the next element.
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + 1] = clrs[0]    # changes color of next element to orange.

        if isSorted:                        # determines if the array is already sorted.
            for i in range(arr_length):     # if the array is sorted, change each element's color to green.
                arr_clr[i] = clrs[3]
                refill()

# ---------------------------------------------------------------------------------------


# Implementation of Cocktail Sort Algorithm
# ---------------------------------------------------------------------------------------
def cocktail_sort(arr):
    """
    Uses the cocktail sort algorithm
    to sort an array of integers.
    """
    # Initializes the boolean 'swapped' to True.
    swapped = True

    # Gets the start and end indices of the array.
    start_index = 0
    end_index = arr_length - 1

    while swapped is True:
        # Resets the swapped boolean when entering the loop
        # since swapped might be true from a previous iteration.
        swapped = False
        pygame.event.pump()

        # Loops the array from left to right, and checks
        # if swapping is needed between two elements.
        for i in range(start_index, end_index):
            if stop_visual:
                return None
            arr_clr[i] = clrs[2]            # changes color of current element to red.
            arr_clr[i + 1] = clrs[2]        # changes color of next element to red.
            refill()
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + 1] = clrs[0]    # changes color of next element to orange.
                swapped = True
            else:                           # determines if current element is less than or equal to the next element.
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + 1] = clrs[0]    # changes color of next element to orange.

        # If no elements were swapped, then array is already
        # sorted.
        if swapped is False:
            break

        # Otherwise, reset the 'swapped' boolean to False.
        swapped = False

        # Moves the end index back by one, since
        # the item at the end of the array is
        # already in its correct position.
        end_index = end_index - 1

        # Loops the array from right to left, and checks
        # if swapping is needed between two elements.
        for i in range(end_index - 1, start_index - 1, -1):
            if stop_visual:
                return None
            arr_clr[i] = clrs[2]            # changes color of current element to red.
            arr_clr[i + 1] = clrs[2]        # changes color of next element to red.
            refill()
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + 1] = clrs[0]    # changes color of next element to orange.
                swapped = True
            else:                           # determines if current element is less than or equal to the next element.
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + 1] = clrs[0]    # changes color of next element to orange.

        # Increases the starting index by 1, since
        # the item at the beginning of the array is
        # already in its correct position.
        start_index = start_index + 1

    # changes each element's color to green after the array has been sorted.
    for i in range(arr_length):
        arr_clr[i] = clrs[3]
        refill()

# ---------------------------------------------------------------------------------------


# Implementation of Comb Sort algorithm
# ---------------------------------------------------------------------------------------
def getNextGap(gap):
    """
    Gets the next gap of
    the current iteration.
    """
    gap = int((gap * 10) / 13)
    if gap < 1:
        return 1
    return gap


def comb_sort(arr):
    """
    Uses the comb sort algorithm
    to sort an array of integers.
    """
    # Initializes the gap to the length
    # of the array.
    gap = arr_length

    # Initializes the boolean 'swapped' to True.
    swapped = True

    while gap != 1 or swapped is True:
        # Gets the next gap value.
        gap = getNextGap(gap)

        # Initializes the 'swapped' boolean as False
        # within the while loop to check if a swap
        # has happened or not.
        swapped = False
        pygame.event.pump()

        # Compares the elements within its current gap,
        # and determines if swapping is needed between
        # two elements of its current gap.
        for i in range(0, arr_length - gap):
            if stop_visual:
                return None
            arr_clr[i] = clrs[2]            # changes color of current element to red.
            arr_clr[i + gap] = clrs[2]      # changes color of element within the current gap to red.
            refill()
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + gap] = clrs[0]  # changes color of element within the current gap to orange.
                swapped = True
            else:                           # determines if current element is less than or equal to other element.
                arr_clr[i] = clrs[0]        # changes color of current element to orange.
                arr_clr[i + gap] = clrs[0]  # changes color of element within the current gap to orange.

    # changes each element's color to green after the array has been sorted.
    for i in range(arr_length):
        arr_clr[i] = clrs[3]
        refill()

# ---------------------------------------------------------------------------------------


def determine_speed(n):
    """Determines the speed of execution based on size 'n' of the array"""
    global speed
    if min_arr_length <= n <= 10:
        speed = min_speed
    elif 11 <= n <= 19:
        speed = 190
    elif 20 <= n <= 49:
        speed = 90
    elif 50 <= n <= 73:
        speed = 65
    elif 74 <= n <= 99:
        speed = 50
    elif 100 <= n <= 299:
        speed = 20
    elif 300 <= n <= 499:
        speed = 10
    else:
        speed = max_speed


def draw():
    global arr_length
    global stop_visual
    global arr
    global arr_clr
    global clrs
    global arr_width
    global arr_distance

    pygame.draw.line(screen, black, (120, 0), (120, 105), 6)
    pygame.draw.line(screen, black, (410, 0), (410, 105), 6)
    pygame.draw.line(screen, black, (0, 105), (screen_width, 105), 6)
    text = font.render(f"Length: {arr_length}", True, black)
    screen.blit(text, (5, 33))

    # draws the buttons on the screen
    for i in range(len(buttons)):
        buttons[i].draw(screen, black)

    # Draws array values as bars on the screen.
    for i in range(len(arr)):
        pygame.draw.rect(screen, arr_clr[i], pygame.Rect((i * arr_distance, 109), (arr_width, arr[i])))

    # Event handler
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Determines if 'Increase Length' Button was pressed.
            if (buttons[0].isOver(mouse_pos)) and (arr_length < max_arr_length):
                stop_visual = False
                arr_length += 1
                arr_distance = screen_width / arr_length
                arr_width = arr_distance - 1
                arr = [0] * arr_length
                arr_clr = [orange] * arr_length
                generate_arr(arr_length)
                determine_speed(arr_length)

            # Determines if 'Decrease Length' Button was pressed.
            if (buttons[1].isOver(mouse_pos)) and (arr_length > min_arr_length):
                stop_visual = False
                arr_length -= 1
                arr_distance = screen_width / arr_length
                arr_width = arr_distance - 1
                arr = [0] * arr_length
                arr_clr = [orange] * arr_length
                generate_arr(arr_length)
                determine_speed(arr_length)

            # Determines if 'Generate New Array' Button was pressed.
            if buttons[2].isOver(mouse_pos):
                stop_visual = False
                arr_distance = screen_width / arr_length
                arr_width = arr_distance - 1
                arr = [0] * arr_length
                arr_clr = [orange] * arr_length
                generate_arr(arr_length)

            # Determines if 'Stop Visualization' Button was pressed.
            if buttons[3].isOver(mouse_pos):
                stop_visual = True

            # Determines if 'Mergesort' Button was pressed.
            if buttons[4].isOver(mouse_pos):
                stop_visual = False
                mergesort(arr, 0, arr_length - 1)

            # Determines if 'Quicksort' Button was pressed.
            if buttons[5].isOver(mouse_pos):
                stop_visual = False
                quicksort(arr, 0, arr_length - 1)

            # Determines if 'Heapsort' Button was pressed.
            if buttons[6].isOver(mouse_pos):
                stop_visual = False
                heapsort(arr)

            # Determines if 'Selection Sort' Button was pressed.
            if buttons[7].isOver(mouse_pos):
                stop_visual = False
                selection_sort(arr)

            # Determines if 'Bubblesort' Button was pressed.
            if buttons[8].isOver(mouse_pos):
                stop_visual = False
                bubblesort(arr)

            # Determines if 'Insertion Sort' Button was pressed.
            if buttons[9].isOver(mouse_pos):
                stop_visual = False
                insertion_sort(arr)

            # Determines if 'Odd-Even Sort' Button was pressed.
            if buttons[10].isOver(mouse_pos):
                stop_visual = False
                odd_even_sort(arr)

            # Determines if 'Cocktail Sort' Button was pressed.
            if buttons[11].isOver(mouse_pos):
                stop_visual = False
                cocktail_sort(arr)

            # Determines if 'Comb Sort' Button was pressed.
            if buttons[12].isOver(mouse_pos):
                stop_visual = False
                comb_sort(arr)

        # Changes Button color to Red if mouse is over the button.
        if event.type == pygame.MOUSEMOTION:
            for i in range(len(buttons)):
                if buttons[i].isOver(mouse_pos):
                    buttons[i].color = red
                else:
                    buttons[i].color = green


while run:
    screen.fill(white)
    draw()
    pygame.display.flip()
    clock.tick(25)
