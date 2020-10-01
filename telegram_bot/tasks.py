from core_logic.models import Wallet, Extend, Income, Category
from django.db.models import Sum
from account.models import Profile 
from celery import task
from .bot import TelegramBot
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Offset
from decimal import Decimal

def is_num(num):
    try:
        float(num)
        return True
    except Exception:
        return False


def add_extend(user_wallet, buf):
    ex = Extend.objects.create(category=Category.objects.get(name=buf[1]),
                                price=buf[2],
                                comment='Added via Bot',
                                wallet=user_wallet)
    ex.save()
    user_wallet.balance=Decimal(
        user_wallet.balance) - Decimal(buf[2])
    user_wallet.save()

def check_and_add_extend(bot, update, user_wallet):
    categories = [x.name for x in Category.objects.all()]
    buf = update["text"].split(" ")
    if len(buf) == 3:
        if buf[1] in categories:
            if is_num(buf[2]):
                if len(str(buf[2]).split('.')) == 2:
                    if len(str(buf[2]).split('.')[1]) <= 2:
                        if user_wallet.balance - Decimal(buf[2]) > 0 and Decimal(buf[2]) > 0:
                            add_extend(user_wallet, buf)
                            bot.send_message({"text": "Extend added", "chat_id": update["chat_id"]})
                        else:
                            bot.send_message({"text":"You don't have enoug money or number is negative one", "chat_id": update["chat_id"]})
                    else:
                        bot.send_message({"text":"Price must be a 00.00 format", "chat_id": update["chat_id"]})
                else:
                    if user_wallet.balance - Decimal(buf[2]) > 0 and Decimal(buf[2]) > 0:
                        add_extend(user_wallet, buf)
                        bot.send_message({"text": "Extend added", "chat_id": update["chat_id"]})
                    else:
                        bot.send_message({"text":"You don't have enoug money or number is negative one", "chat_id": update["chat_id"]})
            else:
                bot.send_message({"text":"Price must be a number", "chat_id": update["chat_id"]})
        else:
            bot.send_message({"text":"No such category", "chat_id": update["chat_id"]})
    else:
        bot.send_message({"text":"You forgot some params", "chat_id": update["chat_id"]})    

def add_income(user_wallet, buf):
    inc = Income.objects.create(price=buf[1],
                        wallet=user_wallet)
    inc.save()
    user_wallet.balance=Decimal(
        user_wallet.balance) + Decimal(buf[1])
    user_wallet.save()

def check_and_add_income(bot, update, user_wallet):
    buf = update["text"].split(" ")
    if len(buf) == 2:
        if is_num(buf[1]):
            if len(str(buf[1]).split('.')) == 2:
                if len(str(buf[1]).split('.')[1]) <= 2:
                    add_income(user_wallet, buf)
                    bot.send_message({"text": "Income added", "chat_id": update["chat_id"]})
                else:
                    bot.send_message({"text":"Price must be a 00.00 format", "chat_id": update["chat_id"]})
            else:
                add_income(user_wallet, buf)
                bot.send_message({"text": "Income added", "chat_id": update["chat_id"]})
        else:
            bot.send_message({"text":"Price must be a number", "chat_id": update["chat_id"]})
    else:
        bot.send_message({"text": "Your command doesn't match to correct one", "chat_id": update["chat_id"]})

@task()
def bot_logic():
    bot = TelegramBot("1327984974:AAFuB5uIYZpbNgsCyA_aOpe1qPcscEllGHU")
    updates = bot.get_updates()
    if updates["ok"] != False:
        if len(updates["result"]) != 0:
            try:
                for i in updates["result"]:
                    bot.change_offset()
                    update = bot.get_last_chat_id_and_text(i)
                    user = Profile.objects.get(telegram_nickname=update["username"])
                    user_wallet = Wallet.objects.get(user=user)
                    if update["text"] == "/total_extends":
                        total_extends = [
                                x.price for x in Extend.objects.filter(wallet=user_wallet)]
                        bot.send_message({"text": f"Total extends : {sum(total_extends)}", "chat_id": update["chat_id"]})
                    elif update["text"] == "/today_extends":
                        today_extends = Extend.objects.filter(wallet=user_wallet, 
                                                date=datetime.now().strftime('%Y-%m-%d')).values(
                                                'date').annotate(price=Sum('price'))
                        if len(today_extends) != 0:
                            bot.send_message({"text": f"Today you spent {round(today_extends[0]['price'], 2)}", "chat_id": update["chat_id"]})
                        else:
                            bot.send_message({"text": f"Today you spent 0", "chat_id": update["chat_id"]})

                    elif update["text"] == "/start":
                        bot.get_url(bot.url+"sendPhoto?chat_id=190406965&photo=https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/6.png")
                        bot.send_message({"text" : "Hello my Lord", "chat_id": update["chat_id"]})
                    
                    elif "/add_extend" in update["text"]:
                        check_and_add_extend(bot, update, user_wallet)
                        
                    elif "/show_balance" in update["text"]:
                        bot.send_message({"text": f"Your blance: {user_wallet.balance}", "chat_id": update["chat_id"]})

                    elif "/add_income" in update["text"] :
                        check_and_add_income(bot, update, user_wallet)

                    elif "/categories" == update["text"]:
                        bot.send_message({"text" : f'Categories: {", ".join([i.name for i in Category.objects.all()])}', "chat_id": update["chat_id"]})
                    else:
                        bot.send_message({"text": "No such command, sorry", "chat_id": update["chat_id"]})
            except Profile.DoesNotExist:
                    bot.send_message({"text": "You need to be register in Wypter site", "chat_id": update["chat_id"]})