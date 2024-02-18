from binance import AsyncClient, BinanceSocketManager
import asyncio

async def btc_price_stream():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    async with bm.trade_socket('BTCUSDT') as stream:
        while True:
            res = await stream.recv()
            print(f"BTC/USDT Price Update: {res['p']}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(btc_price_stream())
