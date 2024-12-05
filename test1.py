import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset using pandas
def load_sensor_data(file_path):
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)
    heart_rate = data['Heart Rate']
    pulse_rate = data['Pulse Rate']
    respiration_rate = data['Respiration Rate']
    return heart_rate, pulse_rate, respiration_rate

# Step 2: Plot sensor data over time
def plot_sensor_data(hr, pr, rr):
    time_stamps = np.arange(0, len(hr))  # Generate timestamps based on the data length
    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plt.plot(time_stamps, hr)
    plt.title("Heart Rate Over Time")
    plt.xlabel('Time (s)')
    plt.ylabel('Heart Rate (bpm)')

    plt.subplot(3, 1, 2)
    plt.plot(time_stamps, pr)
    plt.title("Pulse Rate Over Time")
    plt.xlabel('Time (s)')
    plt.ylabel('Pulse Rate (bpm)')

    plt.subplot(3, 1, 3)
    plt.plot(time_stamps, rr)
    plt.title("Respiration Rate Over Time")
    plt.xlabel('Time (s)')
    plt.ylabel('Respiration Rate (breaths/min)')

    plt.tight_layout()
    plt.show()

# Step 3: Plot CDF (Cumulative Distribution Function)
def plot_cdf(data, title):
    sorted_data = np.sort(data)
    cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    plt.plot(sorted_data, cdf)
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('CDF')
    plt.grid(True)

def main():
    # Corrected file path for Windows
    file_path = r"C:\Users\HP\Documents\Datasets\health_data.csv"
    
    # Load actual data from CSV file
    heart_rate, pulse_rate, respiration_rate = load_sensor_data(file_path)

    # Plot the loaded sensor data
    plot_sensor_data(heart_rate, pulse_rate, respiration_rate)

    # Plot CDF for heart rate, pulse rate, and respiration rate
    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plot_cdf(heart_rate, 'CDF of Heart Rate')

    plt.subplot(3, 1, 2)
    plot_cdf(pulse_rate, 'CDF of Pulse Rate')

    plt.subplot(3, 1, 3)
    plot_cdf(respiration_rate, 'CDF of Respiration Rate')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
