from __future__ import annotations
from collections.abc import Iterable

from aioresponses import aioresponses

from tests.constants import FEED_XML, TEST_CHANNEL_DATA, TEST_VIDEO_DATA
from ytrssil.config import Configuration
from ytrssil.datatypes import Channel, Video
from ytrssil.fetch import AioHttpFetcher, Fetcher


def test_fetch_new_videos():
    class MockFetcher(Fetcher):
        def fetch_feeds(self, urls: Iterable[str]) -> Iterable[str]:
            return [FEED_XML]

    fetcher = MockFetcher()
    channel = Channel.from_dict(TEST_CHANNEL_DATA)
    video = Video.from_dict(TEST_VIDEO_DATA)
    channel.add_video(video)
    channels, new_videos = fetcher.fetch_new_videos(
        config=Configuration(
            feed_url_getter_type='static',
            feed_urls=[''],
        ),
        parser=lambda _: channel,
    )

    assert channels[channel.channel_id] == channel
    assert new_videos[TEST_VIDEO_DATA['video_id']] == video


def test_aiohttpfetcher_fetch_feeds():
    feed_url = 'test_url'
    with aioresponses() as mocked:
        mocked.get(
            url=feed_url,
            body=FEED_XML,
        )
        fetcher = AioHttpFetcher()
        xml = fetcher.fetch_feeds([feed_url])

        assert xml == [FEED_XML]
