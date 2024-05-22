## Learn Wagtail - Wagtailify your static website

by Kalob Taulien: https://learnwagtail.com/courses/wagtailify-your-static-website/

link to GitHub: https://github.com/CodingForEverybody/wagtailify-your-static-website

use PORT 8002 for `python manage.py runserver 0.0.0.0:8002` cmd for localhost instead of 8000 (avoid clashing with jisc-ac-uk setup)

### Customise python for this project
To use different versions of python in different projects use `pyenv` https://python.land/virtual-environments/pyenv
  - `su localadmin` then `brew install pyenv`
  - add pyenv to zsh shell
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOTbin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
  - restart your shell using `exec "$SHELL"` cmd

To manage the python virtual environment add `pyenv-virtualenv` as a plugin to pyenv https://github.com/pyenv/pyenv-virtualenv?tab=readme-ov-file
  - `su localadmin` then `brew install pyenv-virtualenv`
  - add pyenv-virtualenv to zsh shell
```
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```
  - restart your shell using `exec "$SHELL"` cmd

### Set-up
Set python preferred version in project root directory 
- add python version 3.11.4 using `pyenv install 3.11.4` cmd 
- set this project directory to use v3.10 with `pyenv local 3.11.4` cmd
Set up virtual environment in project root directory
- create vitual env using `pyenv virtualenv <venv_name>` cmd
- list all virtual envs with `pyenv virtualenvs` cmd
- start virtual env using `pyenv activate <venv_name>` cmd
- deactivate virtual env using `pyenv deactivate` cmd

### Course
1. Install Wagtail Learnings
   - Create project directory repo in GitHub and `git clone` project to local drive
   - Set project python version in project root directory using `pyenv local <python version>`
   - Create virtual environment for project to install python dependencies in this root folder only using `pyenv activate <name>`
   - Make sure virtual environment is active and run `pip install wagtail` to set up wagtail in this root directory
   - To create an app run `wagtail start <app_name> .`
     - the `.` makes sure the app is created at the root level
     - `wagtail start ...` command generates standard directories `home` and `search`, a `Dockerfile`, a `requirements.txt` file and a `manage.py` file as well as your `app_name` directory
     - Run `pip install -r requirements.txt` just to confirm django & wagtail installed correctly
     - Start server by opening a terminal and run `python manage.py runserver 0.0.0.0:<port>` 
       - default port is `8000`, but if you have other apps using that choose another port e.g. `8001`, `8002` etc
       - You will have a number of unapplied migrations which will need to run to provision the database
     - Open a 2nd terminal and run `python manage.py migrate` to install all the migrations on the server
     - Run `python manage.py createsuperuser` to create a login user for wagtail admin UI
       - name
       - email (optional)
       - password (8 characters requested, can overide)
       - repeat password
     - Go to `localhost:<port>` on oyur web browser and type user and password to access admin UI
  - Create a `.gitignore` file and copy contents of `.dockerignore` file into it, remove `static` folder from `.gitignore` 
    - add your virtual environment name to `gitignore` file
2. Visualise project

