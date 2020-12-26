import requests
import time
from plyer import notification
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=5
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    notifyMe("kiron", "let's go")
    myHtmlData = getData('https://www.mohfw.gov.in/')

    soup = BeautifulSoup(myHtmlData, 'html.parser')

    print(soup.prettify())

    myDataStr = ""
    for tr in soup.find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]
    print(myDataStr.split("\n\n"))
    itemList = myDataStr.split("\n\n")

    states = ['Chandigarh', 'Uttar Pradesh', 'West Bangle']
    for item in itemList[0:22]:
        dataList = item.split('\n')
        if dataList[1] in states:
            print(dataList)
            nTitle = " cases of covid-19"
            nText = f"dataList[1]: Indian:{dataList[2]} Foreign: {dataList[3]} Cured:{dataList[4]} Deaths: {dataList[5]}"
            notifyMe(nTitle, nText)
            time.sleep(2)
    time.sleep(10)



