# WatchThat

## Dev Environment Setup

First, make sure to install `mysql`.

To get the development environment setup, make sure the `python3-dev`, `virtualenv`, and `pip` are installed.

Start the virtual environment and grab the required dependencies:
```bash
$ virtualenv -p <path-to-python3-interpreter> env
$ source env/bin/activate
$ cd python
$ pip install -r requirements.txt
```

Setup a few environment variables:
```bash
$ export FLASK_CONFIG=development
$ export FLASK_APP=run.py
```

## Dev Database Configuration
Log into mysql as the root user:

```bash
$ mysql -u root -p
```

Create a new user (this will be you) and password. Then create the database:

```sql
mysql> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT ALL PRIVILEGES ON * . * TO 'username'@'localhost';
mysql> CREATE DATABASE watchthat_db;
```

To configure the database, add the necessary config values to `python/instance/config.py`:
```bash
$ mkdir instance
$ touch instance/config.py
```

In `python/instance/config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/watchthat_db'
```

## Running the app

```bash
flask run
```
