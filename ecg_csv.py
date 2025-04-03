import serial
import csv
import time

# COM3 for Windows, /dev/ttyUSB0 for Linux and mac
arduino_port = "/dev/cu.usbserial-022F0461"
baud_rate = 9600
csv_filename = "INSERT_FILE_PATH.csv"

# Open serial connection
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Allow time for the connection to establish

# Open CSV file
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "ECG Value"])  # Write headers

    try:
        while True:
            line = ser.readline().decode().strip()  # Read from serial
            if line:
                timestamp = time.time()  # Get current time
                print(f"{timestamp}, {line}")  # Print to console
                writer.writerow([timestamp, line])  # Write to CSV
    except KeyboardInterrupt:
        print("\nLogging stopped. Closing file.")
    finally:
        ser.close()  # Close serial port 
