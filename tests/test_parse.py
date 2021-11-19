from unittest import TestCase
from unittest.mock import Mock

from inject import Binder, clear_and_configure

from tests.constants import FEED_XML, TEST_CHANNEL_DATA, TEST_VIDEO_DATA
from ytrssil.config import Configuration
from ytrssil.datatypes import Channel, Video
from ytrssil.exceptions import ChannelNotFound
from ytrssil.parse import FeedparserParser, create_feed_parser
from ytrssil.protocols import ChannelRepository


def test_feedparser_channel_exists() -> None:
    channel = Channel.from_dict(TEST_CHANNEL_DATA)
    mock_repo = Mock()
    mock_repo.get_channel.return_value = channel
    parser = FeedparserParser(channel_repository=mock_repo)

    assert parser(FEED_XML) == channel


def test_feedparser_new_channel() -> None:
    channel = Channel.from_dict(TEST_CHANNEL_DATA)
    channel.add_video(Video.from_dict(TEST_VIDEO_DATA))
    mock_repo = Mock()
    mock_repo.get_channel.side_effect = ChannelNotFound()
    parser = FeedparserParser(channel_repository=mock_repo)

    assert parser(FEED_XML) == channel


class TestCreateParser(TestCase):
    def setUp(self) -> None:
        clear_and_configure(self.inject)

    def inject(self, binder: Binder) -> None:
        binder.bind(ChannelRepository, Mock())

    def test_create_feedparser_parser(self) -> None:
        parser = create_feed_parser(Configuration(parser_type='feedparser'))
        self.assertIsInstance(parser, FeedparserParser)

    def test_fail_create_parser(self) -> None:
        with self.assertRaises(Exception) as e:
            create_feed_parser(Configuration(parser_type='fail'))
            self.assertEqual('Unknown feed parser type: "fail"', e.exception)
