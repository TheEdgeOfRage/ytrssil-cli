from datetime import datetime
from unittest.mock import MagicMock

from pytest_mock import MockerFixture

from tests.constants import TEST_CHANNEL_DATA, TEST_VIDEO_DATA
from ytrssil import cli
from ytrssil.datatypes import Channel, Video


def test_user_query(mocker: MockerFixture) -> None:
    def mock_query(input: bytes) -> tuple[bytes, bytes]:
        videos = input.decode('UTF-8').split('\n')
        return (videos[0].encode('UTF-8'), b'')

    popen_mock: MagicMock = mocker.patch.object(cli, 'Popen')
    attrs = {'communicate': mock_query}
    communicate_mock = mocker.MagicMock()
    communicate_mock.configure_mock(**attrs)

    popen_mock.return_value = communicate_mock
    videos = {
        f'video_id_{i}': Video(
            video_id=f'video_id_{i}',
            name='video',
            url='url',
            timestamp=datetime.utcnow(),
            channel_id='channel_id',
            channel_name='channel',
        )
        for i in range(2)
    }

    ret = cli.user_query(videos=videos)
    assert ret == [videos['video_id_0']]


def test_watch_videos(mocker: MockerFixture) -> None:
    repository_mock = mocker.MagicMock()
    update_video = mocker.MagicMock()
    repository_mock.__enter__.return_value.update_video = update_video
    fetcher_mock = mocker.MagicMock()
    channel = Channel.from_dict(TEST_CHANNEL_DATA)
    video = Video.from_dict(TEST_VIDEO_DATA)
    channel.add_video(video)
    fetcher_mock.fetch_new_videos.return_value = (
        {channel.channel_id: channel},
        {video.video_id: video},
    )
    query_mock = mocker.patch.object(cli, 'user_query')
    query_mock.return_value = [video]
    fork_mock = mocker.patch.object(cli, 'fork')
    cli.watch_videos(repository_manager=repository_mock, fetcher=fetcher_mock)
    fork_mock.assert_called_once()
    update_video.assert_called_once()  # repository is a context manager


def test_main_no_arg(mocker: MockerFixture) -> None:
    mock = mocker.patch.object(cli, 'watch_videos')
    cli.main(['ytrssil'])

    assert mock.called_once


def test_main_watch_videos(mocker: MockerFixture) -> None:
    mock = mocker.patch.object(cli, 'watch_videos')
    cli.main(['ytrssil', 'watch_videos'])

    assert mock.called_once


def test_main_history(mocker: MockerFixture) -> None:
    mock = mocker.patch.object(cli, 'watch_history')
    cli.main(['ytrssil', 'history'])

    assert mock.called_once


def test_main_mark(mocker: MockerFixture) -> None:
    mock = mocker.patch.object(cli, 'mark_as_watched')
    cli.main(['ytrssil', 'mark', datetime.utcnow().isoformat()])

    assert mock.called_once
