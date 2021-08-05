from datetime import datetime

from tests.constants import TEST_CHANNEL_DATA, TEST_VIDEO_DATA
from ytrssil.datatypes import Channel, Video


def test_video_str() -> None:
    string = str(Video.from_dict(TEST_VIDEO_DATA))

    assert string == 'channel_name - video_name - video_id'


def test_channel_str() -> None:
    channel = Channel.from_dict({
        **TEST_CHANNEL_DATA,
        'new_videos': {
            'video_id': Video(
                video_id='video_id',
                name='video_name',
                url='https://www.youtube.com/watch?v=video_id',
                channel_id='channel_id',
                channel_name='channel_name',
                timestamp=datetime.fromisoformat('1970-01-01T00:00:00+00:00'),
                watch_timestamp=None,
            ),
        },
    })
    string = str(channel)

    assert string == 'channel_name - 1'


def test_channel_add_new_video() -> None:
    channel = Channel.from_dict(TEST_CHANNEL_DATA)
    added_video = channel.add_video(Video(
        video_id='video_id',
        name='video_name',
        url='https://www.youtube.com/watch?v=video_id',
        channel_id='channel_id',
        channel_name='channel_name',
        timestamp=datetime.fromisoformat('1970-01-01T00:00:00+00:00'),
        watch_timestamp=None,
    ))

    assert added_video
    assert list(channel.new_videos.keys()) == ['video_id']


def test_channel_add_existing_video() -> None:
    channel = Channel.from_dict({
        **TEST_CHANNEL_DATA,
        'new_videos': {
            'video_id': Video(
                video_id='video_id',
                name='video_name',
                url='https://www.youtube.com/watch?v=video_id',
                channel_id='channel_id',
                channel_name='channel_name',
                timestamp=datetime.fromisoformat('1970-01-01T00:00:00+00:00'),
                watch_timestamp=None,
            ),
        },
    })
    added_video = channel.add_video(Video(
        video_id='video_id',
        name='video_name',
        url='https://www.youtube.com/watch?v=video_id',
        channel_id='channel_id',
        channel_name='channel_name',
        timestamp=datetime.fromisoformat('1970-01-01T00:00:00+00:00'),
        watch_timestamp=None,
    ))

    assert not added_video
    assert list(channel.new_videos.keys()) == ['video_id']


def test_channel_mark_video_as_watched() -> None:
    video = Video(
        video_id='video_id',
        name='video_name',
        url='https://www.youtube.com/watch?v=video_id',
        channel_id='channel_id',
        channel_name='channel_name',
        timestamp=datetime.fromisoformat('1970-01-01T00:00:00+00:00'),
        watch_timestamp=None,
    )
    channel = Channel.from_dict({
        **TEST_CHANNEL_DATA,
        'new_videos': {'video_id': video},
    })

    channel.mark_video_as_watched(video)

    assert list(channel.new_videos.keys()) == []
    assert list(channel.watched_videos.keys()) == ['video_id']
