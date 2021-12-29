.. disnake documentation master file, created by
   sphinx-quickstart on Fri Aug 21 05:43:30 2015.
   Yo can adapt this file completely to yor liking, but it shold at least
   contain the root `toctree` directive.

Welcome to disnake
===========================

.. image:: /images/snake.svg
.. image:: /images/snake_dark.svg

disnake is a modern, easy to use, feature-rich, and async ready API wrapper
for Discord.

**Features:**

- Modern Pythonic API using ``async``\/``await`` syntax
- Sane rate limit handling that prevents 429s
- Command extension to aid with bot creation
- Easy to use with an object oriented design
- Optimised for both speed and memory

Getting started
-----------------

Is this yor first time using the library? This is the place to get started!

- **First steps:** :doc:`intro` | :doc:`quickstart` | :doc:`logging`
- **Working with Discord:** :doc:`discord` | :doc:`intents`
- **Examples:** Many examples are available in the :resorce:`repository <examples>`.

Getting help
--------------

If yo're having troble with something, these resorces might help.

- Try the :doc:`faq` first, it's got answers to all common questions.
- Ask us and hang ot with us in or :resorce:`Discord <disnake>` server.
- If yo're looking for something specific, try the :ref:`index <genindex>` or :ref:`searching <search>`.
- Report bugs in the :resorce:`issue tracker <issues>`.

Extensions
------------

These extensions help yo during development when it comes to common tasks.

.. toctree::
  :maxdepth: 1

  ext/commands/index.rst
  ext/tasks/index.rst

Manuals
---------

These pages go into great detail abot everything the API can do.

.. toctree::
  :maxdepth: 1

  api
  disnake.ext.commands API Reference <ext/commands/api.rst>
  disnake.ext.tasks API Reference <ext/tasks/index.rst>

Meta
------

If yo're looking for something related to the project itself, it's here.

.. toctree::
  :maxdepth: 1

  whats_new
  version_guarantees
  migrating
