import wikipedia
from aiogram import Bot, Dispatcher, executor, types
import re
from TOKENenvAnonymous import TOKEN
from keyboards import keyboard, keyboard2, ininlinekeyboard
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Отправьте мне любое слово, и я найду его значение на Wikipedia",reply_markup=keyboard)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Отправьте мне любое слово, и я найду его значение на Wikipedia")

@dp.message_handler()
async def any_text_message(message: types.Message):
    await message.answer(getwiki(message.text), reply_markup=ininlinekeyboard)


def getwiki(text):
    try:
        wikipedia.set_lang("ru")
        ny = wikipedia.page(text)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break

        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2

    except Exception as e:
        return 'В энциклопедии нет информации об этом'


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)