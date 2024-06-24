from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from .keyboards import PLAY

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
router = Router()
TELEGRAM_BOT_TOKEN = "7404403100:AAHxn7iAEN-g8LzpZFOqTCW1Z_KEsEO3kwQ"
bot = Bot(token=TELEGRAM_BOT_TOKEN)
GREATING = """We are thrilled to announce the launch of our highly anticipated $BLAZE Tap to Earn Airdrop! Starting on July 1st, participants will have the exciting opportunity to earn $BLAZE tokens directly through our Telegram web app.

Key Dates:

Airdrop Start Date: July 1, 2024
Airdrop End Date: November 15, 2024
How to Participate:
Join our Telegram Group: Follow the link to join our official Telegram group.
Access the Web App: Use the provided link in the group to access the $BLAZE web app.
Start Tapping: Tap daily within the web app to earn $BLAZE tokens directly to your wallet.
Highlights:
Easy Earnings: Simple tap actions will accumulate $BLAZE tokens.
Daily Rewards: Earn rewards every day by participating.
Limited Time Offer: Make the most of this opportunity before it ends on November 15.
Don't miss out on your chance to be a part of the $BLAZE community and earn rewards effortlessly. Mark your calendars and get ready to tap, earn, and enjoy!

Stay tuned for more updates and instructions on our official Telegram group. For any queries, reach out to our support team.

Get ready to ignite your earnings with $BLAZE!

Join our communities: 
Telegram [https://t.me/blazetoken_Community] $BLAZE Community
X []"""

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(GREATING, reply_markup=PLAY)