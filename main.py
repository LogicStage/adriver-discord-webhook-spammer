import time
import requests

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
    message = input(" Enter a message")


    def spam(message, webhook):


        while True:
            try:
                data = requests.post(webhook, json={'content': message})
                if data.status_code == 204:
                    print(f"message sent elooo {message}")
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
    spam(message, webhook)