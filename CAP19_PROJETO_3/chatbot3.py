import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()

async def main() -> None:
    stream = await client.completions.create(
        model="gpt-3.5-turbo",
        prompt="Say this is a test",
        stream=True,
        max_tokens=10,
    )

    async for completion in stream:
        print(completion.choices[0].text, end="")

    print()

asyncio.run(main())