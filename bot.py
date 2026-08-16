import telebot
import json
import threading
import time
import os
import random
import string
from datetime import datetime, timedelta
from faker import Faker
import requests
from telebot import types
from gatet import *
from reg import reg

stopuser = {}
token = '8969140829:AAFH76n3bZBFnpaGaUSc5pXwJwQHJvHbAQA'
bot = telebot.TeleBot(token, parse_mode="HTML")
admin = 1088443477
f = Faker()
name = f.name()
street = f.address()
city = f.city()
state = f.state()
postal = f.zipcode()
phone = f.phone_number()
coun = f.country()
mail = f.email()
command_usage = {}


def reset_command_usage():
  for user_id in command_usage:
    command_usage[user_id] = {'count': 0, 'last_time': None}


@bot.message_handler(commands=['start'])
def start(message):

  def my_function():
    name = message.from_user.first_name
    with open('data.json', 'r') as file:
      json_data = json.load(file)
    id = message.from_user.id

    try:
      BL = json_data[str(id)]['plan']
    except:
      BL = '𝗙𝗥𝗘𝗘'
      with open('data.json', 'r') as json_file:
        existing_data = json.load(json_file)
      new_data = {id: {'plan': '𝗙𝗥𝗘𝗘', 'timer': 'none'}}

      existing_data.update(new_data)
      with open('data.json', 'w') as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
    if BL == '𝗙𝗥𝗘𝗘':
      keyboard = types.InlineKeyboardMarkup()
      ahmed = types.InlineKeyboardButton(
          text='✨ 𝗢𝗪𝗡𝗘𝗥  ✨', url='https://t.me/FJ0FF'
      )
      contact_button = types.InlineKeyboardButton(
          text='✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨', url='https://t.me/mmqxq'
      )
      keyboard.add(contact_button, ahmed)
      video_url = 'https://t.me/zdtuuu/35'
      bot.send_video(
          chat_id=message.chat.id,
          video=video_url,
          caption=f"""<b>مرحبا {name}
عذرا هذا البوت ليس مجانا 


الاسعار ✅ :  
6 ساعات : 2 اسيا
يوم : 3 اسيا
اسبوع : 9 اسيا
شهر : 18 اسيا

للشراء عن طريق اسياسيل من هنا : @FJ0FF

Subscription to the bot prices is now available: 
  
the prices ✅ :  
6 hours : 1 USDT 
day : 2 USDT 
week : 6 USDT 
Month : 12 USDT

To purchase via USDT from here : @FJ0FF
User Bot : @TomeCheckerBot {BL}</b>
	""",
          reply_markup=keyboard,
      )
      return
    keyboard = types.InlineKeyboardMarkup()
    contact_button = types.InlineKeyboardButton(
        text='✨ 𝗢𝗪𝗡𝗘𝗥 ✨', url='https://t.me/FJ0FF'
    )
    ahmed = types.InlineKeyboardButton(
        text='✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ✨', url='https://t.me/mmqxq'
    )
    keyboard.add(contact_button, ahmed)
    bot.send_video(
        chat_id=message.chat.id,
        video='https://t.me/zdtuuu/35',
        caption=(
            '𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏O 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣ْد𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚'
            ' 𝙁𝙞𝙡𝙚 𝘼𝙣ْد I 𝑾𝙞𝒍𝒍 𝘾𝙝𝙚𝙘𝒌 𝙄𝙩'
        ),
        reply_markup=keyboard,
    )

  threading.Thread(target=my_function).start()


