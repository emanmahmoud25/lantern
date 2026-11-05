# Evidence B

**Student B:** Mohamed Hesham (`Mohamed-hesham-21`), collaborator and fork owner, SSH authentication.

---

## E1. Authentication Method

<img width="685" height="172" alt="Image" src="https://github.com/user-attachments/assets/b22d7f8f-1f8b-4f43-81b3-13187d3ec6b0" />

**Description:** `git clone git@github.com:emanmahmoud25/lantern.git` run from `D:\Temp`. The `git@github.com:` URL (rather than `https://`) shows that B authenticates over SSH with a key pair. The clone completes without a password prompt.

---

## E3. Commits, trees and blobs

### E3.1 – Commit hashes

<img width="1097" height="624" alt="Image" src="https://github.com/user-attachments/assets/07d7129d-065e-4c19-baf3-534d29501dc2" />

**Description:** `git log --oneline`. The two commits used for this exercise are highlighted:

- First commit: `822f0de` (`chore(scratch): add placeholder file`)
- Second commit: `64c2ed2` (`chore(scratch): remove placeholder file`)

### E3.2 – Root tree hashes

<img width="858" height="372" alt="Image" src="https://github.com/user-attachments/assets/e50ab146-4966-4839-96a7-3c2f086e8618" />

**Description:** `git cat-file -p 822f0de` and `git cat-file -p 64c2ed2`. Each commit object points to its own root tree, and the second commit's parent is the first one.

- Tree of `822f0de`: `b35ae564d36faad738b3d3480e2682789e3be49c` (parent `0f6dcfd`)
- Tree of `64c2ed2`: `e82a3767746a27e54dc24ea60d156d6a7513d948` (parent `822f0de`)

### E3.3 – File whose stored object is identical in both commits

<img width="810" height="137" alt="Image" src="https://github.com/user-attachments/assets/1adc97c4-6e78-4443-a2bc-0a8f56892dfc" />

**Description:** `git ls-tree 822f0de` and `git ls-tree 64c2ed2`. `README.md` has the same blob hash in both trees, so Git stores it only once.

- File: `README.md`
- Blob hash (unchanged in both): `aa7186593c45f99bb82b9bc52dac46c6d455f5d0`

### E3.4 – File whose stored object differs between commits

<img width="810" height="137" alt="Image" src="https://github.com/user-attachments/assets/3261c45c-dbd8-483b-b76a-d0c29b0498c7" />

**Description:** Same `git ls-tree` output. `scratch.txt` exists as the blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` in the first commit (`822f0de`) and is absent from the tree of the second commit (`64c2ed2`), because it was deleted there.

---

## E4. History graph after the Requirement 3 merges

<img width="1147" height="312" alt="Image" src="https://github.com/user-attachments/assets/102e4e11-0264-4160-b628-6ccb4e6260fd" />

**Description:** `git log --graph --oneline --all --decorate` after the Requirement 3 merges. `fix(storage): sort task keys alphabetically` (`6b865ed`) and `feat(storage): add pretty printing to json dump` (`d35c840`) diverge from the merge commit `9d0de04` and are joined by the merge commit `a4f1e44` (`refactor(storage): standardize task JSON formatting`). The history below `9d0de04` continues in a straight line. `HEAD -> main, origin/main, origin/HEAD` points to `8b7b236` (`fix(git): remove tracked files matching gitignore`). The lower part of the output repeats after the pager's `...skipping...` line.

---

## E5. Drill (b): commit made on main by mistake, moved to a branch, delivered by a merge

<img width="834" height="726" alt="Image" src="https://github.com/user-attachments/assets/3b5f3d52-89e5-4b75-b63f-7143baac5c7c" />

**Description:** `git log --oneline --graph --decorate -8`, `git show -s --format="merge: %H%nparents: %P%nsubject: %s" 654c9dd` and `git reflog -20`.

- Merge commit that delivered the drill: `654c9dd8c1489cb80980accd3b53d205686ffef6` (PR #20, "Merge pull request #20 from emanmahmoud25/docs/usage-heading"). Its parents are `2ae3fe9` (main) and `01c4ccb` (the branch `docs/usage-heading`), so it is a real two-parent merge.
- `HEAD@{7}` is the mistaken commit `01c4ccb` (`docs(usage): add usage heading section`), made while on `main`. `HEAD@{6}` is `reset: moving to HEAD~1`, which moved `main` back to `bdec781` while the commit stayed safe on the branch `docs/usage-heading`.
- `main` is protected, so the branch was pushed and delivered through PR #20.
- `fd465b0`, `b7445e3` and `ca9d56b` (`HEAD@{5}`, `HEAD@{3}`, `HEAD@{1}`) are local-only merges that were never pushed. They were discarded with `git reset --hard origin/main` (`HEAD@{0}`).
- Commit `de67c20` ("Error(usage): commited in main branch") was an earlier failed attempt that stays in history. It was noticed only after finishing the project.

---

## E6. Stash

### E6.1 – `git stash list`

<img width="986" height="64" alt="Image" src="https://github.com/user-attachments/assets/cd168dae-b6c6-4a35-b818-6cbe90cbc622" />

**Description:** `git stash list` shows one stash, `stash@{0}: On list--sort: list --sort in-progress`. It holds the unfinished `list --sort` work that was set aside to switch tasks.

### E6.2 – `git stash pop`

<img width="887" height="306" alt="Image" src="https://github.com/user-attachments/assets/a72563e9-c9e2-4e21-b185-9ddfa1b739ca" />

**Description:** `git stash pop` on branch `list--sort` (up to date with `origin/list--sort`). The change comes back as `modified: lantern.py` in the working directory, not staged, and the stash entry is removed (`Dropped refs/stash@{0} (2f92bf2a1722a0f2ff6b46c359757f7d01077e47)`).