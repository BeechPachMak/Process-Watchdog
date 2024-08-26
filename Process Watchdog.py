import psutil
import subprocess
import time

def get_running_processes():
    """Получить список всех текущих процессов"""
    return {p.info['pid']: p.info['name'] for p in psutil.process_iter(['pid', 'name'])}

def monitor_processes(duration=30):
    """Мониторинг процессов на протяжении заданного времени"""
    print("Собираем данные о запущенных процессах...")
    initial_processes = get_running_processes()

    # Запуск Диспетчера задач
    print("Открытие Диспетчера задач. Пожалуйста, подождите...")
    subprocess.Popen('taskmgr.exe')
    
    # Даем немного времени, чтобы Диспетчер задач открылся
    time.sleep(5)

    print(f"Мониторинг процессов в течение {duration} секунд...")
    end_time = time.time() + duration

    while time.time() < end_time:
        current_processes = get_running_processes()
        closed_processes = set(initial_processes.keys()) - set(current_processes.keys())
        if closed_processes:
            print("Процессы, которые закрылись:")
            for pid in closed_processes:
                print(f"PID: {pid}, Название: {initial_processes[pid]}")
        else:
            print("Нет процессов, которые бы закрылись на данный момент.")
        
        # Обновляем начальные процессы для следующей проверки
        initial_processes = current_processes
        time.sleep(1)  # Проверяем каждые 1 секунду

    print("Мониторинг завершен.")

def main():
    monitor_duration = int(input("Введите продолжительность мониторинга в секундах: ").strip())
    monitor_processes(duration=monitor_duration)

if __name__ == "__main__":
    main()

