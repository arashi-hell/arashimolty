import asyncio
from bot.api_client import MoltyAPI
from bot.credentials import get_api_key

async def main():
    api = MoltyAPI(get_api_key())
    
    result = await api.get_version()
    print("SERVER VERSION:", result)

    await api.close()

asyncio.run(main())
