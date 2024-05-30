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
- set up local environment and create new wagtail app `atlas` from scratch
- edit *atlas* app by modifying `templates/base.html` template page
- copy paste HTML and tailwind code for homepage into *home* app  `templates/home/home_page.html` with hard coded content
- create new *site_settings* app and register code blocks in `site_settings/models.py` to be served on all webpages from `atlas/templates/base.html`
- personalise wagtail default home_page to your wagtail content and inject into `home/../home_page.html` template
- create new *blog* app and set up `blog index` page, `blog` page and use a StreamField and StructBlock to mix and match content types in the body
- how to create and use snippets on pages


### Course
1. & 2. Install summary

  Provides instructions for setting up a 'atlas' project in Wagtail. It covers creating a GitHub repo, setting up a Python virtual environment, installing Wagtail, starting the app, and configuring the Wagtail admin UI.

[Go to Lessons 1 & 2 learnings](Lesson-1-&-2.md)

3. Set up base.html summary

  Details the structure of a Wagtail project, highlighting the 'home' and 'atlas' directories. It explains how to modify 'home_page.html' which extends 'base.html' as the Wagtail UI home page. It also describes the structure and functionality of 'base.html', including how to load static files, templatetags, and the Wagtail admin interface.

[Go to Lesson 3 learnings](Lesson-3.md)

4. Global template tags summary

  Provides instructions for creating a reusable navigation bar in a Wagtail project. It involves creating a 'navigation.html' file, setting up a Django template tag to fetch navigation pages, and integrating this navigation bar into the `base.html` template. Changes require server restart.
  
[Go to Lesson 4 learnings](Lesson-4.md)

5. New global class summary

  Provides instructions for adding social media links to the footer of every page in a Wagtail project. It involves creating a 'social_media.html' file, setting up a new Django app 'site_settings' for managing social media links, and integrating these links into the `base.html` template. Changes require database migrations and server restart.

[Go to Lesson 5 learnings](#5-set-up-global-social-media-links)

6. Creating site_settings app summary

  Provides instructions for adding a logo and website name to the header and footer of every page in a Wagtail project. It involves creating a 'LogoSettings' model, setting up the logo and site name in the Wagtail admin UI, and integrating these elements into the `navigation.html` and `social_media.html` templates. Changes require database migrations.

[Go to Lesson 6 learnings](#6-custom-logo-and-website-name)

7. Create homepage hero summary

Provides instructions for customizing the homepage in a Wagtail project. It involves modifying the `HomePage` model in `home/models.py` to include an author image, summary, and CTA button. These elements are then integrated into the `home_page.html` template using Wagtail's template tags. Changes require database migrations.

[Go to Lesson 7 learnings](Lesson-7.md)

8. Create homepage content summary

Provides instructions for enhancing the homepage in a Wagtail project. It involves adding 'My Story' and 'Blog Posts' sections to the `HomePage` model and template. The 'My Story' section uses static fields, while the 'Blog Posts' section dynamically pulls from the `BlogPage` model. Changes require database migrations.

[Go to Lesson 8 learnings](Lesson-8.md)

9. Creating blog app summary

Provides instructions to create a new Wagtail app called 'blog'. It includes creating the app, defining a `BlogIndexPage` model, making database migrations, and setting up the frontend with a `blog_index_page.html` template. It also explains how to link to the Blog Index page from the HomePage.

[Go to Lesson 9 learnings](Lesson-9.md)

10. & 11. Creating child pages and using StreamFields

Provides instructions for creating a child page in Wagtail, defining a new `BlogPage` model with various fields including a `StreamField`. It also guides on how to create a new template file for the blog page, and how to use Wagtail fields and StreamField in the template.

[Go to Lesson 10 & 11 learnings](Lesson-10-&-11.md)







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
