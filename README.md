# email-notification-api
This project is a web service developed using FastAPI as a backend framework and PostgreSQL as a database management system. Also, a scheduler was developed to make the application fully functional. The scheduler also uses FastAPI, but MongoDB was used as the database management system.
The API helps to realize sending emails at the scheduled time with the scheduled text.
# Techonology Stack
- Python 3.11;
- FastAPI;
- SQLAlchemy;
- Pydantic;
- HTTPX;
# How to use it
### Clone repository
Firstly, the project should be cloned using the following command in the console:
```bash
git clone https://github.com/Temka0994/email-notification-api.git
```
After this navigate to the email-notification-api folder:
```bash
cd notificationAPI
```
### Requirements
Additionally, all the requirements should be downloaded using the following command:
```bash
pip install -r requirements.txt
```
### Database
The ready-made code for creating and populating the database from the [schema.sql](./src/schema.sql) file can be used, or a custom script may be created. The attached file contains queries for both table creation and data insertion. The database will appear as follows:
