import math
import matplotlib.pyplot as plt


def bonjour():
    print('Hello world')

def bonjour_plot():
    # Create a plot
    fig, ax = plt.subplots()

    # Load a custom handwriting font
    plt.rcParams['font.family'] = 'cursive'
    plt.rcParams['font.cursive'] = 'Comic Sans MS'

    # Set the plot limits
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])

    # Plot the text
    ax.plot([1, 9], [4, 4], linewidth=2, color='blue')
    ax.text(5, 5, "Hello world", ha='center', va='center', fontsize=50)


    # Show the plot
    plt.show()