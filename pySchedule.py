# Como Agendar Scripts Python & Execução Paralela

import schedule
import time

def tarefa():
    print("Executando tarefa")

def job():
    print("I'm working...")

# definindo intervalo
schedule.every(10).seconds.do(tarefa)
schedule.every(10).minutes.do(job)
schedule.every().minute.at(":17").do(job)
schedule.every(5).to(10).minutes.do(job) #random (5, 10)
schedule.every().hour.do(job)

schedule.every(3).day.do(tarefa)
schedule.every(1).day.at('08:00').do(tarefa)

schedule.every(1).week.do(tarefa)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    



