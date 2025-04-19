import tkinter as tk
from time import strftime, localtime
import math

root = tk.Tk()
root.title("Analog Clock")
root.geometry("400x400")  # Set window size

def update_clock():
    canvas.delete("all")  

    # clock face
    canvas.create_oval(50, 50, 350, 350, outline="white", width=4)  # Outer circle

    # hour markers 
    for i in range(1, 13):
        angle = math.radians((i / 12) * 360 - 90)  
        x = 200 + 120 * math.cos(angle)
        y = 200 + 120 * math.sin(angle)
        canvas.create_text(x, y, text=str(i), font=("calibri", 16, "bold"), fill="red")

    # Get the current local time
    current_time = localtime()
    hours = current_time.tm_hour % 12  # Convert 24-hour format to 12-hour format
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Display the current date at the center
    current_date = strftime("%d-%m-%Y")  # Format: DD-MM-YYYY
    canvas.create_text(200, 250, text=current_date, font=("calibri", 14, "bold"), fill="white")

    # Calculate the angles for the clock hands
    second_angle = math.radians((seconds / 60) * 360 - 90)
    minute_angle = math.radians((minutes / 60) * 360 - 90)
    hour_angle = math.radians((hours / 12) * 360 + (minutes / 60) * 30 - 90)

    sec_x, sec_y = 200 + 120 * math.cos(second_angle), 200 + 120 * math.sin(second_angle)
    min_x, min_y = 200 + 100 * math.cos(minute_angle), 200 + 100 * math.sin(minute_angle)
    hour_x, hour_y = 200 + 60 * math.cos(hour_angle), 200 + 60 * math.sin(hour_angle)

    canvas.create_line(200, 200, sec_x, sec_y, fill="red", width=1)  # Thin red for second hand
    canvas.create_line(200, 200, min_x, min_y, fill="white", width=3)  # White for minute hand
    canvas.create_line(200, 200, hour_x, hour_y, fill="white", width=5)  # Thicker white for hour hand

    # Draw clock center
    canvas.create_oval(195, 195, 205, 205, fill="white")  # White center circle for realism

    canvas.after(1000, update_clock)

canvas = tk.Canvas(root, width=400, height=400, bg="black")  # Black background color
canvas.pack()

# Start updating the clock
update_clock()

# Run the main Tkinter loop
root.mainloop()
