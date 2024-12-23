import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем экземпляр бота
bot = Bot(token=' ')
dp = Dispatcher()

# Создаем клавиатуру с кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="До 1 миллиона рублей")],
        [KeyboardButton(text="До 1.5 миллиона рублей")],
        [KeyboardButton(text="До 2 миллионов рублей")],
        [KeyboardButton(text="До 3 миллионов рублей")],
        [KeyboardButton(text="До 3.5 миллионов рублей")],
        [KeyboardButton(text="До 4 миллионов рублей")],
        [KeyboardButton(text="До 4.5 миллионов рублей")],
        [KeyboardButton(text="До 5 миллионов рублей")],
        [KeyboardButton(text="До 6 миллионов рублей")],
        [KeyboardButton(text="До 7 миллионов рублей")],
        [KeyboardButton(text="До 8 миллионов рублей")],
        [KeyboardButton(text="До 9 миллионов рублей")],
        [KeyboardButton(text="До 10 миллионов рублей")],
        [KeyboardButton(text="До 20 миллионов рублей")],
        [KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)

# Функция для обработки команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я справочник по подбору автомобилей. Выберите диапазон цен или введите сумму числом:", reply_markup=keyboard)

# Функция для обработки команды /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "Вы можете выбрать один из диапазонов цен, нажав на соответствующую кнопку:\n"
        "- До 1 миллиона рублей\n"
        "- До 1.5 миллиона рублей\n"
        "- До 2 миллионов рублей\n"
        "- До 3 миллионов рублей\n"
        "- До 3.5 миллионов рублей\n"
        "- До 4 миллионов рублей\n"
        "- До 4.5 миллионов рублей\n"
        "- До 5 миллионов рублей\n"
        "- До 6 миллионов рублей\n"
        "- До 7 миллионов рублей\n"
        "- До 8 миллионов рублей\n"
        "- До 9 миллионов рублей\n"
        "- До 10 миллионов рублей\n"
        "- До 20 миллионов рублей\n\n"
        "Или введите число, соответствующее вашему бюджету.\n\n"
    )
    await message.reply(help_text)

