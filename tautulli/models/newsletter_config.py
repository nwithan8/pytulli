# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:44:54+00:00

from __future__ import annotations

from typing import List, Optional, Union

from tautulli.models._base import _Base, Field, EmptyStringNullableInt


class ConfigModel(_Base):
    custom_cron: EmptyStringNullableInt = None
    time_frame: EmptyStringNullableInt = None
    time_frame_units: Optional[str] = None
    formatted: EmptyStringNullableInt = None
    threaded: EmptyStringNullableInt = None
    notifier_id: EmptyStringNullableInt = None
    filename: Optional[str] = None
    save_only: EmptyStringNullableInt = None
    incl_libraries: Optional[List[str]] = None


class EmailConfigModel(_Base):
    from_name: Optional[str] = None
    from_: Optional[str] = Field(..., alias='from')
    to: Optional[List[str]] = None
    cc: Optional[List] = None
    bcc: Optional[List] = None
    smtp_server: Optional[str] = None
    smtp_port: EmptyStringNullableInt = None
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None
    tls: EmptyStringNullableInt = None
    html_support: EmptyStringNullableInt = None
    notifier_id: EmptyStringNullableInt = None


class MovieLibraryModel(_Base):
    value: EmptyStringNullableInt = None
    text: Optional[str] = None


class TVShowLibraryModel(_Base):
    value: EmptyStringNullableInt = None
    text: Optional[str] = None


class MusicLibraryModel(_Base):
    value: EmptyStringNullableInt = None
    text: Optional[str] = None


class OtherVideoLibraryModel(_Base):
    value: EmptyStringNullableInt = None
    text: Optional[str] = None


class SelectOptionsModel(_Base):
    Movie_Libraries: Optional[List[MovieLibraryModel]] = Field(..., alias='Movie Libraries')
    TV_Show_Libraries: Optional[List[TVShowLibraryModel]] = Field(..., alias='TV Show Libraries')
    Music_Libraries: Optional[List[MusicLibraryModel]] = Field(..., alias='Music Libraries')
    Other_Video_Libraries: Optional[List[OtherVideoLibraryModel]] = Field(
        ..., alias='Other Video Libraries'
    )


class ConfigOptionModel(_Base):
    label: Optional[str] = None
    value: Optional[List[str]] = None
    description: Optional[str] = None
    name: Optional[str] = None
    input_type: Optional[str] = None
    select_options: Optional[SelectOptionsModel] = None


class SelectOptionModel(_Base):
    value: Optional[str] = None
    text: Optional[str] = None


class EmailConfigOptionModel(_Base):
    label: Optional[str] = None
    value: Optional[Union[Union[int, str], List[str]]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    input_type: Optional[str] = None
    select_options: Optional[List[SelectOptionModel]] = None


class NewsletterConfigModel(_Base):
    id: EmptyStringNullableInt = None
    agent_id: EmptyStringNullableInt = None
    agent_name: Optional[str] = None
    agent_label: Optional[str] = None
    friendly_name: Optional[str] = None
    cron: Optional[str] = None
    active: EmptyStringNullableInt = None
    id_name: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    config: Optional[ConfigModel] = None
    email_config: Optional[EmailConfigModel] = None
    config_options: Optional[List[ConfigOptionModel]] = None
    email_config_options: Optional[List[EmailConfigOptionModel]] = None



