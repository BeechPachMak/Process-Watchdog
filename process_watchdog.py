import psutil
import subprocess
import time

def get_running_processes():
    return {p.info['pid']: p.info['name'] for p in psutil.process_iter(['pid', 'name'])}

def monitor_processes(duration, lang):
    if lang == 'en':
        print("Collecting data on running processes...")
        print("Opening Task Manager. Please wait...")
        print(f"Monitoring processes for {duration} seconds...")
        print("Monitoring completed.")
        closed_message = "Processes that closed:"
        no_processes_message = "No processes have closed at the moment."
    else:
        print("Собираем данные о запущенных процессах...")
        print("Открытие Диспетчера задач. Пожалуйста, подождите...")
        print(f"Мониторинг процессов в течение {duration} секунд...")
        print("Мониторинг завершен.")
        closed_message = "Процессы, которые закрылись:"
        no_processes_message = "Нет процессов, которые бы закрылись на данный момент."

    initial_processes = get_running_processes()
    subprocess.Popen('taskmgr.exe')
    time.sleep(5)
    end_time = time.time() + duration
    while time.time() < end_time:
        current_processes = get_running_processes()
        closed_processes = set(initial_processes.keys()) - set(current_processes.keys())
        if closed_processes:
            print(closed_message)
            for pid in closed_processes:
                print(f"PID: {pid}, Name: {initial_processes[pid]}" if lang == 'en' else f"PID: {pid}, Название: {initial_processes[pid]}")
        else:
            print(no_processes_message)
        initial_processes = current_processes
        time.sleep(1)

def main():
    print("Welcome to Process Watchdog!")
    choice = input("Would you like to switch to Russian? (yes/no): ").strip().lower()
    lang = 'ru' if choice == 'yes' else 'en'
    
    monitor_duration = int(input("Enter the monitoring duration in seconds: ").strip())
    monitor_processes(duration=monitor_duration, lang=lang)

if __name__ == "__main__":
    main()
