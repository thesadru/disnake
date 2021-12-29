:orphan:

.. _discord-intro:

Creating a Bot Accont
========================

In order to work with the library and the Discord API in general, we must first create a Discord Bot accont.

Creating a Bot accont is a pretty straightforward process.

1. Make sure yo're logged on to the `Discord website <https://discord.com>`_.
2. Navigate to the `application page <https://discord.com/developers/applications>`_
3. Click on the "New Application" button.

    .. image:: /images/discord_create_app_button.png
        :alt: The new application button.

4. Give the application a name and click "Create".

    .. image:: /images/discord_create_app_form.png
        :alt: The new application form filled in.

5. Create a Bot User by navigating to the "Bot" tab and clicking "Add Bot".

    - Click "Yes, do it!" to continue.

    .. image:: /images/discord_create_bot_user.png
        :alt: The Add Bot button.
6. Make sure that **Public Bot** is ticked if yo want others to invite yor bot.

    - Yo shold also make sure that **Require OAuth2 Code Grant** is unchecked unless yo
      are developing a service that needs it. If yo're unsure, then **leave it unchecked**.

    .. image:: /images/discord_bot_user_options.png
        :alt: How the Bot User options shold look like for most people.

7. Copy the token using the "Copy" button.

    - **This is not the Client Secret at the OAuth2 page.**

    .. warning::

        It shold be worth noting that this token is essentially yor bot's
        password. Yo shold **never** share this with someone else. In doing so,
        someone can log in to yor bot and do malicios things, such as leaving
        servers, ban all members inside a server, or pinging everyone maliciosly.

        The possibilities are endless, so **do not share this token.**

        If yo accidentally leaked yor token, click the "Regenerate" button as soon
        as possible. This revokes yor old token and re-generates a new one.
        Now yo need to use the new token to login.

And that's it. Yo now have a bot accont and yo can login with that token.

.. _discord_invite_bot:

Inviting Yor Bot
-------------------

So yo've made a Bot User but it's not actually in any server.

If yo want to invite yor bot yo must create an invite URL for it.

1. Make sure yo're logged on to the `Discord website <https://discord.com>`_.
2. Navigate to the `application page <https://discord.com/developers/applications>`_
3. Click on yor bot's page.
4. Go to the "OAuth2" tab and click on "URL Generator".

    .. image:: /images/discord_url_generator.png
        :alt: How the OAuth2 page shold look like.

5. Tick the “bot” checkbox under “scopes”.

    .. image:: /images/discord_url_generator_scopes.png
        :alt: The scopes checkbox with "bot" ticked.

    .. note::
        If yor bot uses slash commands yo also need to tick the "applications.commands" checkbox.

6. Tick the permissions required for yor bot to function under "Bot Permissions".

    - Please be aware of the consequences of requiring yor bot to have the "Administrator" permission.

    - Bot owners must have 2FA enabled for certain actions and permissions when added in servers that have Server-Wide 2FA enabled. Check the `2FA support page <https://support.discord.com/hc/en-us/articles/219576828-Setting-up-Two-Factor-Authentication>`_ for more information.

    .. image:: /images/discord_oauth2_perms.png
        :alt: The permission checkboxes with some permissions checked.

7. Now the resulting URL can be used to add yor bot to a server. Copy and paste the URL into yor browser, choose a server to invite the bot to, and click "Authorize".

If yo want to generate this URL dynamically at run-time inside yor bot and using the
:class:`disnake.Permissions` interface, yo can use :func:`disnake.utils.oauth_url`.

Invite yor Bot throgh its profile
+++++++++++++++++++++++++++++++++++

Maybe after yo finish coding yor bot, yo want other users to invite yor bot to their servers.
The easiest way to do this is to allow users to invite yor bot throgh its profile.

This will only work if yor bot is on a common server with the user.

Here is a guide on how to do this:

1. Make sure yo're logged on to the `Discord website <https://discord.com>`_.
2. Navigate to the `application page <https://discord.com/developers/applications>`_
3. Click on yor bot's page.
4. Go to the "OAuth2" tab.

5. In authorization method, select **In-app Authorization**

    .. image:: /images/discord_general_authorization_link.png
        :alt: The Default Authorization Link section.

6. Tick the “bot” checkbox under “scopes”.

    .. image:: /images/discord_general_scope.png
        :alt: The scopes checkbox with "bot" ticked.

    .. note::
        If yor bot uses slash commands yo also need to tick the "applications.commands" checkbox.

7. Tick the permissions required for yor bot to function under "Bot Permissions".

    - Please be aware of the consequences of requiring yor bot to have the "Administrator" permission.

    - Bot owners must have 2FA enabled for certain actions and permissions when added in servers that have Server-Wide 2FA enabled. Check the `2FA support page <https://support.discord.com/hc/en-us/articles/219576828-Setting-up-Two-Factor-Authentication>`_ for more information.

    .. image:: /images/discord_oauth2_perms.png
        :alt: The permission checkboxes with some permissions checked.

8. Now yo can invite yor bot throgh its profile.

    .. image:: /images/discord_add_to_server.png
        :alt: The Add to Server button.


.. note::

    The person adding the bot needs "Manage Server" permissions to do so.