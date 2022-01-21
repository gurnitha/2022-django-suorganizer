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


#### 3 Programming Django Models and Creating a SQLite Database

        Specifying and Organizing Data in Django Using Models

        - Tag
            - tag name
            - slug

        - Startup
            - name of company
            - slug
            - description or purpose
            - date founded
            - contact email
            - website
            - tags: a startup can have many tags

        - News Link
            - title or headline
            - publication date
            - link to article
            - startaup (foreign key to Startup)

        - Blog Post
            - post title
            - slug
            - post text or description
            - publication date (not seen in admin, 
              but automatically added using auto_now_add=True)
            - tags: a post can have many tags
            - startups: a post can have many startups

        - One-to-Many Relationship
            - news articles and startup

        - Many-to-Many Relationships
            - startup and tag
            - blog post and tag
            - blog posts and startup

        modified:   README.md
        modified:   blog/admin.py
        new file:   blog/migrations/0001_initial.py
        modified:   blog/models.py
        modified:   organizer/admin.py
        new file:   organizer/migrations/0001_initial.py
        modified:   organizer/models.py


#### 4. Rapidly Producing Flexible HTML with Django Templates

        modified:   README.md
        new file:   blog/templates/blog/base_blog.html
        new file:   blog/templates/blog/post_detail.html
        new file:   blog/templates/blog/post_list.html
        modified:   blog/urls.py
        new file:   organizer/templates/organizer/base_organizer.html
        new file:   organizer/templates/organizer/startup_detail.html
        new file:   organizer/templates/organizer/startup_list.html
        new file:   organizer/templates/organizer/tag_detail.html
        new file:   organizer/templates/organizer/tag_list.html
        new file:   organizer/urls.py
        modified:   organizer/views.py
        modified:   suorganizer/settings.py
        modified:   suorganizer/urls.py
        new file:   templates/base.html


        NOTE:

        From the db:
        
        1. At this stage, it is possible to view
           http://127.0.0.1:8000/
           to view 

            Startup Organizer
            Startup List
            Startup 1
            Startup 2
            © 2015 Andrew Pinkham

            Created for Django Unleashe

        2. To view http://127.0.0.1:8000/tags/

            Startup Organizer
            Tag List
            Cowboys
            Django
            Mobile
            Ninjas
            Pirates
            Web
            © 2015 Andrew Pinkham

            Created for Django Unleashed


### 5 Creating Webpages with Controllers in Django: Views and URL Configurations


#### 5.1 Building Tag Detail Webpage and Generating 404 Errors for Invalid Queries

        modified:   README.md
        modified:   organizer/urls.py
        modified:   organizer/views.py

        NOTE:

        1. To view tags, visit: http://127.0.0.1:8000/tags/
        2. To view tag of django, visit: http://127.0.0.1:8000/tag/django/        
        3. To view error, visit: http://127.0.0.1:8000/tag/djangoxx/


#### 5.2 Implementing the Views and URL Configurations to the Rest of the Site

        modified:   README.md
        modified:   blog/urls.py
        modified:   organizer/urls.py
        modified:   organizer/views.py


#### 5.3 Building a Startup Detail Page

        modified:   README.md
        modified:   blog/urls.py
        modified:   blog/views.py
        modified:   organizer/urls.py
        modified:   organizer/views.py

        NOTE:

        1. To view startups
           visit: http://127.0.0.1:8000/
        2. To view a startup
           visit: http://127.0.0.1:8000/2022/01/great-responsive-template/


### 6 Integrating Models, Templates, Views, and URL Configurations to Create Links between Webpages


#### 6.1 Using the url Template Tag to Build a Navigation Menu

        modified:   README.md
        modified:   blog/templates/blog/post_list.html
        modified:   templates/base.html


#### 6.2 Tag Detail: Using url to Create Detail Page Links

        modified:   README.md
        modified:   organizer/templates/organizer/tag_list.html

