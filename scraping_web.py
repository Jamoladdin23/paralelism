import asyncio
import aiohttp

async def fetch_url(url, keyword):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
                if keyword in html:
                    print(f"Keyword '{keyword}' found on {url}")
                else:
                    print(f"Keyword '{keyword}' not found on {url}")
    except Exception as e:
        print(f"Error occurred while fetching {url}: {e}")

async def main(urls, keyword):
    tasks = [fetch_url(url, keyword) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        'https://www.apple.com',
        'https://www.samsung.com',
        'https://www.hp.com'
    ]
    keyword = "hello"

    asyncio.run(main(urls, keyword))
