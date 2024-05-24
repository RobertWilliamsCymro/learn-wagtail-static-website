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

### TL;DR Summary of Learnings
- set up local environment and create new wagtail app from scratch
- edit your app and set up base.html template page
- set up global code blocks used on all webpages in their own settings models 
- personalise default home_page to your wagtail content


### Course
1. & 2. Install summary

  Provides instructions for setting up a 'atlas' project in Wagtail. It covers creating a GitHub repo, setting up a Python virtual environment, installing Wagtail, starting the app, and configuring the Wagtail admin UI.

[Go to Lessons 1 & 2 learnings](Lesson-1-&-2.md)

3. Set up base.html summary

  Details the structure of a Wagtail project, highlighting the 'home' and 'app_name' directories. It explains how to modify 'home_page.html' to set 'base.html' as the Wagtail UI home page. It also describes the structure and functionality of 'base.html', including how to load static files, templatetags, and the Wagtail admin interface.

[Go to Lesson 3 learnings](Lesson-3.md)

4. Global template tags summary

  Provides instructions for creating a reusable navigation bar in a Wagtail project. It involves creating a 'navigation.html' file, setting up a Django template tag to fetch navigation pages, and integrating this navigation bar into the base template. Changes require server restart.
  
[Go to Lesson 4 learnings](Lesson-4.md)

5. New global class summary

  Provides instructions for adding social media links to the footer of every page in a Wagtail project. It involves creating a 'social_media.html' file, setting up a new Django app 'site_settings' for managing social media links, and integrating these links into the base template. Changes require database migrations and server restart.

[Go to Lesson 5 learnings](#5-set-up-global-social-media-links)

6. Using settings app summary

  Provides instructions for adding a logo and website name to the header and footer of every page in a Wagtail project. It involves creating a 'LogoSettings' model, setting up the logo and site name in the Wagtail admin UI, and integrating these elements into the navigation and social media templates. Changes require database migrations.

[Go to Lesson 6 learnings](#6-custom-logo-and-website-name)

7. Create Homepage Hero

Provides instructions for customizing the homepage in a Wagtail project. It involves modifying the `HomePage` model in `home/models.py` to include an author image, summary, and CTA button. These elements are then integrated into the `home_page.html` template using Wagtail's template tags. Changes require database migrations.

[Go to Lesson 7 learnings](Lesson-7.md)

8. Create Homepage Content


[Go to Lesson 8 learnings](Lesson-8.md)

9. 


[Go to Lesson 9 learnings](Lesson-9.md)

10. 


[Go to Lesson 10 learnings](Lesson-10.md)

11. 



[Go to Lesson 11 learnings](Lesson-11.md)

12. 


[Go to Lesson 12 learnings](Lesson-12.md)

13. 


[Go to Lesson 13 learnings](Lesson-13.md)

14. 




[Go to Lesson 14 learnings](Lesson-14.md)

15. 


[Go to Lesson 15 learnings](Lesson-15.md)

16. 


[Go to Lesson 16 learnings](Lesson-16.md)

17. 


[Go to Lesson 17 learnings](Lesson-17.md)
