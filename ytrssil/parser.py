from datetime import datetime

import feedparser

from ytrssil.datatypes import Channel, Video
from ytrssil.repository import ChannelNotFound, ChannelRepository


class Parser:
    def __init__(self, channel_repository: ChannelRepository) -> None:
        self.repository = channel_repository

    def __call__(self, feed_content: str) -> Channel:
        d = feedparser.parse(feed_content)
        channel_id: str = d['feed']['yt_channelid']
        try:
            channel = self.repository.get_channel(channel_id)
        except ChannelNotFound:
            channel = Channel(
                channel_id=channel_id,
                name=d['feed']['title'],
                url=d['feed']['link'],
            )
            self.repository.update_channel(channel)

        for entry in d['entries']:
            channel.add_video(Video(
                video_id=entry['yt_videoid'],
                name=entry['title'],
                url=entry['link'],
                timestamp=datetime.fromisoformat(entry['published']),
                channel_id=channel.channel_id,
                channel_name=channel.name,
            ))

        self.repository.update_channel(channel)
        return channel
