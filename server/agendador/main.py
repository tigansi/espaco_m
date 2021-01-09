import schedule
import time


def tarefas():
    print("Executado")


schedule.every(1).minutes.do(tarefas)

while True:
    schedule.run_pending()
    time.sleep(1)
