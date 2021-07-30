from __future__ import annotations
import os
import shelve

from ytrssil.constants import config_dir
from ytrssil.datatypes import Channel


class ChannelNotFound(Exception):
    pass


class ChannelRepository:
    def __init__(self) -> None:
        os.makedirs(config_dir, exist_ok=True)
        self.file_path: str = os.path.join(config_dir, 'shelf')

    def __enter__(self) -> ChannelRepository:
        self.repository = shelve.open(self.file_path)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.repository.close()

    def get_channel(self, channel_id: str) -> Channel:
        try:
            return self.repository[channel_id]
        except KeyError as e:
            raise ChannelNotFound(e)

    def update_channel(self, channel: Channel) -> None:
        self.repository[channel.channel_id] = channel