@bot.message_handler(commands=['cmds'])
def cmds_handler(message):
  with open('data.json', 'r') as file:
    json_data = json.load(file)
  id = message.from_user.id
  try:
    BL = json_data[str(id)]['plan']
  except:
    BL = '𝗙𝗥𝗘𝗘'
  keyboard = types.InlineKeyboardMarkup()
  contact_button = types.InlineKeyboardButton(
      text=f'✨ {BL}  ✨', callback_data='plan'
  )
  keyboard.add(contact_button)
  bot.send_message(
      chat_id=message.chat.id,
      text=f"""<b> 
𝗧𝗛𝗘𝗦𝗘 𝗔𝗥𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇'𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 
━━━━━━━━━━━━
𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 > <code>/chk number|mm|yy|cvc</code>
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘 ✅
━━━━━━━━━━━━
3𝗗 𝗟𝗢𝗢𝗞𝗨𝗣 > <code>/vbv number|mm|yy|cvc</code>
𝗢𝗡𝗟𝗜𝗡𝗘 ❌
━━━━━━━━━━━━
𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 > <code>/str number|mm|yy|cvc</code>
𝗢𝗡𝗟𝗜𝗡𝗘 ✅
━━━━━━━━━━━━

𝗪𝗘 𝗪𝗜𝗟𝗟 𝗕𝗘 𝗔𝗗𝗗𝗜𝗡𝗚 𝗦𝗢𝗠𝗘 𝗚𝗔𝗧𝗘𝗪𝗔𝗬𝗦 𝗔𝗡𝗗 𝗧𝗢𝗢𝗟𝗦 𝗦𝗢𝗢𝗡</b>
""",
      reply_markup=keyboard,
  )


@bot.message_handler(content_types=['document'])
def main(message):
  name = message.from_user.first_name
  with open('data.json', 'r') as file:
    json_data = json.load(file)
  id = message.from_user.id

  try:
    BL = json_data[str(id)]['plan']
  except:
    BL = '𝗙𝗥𝗘𝗘'
  if BL == '𝗙𝗥𝗘𝗘':
    with open('data.json', 'r') as json_file:
      existing_data = json.load(json_file)
    new_data = {id: {'plan': '𝗙𝗥𝗘𝗘', 'timer': 'none'}}
    existing_data.update(new_data)
    with open('data.json', 'w') as json_file:
      json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
    keyboard = types.InlineKeyboardMarkup()
    contact_button = types.InlineKeyboardButton(
        text='✨ 𝗢𝗪𝗡𝗘𝗥  ✨', url='https://t.me/FJ0FF'
    )
    ahmed = types.InlineKeyboardButton(
        text='✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨', url='https://t.me/mmqxq'
    )
    keyboard.add(contact_button, ahmed)
    bot.send_message(
        chat_id=message.chat.id,
        text=f"""<b>مرحبا {name}
عذرا هذا البوت ليس مجانا 


الاسعار ✅ :  
6 ساعات : 2 اسيا
يوم : 3 اسيا
اسبوع : 9 اسيا
شهر : 18 اسيا

للشراء عن طريق اسياسيل من هنا : @FJ0FF

Subscription to the bot prices is now available: 
  
the prices ✅ :  
6 hours : 1 USDT 
day : 2 USDT 
week : 6 USDT 
Month : 12 USDT

To purchase via USDT from here : @FJ0FF
User Bot : @TomeCheckerBot {BL}</b>
""",
        reply_markup=keyboard,
    )
    return
  
  keyboard = types.InlineKeyboardMarkup()
  contact_button = types.InlineKeyboardButton(
      text=f'Braintree Auth', callback_data='br'
  )
  # زر Stripe Charge الرئيسي الذي سيقوم باستهداف البوابة وفحص الملف
  stripe_button = types.InlineKeyboardButton(
      text=f'Stripe Charge', callback_data='str'
  )
  keyboard.add(contact_button)
  keyboard.add(stripe_button)
  bot.reply_to(message, text=f'اختر البوابة التي تريد استخدامها', reply_markup=keyboard)
  ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
  with open('combo.txt', 'wb') as w:
    w.write(ee)


