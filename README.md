# Tree Slayer

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/lpmi-13/tree-slayer)

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

```
commit 9e42721b0289c750280b4a0a522df1fae780bf6b (HEAD -> main, origin/main)
Author: Adam Leskis <leskis@gmail.com>
Date:   Thu Nov 18 23:19:24 2021 +0000

    remove secrets file and use environment variable

 main.py    | 3 ++-
 secrets.py | 1 -
 2 files changed, 2 insertions(+), 2 deletions(-)

commit 2a92f794ff5ea884b5a98870716c0901662908d8
Author: Adam Leskis <leskis@gmail.com>
Date:   Thu Nov 18 23:16:46 2021 +0000

    add newly generated api key

 secrets.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

commit bd73b5ed20b92d533d3c0ce7d49deae13446cc22
Author: Adam Leskis <leskis@gmail.com>
Date:   Thu Nov 18 23:16:18 2021 +0000

    add a .gitignore

 .gitignore | 1 +
 1 file changed, 1 insertion(+)

commit b1b41d43f4f2405f559da311630fd93b09388e86
Author: Adam Leskis <leskis@gmail.com>
Date:   Thu Nov 18 23:15:59 2021 +0000

    lets add authentication

 main.py    | 11 +++++++++--
 secrets.py |  1 +
 2 files changed, 10 insertions(+), 2 deletions(-)
```

which has a WHOLE lot of times that `secrets.py` shows up. That's not good. Let's cast a spell to completely remove it from the entire git history (WARNING: this will not affect any forks, and this is a good time to repeat that the official documentation recommends NEVER DOING THIS COMMAND, so if you ever decide to do it for real on an actual repo, you're on your own).

so to confirm that `secrets.py` shows up a bunch, let's run the following:

```
git log --stat | grep secrets
```

which should show you

```
    remove secrets file and use environment variable
 secrets.py | 1 -
 secrets.py | 2 +-
 secrets.py |  1 +
```

now for the spell!

```
git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch secrets.py" HEAD
```

you will see a big official warning:

```
WARNING: git-filter-branch has a glut of gotchas generating mangled history
         rewrites.  Hit Ctrl-C before proceeding to abort, then use an
         alternative filtering tool such as 'git filter-repo'
         (https://github.com/newren/git-filter-repo/) instead.  See the
         filter-branch manual page for more details; to squelch this warning,
         set FILTER_BRANCH_SQUELCH_WARNING=1.
```

This is the official warning we discussed earlier. But we're already far into the deep dark woods, so let's hit return and watch the magic!

> it might take a few seconds to start, but just hit return once and wait a bit...

The output should look something like

```
Proceeding with filter-branch...

Rewrite 7fcb0c3f18a5ca41ef16c577b9b07a85d5679d0c (1/7) (0 seconds passed, remainingRewrite ee28590eaefa01c038ee40b2f20d200279bacd6d (2/7) (0 seconds passed, remainingRewrite b1b41d43f4f2405f559da311630fd93b09388e86 (3/7) (0 seconds passed, remaining 0 predicted)    rm 'secrets.py'
Rewrite bd73b5ed20b92d533d3c0ce7d49deae13446cc22 (4/7) (0 seconds passed, remaining 0 predicted)    rm 'secrets.py'
Rewrite 2a92f794ff5ea884b5a98870716c0901662908d8 (5/7) (0 seconds passed, remaining 0 predicted)    rm 'secrets.py'
Rewrite 9e42721b0289c750280b4a0a522df1fae780bf6b (6/7) (0 seconds passed, remainingRewrite 8df671b674156be190fd0e0e40a79ce3307239bd (7/7) (0 seconds passed, remaining 0 predicted)
Ref 'refs/heads/main' was rewritten
```

and now we can check the log again, and our `secrets.py` file has vanished!

```
git log --stat | grep secret
    remove secrets file and use environment variable
```

We have an empty commit now, where the `secrets.py` file was the only thing in the diff, but removing extra empty commits is a slightly different spell, and we've already delved too deep into the lost arts.

CONGRATULATIONS! You've successfully run one of the most feared git commands and lived to tell the tale. And, as always, you can easily use the `reflog` to time travel back to before you unleashed the furies of `git filter-branch`. If you want to practice `git reflog`, there's a [repo](https://github.com/lpmi-13/reflog-power) for that too!
