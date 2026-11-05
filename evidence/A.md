Evidence A
Student A: Eman Mahmoud Ahmed (emanmahmoud25), repository owner, HTTPS authentication.
________________________________________
E1. Authentication Method
E1 – Remotes of A’s clone (HTTPS)

<img width="662" height="72" alt="Image" src="https://github.com/user-attachments/assets/d4910e84-efc7-464b-9976-bbb7b1ca0e87" />
 
E1 – git remote -v showing HTTPS remote
Description: git remote -v was run inside A’s clone of the Lantern repository. Both the fetch and push URLs for origin use HTTPS (https://github.com/emanmahmoud25/lantern.git). A uses HTTPS authentication with a Personal Access Token (PAT), as required by the project instructions.
________________________________________
E2. Same file staged and not staged
E2.1 – git status with notes.txt in both sections

 <img width="631" height="406" alt="Image" src="https://github.com/user-attachments/assets/943348ba-b5b4-40b9-9313-854e24f50d51" />
 
E2 – git status showing notes.txt staged and unstaged
Description: git status on branch main, up to date with origin/main. The file notes.txt is listed twice: under Changes to be committed (green, the staged change) and under Changes not staged for commit (red, a second edit made after staging). This shows the staging area holding a different version of the file than the working directory.
E2.2 – git diff --cached and git diff for notes.txt

 <img width="628" height="289" alt="Image" src="https://github.com/user-attachments/assets/ca965099-2a3d-4e98-8362-a20ee428e8df" />
 
E2 – git diff –cached and git diff for notes.txt
Description: Two diffs of the same file with different content.
•	git diff --cached (index 42c27bb..e11a7b2) compares HEAD with the staging area and shows the staged edit: the line This is a placeholder draft file. becomes This is a placeholder draft file.First change - staged.
•	git diff (index e11a7b2..fed559a) compares the staging area with the working directory and shows only the second, unstaged edit: the added line Second change - unstaged.
________________________________________
E4. History graph after the Requirement 3 merges
E4.1 – Commit, root tree and blob hashes of two commits

 <img width="952" height="759" alt="Image" src="https://github.com/user-attachments/assets/df8f6e3f-ac86-4fe7-b922-30b7fb664073" />
 
E4 – git show and git ls-tree output for 05c3ff4 and dbea23b
Description: git show -s --format="Commit: %H%nRoot tree: %T%nSubject: %s" for 05c3ff4 (docs: add git practice note, root tree fda8102947c189ebfc77d9eddb2dd286070ed049) and dbea23b (docs: add reflog recovery note, root tree b094d25afb5b16105af07514b79288865b9a8859), followed by git ls-tree for tasks.py and notes.txt. tasks.py has the same blob 1371de4f24b58cc5c07802b42083c948df08ba5f in both commits, while notes.txt has different blobs (db806b03… and 7f7f6f75…), showing that Git stores unchanged files once and re-stores only changed ones.
E4.2 – Full history graph

 <img width="638" height="511" alt="Image" src="https://github.com/user-attachments/assets/099a3b70-6b16-4d46-b35e-09e97155dbf3" />
 
E4 – git log –graph –oneline –all –decorate
Description: git log --graph --oneline --all --decorate after the local merges and later pulls. It shows A’s Requirement 3 result: fix(tasks): strip title whitespace and feat(tasks): add done flag diverge from the same commit and are joined by merge commit 9d0de04 (merge(tasks): combine title and done changes). The fast-forward merge adds no separate merge commit, so its commits appear in a straight line. The graph also shows B’s refactor(storage) merge (a4f1e44), the backup-before-phase2-undo branch, and HEAD -> main, origin/main, and origin/HEAD pointing to 4a1199f. The lower part of the output repeats after the pager’s ...skipping... line.

________________________________________
E5. Reflog for drills (a) and (c)
E5 – git reflog -5 and full git reflog

 <img width="906" height="396" alt="Image" src="https://github.com/user-attachments/assets/8ca3c216-bc1f-42ea-9662-a79b5812ea9b" />
 
E5 – git reflog showing the amend and the reset recovery
Description: Reflog output covering both of A’s undo drills.
•	Drill (a), message typo: HEAD@{4} is the original commit 332819d with the typo in its subject (docs: add git practce note). HEAD@{3} is commit (amend) which rewrote it as 05c3ff4 with the corrected subject docs: add git practice note, with no extra “fix typo” commit.
•	Drill (c), lost commit: HEAD@{2} is the commit dbea23b (docs: add reflog recovery note). HEAD@{1} is reset: moving to HEAD~1, the hard reset that discarded it. HEAD@{0} is reset: moving to dbea23b, the recovery that brought the commit back onto main.
________________________________________
E7. Rejected direct push to protected main
E7 – git push origin main rejected by branch protection

 <img width="741" height="361" alt="Image" src="https://github.com/user-attachments/assets/4c6547aa-50b3-4147-8c83-410e9ca02f2a" />
 
E7 – push rejected with GH006 protected branch error
Description: A direct git push origin main after the protection rule was enabled. GitHub receives the objects but refuses the ref update: remote: error: GH006: Protected branch update failed for refs/heads/main with the reason Changes must be made through a pull request. The push ends with ! [remote rejected] main -> main (protected branch hook declined) and error: failed to push some refs. This proves the rule applies to the repository owner as well.
