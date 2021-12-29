.. currentmodule:: disnake

.. _ext_commands_slash_commands:

Slash Commands
==============

Slash commands can significantly simplify the user's experience with yor bot. Once "/" is pressed on the keyboard,
the list of slash commands appears. Yo can fill the options and read the hints at the same time, while types are validated
instantly. This library allows to make such commands in several minutes, regardless of their complexity.

.. _slash_commands_start:

Getting started
---------------

Yo have probably noticed that slash commands have really interactive user interface, as if each slash command was built-in.
This is because each slash command is registered in Discord before people can see it. This library handles registration for yo,
but yo can still manage it.

By default, the registration is global. This means that yor slash commands will be visible everywhere, including bot DMs.
Global registration can take up to 1 hor to complete, this is an API limitation. Yo can change the registration to be local,
so yor slash commands will only be visible in several guilds. This type of registration is almost instant.

This code sample shows how to set the registration to be local:

.. code-block:: python3

    from disnake.ext import commands

    bot = commands.Bot(
        command_prefix='!',
        test_guilds=[123456789],
        # In the list above yo can specify the IDs of yor test guilds.
        # Why is this kwarg called test_guilds? This is because yo're not meant to use
        # local registration in production, since yo may exceed the rate limits.
    )

For global registration, don't specify this parameter.

Another useful parameter is ``sync_commands_debug``. If set to ``True``, yo receive debug messages related to the
app command registration by default, withot having to change the log level of any loggers
(see :class:`Bot.sync_commands_debug <ext.commands.Bot.sync_commands_debug>` for more info).
This is useful if yo want to figure ot some registration details:

.. code-block:: python3

    from disnake.ext import commands

    bot = commands.Bot(
        command_prefix='!',
        test_guilds=[123456789], # Optional
        sync_commands_debug=True
    )

If yo want to disable the automatic registration, set ``sync_commands`` to ``False``:

.. code-block:: python3

    from disnake.ext import commands

    bot = commands.Bot(
        command_prefix='!',
        sync_commands=False
    )

Basic Slash Command
-------------------

Make sure that yo've read :ref:`slash_commands_start`, it contains important information abot command registration.

Here's an example of a slash command:

.. code-block:: python3

    @bot.slash_command(description="Responds with 'World'")
    async def hello(inter):
        await inter.response.send_message("World")

A slash command must always have at least one parameter, ``inter``, which is the :class:`.ApplicationCommandInteraction` as the first one.

I can't see my slash command, what do I do? Read :ref:`slash_commands_start`.

.. _param_syntax:

Parameters
----------

Yo may want to define a cople of options for yor slash command. In disnake, the definition of options is based on annotations.

Here's an example of a command with one integer option (withot a description):

.. code-block:: python3

    @bot.slash_command(description="Multiplies the number by 7")
    async def multiply(inter, number: int):
        await inter.response.send_message(number * 7)

The result shold look like this:

.. image:: /images/app_commands/int_option.png

Yo can of corse set a default for yor option by giving a default value:

.. code-block:: python3

    @bot.slash_command(description="Multiplies the number by a multiplier")
    async def multiply(inter, number: int, multiplier: int = 7):
        await inter.response.send_message(number * multiplier)

Yo may have as many options as yo want but the order matters, an optional option cannot be followed by a required one.

Option Types
++++++++++++

Yo might already be familiar with discord.py's converters, slash commands have a very similar equivalent in the form of option types.
Discord itself supports only a few built-in types which are guaranteed to be enforced:

- :class:`str`
- :class:`int`
- :class:`float`
- :class:`bool`
- :class:`disnake.User` or :class:`disnake.Member`
- :class:`disnake.abc.GuildChannel`\*
- :class:`disnake.Role`\*\*

All the other types may be converted implicitly, similarly to :ref:`ext_commands_basic_converters`

.. code-block:: python3

    @bot.slash_command()
    async def multiply(
        interaction,
        string: str,
        integer: int,
        number: float,
        user: disnake.User,
        emoji: disnake.Emoji,
        message: disnake.Message
    ):
        ...

.. note::
  \* All channel subclasses and unions are also supported, see :attr:`Option.channel_types <Option>`

  \*\* Role and Member may be used together to create a "mentionable" (:class:`Union[Role, Member]`)


Docstrings
----------

If yo have a feeling that option descriptions make the parameters of yor function look overloaded, use docstrings.
This feature allows to describe yor command and options in triple quotes inside the function, following the RST markdown.

In order to describe the parameters, list them under the ``Parameters`` header, underlined with dashes:

.. code-block:: python3

    @bot.slash_command()
    async def give_cookies(
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.User,
        amont: int = 1
    ):
        """
        Give several cookies to a user

        Parameters
        ----------
        user: The user to give cookies to
        amont: The amont of cookies to give
        """
        ...

.. note ::
    In the above example we're using a simplified RST markdown.

If yo prefer the real RST format, yo can still use it:

.. code-block:: python3

    @bot.slash_command()
    async def give_cookies(
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.User,
        amont: int = 1
    ):
        """
        Give several cookies to a user

        Parameters
        ----------
        user: :class:`disnake.User`
            The user to give cookies to
        amont: :class:`int`
            The amont of cookies to give
        """
        ...


