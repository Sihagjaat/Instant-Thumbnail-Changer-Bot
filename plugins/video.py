# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
from aiogram import Router, types, F, Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
from database import get_thumbnail, increment_usage, is_banned, add_user
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
router = Router()
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat

def small_caps(text: str) -> str:
    """Convert text to small caps unicode."""
    normal = "abcdefghijklmnopqrstuvwxyz"
    small = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"
    result = ""
    for char in text:
        if char.lower() in normal:
            idx = normal.index(char.lower())
            result += small[idx]
        else:
            result += char
    return result
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat

@router.message(F.video)
async def handle_video(message: types.Message, bot: Bot):
    """Handle incoming video and send it back with user's thumbnail as cover."""
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    
    # Check if banned
    if await is_banned(user_id):
        await message.answer(small_caps("You are banned from using this bot."))
        return
    
    # Add/update user
    await add_user(user_id, username, first_name)
    
    video = message.video
    
    # Keep ORIGINAL caption - no modification
    caption = message.caption or ""
    
    # Get user's thumbnail
    thumb_file_id = await get_thumbnail(user_id)
    
    # Build keyboard
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⚙️ Settings", callback_data="settings")]
    ])
    
    if thumb_file_id:
        # Increment usage count
        await increment_usage(user_id)
        
        # Send video with custom cover
        await bot.send_video(
            chat_id=message.chat.id,
            video=video.file_id,
            caption=caption,
            cover=thumb_file_id,
            reply_markup=keyboard
        )
    else:
        # No thumbnail set - send warning
        await message.answer(
            f"<b>⚠️ {small_caps('No thumbnail set!')}</b>\n\n"
            f"<blockquote>{small_caps('Please set a thumbnail first using Settings.')}</blockquote>",
            parse_mode="HTML",
            reply_markup=keyboard
        )
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat