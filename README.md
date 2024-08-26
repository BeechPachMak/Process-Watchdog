# 👀 **Process Watchdog**

A Python tool to monitor processes on your Windows system and detect those that disappear while the Task Manager is open. 🕵️‍♂️

## 📜 **Description**

**Process Watchdog** is a lightweight Python script designed to help you identify processes that might be hiding or quickly disappearing. This can be particularly useful for detecting suspicious activities, such as cryptomining software that may try to avoid detection.

## 🚀 **Features**

- **Real-Time Monitoring**: Track processes in real-time and identify those that close while the Task Manager is open.
- **Dynamic Detection**: Continuously monitor and update process lists to catch rapidly disappearing processes.
- **Customizable Monitoring Duration**: Set how long the program should monitor for disappearing processes.

## 🛠️ **Installation**

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/process-watchdog.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd process-watchdog
    ```

3. **Install dependencies**:

    Ensure you have `psutil` installed. If not, install it using pip:

    ```bash
    pip install psutil
    ```

## 📖 **Usage**

1. **Run the script**:

    ```bash
    python process_watchdog.py
    ```

2. **Enter the duration** for monitoring when prompted (in seconds).

3. **The script will**:
    - Open the Task Manager.
    - Monitor processes for the specified duration.
    - Print out processes that disappear during the monitoring period.

## 🛡️ **Notes**

- **Admin Rights**: Ensure you run the script with sufficient privileges to monitor processes and open Task Manager.
- **Detection Limitations**: The script may not catch all types of hidden or rapidly changing processes.

## 🤝 **Contributing**

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull requests.