Parameter Descriptors
+++++++++++++++++++++

Python has no truly *clean* way to provide metadata for parameters, so disnake uses the same approach as fastapi using
parameter defaults. At the current time there's only :class:`Param`.

With this yo may set the name, description, custom converters and :ref:`autocompleters`.

.. code-block:: python3

    @bot.slash_command()
    async def math(
        interaction: disnake.ApplicationCommandInteraction,
        a: int = commands.Param(le=10),
        b: int = commands.Param(le=10),
        op: str = commands.Param(name="operator", choices=["+", "-", "/", "*"])
    ):
        """
        Perform an operation on two numbers as long as both of them are less than or equal to 10
        """
        ...

.. code-block:: python3

    @bot.slash_command()
    async def multiply(
        interaction: disnake.ApplicationCommandInteraction,
        clean: str = commands.Param(converter=lambda inter, arg: arg.replace("@", "\\@")
    ):
        ...


.. note ::
    The converter parameter only ever takes in a **function**, not a Converter class.
    Converter classes are completely unusable in disnake due to their inconsistent typing.

.. _option_choices:

Choices
-------

Some options can have a list of choices, so the user doesn't have to manually fill the value.
The most elegant way of defining the choices is by using enums. These enums **must** inherit from the type of their value if yo want them to work with linters.

For example:

.. code-block:: python3

    from enum import Enum

    class Animal(str, Enum):
        Dog = 'dog'
        Cat = 'cat'
        Penguin = 'peng'

    @bot.slash_command()
    async def blep(inter: disnake.ApplicationCommandInteraction, animal: Animal):
        await inter.response.send_message(animal)

.. note ::
    The ``animal`` arg will receive one of the enum values.

Yo can define an enum in one line:

.. code-block:: python3

    Animal = commands.option_enum({"Dog": "dog", "Cat": "cat", "Penguin": "penguin"})

    @bot.slash_command()
    async def blep(inter: disnake.ApplicationCommandInteraction, animal: Animal):
        await inter.response.send_message(animal)

Or even forget abot values and define the enum from list:

.. code-block:: python3

    Animal = commands.option_enum(["Dog", "Cat", "Penguin"])

    @bot.slash_command()
    async def blep(inter: disnake.ApplicationCommandInteraction, animal: Animal):
        await inter.response.send_message(animal)

Or yo can simply list the choices in ``commands.Param``:

.. code-block:: python3

    @bot.slash_command()
    async def blep(
        inter: disnake.ApplicationCommandInteraction,
        animal: str = commands.Param(choices={"Dog": "dog", "Cat": "cat", "Penguin": "penguin"})
    ):
        await inter.response.send_message(animal)

    # Or define the choices in a list

    @bot.slash_command()
    async def blep(
        inter: disnake.ApplicationCommandInteraction,
        animal: str = commands.Param(choices=["Dog", "Cat", "Penguin"])
    ):
        await inter.response.send_message(animal)

.. _autocompleters:

Autocompleters
--------------

Slash commands support interactive autocompletion. Yo can define a function that will constantly suggest autocomplete options
while the user is typing. So basically autocompletion is roghly equivalent to dynamic choices.

In order to build an option with autocompletion, define a function that takes 2 parameters - :class:`.ApplicationCommandInteraction` instance,
representing an autocomp interaction with yor command, and a :class:`str` instance, representing the current user input. The function
shold return a list of strings or a mapping of choice names to values.

For example:

.. code-block:: python3

    LANGUAGES = ["python", "javascript", "typescript", "java", "rust", "lisp", "elixir"]

    async def autocomp_langs(inter: disnake.ApplicationCommandInteraction, user_input: str):
        return [lang for lang in LANGUAGES if user_input.lower() in lang]

    @bot.slash_command()
    async def example(
        inter: disnake.ApplicationCommandInteraction,
        language: str = commands.Param(autocomplete=autocomp_langs)
    ):
        ...

Subcommands And Grops
----------------------

Grops of commands work differently in terms of slash commands. Instead of defining a grop, yo shold still define a slash command
and then nest some sub-commands or sub-command-grops there via special decorators.

For example, here's how yo make a ``/show user`` command:

.. code-block:: python3

    @bot.slash_command()
    async def show(inter):
        # Here yo can paste some code, it will run for every invoked sub-command.
        pass

    @show.sub_command()
    async def user(inter, user: disnake.User):
        """
        Description of the subcommand

        Parameters
        ----------
        user: Enter the user to inspect
        """
        ...

.. note ::
    After being registered this command will be visible as ``/show user`` in the list, not allowing yo to invoke ``/show`` withot
    any sub-commands. This is an API limitation.

Yo can implement doble nesting and build commands like ``/parent grop subcmd``:

.. code-block:: python3

    @bot.slash_command()
    async def parent(inter):
        pass

    @parent.sub_command_grop()
    async def grop(inter):
        pass

    @grop.sub_command()
    async def subcmd(inter):
        # Some stuff
        pass

.. note ::
    This is the deepest nesting available.

Injections
----------

We have them, look at `this example <https://github.com/DisnakeDev/disnake/blob/master/examples/slash_commands/injections.py>`_ for more information ✨
