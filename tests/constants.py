from datetime import datetime

from ytrssil.datatypes import ChannelData, VideoData

FEED_XML: str = '''
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns:yt="http://www.youtube.com/xml/schemas/2015">
 <yt:channelId>channel_id</yt:channelId>
 <title>channel_name</title>
 <entry>
  <yt:videoId>video_id</yt:videoId>
  <yt:channelId>channel_id</yt:channelId>
  <title>video_name</title>
  <link rel="alternate" href="https://www.youtube.com/watch?v=video_id"/>
  <published>1970-01-01T00:00:00+00:00</published>
 </entry>
</feed>
'''

TEST_VIDEO_DATA: VideoData = {
    'video_id': 'video_id',
    'name': 'video_name',
    'url': 'https://www.youtube.com/watch?v=video_id',
    'channel_id': 'channel_id',
    'channel_name': 'channel_name',
    'timestamp': datetime.fromisoformat('1970-01-01T00:00:00+00:00'),
    'watch_timestamp': None,
}
TEST_CHANNEL_DATA: ChannelData = {
    'channel_id': 'channel_id',
    'name': 'channel_name',
    'new_videos': {},
    'watched_videos': {},
}
