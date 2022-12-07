import pyautogui as gui
import pywhatkit as kit
import time

from Client import Client


def sendWhatsappSMS(recipientData):
    kit.sendwhatmsg_instantly(recipientData[0], getBodyText(recipientData), 5)
    time.sleep(5)
    gui.hotkey("ctrl", "w")



def sendMultipleWhatsappMessages():
    with open("Recipients.txt") as f:
        recipientsDatalist = sorted(word.strip() for line in f for word in line.split('\n') if word != "")
        for recipientData in recipientsDatalist:
            sendWhatsappSMS(recipientData.split(';'))


def getBodyText(recipientData):
    client = Client(recipientData)
    return f"Greetings {client.name}. Based on your public profile at Yell, we noticed that you provide {client.service}" \
           f" in {client.area}. We would very much appreciate " \
           f"if you would take some time by completing the following survey regarding" \
           f"the way how you find the way your business run:\n\n" \
           f" \n1) Do you feel satisfied with the current status of your business and income you earn from it?" \
           f" \n2) If you are offered extra jobs or collaboration, will you open to listen to or accept them?" \
           f" \n3) If yes, what would be the perfect conditions or terms to accept them?"


if __name__ == '__main__':
    sendMultipleWhatsappMessages()