# Функция для обработки нажатий на кнопки
@dp.message(lambda message: message.text in [
    "До 1 миллиона рублей", "До 1.5 миллиона рублей", "До 2 миллионов рублей", "До 3 миллионов рублей", "До 3.5 миллионов рублей",
    "До 4 миллионов рублей", "До 4.5 миллионов рублей", "До 5 миллионов рублей",
    "До 6 миллионов рублей", "До 7 миллионов рублей", "До 7.5 миллионов рублей",
    "До 8 миллионов рублей", "До 8.5 миллионов рублей", "До 9 миллионов рублей",
    "До 10 миллионов рублей", "До 20 миллионов рублей"
])
async def process_button(message: types.Message):
        if message.text == "До 1 миллиона рублей":
            await message.reply("Вот ссылки на автомобили до 1 миллиона рублей: https://auto.ru/catalog/cars/honda/civic/2306765/2306777/, https://auto.ru/catalog/cars/chevrolet/cruze/8538371/8538412/,")
        elif message.text == "До 1.5 миллиона рублей":
            await message.reply("Вот ссылки на автомобили до 1.5 миллиона рублей: https://auto.ru/catalog/cars/toyota/camry/7722388/7722389/, https://auto.ru/catalog/cars/audi/a4/2323576/2323599/")
        elif message.text == "До 2 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 2 миллионов рублей: https://auto.ru/catalog/cars/volkswagen/passat/20232305/20232338/, https://auto.ru/catalog/cars/kia/optima/21342050/21342121/, https://auto.ru/catalog/cars/mazda/6/20435551/20435559/")
        elif message.text == "До 3 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 3 миллионов рублей: https://auto.ru/catalog/cars/bmw/3er/21398591/21398651/, https://auto.ru/catalog/cars/volvo/s60/21320062/21320121/")
        elif message.text == "До 3.5 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 3.5 миллионов рублей: https://auto.ru/catalog/cars/mercedes/c_klasse/22779665/22780010/, https://auto.ru/catalog/cars/genesis/g70/22939107/22939153/")
        elif message.text == "До 4 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 4 миллионов рублей: https://auto.ru/catalog/cars/bmw/5er/22212692/22213464/, https://auto.ru/catalog/cars/mercedes/e_klasse/22284156/22284200/")
        elif message.text == "До 4.5 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 4.5 миллионов рублей: https://auto.ru/catalog/cars/audi/a6/21210593/21210635/, https://auto.ru/catalog/cars/audi/a8/21040120/21040166/ ")
        elif message.text == "До 5 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 5 миллионов рублей: https://auto.ru/catalog/cars/jeep/grand_cherokee/20040921/20040933/, https://auto.ru/catalog/cars/volkswagen/teramont/23777686/23777856/")
        elif message.text == "До 6 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 6 миллионов рублей: https://auto.ru/catalog/cars/cadillac/ct5/21655319/21655371/?complectation_id=21655371__21655500&only-content=true, https://auto.ru/catalog/cars/bmw/m4/21783528/21783585/")
        elif message.text == "До 7 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 7 миллионов рублей: https://auto.ru/catalog/cars/ford/mustang/23606535/23606663/, https://auto.ru/catalog/cars/bmw/m3/22516760/22516867/?only-content=true")
        elif message.text == "До 8 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 8 миллионов рублей: https://auto.ru/catalog/cars/bmw/x5/21307931/21307996/, https://auto.ru/catalog/cars/dodge/charger/20514921/20514929/")
        elif message.text == "До 9 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 9 миллионов рублей: https://auto.ru/catalog/cars/audi/rs6/20246447/20246455/, https://auto.ru/catalog/cars/bmw/x7/21406086/21406152/?only-content=true")
        elif message.text == "До 10 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 10 миллионов рублей: https://auto.ru/catalog/cars/mercedes/e_klasse/23584850/23584891/, https://auto.ru/catalog/cars/bmw/m5/22361368/22361488/?only-content=true")
        elif message.text == "До 20 миллионов рублей":
            await message.reply("Вот ссылки на автомобили до 20 миллионов рублей: https://auto.ru/catalog/cars/mercedes/g_klasse_amg/21203440/21203483/?complectation_id=21203483_21217612_21203530&only-content=true, https://auto.ru/catalog/cars/audi/rs7/21718520/21718571/?only-content=true, https://auto.ru/catalog/cars/mercedes/e_klasse_amg/22298932/22348747/, https://auto.ru/catalog/cars/bmw/m8/21578636/21578720/?only-content=true, https://auto.ru/catalog/cars/audi/rs_q8/21757239/21757302/?only-content=true, https://auto.ru/catalog/cars/bmw/x5_m/21679476/21679551/?only-content=true")

