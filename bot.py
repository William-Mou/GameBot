import telepot
from telepot.loop import MessageLoop
from random import choice
import requests
import random
import time
import json
import sys
import cons
import game

TOKEN = "628859102:AAE2FXX5BA88kq-dQVVxDJ_4ab9e6xWgHQg"
bot = telepot.Bot(TOKEN)
# {userid:[True,constellation]}
constellation_dict = {}
constellation = ("牡羊","金牛","雙子","巨蟹", "獅子", "處女", "天秤", "天蠍", "射手", "摩羯", "水瓶", "雙魚")
game_dict = {}

def print_msg(msg):
    print(json.dumps(msg, indent=4))

# 接收chat後執行：
def on_chat(msg):
    header = telepot.glance(msg, flavor="chat")
    # 列印傳入文字訊息
    print_msg(msg)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # 判斷是否為指令
    chat_id = msg["chat"]["id"]
    user_id = msg["from"]["id"]
    username = msg["from"]["username"]
    text = msg["text"]

    if text.startswith("/"):
        command = text.lstrip("/").split()
        if command[0] == "setconstellation":
            if user_id in constellation_dict:
                constellation_dict[user_id][0] = True
            else:
                constellation_dict[user_id] = [True, ""]
        elif command[0] == "getfate_all":
            for i in constellation:
                ans = ""
                ans += i +"座：\n"
                ans += cons.find_cons(i)
                ans += "\n~~~~~~~~~~~~~~~\n"
                bot.sendMessage(header[2], ans)

        elif command[0] == "getfate":
            bot.sendMessage(header[2], cons.find_cons(constellation_dict[user_id][1]))
        elif command[0] == "newgame":
            if chat_id in game_dict:
                bot.sendMessage(header[2], "此聊天室已開始遊戲")
            else:
                game_dict[chat_id] = game.game(chat_id)
        elif command[0] == "closegame":
            if chat_id in game_dict:
                del game_dict[chat_id]
                bot.sendMessage(header[2], "此聊天室已關閉遊戲")
            else:
                bot.sendMessage(header[2], "此聊天室未開始遊戲")
        elif command[0] == 'help':
            bot.sendMessage(chat_id, (
                '/newgame - 創建遊戲\n'
                '/startgame - 開始遊戲\n'
                '/closegame - 結束遊戲\n'
                '/joingame - 加入遊戲\n'
                '/setconstellation - 設定星座\n'
                '/getfate - 取得星座運勢\n'
                '/getfate_all - 取得所有星座運勢\n'
                '/help - 機器人說明'))
        else:
            if chat_id in game_dict:
                game_dict[chat_id].input(command, msg)
            else:
                bot.sendMessage(header[2], "此聊天室未開始遊戲")
    else:
        if constellation_dict[user_id][0] and text in constellation:
            constellation_dict[user_id][1] = text
            bot.sendMessage(header[2], cons.find_cons(text))
            constellation_dict[user_id][0] = False
MessageLoop(bot, {'chat': on_chat,}).run_as_thread()
print('Listening ...')

while True:
    time.sleep(10)