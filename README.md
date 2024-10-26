# CS504-Project
Our shared repo for the CS504 code.

## Configuration
To simplify coordination among developers I took the liberty of initializng a couple files into the repo. Since we are not all going to have the same file tree to reference data in, I've created a file at `./src/static.py` to contain individual data directories for each of the developers. By referencing this variable in any future code, the individual location of the data wont matter as it can be represented by `DATA_DIR`. This way I can store my data files in `/home/my_foldername/data/cs504` and someone else could store them in `/home/disco_still_cool/not_the_same_place` and the code would still find the data. 

I've also written a file called `config.py` which will setup your static.py file for you if you just run `python config.py` from the root of the repo.

## Main and Develop Branches
I also started a develop branch and put some protections on the main branch as is good practice. When you begin working on code in the repo pull down the develop branch and then work off it (or create a feature branch which you can then merge back in to develop) then when we have milestones in develop we can merge into main. 
