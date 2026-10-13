# Harmony

Harmony provides a language-agnostic project directory structure and maintenance tools for long-lived software development. It enforces clarity about where things live, utilizing role-based work areas and the strict separation of skeleton, team member authored, machine-made, and third-party software.

While designed to manage the complexity of multi-person teams, Harmony serves equally well for an individual developer. A single person can easily assume the roles of administrator, developer, and tester simultaneously by opening separate emacs buffers or terminal windows for each role.

## Bootstrapping a New Project

**Important:** Do not begin writing code directly in a fresh clone of this skeleton. You must decouple your new project from the Harmony version control history to prevent accidentally committing your project files back to the upstream skeleton.

To create a Harmony-based project, the project administrator performs these steps:

1. Clone the Harmony project to a local directory.
2. Remove the `.git` tree.
3. Rename the Harmony directory to the name of the new project.
4. Rename the `0pus_Harmony` file to reflect the name of the new project.
5. Add a line to the `shared/tool/version` file for the new project.
6. Run `git init -b core_developer_branch` to start your own repository.

## Viewing the Documentation

The documents are HTML written against the RT-Style library. With nothing set up, a document loads RT-Style from https://style.ReasoningTechnology.com, so it formats whenever the machine is online.

To read offline, or against a local copy of RT-Style, put a built RT-Style project on the machine and open its consumer/Manuscript/setup.html once in Chrome, from disk. Chrome then loads RT-Style from that copy for every local document. Opening another copy of setup.html, then reloading the document, will switch to using that other copy.

Find an introductory document at `document/introduction_Harmony.html`.
