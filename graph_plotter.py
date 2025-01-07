import matplotlib.pyplot as plt
import numpy as np

def graph_plotter():
    def display_menu():
        print("\n=== Graph Plotter ===")
        print("1. Line Plot")
        print("2. Bar Plot")
        print("3. Scatter Plot")
        print("4. Exit")

    def line_plot():
        x = list(map(float, input("Enter x values (comma-separated): ").split(",")))
        y = list(map(float, input("Enter y values (comma-separated): ").split(",")))
        plt.plot(x, y, marker="o")
        plt.title("Line Plot")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid()
        plt.show()

    def bar_plot():
        x = list(map(str, input("Enter categories (comma-separated): ").split(",")))
        y = list(map(float, input("Enter values (comma-separated): ").split(",")))
        plt.bar(x, y, color="skyblue")
        plt.title("Bar Plot")
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.grid(axis="y")
        plt.show()

    def scatter_plot():
        x = list(map(float, input("Enter x values (comma-separated): ").split(",")))
        y = list(map(float, input("Enter y values (comma-separated): ").split(",")))
        plt.scatter(x, y, color="red")
        plt.title("Scatter Plot")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid()
        plt.show()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            line_plot()
        elif choice == '2':
            bar_plot()
        elif choice == '3':
            scatter_plot()
        elif choice == '4':
            print("Exiting Graph Plotter.")
            break
        else:
            print("Invalid choice. Please try again!")