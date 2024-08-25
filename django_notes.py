zaykahub.com
===============
1) Create a virtual env :
-------------------------
    python3 -m venv zaykahub_env
	// after this also if we check pip3 freeze It'll still show system wide pkgs. So need to activate created venv..
	
	$ source zaykahub_env/Scripts/activate
	(zaykahub_env)

	$ pip3 freeze
	(zaykahub_env)


2) Install Django
----------------------------
   pip3 install django
   //after Installation...
   $ pip3 freeze
	asgiref==3.8.1
	Django==4.2.15
	sqlparse==0.5.1
	typing_extensions==4.12.2
	tzdata==2024.1
	(zaykahub_env)
    Note: Django uses asgiref to support both synchronous and asynchronous views and operations, enabling compatibility with ASGI servers and allowing Django to handle asynchronous tasks.
	
3) Creating a project:
-------------------------
    $ django-admin -h

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).
(zaykahub_env)


   $ django-admin startproject zaykahub
	


4)Run project:
---------------
	$ python manage.py runserver
	
	
example:
----------
urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]


Explanation of path('', views.home, name='home'):
--------------------------------------------------
'': The first argument is the URL pattern. An empty string ('') means this view will be triggered when you visit the root URL (http://127.0.0.1:8000/).
views.home: The second argument specifies the view function to be called when the URL pattern matches. Here, it’s the home function in your views.py file.
name='home': The name parameter is an optional keyword argument that assigns a name to the URL pattern. This name can be used to refer to this URL pattern in templates or other parts of your code using the {% url %} template tag or the reverse() function.

How to Use name='home':
----------------------
The name parameter is useful for reverse URL resolution. For example, in a template, you can link to this view like this:
<a href="{% url 'home' %}">Home</a>
This will generate a link to the root URL (http://127.0.0.1:8000/). If you later change the URL pattern for this view, you only need to update it in urls.py, and all template links using {% url 'home' %} will automatically update.


How Django Passes the Request Automatically
-------------------------------------------
In Django, when a user accesses a URL, Django does the following:
URL Routing: Django looks up the URL pattern in the urlpatterns list in urls.py. In your case:
path('', views.home, name='home')
Django sees that the root URL ('') should call the home view function.

Request Handling: When the URL is matched, Django automatically creates a HttpRequest object. This object contains all the information about the incoming request (e.g., GET/POST data, headers, user session, etc.).

Calling the View: Django then passes this HttpRequest object as the first argument to your view function. That’s why your view function needs to accept the request parameter:


def home(request):
    return HttpResponse("Hello Shailesh")

Returning a Response: Your view returns an HttpResponse object that Django sends back to the client (e.g., the browser).



Django’s Approach vs. Tornado’s Approach
------------------------------------------
Django: It abstracts away the need for manual request handling classes. You define a simple function that takes a request, and Django handles all the routing, object creation, and passing of the request behind the scenes.

Tornado: You define request handlers as classes and manually map them to URLs, offering more control but requiring more boilerplate code.



Summary of How Django Handles Requests Automatically:
------------------------------------------------------
Request Object Creation: Django creates a request object when it matches a URL.
Automatic Passing of Request: Django passes the request object as the first argument to your view function.
Simplified View Functions: You focus on the logic in your view, without worrying about manual request handling.



render:
-------
In Django, render() is a function used to combine a template with a context (data) and return an HttpResponse object with that rendered text. It’s a convenient shortcut that helps you display HTML templates with dynamic data.

The Purpose of render()
The render() function simplifies the process of:

Loading an HTML template.
Filling the template with dynamic data.
Returning the rendered template as an HttpResponse.


How Django Finds Templates Using render()
-----------------------------------------
In Django, when we use the render() function to return a template (e.g., render(request, "home.html")), it automatically knows where to look for the template based on the TEMPLATES setting in settings.py.

Key Points:
TEMPLATES Setting in settings.py:

DIRS: This specifies custom directories for templates, usually pointing to a templates/ folder in our project.
'DIRS': ['templates'],  //set this 

APP_DIRS=True: When enabled, Django also searches inside each installed app's templates/ folder.
Template Search Order:

Django first checks the directories listed in DIRS.
Then, if APP_DIRS is set to True, it checks the templates/ folder in each installed app.

myproject/
├── templates/
│   └── home.html
└── myapp/
    └── templates/
        └── home.html

In this structure, Django will first look for home.html in the project-level templates/ directory, and then in each app's templates/ folder.

This setup allows us to use render(request, "home.html") without specifying the full path, as Django knows where to find the templates based on the project configuration.




Craeting a Superuser:
=====================

$ python manage.py createsuperuser

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.   
Run 'python manage.py migrate' to apply them.
Traceback (most recent call last):
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\backends\utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\backends\sqlite3\base.py", line 328, in execute
    return super().execute(query, params)
sqlite3.OperationalError: no such table: auth_user

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\shailesh2\zaykahub\zaykahub\manage.py", line 22, in <module>
    main()
  File "D:\shailesh2\zaykahub\zaykahub\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\core\management\__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\core\management\__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\core\management\base.py", line 412, in run_from_argv
    self.execute(*args, **cmd_options)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\contrib\auth\management\commands\createsuperuser.py", line 88, in execute
    return super().execute(*args, **options)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\core\management\base.py", line 458, in execute
    output = self.handle(*args, **options)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\contrib\auth\management\commands\createsuperuser.py", line 109, in handle
    default_username = get_default_username(database=database)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\contrib\auth\management\__init__.py", line 168, in get_default_username
    auth_app.User._default_manager.db_manager(database).get(
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\models\query.py", line 633, in get
    num = len(clone)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\models\query.py", line 380, in __len__
    self._fetch_all()
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\models\query.py", line 1881, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\models\query.py", line 91, in __iter__
    results = compiler.execute_sql(
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\models\sql\compiler.py", line 1562, in execute_sql
    cursor.execute(sql, params)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\backends\utils.py", line 102, in execute
    return super().execute(sql, params)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\backends\utils.py", line 67, in execute
    return self._execute_with_wrappers(
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\backends\utils.py", line 80, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\backends\utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\backends\utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
  File "D:\shailesh2\zaykahub\zaykahub_env\lib\site-packages\django\db\backends\sqlite3\base.py", line 328, in execute
    return super().execute(query, params)
django.db.utils.OperationalError: no such table: auth_user
(zaykahub_env) 



$ python manage.py showmigrations
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
(zaykahub_env)

The [ ] indicates that these migrations are pending (not yet applied).

App Names: The output is grouped by Django apps, such as admin, auth, contenttypes, and sessions. These are built-in apps that come with Django. Each app can have its own set of migrations.

Migration Files: Under each app, the list of migration files is shown. For example:
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices

These migrations are listed in the order they would be applied. The 0001_initial migration is usually the one that creates the necessary tables for that app (e.g., the auth_user table in the auth app).

[ ] Indicator: The [ ] symbol means the migration has not been applied yet. Once applied, it will change to [X].


Next Steps
-----------
python manage.py migrate
This will create the required tables and apply all pending migrations.

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(zaykahub_env) 

Check Migration Status Again: After running migrate, you can check the status again with:

$ python manage.py showmigrations
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
 [X] 0012_alter_user_first_name_max_length
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
sessions
 [X] 0001_initial
(zaykahub_env) 


Create Superuser: Once the migrations are applied, you can proceed with creating a superuser using:
----------------
$ python manage.py createsuperuser
Username (leave blank to use 'shaileshyadav'): shaileshyadav7958@gmail.com
Email address: shaileshyadav7958@gmail.com
Password:
Password (again):
Superuser created successfully.
(zaykahub_env) 




Why Migrations Are Important
==============================
Migrations are crucial in Django because they handle database schema changes in a systematic way. Whether you are adding new models, changing fields, or deleting tables, migrations ensure that these changes are applied to your database in the correct order without losing data or breaking the application.

makemigrations vs. migrate
--------------------------
makemigrations: This command doesn’t affect the database directly. It analyzes your models and creates migration files that describe the changes needed in the database schema (e.g., adding a table, modifying a field). Think of it as creating a "plan" for what needs to change.

migrate: This command applies those migration files to your database. It’s the actual execution of the "plan" created by makemigrations. During this process, Django modifies your database structure according to the migration files.

1. Model Changes
   |
   |---> makemigrations
   |       |
   |       |---> Generates migration files (e.g., 0001_initial.py)
   |               |
   |               |---> Describes the changes like creating a table, adding a field
   |
   |---> migrate
           |
           |---> Reads the migration files
                   |
                   |---> Applies the changes to the actual database (creates/updates tables)


Diagram Visualization
========================

+----------------------+      +---------------------+
|   Django Models      |      |   Database Schema   |
| (models.py)          |      |  (Tables, Fields)   |
+----------------------+      +---------------------+
            |                           ^
            |                           |
       Model Changes                Database Changes
            |                           ^
            |                           |
     makemigrations                    migrate
            |                           |
            |-----> Generates          Applies Migration Files
                    Migration Files
                    (e.g., 0001_initial.py)


Key Differences Between makemigrations and migrate
---------------------------------------------------
Command	Purpose	When to Use
makemigrations	Creates migration files based on model changes	Run this after making changes to your models (e.g., adding a new field)
migrate	Applies the migration files to the database	Run this to execute the schema changes in the database


How Django Manages Database Differences
----------------------------------------
Database Abstraction Layer (DBAL): Django’s Database Abstraction Layer allows us to write database-agnostic code. Whether we are running migrations or querying data, this layer ensures our code is translated appropriately for the underlying database.

Database Backends: Django comes with built-in backends for major databases:

django.db.backends.sqlite3: SQLite
django.db.backends.postgresql: PostgreSQL
django.db.backends.mysql: MySQL
django.db.backends.oracle: Oracle
These backends generate database-specific SQL commands based on our models and migrations.

ORM (Object-Relational Mapping): Django’s ORM provides a high-level interface to work with our database using Python objects. The ORM handles the conversion of our Python code into SQL queries that are optimized for the target database.

Migration System: Django’s migration system works in tandem with the database backends. When we make changes to our models (like adding fields or new tables), the migration system generates appropriate SQL commands that match our database’s requirements.

Database-Independent Migration Files: Migration files generated by makemigrations are database-agnostic. The migration files describe schema changes in Python code, which Django then converts into the appropriate SQL when we run migrate.


Example: Handling Database-Specific SQL
Let’s say we define a model:

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

The migration file would include:

class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('salary', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]

For PostgreSQL, Django might generate:
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary NUMERIC(10, 2)
);


For SQLite, Django might generate:
CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    salary DECIMAL(10, 2)
);
