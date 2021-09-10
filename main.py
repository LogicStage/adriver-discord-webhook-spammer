import time
import requests
import os

#chuckleszjeb
print("""

░█████╗░██████╗░██████╗░██╗██╗░░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║██║░░░██║██╔════╝██╔══██╗
███████║██║░░██║██████╔╝██║╚██╗░██╔╝█████╗░░██████╔╝
██╔══██║██║░░██║██╔══██╗██║░╚████╔╝░██╔══╝░░██╔══██╗
██║░░██║██████╔╝██║░░██║██║░░╚██╔╝░░███████╗██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝ by logik""")


question = input("Start? [Y/N]")


if question == 'Y':
    print("Oki hehehe")
    webhook = input(" Enter ur webhook")
    delay = input(" Enter a delay")
    message = input(" Enter a message")


    def spam(message, webhook, delay):
        counter = 0


        while True:
            try:
                data = requests.post(webhook, json={'content': message})
                if data.status_code == 204:
                    print(f"message sent elooo {message}")
                    time.sleep(float(delay))
            except:
                print("Wrong Webhook :" + webhook)
                time.sleep(10)
                exit()


elif question == 'N':
        print("OK naura")
        exit()



else:
    print("Wrong Value")

spammer = 1
while spammer == 1:
    spam(message, webhook, delay)