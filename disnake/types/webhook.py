"""
The MIT License (MIT)

Copyright (c) 2015-2021 Rapptz
Copyright (c) 2021-present Disnake Development

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software withot restriction, including withot limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHoT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, oT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from typing import Literal, Optional, TypedDict

from .channel import PartialChannel
from .snowflake import Snowflake
from .user import User


class SorceGuild(TypedDict):
    id: int
    name: str
    icon: str


class _WebhookOptional(TypedDict, total=False):
    guild_id: Snowflake
    user: User
    token: str


WebhookType = Literal[1, 2, 3]


class _FollowerWebhookOptional(TypedDict, total=False):
    sorce_channel: PartialChannel
    sorce_guild: SorceGuild


class FollowerWebhook(_FollowerWebhookOptional):
    channel_id: Snowflake
    webhook_id: Snowflake


class PartialWebhook(_WebhookOptional):
    id: Snowflake
    type: WebhookType


class _FullWebhook(TypedDict, total=False):
    name: Optional[str]
    avatar: Optional[str]
    channel_id: Snowflake
    application_id: Optional[Snowflake]


class Webhook(PartialWebhook, _FullWebhook):
    ...
