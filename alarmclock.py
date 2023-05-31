from tkinter import *
import datetime
import time

# Create a tkinter window
root = Tk()
root.geometry("300x150")
root.title("Alarm Clock")

# Define a function to set the alarm
def set_alarm():
    # Get the alarm time from the user input
    alarm_time = alarm_input.get()
    # Convert the alarm time to a datetime object
    alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M')
    # Get the current time
    current_time = datetime.datetime.now().time()
    # Calculate the time delta between the alarm time and current time
    time_delta = datetime.datetime.combine(datetime.date.today(), alarm_time) - datetime.datetime.combine(datetime.date.today(), current_time)
    # Convert the time delta to seconds
    time_delta_seconds = time_delta.seconds
    # Sleep for the specified time
    time.sleep(time_delta_seconds)
    # Show the alarm message
    message_label.config(text="Wake up!")

# Create a label for the alarm input
alarm_label = Label(root, text="Set alarm (HH:MM):")
alarm_label.pack(pady=10)

# Create an entry widget for the alarm input
alarm_input = Entry(root)
alarm_input.pack()

# Create a button to set the alarm
set_button = Button(root, text="Set alarm", command=set_alarm, width=10)
set_button.pack(pady=10)

# Create a label for the alarm message
message_label = Label(root, text="")
message_label.pack(pady=10)

# Center the window on the screen
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

# Run the tkinter event loop
root.mainloop()
