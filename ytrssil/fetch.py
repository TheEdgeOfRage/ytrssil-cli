from asyncio import gather, run
from collections.abc import Iterable

from aiohttp import ClientResponse, ClientSession

from ytrssil.config import get_feed_urls
from ytrssil.datatypes import Channel, Video
from ytrssil.repository import ChannelRepository
from ytrssil.parser import Parser


async def request(session: ClientSession, url: str) -> ClientResponse:
    return await session.request(method='GET', url=url)


async def fetch_feeds(urls: Iterable[str]) -> Iterable[str]:
    async with ClientSession() as session:
        responses: list[ClientResponse] = await gather(*[
            request(session, url) for url in urls
        ])
        return [
            await response.text(encoding='UTF-8')
            for response in responses
        ]


def fetch_new_videos(
    repository: ChannelRepository,
) -> tuple[dict[str, Channel], dict[str, Video]]:
    feed_urls = get_feed_urls()
    parser = Parser(repository)
    channels: dict[str, Channel] = {}
    new_videos: dict[str, Video] = {}
    for feed in run(fetch_feeds(feed_urls)):
        channel = parser(feed)
        channels[channel.channel_id] = channel
        new_videos.update(channel.new_videos)

    return channels, new_videos