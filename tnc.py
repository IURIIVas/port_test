import subprocess

ip = input("Введите ip: ")
numberOfPorts = int(input("Введите количество портов: "))

for i in range(numberOfPorts):
    port = input("Введите порт: ")
    responce = subprocess.Popen(['powershell', 'Test-NetConnection ' + ip + ' -p ' + port + ' -InformationLevel Quiet']) #запуск powershell и передача ему ip и порта
    responce.wait()
    print(responce)

input("Для выхода нажмите Enter: ")