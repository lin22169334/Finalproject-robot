from selenium import webdriver
from linebot.models import *
from config import *
import time
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('uzmph5Y7zgSs/qSnmRVER/wPE5D4Q5FtKIDeFXOtNR0izbF15mxOv33syV8Igl1lyPCCI5qHcQOMyzyqBVP4qKVGD7a+0EvH97jphk9VIPaxHLLEVFQrwYTsFk+H0IUXAfnWExwgdtufeBpqHe6EMgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('08d63e6071071a3d5ee05b284c32df32')

line_bot_api.push_message('U796f6dae05bea1c7a053dd89d567a079', TextSendMessage(text='你可以躺下了'))
def youtube_vedio_parser():
    
    url = 'https://www.instagram.com/'
    
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    PATH='C:/Users/lin43/OneDrive/桌面/selenium/chromedriver.exe'
    driver=webdriver.Chrome(PATH,options=option)
    driver.get(url)
    
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
    username.clear()
    password.clear()
    username.send_keys('dkqoel')
    password.send_keys('tang1128')
    login=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
    login.click()
    search=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
        )
    search.clear()
    keyword='張香香'
    search.send_keys(keyword)
    time.sleep(1)
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    search.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD'))
        )
    image=driver.find_element(By.CLASS_NAME,'FFVAD')
    image_url=image.get_attribute('src')
    return image_url

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

 
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    image_url= youtube_vedio_parser()
    message = ImageSendMessage(original_content_url=image_url,preview_image_url=image_url)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)