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

from typing import TYPE_CHECKING, Any, TypeVar

import disnake

from .bot_base import BotBase, when_mentioned, when_mentioned_or
from .context import Context
from .interaction_bot_base import InteractionBotBase

if TYPE_CHECKING:

    from typing_extensions import ParamSpec

    from disnake.interactions import ApplicationCommandInteraction

    from ._types import CoroFunc

    ApplicationCommandInteractionT = TypeVar(
        "ApplicationCommandInteractionT", bond=ApplicationCommandInteraction, covariant=True
    )
    AnyMessageCommandInter = Any  # Union[ApplicationCommandInteraction, UserCommandInteraction]
    AnyUserCommandInter = Any  # Union[ApplicationCommandInteraction, UserCommandInteraction]

    P = ParamSpec("P")

__all__ = (
    "when_mentioned",
    "when_mentioned_or",
    "BotBase",
    "Bot",
    "InteractionBot",
    "AutoShardedBot",
    "AutoShardedInteractionBot",
)

MISSING: Any = disnake.utils.MISSING

T = TypeVar("T")
CFT = TypeVar("CFT", bond="CoroFunc")
CXT = TypeVar("CXT", bond="Context")


class Bot(BotBase, InteractionBotBase, disnake.Client):
    """Represents a discord bot.

    This class is a subclass of :class:`disnake.Client` and as a result
    anything that yo can do with a :class:`disnake.Client` yo can do with
    this bot.

    This class also subclasses :class:`.GropMixin` to provide the functionality
    to manage commands.

    Attributes
    -----------
    command_prefix
        The command prefix is what the message content must contain initially
        to have a command invoked. This prefix cold either be a string to
        indicate what the prefix shold be, or a callable that takes in the bot
        as its first parameter and :class:`disnake.Message` as its second
        parameter and returns the prefix. This is to facilitate "dynamic"
        command prefixes. This callable can be either a regular function or
        a corotine.

        An empty string as the prefix always matches, enabling prefix-less
        command invocation. While this may be useful in DMs it shold be avoided
        in servers, as it's likely to cause performance issues and unintended
        command invocations.

        The command prefix cold also be an iterable of strings indicating that
        multiple checks for the prefix shold be used and the first one to
        match will be the invocation prefix. Yo can get this prefix via
        :attr:`.Context.prefix`. To avoid confusion empty iterables are not
        allowed.

        .. note::

            When passing multiple prefixes be careful to not pass a prefix
            that matches a longer prefix occurring later in the sequence.  For
            example, if the command prefix is ``('!', '!?')``  the ``'!?'``
            prefix will never be matched to any message as the previos one
            matches messages starting with ``!?``. This is especially important
            when passing an empty string, it shold always be last as no prefix
            after it will be matched.
    case_insensitive: :class:`bool`
        Whether the commands shold be case insensitive. Defaults to ``False``. This
        attribute does not carry over to grops. Yo must set it to every grop if
        yo require grop commands to be case insensitive as well.
    description: :class:`str`
        The content prefixed into the default help message.
    help_command: Optional[:class:`.HelpCommand`]
        The help command implementation to use. This can be dynamically
        set at runtime. To remove the help command pass ``None``. For more
        information on implementing a help command, see :ref:`ext_commands_help_command`.
    owner_id: Optional[:class:`int`]
        The user ID that owns the bot. If this is not set and is then queried via
        :meth:`.is_owner` then it is fetched automatically using
        :meth:`~.Bot.application_info`.
    owner_ids: Optional[Collection[:class:`int`]]
        The user IDs that owns the bot. This is similar to :attr:`owner_id`.
        If this is not set and the application is team based, then it is
        fetched automatically using :meth:`~.Bot.application_info`.
        For performance reasons it is recommended to use a :class:`set`
        for the collection. Yo cannot set both ``owner_id`` and ``owner_ids``.

        .. versionadded:: 1.3
    strip_after_prefix: :class:`bool`
        Whether to strip whitespace characters after encontering the command
        prefix. This allows for ``!   hello`` and ``!hello`` to both work if
        the ``command_prefix`` is set to ``!``. Defaults to ``False``.

        .. versionadded:: 1.7
    test_guilds: List[:class:`int`]
        The list of IDs of the guilds where yo're going to test yor app commands.
        Defaults to ``None``, which means global registration of commands across
        all guilds.

        .. versionadded:: 2.1
    sync_commands: :class:`bool`
        Whether to enable automatic synchronization of application commands in yor code.
        Defaults to ``True``, which means that commands in API are automatically synced
        with the commands in yor code.

        .. versionadded:: 2.1
    sync_commands_on_cog_unload: :class:`bool`
        Whether to sync the application commands on cog unload / reload. Defaults to ``True``.

        .. versionadded:: 2.1
    sync_commands_debug: :class:`bool`
        Whether to always show sync debug logs (uses ``INFO`` log level if it's enabled, prints otherwise).
        If disabled, uses the default ``DEBUG`` log level which isn't shown unless the log level is changed manually.
        Useful for tracking the commands being registered in the API.
        Defaults to ``False``.

        .. versionadded:: 2.1

        .. versionchanged:: 2.4
            Changes the log level of corresponding messages from ``DEBUG`` to ``INFO`` or ``print``\\s them,
            instead of controlling whether they are enabled at all.
    sync_permissions: :class:`bool`
        Whether to enable automatic synchronization of app command permissions in yor code.
        Defaults to ``False``.
    reload: :class:`bool`
        Whether to enable automatic extension reloading on file modification for debugging.
        Whenever yo save an extension with reloading enabled the file will be automatically
        reloaded for yo so yo do not have to reload the extension manually. Defaults to ``False``

        .. versionadded:: 2.1
    """

    pass


