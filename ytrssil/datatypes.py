from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Video:
    video_id: str
    name: str
    url: str
    timestamp: datetime
    channel_id: str
    channel_name: str

    def __str__(self) -> str:
        return f'{self.channel_name} - {self.name} - {self.video_id}'


@dataclass
class Channel:
    channel_id: str
    name: str
    url: str
    new_videos: dict[str, Video] = field(default_factory=lambda: dict())
    watched_videos: dict[str, Video] = field(default_factory=lambda: dict())

    def add_video(self, video: Video) -> None:
        if video.video_id in self.watched_videos:
            return

        self.new_videos[video.video_id] = video

    def remove_old_videos(self) -> None:
        vid_list: list[Video] = sorted(
            self.watched_videos.values(),
            key=lambda x: x.timestamp,
        )
        for video in vid_list[15:]:
            self.watched_videos.pop(video.video_id)

    def mark_video_as_watched(self, video: Video) -> None:
        self.new_videos.pop(video.video_id)
        self.watched_videos[video.video_id] = video
        self.remove_old_videos()