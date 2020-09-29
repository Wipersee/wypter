from core_logic.models import Wallet, Extend, Income, Category
from django.db.models import Sum
from account.models import Profile 
from celery import task
from .bot import TelegramBot
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Offset
from decimal import Decimal

@task()
def bot_logic():
    bot = TelegramBot("1327984974:AAFuB5uIYZpbNgsCyA_aOpe1qPcscEllGHU")
    updates = bot.get_updates()
    if len(updates["result"]) != 0:
        try:
            for i in updates["result"]:
                # offset = Offset.objects.all()[::-1]
                # Offset.objects.create(offset = list(offset)[0].offset+1)
                # url = bot.url + f"getUpdates?o
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
                    buf = update["text"].split(" ")
                    categories = [x.name for x in Category.objects.all()]
                    
                    if len(buf) == 3 and buf[1] in categories and user_wallet.balance - Decimal(buf[2]) > 0 and Decimal(buf[2]) > 0:
                        ex = Extend.objects.create(category=Category.objects.get(name=buf[1]),
                                              price=buf[2],
                                              comment='Added via Bot',
                                              wallet=user_wallet)
                        ex.save()
                        user_wallet.balance=Decimal(
                            user_wallet.balance) - Decimal(buf[2])
                        user_wallet.save()
                        bot.send_message({"text": "Extend added", "chat_id": update["chat_id"]})
                    else:
                         bot.send_message({"text": "No such category or your command doesn't match to correct one or you don't have enough money", "chat_id": update["chat_id"]})
                elif "/show_balance" in update["text"]:
                    bot.send_message({"text": f"Your blance: {user_wallet.balance}", "chat_id": update["chat_id"]})
                elif "/add_income" in update["text"] :
                    buf = update["text"].split(" ")
                    if len(buf) == 2 and Decimal(buf[1]) > 0:
                        inc = Income.objects.create(price=buf[1],
                                              wallet=user_wallet)
                        inc.save()
                        user_wallet.balance=Decimal(
                            user_wallet.balance) + Decimal(buf[1])
                        user_wallet.save()
                        bot.send_message({"text": "Income added", "chat_id": update["chat_id"]})
                    else:
                         bot.send_message({"text": "Your command doesn't match to correct one", "chat_id": update["chat_id"]})
                elif "/categories" == update["text"]:
                    bot.send_message({"text" : f'Categories: {", ".join([i.name for i in Category.objects.all()])}', "chat_id": update["chat_id"]})
                else:
                    bot.send_message({"text": "No such command, sorry", "chat_id": update["chat_id"]})
        except Profile.DoesNotExist:
                bot.send_message({"text": "You need to be register in Wypter site", "chat_id": update["chat_id"]})