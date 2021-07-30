import aiohttp

ACCESS_KEY = '<ACCESS_KEY>'


async def get_rates(session: aiohttp.ClientSession, base: str):
    async with session.get(
        f"http://api.exchangeratesapi.io/latest?access_key={ACCESS_KEY}&base={base}"
    ) as response:
        rates = (await response.json())['rates']
        rates[base] = 1.

        return base, rates
