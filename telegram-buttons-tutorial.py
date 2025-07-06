import requests
from time import sleep

global OFFSET
OFFSET = 0

botToken = "7541470537:AAHrKAT-c1e4ayZmGyWPxU969Z8_8V0bifk"

global requestURL
global sendURL

requestURL = "https://api.telegram.org/bot" + botToken + "/getUpdates"
sendURL = "https://api.telegram.org/bot" + botToken + "/sendMessage"

def update(url):
    global OFFSET

    update_raw = requests.get(url + "?offset=" + str(OFFSET))
    update = update_raw.json()
    result = extract_results(update)

    if result != False:

        OFFSET = result['update_id'] + 1

        chat_id = result['message']['chat']['id']
        text = result['message']['text']

        send_message(chat_id, text)

def extract_results(dict):
    result_array = dict['result']


    if result_array == []:
        return False
    else:
        result_dic = result_array[0]
        return result_dic

def send_message(chatId, message):
    requests.post(sendURL + "?chat_id=" + str(chatId) + "&text=" + message)


while True:
    update (requestURL)
    sleep(1)
