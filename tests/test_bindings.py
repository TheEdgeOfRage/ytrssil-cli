from ytrssil.bindings import setup_dependencies
from ytrssil.config import Configuration
from ytrssil.fetch import Fetcher, AioHttpFetcher
from ytrssil.parse import Parser, FeedparserParser
from ytrssil.repository import ChannelRepository, SqliteChannelRepository


def test_setup_dependencies() -> None:
    injector = setup_dependencies()
    config = injector.get_instance(Configuration)
    assert isinstance(config, Configuration)
    assert isinstance(
        injector.get_instance(ChannelRepository),
        SqliteChannelRepository,
    )
    assert isinstance(injector.get_instance(Fetcher), AioHttpFetcher)
    assert isinstance(injector.get_instance(Parser), FeedparserParser)
