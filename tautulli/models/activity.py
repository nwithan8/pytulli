# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T01:23:27+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel

from tautulli.internal import utils as internal_utils, static
from tautulli.tools.utils import to_human_bitrate


class Session(BaseModel):
    session_key: Optional[str] = None
    media_type: Optional[str] = None
    view_offset: Optional[str] = None
    progress_percent: Optional[str] = None
    quality_profile: Optional[str] = None
    synced_version_profile: Optional[str] = None
    optimized_version_profile: Optional[str] = None
    user: Optional[str] = None
    channel_stream: Optional[int] = None
    section_id: Optional[str] = None
    library_name: Optional[str] = None
    rating_key: Optional[str] = None
    parent_rating_key: Optional[str] = None
    grandparent_rating_key: Optional[str] = None
    title: Optional[str] = None
    parent_title: Optional[str] = None
    grandparent_title: Optional[str] = None
    original_title: Optional[str] = None
    sort_title: Optional[str] = None
    media_index: Optional[str] = None
    parent_media_index: Optional[str] = None
    studio: Optional[str] = None
    content_rating: Optional[str] = None
    summary: Optional[str] = None
    tagline: Optional[str] = None
    rating: Optional[str] = None
    rating_image: Optional[str] = None
    audience_rating: Optional[str] = None
    audience_rating_image: Optional[str] = None
    user_rating: Optional[str] = None
    duration: Optional[str] = None
    year: Optional[str] = None
    thumb: Optional[str] = None
    parent_thumb: Optional[str] = None
    grandparent_thumb: Optional[str] = None
    art: Optional[str] = None
    banner: Optional[str] = None
    originally_available_at: Optional[str] = None
    added_at: Optional[str] = None
    updated_at: Optional[str] = None
    last_viewed_at: Optional[str] = None
    guid: Optional[str] = None
    parent_guid: Optional[str] = None
    grandparent_guid: Optional[str] = None
    directors: Optional[List] = None
    writers: Optional[List] = None
    actors: Optional[List] = None
    genres: Optional[List[str]] = None
    labels: Optional[List] = None
    collections: Optional[List] = None
    guids: Optional[List] = None
    full_title: Optional[str] = None
    children_count: Optional[int] = None
    live: Optional[int] = None
    id: Optional[str] = None
    container: Optional[str] = None
    bitrate: Optional[str] = None
    height: Optional[str] = None
    width: Optional[str] = None
    aspect_ratio: Optional[str] = None
    video_codec: Optional[str] = None
    video_resolution: Optional[str] = None
    video_full_resolution: Optional[str] = None
    video_framerate: Optional[str] = None
    video_profile: Optional[str] = None
    audio_codec: Optional[str] = None
    audio_channels: Optional[str] = None
    audio_channel_layout: Optional[str] = None
    audio_profile: Optional[str] = None
    optimized_version: Optional[int] = None
    channel_call_sign: Optional[str] = None
    channel_identifier: Optional[str] = None
    channel_thumb: Optional[str] = None
    file: Optional[str] = None
    file_size: Optional[str] = None
    indexes: Optional[int] = None
    selected: Optional[int] = None
    type: Optional[str] = None
    video_codec_level: Optional[str] = None
    video_bitrate: Optional[str] = None
    video_bit_depth: Optional[str] = None
    video_chroma_subsampling: Optional[str] = None
    video_color_primaries: Optional[str] = None
    video_color_range: Optional[str] = None
    video_color_space: Optional[str] = None
    video_color_trc: Optional[str] = None
    video_frame_rate: Optional[str] = None
    video_ref_frames: Optional[str] = None
    video_height: Optional[str] = None
    video_width: Optional[str] = None
    video_language: Optional[str] = None
    video_language_code: Optional[str] = None
    video_scan_type: Optional[str] = None
    audio_bitrate: Optional[str] = None
    audio_bitrate_mode: Optional[str] = None
    audio_sample_rate: Optional[str] = None
    audio_language: Optional[str] = None
    audio_language_code: Optional[str] = None
    subtitle_codec: Optional[str] = None
    subtitle_container: Optional[str] = None
    subtitle_format: Optional[str] = None
    subtitle_forced: Optional[int] = None
    subtitle_location: Optional[str] = None
    subtitle_language: Optional[str] = None
    subtitle_language_code: Optional[str] = None
    row_id: Optional[int] = None
    user_id: Optional[int] = None
    username: Optional[str] = None
    friendly_name: Optional[str] = None
    user_thumb: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[int] = None
    is_admin: Optional[int] = None
    is_home_user: Optional[int] = None
    is_allow_sync: Optional[int] = None
    is_restricted: Optional[int] = None
    do_notify: Optional[int] = None
    keep_history: Optional[int] = None
    deleted_user: Optional[int] = None
    allow_guest: Optional[int] = None
    shared_libraries: Optional[List[str]] = None
    ip_address: Optional[str] = None
    ip_address_public: Optional[str] = None
    device: Optional[str] = None
    platform: Optional[str] = None
    platform_name: Optional[str] = None
    platform_version: Optional[str] = None
    product: Optional[str] = None
    product_version: Optional[str] = None
    profile: Optional[str] = None
    player: Optional[str] = None
    machine_id: Optional[str] = None
    state: Optional[str] = None
    local: Optional[int] = None
    relayed: Optional[int] = None
    secure: Optional[int] = None
    session_id: Optional[str] = None
    bandwidth: Optional[str] = None
    location: Optional[str] = None
    transcode_key: Optional[str] = None
    transcode_throttled: Optional[int] = None
    transcode_progress: Optional[int] = None
    transcode_speed: Optional[str] = None
    transcode_audio_channels: Optional[str] = None
    transcode_audio_codec: Optional[str] = None
    transcode_video_codec: Optional[str] = None
    transcode_width: Optional[str] = None
    transcode_height: Optional[str] = None
    transcode_container: Optional[str] = None
    transcode_protocol: Optional[str] = None
    transcode_hw_requested: Optional[int] = None
    transcode_hw_decode: Optional[str] = None
    transcode_hw_decode_title: Optional[str] = None
    transcode_hw_encode: Optional[str] = None
    transcode_hw_encode_title: Optional[str] = None
    transcode_hw_full_pipeline: Optional[int] = None
    transcode_max_offset_available: Optional[int] = None
    transcode_min_offset_available: Optional[int] = None
    audio_decision: Optional[str] = None
    video_decision: Optional[str] = None
    subtitle_decision: Optional[str] = None
    throttled: Optional[str] = None
    transcode_hw_decoding: Optional[int] = None
    transcode_hw_encoding: Optional[int] = None
    stream_container: Optional[str] = None
    stream_bitrate: Optional[str] = None
    stream_aspect_ratio: Optional[str] = None
    stream_audio_codec: Optional[str] = None
    stream_audio_channels: Optional[str] = None
    stream_audio_channel_layout: Optional[str] = None
    stream_video_codec: Optional[str] = None
    stream_video_framerate: Optional[str] = None
    stream_video_resolution: Optional[str] = None
    stream_video_height: Optional[str] = None
    stream_video_width: Optional[str] = None
    stream_duration: Optional[str] = None
    stream_container_decision: Optional[str] = None
    optimized_version_title: Optional[str] = None
    synced_version: Optional[int] = None
    live_uuid: Optional[str] = None
    bif_thumb: Optional[str] = None
    subtitles: Optional[int] = None
    transcode_decision: Optional[str] = None
    container_decision: Optional[str] = None
    stream_video_full_resolution: Optional[str] = None
    video_dynamic_range: Optional[str] = None
    stream_video_dynamic_range: Optional[str] = None
    stream_video_bitrate: Optional[str] = None
    stream_video_bit_depth: Optional[str] = None
    stream_video_chroma_subsampling: Optional[str] = None
    stream_video_color_primaries: Optional[str] = None
    stream_video_color_range: Optional[str] = None
    stream_video_color_space: Optional[str] = None
    stream_video_color_trc: Optional[str] = None
    stream_video_codec_level: Optional[str] = None
    stream_video_ref_frames: Optional[str] = None
    stream_video_language: Optional[str] = None
    stream_video_language_code: Optional[str] = None
    stream_video_scan_type: Optional[str] = None
    stream_video_decision: Optional[str] = None
    stream_audio_bitrate: Optional[str] = None
    stream_audio_bitrate_mode: Optional[str] = None
    stream_audio_sample_rate: Optional[str] = None
    stream_audio_channel_layout_: Optional[str] = None
    stream_audio_language: Optional[str] = None
    stream_audio_language_code: Optional[str] = None
    stream_audio_decision: Optional[str] = None
    stream_subtitle_codec: Optional[str] = None
    stream_subtitle_container: Optional[str] = None
    stream_subtitle_format: Optional[str] = None
    stream_subtitle_forced: Optional[int] = None
    stream_subtitle_location: Optional[str] = None
    stream_subtitle_language: Optional[str] = None
    stream_subtitle_language_code: Optional[str] = None
    stream_subtitle_decision: Optional[str] = None
    stream_subtitle_transient: Optional[int] = None

    @property
    def duration_milliseconds(self):
        try:
            return int(self.duration)
        except:
            return 0

    @property
    def location_milliseconds(self):
        try:
            return int(self.view_offset)
        except:
            return 0

    @property
    def progress_percentage(self):
        if not self.duration_milliseconds:
            return 0
        return int(self.location_milliseconds / self.duration_milliseconds)

    @property
    def progress_marker(self):
        if not self.location_milliseconds or not self.duration_milliseconds:
            return ""
        current_progress_min_sec = internal_utils.milliseconds_to_minutes_seconds(
            milliseconds=self.location_milliseconds)
        total_min_sec = internal_utils.milliseconds_to_minutes_seconds(milliseconds=self.duration_milliseconds)
        return f"{current_progress_min_sec}/{total_min_sec}"

    @property
    def eta(self):
        if not self.duration_milliseconds or not self.location_milliseconds:
            return ""
        milliseconds_remaining = self.duration_milliseconds - self.location_milliseconds
        eta_datetime = internal_utils.now_plus_milliseconds(milliseconds=milliseconds_remaining)
        eta_string = internal_utils.datetime_to_string(datetime_object=eta_datetime, string_format="%H:%M")
        return eta_string

    @property
    def status_icon(self):
        """
        Get icon for a stream state

        :returns: emoji icon
        """
        return static.switcher.get(self.state, "")

    @property
    def type_icon(self):
        if self.media_type in static.media_type_icons:
            return static.media_type_icons[self.media_type]
        # thanks twilsonco
        elif self.live:
            return static.media_type_icons['live']
        return ""

    @property
    def human_bandwidth(self) -> str:
        try:
            return to_human_bitrate(float(self.bandwidth))
        except:
            return to_human_bitrate(0)

    @property
    def transcoding_stub(self):
        return ' (Transcode)' if self.stream_container_decision == 'transcode' else ''

    @property
    def summary(self) -> str:
        return f"{static.session_title_message.format(icon=self.status_icon, username=self.username, media_type_icon=self.type_icon, title=self.title)}\n" \
               f"{static.session_player_message.format(product=self.product, player=self.player)}\n" \
               f"{static.session_details_message.format(quality_profile=self.quality_profile, bandwidth=self.human_bandwidth, transcoding=self.transcoding_stub)}\n" \
               f"{static.session_progress_message.format(progress=self.progress_marker, eta=self.eta)}"


