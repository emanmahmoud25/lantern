# Evidence A

**Student A:** Eman Mahmoud Ahmed (`emanmahmoud25`), repository owner, HTTPS authentication.

---

## E1. Authentication Method

<img width="816" height="97" alt="Image" src="https://github.com/user-attachments/assets/82026ce6-f3e6-48e8-a8bb-33e2591bfad8" />

**Description:** `git remote -v` run inside A's clone of `lantern`. Both the fetch and the push URL for `origin` are `https://github.com/emanmahmoud25/lantern.git`. An `https://` URL (rather than `git@github.com:`) shows that A authenticates over HTTPS with a personal access token.

---

## E2. Same file staged and not staged

### E2.1 – `git status` with `notes.txt` in both sections

<img width="790" height="516" alt="Image" src="https://github.com/user-attachments/assets/0d68a8af-33ce-4305-839c-251857f43052" />

**Description:** `git status` on branch `main`, up to date with `origin/main`. The file `notes.txt` is listed twice: under *Changes to be committed* (green, the staged change) and under *Changes not staged for commit* (red, a second edit made after staging). This shows the staging area holding a different version of the file than the working directory.

### E2.2 – `git diff --cached` and `git diff` for `notes.txt`

<img width="801" height="367" alt="Image" src="https://github.com/user-attachments/assets/93778da5-64e4-42c6-8160-c0dac1f079ee" />

**Description:** Two diffs of the same file with different content.

- `git diff --cached` (index `42c27bb..e11a7b2`) compares HEAD with the staging area and shows the staged edit: the line `This is a placeholder draft file.` becomes `This is a placeholder draft file.First change - staged`.
- `git diff` (index `e11a7b2..fed559a`) compares the staging area with the working directory and shows only the second, unstaged edit: the added line `Second change - unstaged`.

---

## E4. History graph after the Requirement 3 merges

<img width="805" height="643" alt="Image" src="https://github.com/user-attachments/assets/5e983fe9-494a-4a29-964a-fb63af9c2c70" />

**Description:** `git log --graph --oneline --all --decorate` after the Requirement 3 merges. `fix(tasks): strip title whitespace` and `feat(tasks): add done flag` diverge from the same commit and are joined by the merge commit `9d0de04` (`merge(tasks): combine title and done changes`). The fast-forward merge adds no separate merge commit, so its commits appear in a straight line. The graph also shows B's `refactor(storage)` merge (`a4f1e44`), the `backup-before-phase2-undo` branch, and `HEAD -> main, origin/main, origin/HEAD` pointing to `4a1199f`. The lower part of the output repeats after the pager's `...skipping...` line.

---

## E5 (a). Reflog for drill (a): message typo

<img width="1137" height="493" alt="Image" src="https://github.com/user-attachments/assets/53ef4558-ab43-4a77-9a6f-951f06abbc23" />

**Description:** `git reflog -5` and `git reflog`. `HEAD@{4}` is the original commit `332819d` with the typo in its subject (`docs: add git practce note`). `HEAD@{3}` is `commit (amend)`, which rewrote it as `05c3ff4` with the corrected subject `docs: add git practice note`, with no extra "fix typo" commit.

## E5 (c). Reflog for drill (c): lost commit

<img width="1137" height="506" alt="Image" src="https://github.com/user-attachments/assets/247043e1-1e0a-4d78-b6f1-a706e4f2ac20" />

**Description:** Same reflog output, lines `HEAD@{2}` to `HEAD@{0}`. `HEAD@{2}` is the commit `dbea23b` (`docs: add reflog recovery note`). `HEAD@{1}` is `reset: moving to HEAD~1`, the reset that discarded it. `HEAD@{0}` is `reset: moving to dbea23b`, the recovery that brought the commit back onto `main`.

---

## E7. Rejected direct push to protected `main`

<img width="925" height="447" alt="Image" src="https://github.com/user-attachments/assets/31a49008-296a-43c7-8f32-ca39fc165da5" />

**Description:** A direct `git push origin main` after the protection rule was enabled. GitHub receives the objects but refuses the ref update: `remote: error: GH006: Protected branch update failed for refs/heads/main` with the reason `Changes must be made through a pull request`. The push ends with `! [remote rejected] main -> main (protected branch hook declined)` and `error: failed to push some refs`. This proves the rule applies to the repository owner as well.
