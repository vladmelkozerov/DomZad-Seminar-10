import game
from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
         
        await message.answer(f'Привет, {message.from_user.full_name}'
                             f'Мы будем играть в конфеты. Бери от 1 до 28...')
        my_game = [message.from_user.id, message.from_user.first_name, game.max_total]
        game.total.append(my_game)

@dp.message_handler(commands=['set'])
async def mes_start(message: Message):
    game.max_total = int(message.text.split()[1])
    await message.answer(f'Игрок {message.from_user.first_name} установил исходное количество конфет в размере {game.max_total}')