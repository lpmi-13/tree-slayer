# Tree Slayer

Have you ever wondered about the deep git magicks...?

Have you ever heard about git's ability to delete a file across the entire git history in a recursive rebase-like fashion...?

Have you ever been reading the ancient scrolls late at night, and come across the `git filter-branch` command...?

Have you ever wanted to actually invoke this arcane and forbidden spell just to see what happens...?

Well wonder no more, this repo is exactly the opportunity to run the infamous command and see what happens!

## *HOWEVER!!! BIG WARNING SIGN AND DISCLAIMER HERE*

For historical reasons, this command is full of possible side-effects and things that can go horribly wrong (like any good powerful magic spell), and it's the official recommendation of git that you *DO NOT USE IT*.

Instead, you should use the `git filter-repo` command (https://github.com/newren/git-filter-repo).

For a full list of potential issues, see [the documentation](https://git-scm.com/docs/git-filter-branch#SAFETY).

...but if you still would like to just try it out, you've come to the right place.

## Running the command locally to delete a file completely from git history

first, clone this repo, and take a look at the history.

```
git log --stat
```

Should show you something like the following:


