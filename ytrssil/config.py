import os
from collections.abc import Iterator

from ytrssil.constants import config_dir


def get_feed_urls() -> Iterator[str]:
    file_path = os.path.join(config_dir, 'feeds')
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
