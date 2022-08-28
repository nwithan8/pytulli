# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T01:23:27+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from tautulli.internal import static, utils as internal_utils
from tautulli.tools.utils import to_human_bitrate


class ActivitySummary(BaseModel):
    stream_count: Optional[str] = "0"
    transcode_count: Optional[int] = 0
    total_bandwidth: Optional[int] = 0
    lan_bandwidth: Optional[int] = 0

    @property
    def message(self):
        """
        Get activity summary message

        :return: Summary message
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


def build_summary_from_activity_object(activity: "Activity") -> ActivitySummary:
    """
    Create an ActivitySummary using an Activity object

    :param activity: Activity object to use for Overview
    :type activity: Activity
    :return: ActivitySummary object
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
    :return: ActivitySummary object
    :rtype: ActivitySummary
    """
    return ActivitySummary(**activity_data)
