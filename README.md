# Github API - Reports

A simple Django framework based project to -

* Search Github Users using username and retrieve relevant data.
* Saving the same in admin views.
* Filtering data with search bar in admin view.
* Creating reports on the basis of API requests per day/month/year.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need Django framework to run this project smoothly. Go to your terminal and execute the following command or visit [Django](https://www.djangoproject.com/) website.

```
pip install django
```

### Deployment

A step by step series of examples that tells what you have to do to get this project running -

* Enter the project directory.
* Make migrations for the project -

```
python manage.py makemigrations
```

* Migrate the changes -

```
python manage.py migrate
```

* Create SuperUser-

```
python manage.py createsuperuser

Provide username, email and password and remember it matey!
Default added = username - admin | password - admin12345
```

* Run the server -

```
python manage.py runserver
```

* Access http://127.0.0.1:8000/ on your browser to use the application.

### Usage

* Add username in search bar and hit 'Get data' to retrieve user data.<br />
* Access Admin Panel by clicking 'Admin Panel' button.<br />

![Screenshot](/Screenshots/Welcome_Page.png)

* Authenticate yourself to enter admin table.<br />
![Screenshot](/Screenshots/Authentication.png)

* Choose '1_User_Data' to access user data table to see all API calls.<br />
![Screenshot](/Screenshots/User_Data.png)

* Use Search bar to filter data according to fields given in table.<br />
![Screenshot](/Screenshots/Search_Filter.png)

* Choose 'Report Today' to review report of API calls done on present date.<br />
* Choose 'Report Month' to review report of API calls done in past month.<br />
* Choose 'Report Year' to review report of API calls done in present year.<br />
![Screenshot](/Screenshots/User_Data_Year.png)

## Built With

* [Django](https://www.djangoproject.com/) - Python web framework used.
* [Python](https://www.python.org/) - Python programming language.
* [Bower](https://bower.io/) - A Package Manager for the web.

## Contributing

If you want to contribute to this project, for some reason I won't understand, then you can create a pull request. Happy Coding!

## Versioning

Version 1.something Mehh...

## Authors

* **Shivam Kapoor** - An avid learner who likes to know every tiny detail in working of real life systems. Real enthusiast of cyber security and underlying networking concepts. (Email - kapoor.shivam88@gmail.com)

## License

Too lazy to decide on a License. zZzZ

## Acknowledgments

* YouTube Videos __/\\__
* StackOverFlow xD
* Django Documentation FTW
