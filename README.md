# Git Python Task Manager

A simple command-line Task Manager built using Python.

## Project Features

- Add tasks
- View tasks
- Mark tasks as completed
- Simple menu-driven interface
- Object-oriented Python structure

## Project Structure

```text
git-python-task-manager/
│
├── main.py
├── task.py
├── task_manager.py
├── utils.py
├── README.md
└── .gitignore


Python Files
main.py

Contains the main application loop and connects all other modules.

task.py

Contains the Task class.

task_manager.py

Contains the TaskManager class for managing tasks.

utils.py

Contains helper functions such as displaying the menu and collecting task information.

How to Run

Open the terminal inside the project folder.

Run:

python main.py
Git Commands Demonstrated

This project demonstrates:

git init
git status
git add
git commit
git log
git diff
.gitignore
Git Commit History

The project contains multiple meaningful commits showing the development process.

Author

Urmil Kashyap


---

# 4. Open the project in VS Code

Open VS Code.

Go to:

**File → Open Folder**

Select:

```text
git-python-task-manager

Then open the VS Code terminal:

Terminal → New Terminal

Check that you are inside the project folder:

pwd

On Windows PowerShell, you can also use:

Get-Location
5. Initialize Git

Run:

git init

You should see something similar to:

Initialized empty Git repository

Now check Git status:

git status

You should see your untracked files.

This demonstrates:

git init
git status
6. Make your first commit

Initially, create the basic project files:

main.py
task.py
README.md

Then:

git status

Add them:

git add main.py task.py README.md

Check status:

git status

Commit:

git commit -m "Initial project setup"

Now check:

git log --oneline

You should see:

abc1234 Initial project setup
7. Second meaningful commit

Now add task_manager.py.

Run:

git status

Then:

git add task_manager.py

Commit:

git commit -m "Add task manager functionality"

Check:

git log --oneline

You now have 2 commits.

8. Demonstrate git diff

Now modify task_manager.py.

For example, change:

print("Task added successfully.")

to:

print("Task added successfully!")

Before committing, run:

git diff

Git will show the exact change you made.

For example:

- print("Task added successfully.")
+ print("Task added successfully!")

This is an important part of your assignment because it proves you understand what git diff does.

Now commit the change:

git add task_manager.py
git commit -m "Improve task messages"

You now have 3 commits.

9. Third/fourth Python file

Add utils.py.

Run:

git status

Then:

git add utils.py

Commit:

git commit -m "Add utility functions"

You now have 4 commits.

10. Add .gitignore

Create:

.gitignore

Add:

__pycache__/
*.pyc
.env
.venv/
venv/
tasks.json

Then:

git status

You should see .gitignore.

Add it:

git add .gitignore

Commit:

git commit -m "Add gitignore configuration"

Now you have 5 meaningful commits.

That satisfies the minimum requirement.

11. Check your complete Git history

Run:

git log --oneline

You should have something similar to:

a91f321 Add gitignore configuration
b82e654 Add utility functions
c73d921 Improve task messages
d64e812 Add task manager functionality
e51f703 Initial project setup

Your commit IDs will be different.

You can also run:

git log

for the detailed history.

12. Check final Git status

Run:

git status

Ideally you should see:

nothing to commit, working tree clean

This is a good screenshot for your assignment.

13. Test your Python application

Run:

python main.py

You should get:

===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Complete Task
4. Exit
Enter your choice:

Try:

1

Then enter:

Learn Git
Practice Git commands

Then choose:

2

You should see your task.

14. Create the GitHub repository

Go to GitHub and create a new repository.

Repository name:

git-python-task-manager

Choose:

Public

Important: Do not add another README from GitHub because you already created one locally.

15. Connect your local project to GitHub

GitHub will give you a repository URL similar to:

https://github.com/YOUR_USERNAME/git-python-task-manager.git

In your VS Code terminal:

git remote add origin https://github.com/YOUR_USERNAME/git-python-task-manager.git

Check it:

git remote -v

Then rename your branch to main:

git branch -M main

Finally push:

git push -u origin main
16. Verify GitHub

Refresh your GitHub repository.

We should see:

.gitignore
README.md
main.py
task.py
task_manager.py
utils.py

And your commit history should contain at least:

Initial project setup
Add task manager functionality
Improve task messages
Add utility functions
Add gitignore configuration
Commands you need to demonstrate

For your YouTube video, show these commands one by one:

git init
git status
git add .
git commit -m "Initial project setup"
git log --oneline

Make a code change and then:

git diff

Then:

git add .
git commit -m "Improve task messages"

Finally:

git status

and:

git push -u origin main
Your assignment checklist
Requirement	Completed
Python project created locally	✅
Git initialized	✅
At least 4 Python files	✅
git init demonstrated	✅
git status demonstrated	✅
git add demonstrated	✅
git commit demonstrated	✅
git log demonstrated	✅
git diff demonstrated	✅
.gitignore added	✅
At least 5 meaningful commits	✅
GitHub repository	✅
Repository published	✅


