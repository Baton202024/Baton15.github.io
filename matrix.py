import os
import time
import random
import threading

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def matrix_snake_animation_column(column, rows):
    position = random.randint(0, rows - 1)

    while True:
        length = random.randint(5, 15)

        for i in range(length):
            row = (position + i) % rows
            symbol = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()-_=+[{]};:'\",<.>/?`~")

            matrix_char = f"\033[32m{symbol}\033[0m"  # ANSI color code for green
            print(f"\033[{row};{column}H{matrix_char}", end='', flush=True)
            time.sleep(0.05)

        time.sleep(0.2)

        # Clear the column after the snake passes through
        for i in range(length):
            row = (position + i) % rows
            print(f"\033[{row};{column}H ", end='', flush=True)

        position = (position + 1) % rows

def matrix_snake_animation():
    clear_screen()  # Clear the console before starting the animation

    rows = os.get_terminal_size().lines
    columns = os.get_terminal_size().columns

    # Create a thread for each column
    threads = [threading.Thread(target=matrix_snake_animation_column, args=(column, rows)) for column in range(columns)]

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    try:
        matrix_snake_animation()
    except KeyboardInterrupt:
        print("\033[0m")  # Reset color to default on keyboard interrupt
