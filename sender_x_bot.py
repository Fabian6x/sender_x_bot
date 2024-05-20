from telegram import Bot
from asyncio import run
import inspect
class CustomBot(Bot):
    token='925207790:AAFACRkU3fSScjxaEoZRUVHF0cgDh3TGE7Y'
    chat_id=267811391
    def __init__(self,**kwargs):
        print('Bot initialized')
    def __str__(self):
        return f'Bot information:\n - Token  : '+self.token + '\n - Chat_id: ' +str(self.chat_id)

def bot_method_decorator(orig_func):
    def decorator(*args, **kwargs):
        async def interior(*args,**kwargs):
            kwargs['chat_id']=args[0].chat_id
            async with Bot(token=args[0].token) as bot:
                return await getattr(bot, orig_func.__name__)(**kwargs)
        return run(interior(*args,**kwargs))
    return decorator
# Apply the decorator to all bot methods except dunder methods
for name, fn in inspect.getmembers(CustomBot,inspect.isfunction):
    if not name.startswith('__'):
        setattr(CustomBot, name, bot_method_decorator(fn))


def main() -> None:
    MyBot=CustomBot()
    MyBot.send_message(text='holi12')

if __name__ == "__main__":
    main()