class Activity(BaseModel):
    stream_count: Optional[str] = None
    sessions: Optional[List[Session]] = None
    stream_count_direct_play: Optional[int] = None
    stream_count_direct_stream: Optional[int] = None
    stream_count_transcode: Optional[int] = None
    total_bandwidth: Optional[int] = None
    lan_bandwidth: Optional[int] = None
    wan_bandwidth: Optional[int] = None

    @property
    def summary(self) -> ActivitySummary:
        return build_summary_from_activity_object(activity=self)


class Response(BaseModel):
    result: Optional[str] = None
    message: Any = None
    data: Activity


class Model(BaseModel):
    response: Response


class ActivitySummary(BaseModel):
    stream_count: Optional[str] = "0"
    transcode_count: Optional[int] = 0
    total_bandwidth: Optional[int] = 0
    lan_bandwidth: Optional[int] = 0

    @property
    def message(self):
        """
        Get activity summary message

        :returns: Summary message
        :rtype: Optional[str]
        """
        overview_message = ""
        stream_count = 0
        try:
            stream_count = int(self.stream_count)
        except:
            pass

        if stream_count > 0:
            overview_message += static.sessions_message.format(stream_count=stream_count,
                                                               word=internal_utils.make_plural(word='stream',
                                                                                               count=stream_count))
            if self.transcode_count > 0:
                overview_message += f" ({static.transcodes_message.format(transcode_count=self.transcode_count, word=internal_utils.make_plural(word='transcode', count=self.transcode_count))}) "

        if self.total_bandwidth > 0:
            overview_message += f" | {static.bandwidth_message.format(bandwidth=to_human_bitrate(float(self.total_bandwidth)))}"
            if self.lan_bandwidth > 0:
                overview_message += f" {static.lan_bandwidth_message.format(bandwidth=to_human_bitrate(float(self.lan_bandwidth)))}"

        return overview_message


def build_summary_from_activity_object(activity: Activity) -> ActivitySummary:
    """
    Create an ActivitySummary using an Activity object

    :param activity: Activity object to use for Overview
    :type activity: Activity
    :returns: ActivitySummary object
    :rtype: ActivitySummary
    """
    overview = ActivitySummary()
    overview.stream_count = activity.stream_count
    overview.transcode_count = activity.stream_count_transcode
    overview.total_bandwidth = activity.total_bandwidth
    overview.lan_bandwidth = activity.lan_bandwidth

    return overview


def build_summary_from_activity_json(activity_data: dict) -> ActivitySummary:
    """
    Create an ActivitySummary using Activity JSON data

    :param activity_data: Activity JSON data to use for Overview
    :type activity_data: dict
    :returns: ActivitySummary object
    :rtype: ActivitySummary
    """
    return ActivitySummary(**activity_data)
