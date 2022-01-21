# 2022-django-suorganizer
My exercise based on book of Django Core by Mr. Andrew Pinkham 
https://github.com/gurnitha/2022-django-suorganizer


### 1 Starting a New Django Project: Building a Startup Categorizer with Blog


        1. Defining the Project

        1. A page to list tags
        2. A page to list startups
        3. A page to list blog posts
        4. A page for each tag
        5. A page for each startup
        6. A page for each blog post (which also lists news articles)
        7. A page to add a new tag
        8. A page to add a new startup
        9. A page to add a new blog post
        10. A page to add and connect news articles to blog posts

        2. Creating a New Django Project and Django Apps

        - Install: 
        -- Python
        -- Pip
        - Create virtualenv
        - Activate virtualenv
        - Install Django 3.2.7
        - Create Django Project
        - Create Django Apps
        - Connecting django apps with the project in settings.py
        - Run the server
        - File structures

        E:.
        └───2022-django-suorganizer
            │   .gitignore
            │   LICENSE
            │   README.md
            │   TOC.txt
            │
            ├───blog
            │   │   admin.py
            │   │   apps.py
            │   │   models.py
            │   │   tests.py
            │   │   views.py
            │   │   __init__.py
            │   │
            │   └───migrations
            │           __init__.py
            │
            ├───organizer
            │   │   admin.py
            │   │   apps.py
            │   │   models.py
            │   │   tests.py
            │   │   views.py
            │   │   __init__.py
            │   │
            │   └───migrations
            │           __init__.py
            │
            └───suorganizer
                │   manage.py
                │
                └───suorganizer
                        asgi.py
                        settings.py
                        urls.py
                        wsgi.py
                        __init__.py        


#### 2 Hello World: Building a Basic Webpage in Django   

        modified:   README.md
        new file:   blog/urls.py
        modified:   blog/views.py
        modified:   suorganizer/urls.py