# جعل زر Stripe Charge (callback_data='str') هو المسؤول حصرياً عن فحص البوابة وتشغيل الدالة
@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback_stripe_charge(call):

  def my_function():
    id = call.from_user.id
    gate = 'Stripe Charge'
    dd = 0
    live = 0
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text='يتم فحص بطائقك',
    )
    try:
      with open('combo.txt', 'r') as file:
        lino = file.readlines()
        total = len(lino)
        try:
          stopuser[f'{id}']['status'] = 'start'
        except:
          stopuser[f'{id}'] = {'status': 'start'}
        for cc in lino:
          cc = cc.strip()
          if not cc:
            continue
          if stopuser[f'{id}']['status'] == 'stop':
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text='تم الايقاف بنجاح مالك البوت @FJ0FF',
            )
            return
          
          bin_code = cc[:6]
          data = {}
          try:
            r = requests.get(f'https://bins.antipublic.cc/bins/{bin_code}', timeout=5)
            if r.status_code == 200:
              data = r.json()
          except:
            pass

          if not data or 'brand' not in data:
            try:
              r = requests.get(f'https://lookup.binlist.net/{bin_code}', timeout=5)
              if r.status_code == 200:
                binlist_data = r.json()
                data['brand'] = binlist_data.get('scheme', 'unknown')
                data['type'] = binlist_data.get('type', 'unknown')
                bank_dict = binlist_data.get('bank', {})
                data['bank'] = bank_dict.get('name', 'unknown') if isinstance(bank_dict, dict) else 'unknown'
                country_dict = binlist_data.get('country', {})
                if isinstance(country_dict, dict):
                  data['country_name'] = country_dict.get('name', 'unknown')
                  data['country_flag'] = country_dict.get('emoji', 'unknown')
                else:
                  data['country_name'] = 'unknown'
                  data['country_flag'] = 'unknown'
            except:
              pass

          brand = data.get('brand') or data.get('scheme') or 'unknown'
          card_type = data.get('type') or 'unknown'
          bank = data.get('bank') or 'unknown'
          country = data.get('country_name') or data.get('country') or 'unknown'
          country_flag = data.get('country_flag') or data.get('emoji') or 'unknown'

          start_time = time.time()
          try:
            last = str(scc(cc))
          except Exception as e:
            print(e)
            last = 'Error'

          success_keywords = ['CHARGED', 'SUCCESS', 'approved', 'succeeded', 'live', 'Funds', 'avs', 'دفع بنجاح', '15']
          is_approved = any(keyword.lower() in last.lower() for keyword in success_keywords)
          
          if is_approved:
            live += 1
          else:
            dd += 1

          mes = types.InlineKeyboardMarkup(row_width=1)
          cm1 = types.InlineKeyboardButton(f'• {cc} •', callback_data='u8')
          status = types.InlineKeyboardButton(
              f'• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •', callback_data='u8'
          )
          cm3 = types.InlineKeyboardButton(
              f'• 𝘼𝙋𝙿𝙍𝑶𝑽𝑬𝑫 ✅ ➜ [ {live} ] •', callback_data='x'
          )
          cm4 = types.InlineKeyboardButton(
              f'• 𝘿𝙀𝗖𝙇𝙄Ն𝙀𝘿 ❌ ➜ [ {dd} ] •', callback_data='x'
          )
          cm5 = types.InlineKeyboardButton(
              f'• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •', callback_data='x'
          )
          stop = types.InlineKeyboardButton(
              f'[ 𝙎𝙏𝙊𝙋 ]', callback_data='stop'
          )
          mes.add(cm1, status, cm3, cm4, cm5, stop)
          end_time = time.time()
          execution_time = end_time - start_time
          
          bot.edit_message_text(
              chat_id=call.message.chat.id,
              message_id=call.message.message_id,
              text=f"""رجائا انتظر ليتم فحص بطائقك على بوابة {gate}
مالك البوت @FJ0FF""",
              reply_markup=mes,
          )

          msg = f"""<b>𝗔𝗽𝗽𝗿𝙤𝘃𝗲𝗱 ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{bin_code}</code> - <code>{card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝙺 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @FJ0FF
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {'{:.1f}'.format(execution_time)} secounds .</b>"""

          # إرسال رسالة البطاقة المقبولة فوراً للمستخدم بدون أي تأخير
          if is_approved:
            try:
              bot.send_message(call.from_user.id, msg)
            except Exception as err:
              print(f"Error sending approved card: {err}")
            
          time.sleep(2)
    except Exception as e:
      print(e)
    stopuser[f'{id}']['status'] = 'start'
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text='تم الانتهاء من الفحص مالك البوت @FJ0FF',
    )

  threading.Thread(target=my_function).start()


@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_callback(call):
  user_id = str(call.from_user.id)
  stopuser.setdefault(user_id, {})['status'] = 'stop'
  bot.answer_callback_query(call.id, text='تم طلب إيقاف الفحص...')


@bot.callback_query_handler(func=lambda call: True)
def menu_callback(call):
  user_id = str(call.from_user.id)
  stopuser.setdefault(user_id, {})['status'] = 'stop'


print('تم تشغيل البوت')
if __name__ == '__main__':
  try:
    bot.remove_webhook()
    bot.infinity_polling(timeout=20, long_polling_timeout=5)
  except Exception as e:
    print(f'حدث خطأ: {e}')
