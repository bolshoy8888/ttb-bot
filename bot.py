# -*- coding: utf-8 -*-
import telebot
import pandas as pd 
from ta.momentum import RSIIndicator
from ta.trend import MACD
from telebot import types
from openai import OpenAI
import base64
analysis_count = {}
FREE_LIMIT = 3
vip_users = [8142357138]
import os
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=OPENAI_API_KEY
)
import requests
import pandas as pd 
TOKEN = "8085188538:AAEcxsPzXleng-ybklF_PDNvINMucy3f3D4"
bot = telebot.TeleBot (TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📊 Анализ графика")
    btn2 = types.KeyboardButton("💎 VIP сигналы")
    btn3 = types.KeyboardButton("📈 BTC цена")
    btn4 = types.KeyboardButton("🛠 Профиль")
    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4)
    bot.send_message(
        message.chat.id,
        "🚀 <b>TTB AI BOT</b>\n\n"
        "AI crypto assistant нового поколения\n\n"
        "📊 Анализ графиков\n"
        "💎 VIP сигналы\n"
        "⚡️ BTC price\n"
        "🧠 AI market scanner\n\n"
        "Выбери действие ниже 👇",
        parse_mode="HTML",
        reply_markup=markup
    )
@bot.message_handler(func=lambda message: message.text == "📈 BTC цена") 
def btc_price(message):
    response = requests.get(
        "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    )   
    data = response.json()
    bot.send_message(
        message.chat.id,
        f"📈 BTC: {data['price']}$"
    )
@bot.message_handler(func=lambda message: message.text == "💎 VIP сигналы")
def vip(message):
    bot.send_message(
        message.chat.id,
        "💎 VIP ДОСТУП\n\n"
        "✅ Безлимитные анализы\n"
        "✅ Более точные сигналы\n"
        "✅ Приоритетный AI анализ\n"
        "✅ VIP поддержка\n\n"
        "💰 Цена 10$/месяц\n\n"
        "📩 Для покупки напиши: @ttbsupport"
    )    
@bot.message_handler(func=lambda message: message.text == "🛠 Профиль")
def profile(message):
    bot.send_message(
        message.chat.id,
        f"👤 Профиль\n\n📊 Анализов: {analysis_count.get(message.chat.id, 0)}\n💎 VIP: {'Да' if message.chat.id in vip_users else 'Нет'}\n🚀 Статус: Trader"
    )
@bot.message_handler(func=lambda message: message.text == "📊 Анализ графика")
def analyze(message):
    user_id = message.chat.id 
    if user_id not in vip_users:
        used = analysis_count.get(user_id, 0)
        if used >= FREE_LIMIT:
            bot.send_message(
                message.chat.id,
                "🚫 Лимит бесплатных анализов исчерпан.\n\n💎 Купи VIP для безлимитного доступа."
            )
            return
        analysis_count[user_id] = used + 1    
    bot.send_message(
        message.chat.id,
        "📸 Отправь скриншот графика."
    )        
@bot.message_handler(commands=['price'])
def price(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.send_message(
            message.chat.id,
            "Напиши так:\n/price BTC"
        ) 
        return
    coin = parts[1]
    url =f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
    response = requests.get(url)
    data = response.json()
    if "symbol" in data:
        bot.send_message(
            message.chat.id,
            f"Монета: {data['symbol']}\nЦена: {data['price']}$"
        )
    else:
        bot.send_message(
            message.chat.id,
            "Монета не найдена"
        )    
@bot.message_handler(content_types=['photo'])
def get_photo(message) :
    user_id = message.chat.id
    if user_id not in vip_users:
        if analysis_count.get(user_id, 0) >=3:
            bot.send_message(
                message.chat.id,
                "🚫 Лимит анализов исчерпан.\n\n💎 Купи VIP для безлимитного доступа."
            )
            return 
    analysis_count[user_id] = analysis_count.get(user_id, 0) + 1      
    if user_id not in analysis_count:
        analysis_count[user_id] = 0 
    analysis_count[user_id]+=1    
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    download_file = bot.download_file(file_info.file_path)
    with open("chart.jpg", "wb") as new_file:
        new_file.write(download_file)
        with open("chart.jpg", "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    bot.send_message(
        message.chat.id,    
        "📸 Скриншот получен.\n\n"
        "🧠 AI анализирует рынок...\n"
        "📡 Проверка тренда...\n"
        "📊 Анализ объёмов...\n"
        "⚡️ Поиск точки входа..."
    )       
    candles = requests.get(
        "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=50"
    ).json()
    closes = [float(candle[4]) for candle in candles]
    df = pd.DataFrame(closes, columns=["close"])
    ma7 = df["close"].rolling(7).mean().iloc[-1]
    ma25 = df["close"].rolling(25).mean().iloc[-1]
    rsi = RSIIndicator(close=df["close"], window=14).rsi().iloc[-1]
    macd = MACD(close=df["close"])
    macd_value = macd.macd().iloc[-1]
    macd_signal = macd.macd_signal().iloc[-1]
    current_price = df["close"].iloc[-1]
    trend = "bullish" if ma7 > ma25 else "bearish"
    signal = "HOLD"
    if rsi > 60 and macd_value > macd_signal and ma7 > ma25:
        signal = "LONG"
    elif rsi < 40 and macd_value < macd_signal and ma7 < ma25:
        signal = "SHORT"    
    if user_id in vip_users:
        ai_mode = """
        VIPMODE:
        Используй углублённый анализ RSI, MACD, MA, volume, price action.
        Давай более профессиональные сигналы.
        Определяй силу тренда.
        Пиши подробнее и точнее.
        - Не придумывай RSI/MACD если индикатор не виден
        - Не выдумывай данные
        - Используй только информацию со скриншота
        - Если есть умеренное преимущество одной стороны - допускаеться LONG или SHORT
        - HOLD только при полном отсутствии направления
        - Оцени momentum свечей и структуру тренда
        - При сильном импульсе не бойся давать сигнал
        - Отвечай кратко и профессионально
        - Не повторяй одни и те же причины разными словами
        - Не пиши длинные сообщения
        - HOLD только если рынок действительно во флэте
        - Если есть перевес продавцов — SHORT
        - Если есть перевес покупателей — LONG
        - Анализируй momentum свечей
        - Анализируй силу импульса
        - Анализируй пробои и откупы
        - Не бойся давать направление при наличии преимущества одной стороны
        """
    else:
        ai_mode = """
        FREE MODE:
        Давай краткий базовый анализ.
        """

    response = client.responses.create(
        model="gpt-4.1",
        input=[{
        "role": "user",
        "content": [
            {
                "type": "input_text",
                "text": f"""
{ai_mode}

Ты профессиональный crypto trader и market analyst.

Не придумывай RSI/MACD если индикатор не виден.
Не выдумывай данные.
Используй только информацию со скриншота.
Если данных мало — пиши HOLD.

Ответ строго в формате:

📉 Сигнал: LONG / SHORT / HOLD

Тренд: bullish / bearish / neutral
Сила: weak / medium / strong
Вероятность: %

Entry:
SL:
TP:

Причины:
• причина
• причина
• причина

Риск:
кратко
"""
            },

            {
    "type": "input_image",
    "image_url": f"data:image/jpeg;base64,{base64_image}",
},
        

        ]
    }]
)
    answer = response.output_text

    bot.send_message(
    message.chat.id,
    f"🤖 AI сигнал:\n\n{answer}"
)           
            
            
@bot.message_handler(commands=['id'])
def get_id(message):
    bot.send_message(
        message.chat.id,
        f"🆔 Твой ID: {message.chat.id}"
    )             
while True:
    try: bot.polling(none_stop=True, interval=1)
    except Exception as e:
        print(e)