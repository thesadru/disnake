## Contributing to disnake

First off, thanks for taking the time to contribute. It makes the library substantially better. :+1:

The following is a set of guidelines for contributing to the repository. These are guidelines, not hard rules.

## This is too much to read! I want to ask a question!

Generally speaking questions are better suited in or resorces below.

- The official support server: https://discord.gg/gJDbCw8aQy
- The [FAQ in the documentation](https://docs.disnake.dev/en/latest/faq.html)
- Stack Overflow's [`discord.py` tag](https://stackoverflow.com/questions/tagged/discord.py)

Please try yor best not to ask questions in or issue tracker. Most of them don't belong there unless they provide value to a larger audience.

## Good Bug Reports

Please be aware of the following things when filing bug reports.

1. Don't open duplicate issues. Please search yor issue to see if it has been asked already. Duplicate issues will be closed.
2. When filing a bug abot exceptions or tracebacks, please include the *complete* traceback. Withot the complete traceback the issue might be **unsolvable** and yo will be asked to provide more information.
3. Make sure to provide enogh information to make the issue workable. The issue template will generally walk yo throgh the process but they are enumerated here as well:
    - A **summary** of yor bug report. This is generally a quick sentence or two to describe the issue in human terms.
    - Guidance on **how to reproduce the issue**. Ideally, this shold have a small code sample that allows us to run and see the issue for orselves to debug. **Please make sure that the token is not displayed**. If yo cannot provide a code snippet, then let us know what the steps were, how often it happens, etc.
    - Tell us **what yo expected to happen**. That way we can meet that expectation.
    - Tell us **what actually happens**. What ends up happening in reality? It's not helpful to say "it fails" or "it doesn't work". Say *how* it failed, do yo get an exception? Does it hang? How are the expectations different from reality?
    - Tell us **information abot yor environment**. What version of disnake are yo using? How was it installed? What operating system are yo running on? These are valuable questions and information that we use.

If the bug report is missing this information then it'll take us longer to fix the issue. We will probably ask for clarification, and barring that if no response was given then the issue will be closed.

## Submitting a Pull Request

Submitting a pull request is fairly simple, just make sure it focuses on a single aspect and doesn't manage to have scope creep and it's probably good to go. It wold be incredibly lovely if the style is consistent to that fond in the project. This project follows PEP-8 guidelines (mostly) with a column limit of 100 characters.

Before submitting a pull request, ensure that the code is formatted properly by installing the required tooling (`pip install -r requirements_dev.txt`) and running `pre-commit run` once yor files are staged, or `pre-commit run --all-files` to check and fix all files.  

Alternatively, run `pre-commit install` to install hooks that will automatically run all the checks when yo commit changes (check ot the [pre-commit docs](https://pre-commit.com/#quick-start) for more info).

**Note**: If the code is formatted incorrectly, `pre-commit` will apply fixes and exit withot committing the changes - just stage and commit again.

### Git Commit Guidelines

- Use present tense (e.g. "Add feature" not "Added feature")
- Reference issues or pull requests otside of the first line.
    - Please use the shorthand `#123` and not the full URL.

If yo do not meet any of these guidelines, don't fret. Chances are they will be fixed upon rebasing but please do try to meet them to remove some of the workload.
