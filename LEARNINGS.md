# Learnings log

One entry per day. Be honest about what you could not do without notes.

## Day 1: How Git stores history
- What I did: inspected commit, tree, blob; read .git/HEAD
- What broke / confused me:
- Command or fix to remember: git cat-file -p HEAD ; git log --oneline --graph --all
- Could I do it again without notes? yes / no

## Day 2: Feature branch, commit, push
- What I did: created feature/add-discount, added apply_discount to app/orders.py, checked it with git status and git diff, staged and committed it, pushed with -u, then merged the pull request on GitHub and ran git pull on main
- What broke / confused me: what "local main is one commit ahead of origin/main" means (main is my branch, origin/main is my last known copy of GitHub's main)
- Command or fix to remember: git switch -c ; git add ; git commit ; git push -u origin <branch>
- Could I do it again without notes? yes / no