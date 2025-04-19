##🕰️ Analog Clock with Tkinter

This project is a simple Analog Clock built using Python's tkinter library. It visually represents the current local time with moving hour, minute, and second hands, along with the current date displayed in the center.


#🛠 Features

🕒 Real-time analog clock with dynamic hour, minute, and second hands

📆 Displays current date at the center

🔴 Red second hand for visibility

⚪ White hour and minute hands

🕳️ Realistic clock face and center point

🕐 Numbered hour markers (1–12)

⏱ Updates every second using canvas.after()

#📦 Requirements

Python 3.x

No additional libraries required (only uses standard Python libraries)

#🚀 How to Run

Run the script:

`bash`

python analog_clock.py

#🧠 How It Works

- Uses tk.Canvas to draw clock face, hands, and texts.
- Updates the clock every second with the current system time using time.localtime().
- Calculates hand positions using trigonometry (math.sin and math.cos) to animate rotation based on time.



