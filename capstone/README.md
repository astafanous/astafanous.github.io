# MY Capstone TITLE: DjangoPress

## Overview

**DjangoPress** is a content management system (CMS) built with Django, inspired by WordPress

Live Project: **Egphoto Gallery**

## Setup Instructions

```bash
django-admin startproject capstone
python manage.py startapp mysite

# To run the project locally:

git clone https://github.com/me50/fawzi2019.git
cd capstone directory
python manage.py makemigrations mysite
python manage.py migrate
python manage.py runserver

# Visit `http://127.0.0.1:8000/` in your browser.Users can Register and login

Note: Summernote is integrated via CDN (https://cdn.jsdelivr.net)

```

```markdown
## File Contributions

* models.py: Defined models for User, Post, Page, Category, and Comment.

Used ForeignKey relationships to link content types. Included a custom __str__ method for readable display. formatted.

Used auto_now_add and strftime formatting for timestamps.

* views.py: Implemented logic for user authentication, dashboard rendering, post/page creation and editing, comment, page_home,  addCategory, and dynamic content display

* urls.py: Mapped URL patterns to views, including dynamic slugs for individual posts and pages and all views

* admin.py: Registered models and customized the admin interface for easier content management.
* Added __str__ methods for readable admin display.

* templates/mysite/: Created 13 HTML templates for layout, dashboard, post/page views, forms, and navigation. Used Django’s template inheritance and Bootstrap for responsive design.

* templates/mysite/layout.html: Base template includes:

***Bootstrap, Font Awesome, Summernote

Custom styles and scripts

A carousel slide for autoplaying visuals

{% block body %} and {% block content %} ***for dynamic rendering For load A carousel slide for some page & another navbar for other page***

* static/mysite/main.js: Wrote JavaScript functions for dynamic page switching for single page , image animations with addEventListener and Initialize Summernote for Posts, pages .
- Use script of Initialize Summernote inside `edit_post.html`


* static/mysite/styles.css: Designed custom styles for layout, buttons, carousel slide, dropdown menus, accordion and mobile responsiveness & colors .
```
## Features

## Authentication & Navigation

Before login: Users see navbar login.html, register.html, and the public gallery (`index.html`)

#### Homepage | Visit Site(`index.html`)
After Layout Extend

Displays posts in a 3-column, 2-row layout

Each post includes title, image, excerpt, author, and “Read More” button linking to detailed in  `post.html`

Pagination for browsing older posts

After login: Access to (`dashboard.html`) with post/page management tools which contain navbar with *Egphoto Gallery menu* link to *Visit Site item* Homepage (`index.html`) and

## Main distribution  Dashboard

Left Sidebar navigation: Home, Posts, Pages, Categories, Comments

Main panel: Welcome message, previews of recent posts and pages

#### Home (`page_home.html`)

- Displays navbar "Egphoto Gallery menu"-->Visit Site Item (`index.html`) and interactive button group (1–7) triggers JavaScript showPage() function

Each section includes:

1. Gallery & Cultural Features

2. “Lotus Photo” – 15 animated images By JavaScript

3. Holy Family’s path to Egypt

4. Latest Posts

5. Carousel slides with hover effects

6. “Follow Me to Egypt”

7. “Why Choose Egypt” – featuring Abu Simbel Temple

#### Posts Management

Post model : title, excerpt, image, body, author, and category

*Add Post Item* for create post with rich text editing via Summernote(CDN) in `create.html`

Posts listed in `all_posts.html`, detailed in `post.html` has Body and Comments enabled via Comment model textarea input in main panel

Categories shown in the right sidebar after card img,

`edit_post.html` for updates via Summernote

#### Pages Management

Page model: title, imageUrl, content

Pages listed in all_pages.html, detailed in new_page.html

add_page.html for creation with Summernote
#### Comments

Previews latest comments

#### Users

Displays current user

Add User link to `register.html`

## Distinctiveness

**DjangoPress** is not a clone—it’s a reinterpretation of a CMS focused on cultural storytelling. Unlike typical CS50 projects such as social networks or e-commerce platforms, DjangoPress emphasizes editorial publishing and dynamic page creation.

* Combines a gallery-style Main distribution with a full-featured dashboard

The project introduces a Main Distribution Dashboard that mimics professional CMS interfaces, featuring sidebar navigation, dropdown menus, and modular content zones.


* The integration of Summernote via CDN allows for rich text editing without the overhead of heavy dependencies, aligning with DjangoPress’s lightweight philosophy.


**DjangoPress** is tailored for historical content presentation using Django’s template system and Python logic. What makes it distinct.

> Is its fusion of form and function: the homepage (index.html) presents posts in a visually engaging grid, while **Home** is the `page_home.html` view offers interactive sections like “Lotus Photo,” “Holy Family’s Path to Egypt,”"FOLLOW ME," and “Why Choose Egypt,” some powered by JavaScript animations and dynamic rendering. These aren’t static pages—they’re curated experiences that invite users to explore history through a modern lens and link them to some useful site.

## Complexity

- **DjangoPress** demonstrates advanced use of Django’s backend architecture and front-end integration.

- Handling form validation and CSRF tokens

- Dynamic Page Rendering: JavaScript showPage() function loads content without refreshing and  animation enlarge and rotate

- Rich Text Editing: Summernote integrated via CDN with HTML sanitization , JavaScript and database storage


- ***The project features multiple custom models***— **Post, Page, Category, and Comment** —linked via ForeignKey relationships and rendered dynamically through **Django’s template system**. Each model includes custom methods for timestamp formatting and __str__ method for readable display content, enhancing both UX and maintainability.

> Authentication is handled with Django’s built-in system, but extended to support role-based access to ***dashboard features*** login required else link to **Login**. Users dropdown menu Add User by link to **Register** and manage content through a secure interface that includes CSRF protection and form validation. The dashboard itself is a complex

* **Responsive Design:** Bootstrap and custom CSS for mobile-friendly layout

* Implementing pagination and user roles, content tagging, etc.

* **ORM Usage:** Leveraged Django’s ORM to query related models and format timestamps using strftime

## Challenges & Reflections

- Designing an intuitive dashboard while managing dynamic content was a major challenge.
- Integrating Summernote via CDN required careful handling of form submissions and HTML storage.
- Building the gallery with JavaScript functions that switch views without reloading pushed me to better understand DOM manipulation and Django’s static file handling.

>I chose this project because I’m passionate about Egyptian history and wanted to create a platform that presents it in a modern, engaging way. DjangoPress is more than a CMS—it’s a tribute to storytelling through technology and can be used in many different subjects beyond just mysite.