PS E:\Git Repository from Scratch> git init
Initialized empty Git repository in E:/Git Repository from Scratch/.git/
PS E:\Git Repository from Scratch> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md
        main.py
        task.py
        task_manager.py
        utils.py

nothing added to commit but untracked files present (use "git add" to track)
PS E:\Git Repository from Scratch> git add main.py task.py README.md
PS E:\Git Repository from Scratch> git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
        new file:   main.py
        new file:   task.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        task_manager.py
        utils.py

PS E:\Git Repository from Scratch> git commit -m "Initial project setup"
[master (root-commit) 2f7babd] Initial project setup
 3 files changed, 465 insertions(+)
 create mode 100644 README.md
 create mode 100644 main.py
 create mode 100644 task.py
PS E:\Git Repository from Scratch> git log --oneline
2f7babd (HEAD -> master) Initial project setup
PS E:\Git Repository from Scratch> git status                       
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        task_manager.py
        utils.py

nothing added to commit but untracked files present (use "git add" to track)
PS E:\Git Repository from Scratch> git add task_manager.py
PS E:\Git Repository from Scratch> git commit -m "Add task manager functionality"
[master 0ead3f4] Add task manager functionality
 1 file changed, 23 insertions(+)
 create mode 100644 task_manager.py
PS E:\Git Repository from Scratch> git log --oneline
0ead3f4 (HEAD -> master) Add task manager functionality
2f7babd Initial project setup
PS E:\Git Repository from Scratch> git diff
diff --git a/task_manager.py b/task_manager.py
index 0df6880..d479baa 100644
--- a/task_manager.py
+++ b/task_manager.py
@@ -4,7 +4,7 @@ class TaskManager:
 
     def add_task(self, task):
         self.tasks.append(task)
-        print("Task added successfully.")
+        print("Task added successfully!")
 
     def show_tasks(self):
PS E:\Git Repository from Scratch> git add task_manager.py
PS E:\Git Repository from Scratch> git commit -m "Improve task messages"
[master 648f102] Improve task messages
 1 file changed, 1 insertion(+), 1 deletion(-)
PS E:\Git Repository from Scratch> git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        utils.py

nothing added to commit but untracked files present (use "git add" to track)
PS E:\Git Repository from Scratch> git add utils.py
PS E:\Git Repository from Scratch> git commit -m "Add utility functions"
[master 92e3bbe] Add utility functions
 1 file changed, 12 insertions(+)
 create mode 100644 utils.py
PS E:\Git Repository from Scratch> git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)
PS E:\Git Repository from Scratch> git add .gitignore
PS E:\Git Repository from Scratch> git commit -m "Add gitignore configuration"
[master f825edc] Add gitignore configuration
 1 file changed, 6 insertions(+)
 create mode 100644 .gitignore
PS E:\Git Repository from Scratch> git log --oneline
f825edc (HEAD -> master) Add gitignore configuration
92e3bbe Add utility functions
648f102 Improve task messages
0ead3f4 Add task manager functionality
2f7babd Initial project setup
PS E:\Git Repository from Scratch> git log
commit f825edc4cdd2f712b5c28110c11f8a8ec0162396 (HEAD -> master)
Author: Urmil <urmilkashyap845@gmail.com>
Date:   Thu Sep 24 08:08:12 2026 +0530

    Add gitignore configuration

commit 92e3bbe5b412bec5fac6dcc690a9eb232d4a298c
Author: Urmil <urmilkashyap845@gmail.com>
Date:   Thu Sep 24 08:07:48 2026 +0530

    Add utility functions

PS E:\Git Repository from Scratch> git status
On branch master
nothing to commit, working tree clean
PS E:\Git Repository from Scratch> python main.py

===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Complete Task
4. Exit
Enter your choice: 1
Enter task title: learn git
Enter task description: practice git commands
Task added successfully!

===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Complete Task
4. Exit
Enter your choice: 2

Task 1
Title: learn git
Description: practice git commands
Status: Pending

===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Complete Task
4. Exit
Enter your choice: 3

Task 1
Title: learn git
Description: practice git commands
Status: Pending
Enter task number to complete: 1
Task marked as completed.

===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Complete Task
4. Exit
Enter your choice: 4
Thank you for using Task Manager.
PS E:\Git Repository from Scratch> git remote add origin https://github.com/shanukashyap/Git-Repository-from-Scratch.git
PS E:\Git Repository from Scratch> git remote -v
origin  https://github.com/shanukashyap/Git-Repository-from-Scratch.git (fetch)
origin  https://github.com/shanukashyap/Git-Repository-from-Scratch.git (push)
PS E:\Git Repository from Scratch> git branch -M main
PS E:\Git Repository from Scratch> git push -u origin main
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 12 threads
Compressing objects: 100% (16/16), done.
Writing objects: 100% (17/17), 4.18 KiB | 534.00 KiB/s, done.
Total 17 (delta 5), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (5/5), done.
To https://github.com/shanukashyap/Git-Repository-from-Scratch.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.