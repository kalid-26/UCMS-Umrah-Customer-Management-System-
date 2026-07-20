# UCMS(Umrah Customer Management System)
UCMS (Umrah Customer Management System) is a web application built to help Umrah travel agencies manage their customers, applications, packages, and payments in one place.

The project started as a learning project to practice building a complete Django application from planning and database design to deployment on a live server. Instead of focusing on many advanced features, the goal of V1 was to build a solid foundation with clean CRUD operations, validation, authentication, search, pagination, and dashboard statistics.

### Features

#### Customer Management
* Register new customers
* View customer details
* Update customer information
* Archive customers
* Search customers
* Pagination support

#### Umrah Applications
* Create and manage Umrah applications
* Track application status
* Update application records
* Archive applications
* Search applications

#### Package Management
* Create Umrah packages
* Update package information
* Archive packages

#### Payment Management
* Record customer payments
* Track payment history
* Search payments
* Revenue statistics

#### Dashboard
* Total Customers
* Total Applications
* Total Payments
* Total Revenue

#### Authentication

* Secure login system
* Custom user model
* Login required for protected pages

## Technology Stack

#### Backend
* Python
* Django

#### Database
* SQLite (V1)

#### Frontend
* HTML
* CSS
* Bootstrap 5
* Bootstrap Icons

#### Deployment
* cPanel Python Application
* WSGI


Project Structure
UCMS/
│
├── apps/
│   ├── accounts/
│   └── umrah/
│
├── config/
│
├── templates/
│
├── static/
│
├── manage.py
└── requirements.txt


## Installation

Clone the repository:

``` bash
git clone [](https://github.com/kalid-26/UCMS-Umrah-Customer-Management-System-.git)

cd UCMS

Create and activate a virtual environment:

python -m venv venv

Windows: venv\Scripts\activate

Linux/macOS: source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Start the development server:

python manage.py runserver

```
Current Version
V1

The first version focuses on the core business workflow:

Customer → Application → Package → Payment

The goal of V1 is to provide a stable and usable system before introducing more advanced functionality.

#### Future Plans (V2)

* Some ideas planned for future versions:

* Installment payments
* Reporting and analytics
* Document management
* Customer communication tracking
* Better role and permission management
* Export to PDF and Excel
* Improved dashboard insights

### What I Learned

##### This project helped me understand the complete software development process, including:

* Project planning
* Database design
* Django application structure
* Form validation
* Authentication and authorization
* Search and pagination
* Deployment and server configuration
* Debugging production issues

#### Author

* Developed by Kalid Mohammed as a practical Django project to gain hands-on experience building and deploying real-world web applications.