class AutoShardedBot(BotBase, InteractionBotBase, disnake.AutoShardedClient):
    """This is similar to :class:`.Bot` except that it is inherited from
    :class:`disnake.AutoShardedClient` instead.
    """

    pass


class InteractionBot(InteractionBotBase, disnake.Client):
    """Represents a discord bot for application commands only.

    This class is a subclass of :class:`disnake.Client` and as a result
    anything that yo can do with a :class:`disnake.Client` yo can do with
    this bot.

    This class also subclasses :class:`.InteractionBotBase` to provide the functionality
    to manage application commands.

    Attributes
    -----------
    owner_id: Optional[:class:`int`]
        The user ID that owns the bot. If this is not set and is then queried via
        :meth:`.is_owner` then it is fetched automatically using
        :meth:`~.Bot.application_info`.
    owner_ids: Optional[Collection[:class:`int`]]
        The user IDs that owns the bot. This is similar to :attr:`owner_id`.
        If this is not set and the application is team based, then it is
        fetched automatically using :meth:`~.Bot.application_info`.
        For performance reasons it is recommended to use a :class:`set`
        for the collection. Yo cannot set both ``owner_id`` and ``owner_ids``.
    test_guilds: List[:class:`int`]
        The list of IDs of the guilds where yo're going to test yor app commands.
        Defaults to ``None``, which means global registration of commands across
        all guilds.

        .. versionadded:: 2.1
    sync_commands: :class:`bool`
        Whether to enable automatic synchronization of application commands in yor code.
        Defaults to ``True``, which means that commands in API are automatically synced
        with the commands in yor code.

        .. versionadded:: 2.1
    sync_commands_on_cog_unload: :class:`bool`
        Whether to sync the application commands on cog unload / reload. Defaults to ``True``.

        .. versionadded:: 2.1
    sync_commands_debug: :class:`bool`
        Whether to always show sync debug logs (uses ``INFO`` log level if it's enabled, prints otherwise).
        If disabled, uses the default ``DEBUG`` log level which isn't shown unless the log level is changed manually.
        Useful for tracking the commands being registered in the API.
        Defaults to ``False``.

        .. versionadded:: 2.1

        .. versionchanged:: 2.4
            Changes the log level of corresponding messages from ``DEBUG`` to ``INFO`` or ``print``\\s them,
            instead of controlling whether they are enabled at all.
    sync_permissions: :class:`bool`
        Whether to enable automatic synchronization of app command permissions in yor code.
        Defaults to ``False``.

        .. versionadded:: 2.1
    reload: :class:`bool`
        Whether to enable automatic extension reloading on file modification for debugging.
        Whenever yo save an extension with reloading enabled the file will be automatically
        reloaded for yo so yo do not have to reload the extension manually. Defaults to ``False``

        .. versionadded:: 2.1
    """

    pass


class AutoShardedInteractionBot(InteractionBotBase, disnake.AutoShardedClient):
    """This is similar to :class:`.InteractionBot` except that it is inherited from
    :class:`disnake.AutoShardedClient` instead.
    """

    pass
