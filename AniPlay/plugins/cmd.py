from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN
from AniPlay.plugins.stats import day, over


@app.on_message(filters.command(['start', 'ping', 'help', 'alive']))
async def start(_, message: Message):
    try:
        await message.reply_text('#JaiShreeRam🚩,\nI‘m **ANIME SEARCH BOT** Created by- **@StupidBoi69**.\n\n**NOTE:** To Get Started, Simply Use\n(**"/s" or "/search"**)\nThen [**TYPE THE NAME OF ANIME**] You‘re Looking For And We‘ll Search Our Database to Find it For You.\n\n(**HINT:** Choose Server5 for Downloading.)\n\n╔══════════════════════╗\n┣**SEARCH ANIME LIKE THIS-**\n┃/s One Piece ✅\n┃/search Naruto ✅\n┃\n┣**DON‘T SEARCH LIKE THIS -**\n┃/s One Piece Episode 69 ❎\n┃/s Bleach English Dub ❎\n╚══════════════════════╝\n\n@AnimeDownloaderChat_Bot.')
    except:
        return


QUERY = '**Search Results:** `{}`'


@app.on_message(filters.command(['search', 's', 'giveme', 'animename']))
async def searchCMD(_, message: Message):
    try:
        user = message.from_user.id
        query = ' '.join(message.command[1:])
        if query == '':
            return await message.reply_text('Give me something to search ^_^')
        data = AnimeDex.search(query)
        button = BTN.searchCMD(user, data, query)
        await message.reply_text(QUERY.format(query), reply_markup=button)
    except Exception as e:
        try:
            return await message.reply_text('**Anime Not Found...**\n\nProbably Incorrect Name, Try again')
        except:
            return


@app.on_message(filters.command('stats'))
async def stats(_, message: Message):
    try:
        await message.reply_text('Use /stats1 For Day Wise Stats\nAnd /stats2 For Overall Stats')
    except:
        return


@app.on_message(filters.command('stats1'))
async def stats1(_, message: Message):
    try:
        img = day()
        await message.reply_photo(img, caption='**AnimeDex | Day Wise Stats**')
    except:
        return


@app.on_message(filters.command('stats2'))
async def stats2(_, message: Message):
    try:
        img = over()
        await message.reply_photo(img, caption='**AnimeDex | Overall Stats**')
    except:
        return