# Функция для обработки числового ввода
@dp.message(lambda message: message.text.isdigit())
async def process_numeric_input(message: types.Message):
    budget = int(message.text)
    if budget <= 1000000:
        await message.reply("Вот ссылки на автомобили до 1 миллиона рублей: https://auto.ru/catalog/cars/honda/civic/2306765/2306777/, https://auto.ru/catalog/cars/chevrolet/cruze/8538371/8538412/")
    elif budget <= 1500000:
        await message.reply("Вот ссылки на автомобили до 1.5 миллиона рублей: https://auto.ru/catalog/cars/toyota/camry/7722388/7722389/, https://auto.ru/catalog/cars/audi/a4/2323576/2323599/")
    elif budget <= 2000000:
        await message.reply("Вот ссылки на автомобили до 2 миллионов рублей: https://auto.ru/catalog/cars/volkswagen/passat/20232305/20232338/, https://auto.ru/catalog/cars/kia/optima/21342050/21342121/, https://auto.ru/catalog/cars/mazda/6/20435551/20435559/")
    elif budget <= 3000000:
        await message.reply("Вот ссылки на автомобили до 3 миллионов рублей: https://auto.ru/catalog/cars/bmw/3er/21398591/21398651/, https://auto.ru/catalog/cars/volvo/s60/21320062/21320121/")
    elif budget <= 3500000:
        await message.reply("Вот ссылки на автомобили до 3.5 миллионов рублей: https://auto.ru/catalog/cars/mercedes/c_klasse/22779665/22780010/, https://auto.ru/catalog/cars/genesis/g70/22939107/22939153/")
    elif budget <= 4000000:
        await message.reply("Вот ссылки на автомобили до 4 миллионов рублей: https://auto.ru/catalog/cars/bmw/5er/22212692/22213464/, https://auto.ru/catalog/cars/mercedes/e_klasse/22284156/22284200/")
    elif budget <= 4500000:
        await message.reply("Вот ссылки на автомобили до 4.5 миллионов рублей: https://auto.ru/catalog/cars/audi/a6/21210593/21210635/, https://auto.ru/catalog/cars/audi/a8/21040120/21040166/ ")
    elif budget <= 5000000:
        await message.reply("Вот ссылки на автомобили до 5 миллионов рублей: https://auto.ru/catalog/cars/jeep/grand_cherokee/20040921/20040933/, https://auto.ru/catalog/cars/volkswagen/teramont/23777686/23777856/")
    elif budget <= 6000000:
        await message.reply("Вот ссылки на автомобили до 6 миллионов рублей: https://auto.ru/catalog/cars/cadillac/ct5/21655319/21655371/?complectation_id=21655371__21655500&only-content=true, https://auto.ru/catalog/cars/bmw/m4/21783528/21783585/")
    elif budget <= 7000000:
        await message.reply("Вот ссылки на автомобили до 7 миллионов рублей: https://auto.ru/catalog/cars/ford/mustang/23606535/23606663/, https://auto.ru/catalog/cars/bmw/m3/22516760/22516867/?only-content=true")
    elif budget <= 8000000:
        await message.reply("Вот ссылки на автомобили до 8 миллионов рублей: https://auto.ru/catalog/cars/bmw/x5/21307931/21307996/, https://auto.ru/catalog/cars/dodge/charger/20514921/20514929/")
    elif budget <= 9000000:
        await message.reply("Вот ссылки на автомобили до 9 миллионов рублей: https://auto.ru/catalog/cars/audi/rs6/20246447/20246455/, https://auto.ru/catalog/cars/bmw/x7/21406086/21406152/?only-content=true")
    elif budget <= 10000000:
        await message.reply("Вот ссылки на автомобили до 10 миллионов рублей: https://auto.ru/catalog/cars/mercedes/e_klasse/23584850/23584891/, https://auto.ru/catalog/cars/bmw/m5/22361368/22361488/?only-content=true")
    elif budget <= 20000000:
        await message.reply("Вот ссылки на автомобили до 20 миллионов рублей: https://auto.ru/catalog/cars/mercedes/g_klasse_amg/21203440/21203483/?complectation_id=21203483_21217612_21203530&only-content=true, https://auto.ru/catalog/cars/audi/rs7/21718520/21718571/?only-content=true, https://auto.ru/catalog/cars/mercedes/e_klasse_amg/22298932/22348747/, https://auto.ru/catalog/cars/bmw/m8/21578636/21578720/?only-content=true, https://auto.ru/catalog/cars/audi/rs_q8/21757239/21757302/?only-content=true, https://auto.ru/catalog/cars/bmw/x5_m/21679476/21679551/?only-content=true")
    else:
        await message.reply("К сожалению, у нас нет информации о автомобилях выше 20 миллионов рублей.")

# Функция для обработки нечислового ввода
@dp.message(lambda message: not message.text.isdigit() and message.text not in ["До 1 миллиона рублей", "До 5 миллионов рублей", "До 10 миллионов рублей", "До 20 миллионов рублей", "Помощь"])
async def process_invalid_input(message: types.Message):
    await message.reply("Пожалуйста, выберите диапазон цен с помощью кнопки или введите корректную цену.")

# Функция для обработки нажатия кнопки "Помощь"
@dp.message(lambda message: message.text == "Помощь")
async def process_help_button(message: types.Message):
    await cmd_help(message)

# Основная функция для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())