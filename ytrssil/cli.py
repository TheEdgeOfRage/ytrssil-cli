from os import execv, fork
from sys import stderr

from ytrssil.constants import mpv_options
from ytrssil.repository import ChannelRepository
from ytrssil.fetch import fetch_new_videos
from ytrssil.query import query


def main() -> int:
    with ChannelRepository() as repository:
        channels, new_videos = fetch_new_videos(repository)

        selected_videos = query(new_videos)
        if not selected_videos:
            print('No video selected', file=stderr)
            return 1

        video_urls = [video.url for video in selected_videos]
        cmd = ['/usr/bin/mpv', *mpv_options, *video_urls]
        if (fork() == 0):
            execv(cmd[0], cmd)

        for video in selected_videos:
            selected_channel = channels[video.channel_id]
            selected_channel.mark_video_as_watched(video)
            repository.update_channel(selected_channel)

    return 0


if __name__ == '__main__':
    main()
