# Demo API
---
This is a Demo Project to try djanngo-mptt to build texonomy in django, with features like drag child objects 
move objects around nodes (draggable), wherein only admin users can drag-shift nodes object and other users can view tree like structure built using Python Django.

---

### Getting Started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Programming Language and Frameowork
---
* Python
* Django 
* django-mptt

### Version Used
---
* Python: 3.7.2
* Django: 3.1


### Library Used
---
**P.S**:*For installation of required library or modules refer [requirement.txt](https://github.com/Pratik-Nikam/django-mptt/blob/master/requirements.txt) file and directly install using following command*
		$ pip install -r requirements.txt

### Prerequisites/Requirements
---
* Python
* Visual Studio Code/Sublime or any IDE

### Project Description
---
This project usage django-mptt to build tree like model-data view.
Admin models views has been modified to have view like tree. Admin can access tree structure 
and move model data around nodes using draggable feature of django-mptt.

Following are the sample urls deployed 
* https://djangotree.herokuapp.com/treeview/genres/ : Tree View in template
* https://djangotree.herokuapp.com/: Dashboard 

### Data Source
---
* SQLite3 database

## Run this Project in your machine.

1. Clone the project to your workspace.Please check for the requirements.txt and .gitignore files.
2. Create Virtual Env and Activate it
2. Activate base environement and run following command to install required libraries.

		$ pip install -r requirements.txt

3. In .gitignore file add necessary apps,files like migrtaions, __init__.py and append ignore('*') or not  ignore(!*/) as per your need.
4. Change the **settings:Database** and do the miggrations using following commands to create tabales.

		$ python manage.py makemigrations
		$ python manage.py migrate

5. Finally run server to run the project using following commands

		$ python manage.py migrate`

5. Finally run server to run the project using following commands

		$ python manage.py runserver`


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used


## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.
Please note we have a code of conduct, please follow it in all your interactions with the project.


## Authors

* **Developers**: Pratik Nikam


## License

[Pratik-Nikam](https://djangotree.herokuapp.com/) © Copyright (c).
All rights reserved.
# django-mptt