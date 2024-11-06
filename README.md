# Workshop #3: Machine Learning and Data Streaming <img src="https://cdn-icons-png.flaticon.com/512/2980/2980560.png" alt="Data Icon" width="30px"/>

Realized by **Martín García** ([@mitgar14](https://github.com/mitgar14)).

## Overview ✨

(add info)

The tools used are:

* Python 3.10 ➜ [Download site](https://www.python.org/downloads/)
* Jupyter Notebook ➜ [VS Code tool for using notebooks](https://youtu.be/ZYat1is07VI?si=BMHUgk7XrJQksTkt)
* PostgreSQL ➜ [Download site](https://www.postgresql.org/download/)
* Power BI (Desktop version) ➜ [Download site](https://www.microsoft.com/es-es/power-platform/products/power-bi/desktop)

The dependencies needed for Python are

* python-dotenv
* kafka-python
* pandas
* matplotlib
* scikit-learn
* seaborn
* sqlalchemy

These libraries are included in the Poetry project config file (pyproject.toml). The step-by-step installation will be described later.

## Dataset Information <img src="https://github.com/user-attachments/assets/5fa5298c-e359-4ef1-976d-b6132e8bda9a" alt="Dataset" width="30px"/>

(add info)

## Data flow <img src="https://cdn-icons-png.flaticon.com/512/1953/1953319.png" alt="Data flow" width="22px"/>

![Flujo de datos](https://github.com/user-attachments/assets/6e9d34c0-8611-4f1a-b283-87029d2621da)

## Run the project <img src="https://github.com/user-attachments/assets/99bffef1-2692-4cb8-ba13-d6c8c987c6dd" alt="Running code" width="30px"/>


### 🛠️ Clone the repository

Execute the following command to clone the repository:

```bash
  git clone https://github.com/mitgar14/etl-workshop-3.git
```

#### Demonstration of the process

(gif of the demonstration)

---

### 🌍 Enviromental variables

For this project we use some environment variables that will be stored in one file named ***.env***, this is how we will create this file:

1. We create a directory named ***env*** inside our cloned repository.

2. There we create a file called ***.env***.

3. In that file we declare 6 enviromental variables. Remember that some variables in this case go without double quotes, i.e. the string notation (`"`). Only the absolute routes go with these notation:
  ```python
  # PostgreSQL Variables
  
  # PG_HOST: Specifies the hostname or IP address of the PostgreSQL server.
  PG_HOST = # db-server.example.com
  
  # PG_PORT: Defines the port used to connect to the PostgreSQL database.
  PG_PORT = # 5432 (default PostgreSQL port)
  
  # PG_USER: The username for authenticating with the PostgreSQL database.
  PG_USER = # your-postgresql-username
  
  # PG_PASSWORD: The password for authenticating with the PostgreSQL database.
  PG_PASSWORD = # your-postgresql-password
  
  # PG_DATABASE: The name of the PostgreSQL database to connect to.
  PG_DATABASE = # your-database-name

  ```

#### Demonstration of the process (update gif)

![env variables](https://github.com/user-attachments/assets/1ace0df1-3313-4e59-b73b-8f5b280dbaed)

---

### 📦 Installing the dependencies with *Poetry*

(info and demonstration of poetry)

---

### 📔 Running the notebooks

(info of the section)

After you have run that notebook, then run the others in the following order. Remember that you can run all the cells in the notebook using the “Run All” button:

   1. *01-EDA.ipynb*
   2. *02-model_training.ipynb*
   3. *03-metrics.ipynb*

(ejecutar image)
  
Remember to choose **the right Python kernel** at the time of running the notebook.

(python kernel img)

---

### ☁ Deploy the Database at a Cloud Provider

To perform the Airflow tasks related to Data Extraction and Loading we recommend **making use of a cloud database service**. Here are some guidelines for deploying your database in the cloud:

* [Microsoft Azure - Guide](https://github.com/mitgar14/etl-workshop-3/blob/main/docs/guides/azure_postgres.md)
* [Google Cloud Platform (GCP) - Guide](https://github.com/mitgar14/etl-workshop-3/blob/main/docs/guides/gcp_postgres.md)

---


## Thank you! 💕

Thanks for visiting my project. Any suggestion or contribution is always welcome 🐍.
