## 1. Install Wagtail and create 'atlas' app
  - Create project directory repo in GitHub and `git clone` project to local drive
  - Set project python version in project root directory using `pyenv local <python version>`
  - Create virtual environment for project to install python dependencies in this root folder only using `pyenv activate <name of environment>`
  - Make sure virtual environment is active and run `pip install wagtail` to set up wagtail in this root directory
  - To create an app 
    - run `wagtail start atlas .`
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
    - Go to `localhost:<port>` on your web browser and type user and password to access admin UI
  - Create a `.gitignore` file and copy contents of `.dockerignore` file into it
  - remove `static` folder from `.gitignore` 
  - add your virtual environment name to `gitignore` file

## 2. Visualise project
  - create a tree hierarchy for where each webpage will exist under Home page

[return to README.md](README.md#course)