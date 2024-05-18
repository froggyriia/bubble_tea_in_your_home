from __future__ import annotations

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import text_stuff
from env import token, admin_name
import keyboard as kb
import text_stuff as ts
bot = Bot(token=token)
dp = Dispatcher()

customerMode = False



class BotStates(StatesGroup):
    """Хранит все возможные стейты пользователя в Finite State Machine"""
    add_new_ingredient = State()
    remove_ingredient = State()

class Order:

    __instances__: dict[int, Order] = {}

    def __init__(self, user_name: str, status):
        self.user_name = user_name
        self.ingreds = None
        self.time_slot = None
        self.status = None

#[номер заказа] - имя заказавшего, состав заказа, выбранное время, статус заказа
    @staticmethod
    def create_a_new_order(user_name: str, status = 'new'):
        Order.__instances__[len(Order.__instances__)] = Order(user_name, status= status)
        # return Order.__instances__[len(Order.__instances__) + 1]
        return len(Order.__instances__)


ingredients = list()


def admin_add_ingredient(ingredient: str):
    ingredients.append(ingredient)


def admin_remove_ingredient(ingredient: str):
    ingredients.remove(ingredient)


def get_list_of_ingredients():
    return ingredients


@dp.message(CommandStart())
async def cmd_start(message: Message):
    if message.from_user.username == admin_name and not customerMode:
        await message.answer(ts.greeting_for_admin, reply_markup=kb.admin_starting_keyboard_markup)
    else:
        await message.answer(ts.greeting_message_for_user, reply_markup=kb.user_starting_keyboard_markup)


@dp.message(F.text == 'Сделать заказ')
async def make_an_order(message: Message):
    order_number = Order.create_a_new_order(message.from_user.username)
    await message.answer(text_stuff.make_an_order_instruction + f'\nНомер вашего заказа: {order_number}',
                         reply_markup=kb.user_making_order_keyboard_markup)


@dp.message(F.text == 'Выбрать ингредиенты')
async def choose_ingredients(message: Message):
    if ingredients:
        await message.answer('\n'.join([str(x) for x in get_list_of_ingredients()]),
                             reply_markup=kb.update_ingredients_user_keyboard(ingredients))
    else:
        await message.answer('к сожалению список пуст свяжитесь с администратором')


@dp.message(F.text == 'Выбрать временной слот')
async def choose_time_slot(message: Message):
    await message.answer('pipi')


@dp.message(F.text == 'Связаться с администратором')
async def contact_admin(message: Message):
    await message.answer('kaka')


@dp.message(F.text == 'Отмена заказа')
async def contact_admin(message: Message):
    await message.answer('sam kaka')


@dp.message(F.text == 'Подробнее о кафе')
async def get_more_info(message: Message):
    await message.answer(text_stuff.additional_info)


@dp.message(F.text == 'Редактировать ингредиенты')
async def _(message: Message, state: FSMContext):
    await message.answer('режим изменения ингредиентов')
    await state.set_state(BotStates.add_new_ingredient)


@dp.message(F.text == 'Готово')
async def _(message: Message, state: FSMContext):
    await message.answer(f'список ингредиентов: {ingredients}')
    await state.set_state(None)


@dp.message(BotStates.add_new_ingredient)
async def _(message: Message, state: FSMContext):
    admin_add_ingredient(message.text)
    # await message.answer(f'список ингредиентов: {ingredients}')

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())