import asyncio
import time
from kasa import SmartPlug

async def main():
    p = SmartPlug("192.168.137.212")
    while True:
        await p.update()
        print(p.emeter_realtime["power"])
        time.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())