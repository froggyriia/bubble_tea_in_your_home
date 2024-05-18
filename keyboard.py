from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from main import ingredients
from aiogram.utils.callback_answer import CallbackAnswer


'''user keyboard section'''
make_an_order = KeyboardButton(text='Сделать заказ')
cancel_button = KeyboardButton(text='Отмена')
choose_ingredients = KeyboardButton(text='Выбрать ингредиенты')
choose_time_slot = KeyboardButton(text='Выбрать временной слот')
connect_to_admin = KeyboardButton(text='Связаться с администратором')
get_more_info = KeyboardButton(text='Подробнее о кафе')
show_order = KeyboardButton(text='Показать заказ')
confirm_order = KeyboardButton(text='Отправить заказ')

user_starting_keyboard = [[make_an_order], [connect_to_admin, get_more_info]]
user_starting_keyboard_markup = ReplyKeyboardMarkup(keyboard=user_starting_keyboard, resize_keyboard=True)
user_making_order_keyboard = [[choose_ingredients], [choose_time_slot], [cancel_button, connect_to_admin]]
user_making_order_keyboard_markup = ReplyKeyboardMarkup(keyboard=user_making_order_keyboard, resize_keyboard=True)


'''admin keyboard section'''
edit_ingredients = KeyboardButton(text='Редактировать ингредиенты')
edit_time_slot = KeyboardButton(text='Редактировать расписание')
contact_customer = KeyboardButton(text='Связаться с клиентом')
post_an_announcement = KeyboardButton(text='Сделать объявление')
done_editing = KeyboardButton(text='Готово')

admin_starting_keyboard = [[edit_ingredients], [edit_time_slot], [contact_customer, post_an_announcement], [done_editing]]
admin_starting_keyboard_markup = ReplyKeyboardMarkup(keyboard=admin_starting_keyboard, resize_keyboard=True)

available_ingredients = InlineKeyboardButton(text='доступные ингредиенты', callback_data='available_ingredients')
inline_buttons = [[available_ingredients]]
inline_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_buttons)
user_choosing_specific_ingredients_keyboard_markup = None
def update_ingredients_user_keyboard(ingredients: list):
    choose_specific_ingredients = []
    for ingr in ingredients:
        choose_specific_ingredients.append([KeyboardButton(text=ingr)])
    return ReplyKeyboardMarkup(keyboard=choose_specific_ingredients, resize_keyboard=True)
