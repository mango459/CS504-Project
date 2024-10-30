# CS504-Project
Our shared repo for the CS504 code.

## Configuration
To simplify coordination among developers I took the liberty of initializng a couple files into the repo. Since we are not all going to have the same file tree to reference data in, I've created a file at `./src/static.py` to be updated with your individual directory to the data on your machine. By referencing this variable in any future code, the individual location of the data wont matter as it can be represented by `DATA_DIR`. This way I can store my data files in `/home/my_foldername/data/cs504` and someone else could store them in `/home/disco_still_cool/not_the_same_place` and the code would still find the data. 

I've also written a file called `config.py` which will setup your static.py file for you if you just run `python config.py` from the root of the repo.

## youTrack Integration
This repo has been integrated with youTrack to allow developers to reference specific issues and use a set of predefined commands to update them over on youTrack. This means if you add the commit message `[commit message text] #issueID [command 1] [command 2] ... [command n]
[issue comment text]
...` following that format you wont have to interact with the issue directly on youTrack. Reference command syntax here for more information on how to use: [Command Syntax](https://www.jetbrains.com/help/youtrack/server/apply-commands-in-vcs-commits.html#vcs-commit-command-syntax)
