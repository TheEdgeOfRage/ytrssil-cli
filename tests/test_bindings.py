from ytrssil.bindings import setup_dependencies
from ytrssil.config import Configuration
from ytrssil.fetch import AioHttpFetcher
from ytrssil.parse import FeedparserParser
from ytrssil.protocols import ChannelRepository, Fetcher, Parser
from ytrssil.repository import SqliteChannelRepository


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
