from loader import dp ,bot
from aiogram.types import ContentType, Message
from pathlib import Path

# download_path = Path().joinpath(*other: "downloads","categories")
download_path=Path().joinpath(*other: "downloads","categories")
download_path.mkdir (parents=True, exist_ok=True)



@dp.message_handler(content_types=ContentType.DOCUMENT)
# @dp.message_handler(content_types='document')
async def doc_handler(message: Message):
    await message.document.download (destination=download_path)
    doc_id =message.document.file_id
    await message.reply("Siz hujjat yubordingiz!\n"
                        f"file_id = {doc_id}")