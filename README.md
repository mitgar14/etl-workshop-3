# Workshop #3: Machine Learning and Data Streaming <img src="https://cdn-icons-png.flaticon.com/512/2980/2980560.png" alt="Data Icon" width="30px"/>

Realized by **Martín García** ([@mitgar14](https://github.com/mitgar14)).

## Overview ✨

In this workshop, the [World Happiness Report dataset](https://www.kaggle.com/datasets/unsdsn/world-happiness) will be used, comprising four CSV files with data from 2015 to 2019. A streaming data pipeline will be implemented using Apache Kafka. Once processed, the data will be fed into a Random Forest regression model to estimate the Happiness Score based on other scores in the dataset. The results will then be uploaded to a database, where the information will be analyzed to assess the accuracy and insights of the predictions.

**The tools used are:**

* Python 3.10 ➜ [Download site](https://www.python.org/downloads/)
* Jupyter Notebook ➜ [VS Code tool for using notebooks](https://youtu.be/ZYat1is07VI?si=BMHUgk7XrJQksTkt)
* Docker ➜ [Download site for Docker Desktop](https://www.docker.com/products/docker-desktop/)
* PostgreSQL ➜ [Download site](https://www.postgresql.org/download/)
* Power BI (Desktop version) ➜ [Download site](https://www.microsoft.com/es-es/power-platform/products/power-bi/desktop)

---

**The dependencies needed for Python are:**

* python-dotenv
* kafka-python
* pandas
* matplotlib
* scikit-learn
* seaborn
* sqlalchemy

These libraries are included in the Poetry project config file ([`pyproject.toml`](https://github.com/mitgar14/etl-workshop-3/blob/main/pyproject.toml)). The step-by-step installation will be described later.

---

**The images used in Docker are:**

* confluentinc/cp-zookeeper
* confluentinc/cp-kafka

The configuration and installation of these images are facilitated by the Docker Compose config file ([`docker-compose.yml`](https://github.com/mitgar14/etl-workshop-3/blob/main/docker-compose.yml)). The explanation for using these images will be explained later.

## Dataset Information <img src="https://github.com/user-attachments/assets/5fa5298c-e359-4ef1-976d-b6132e8bda9a" alt="Dataset" width="30px"/>

After performing several transformations on the data, the columns to be analyzed in this workshop are as follows:

| Column                 | Description                                       | Data Type   |
|------------------------|---------------------------------------------------|-------------|
| **country**            | The country name, representing each nation        | Object      |
| **continent**          | The continent to which each country belongs       | Object      |
| **year**               | The year the data was recorded                    | Integer     |
| **economy**            | A measure of each country's economic status       | Float       |
| **health**             | Health index indicating general well-being        | Float       |
| **social_support**     | Perceived social support within each country      | Float       |
| **freedom**            | Citizens' perception of freedom                   | Float       |
| **corruption_perception** | Level of corruption as perceived by citizens  | Float       |
| **generosity**         | Level of generosity within the country            | Float       |
| **happiness_rank**     | Global ranking based on happiness score           | Integer     |
| **happiness_score**    | Overall happiness score for each country          | Float       |

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

3. In that file we declare 5 enviromental variables. Remember that some variables in this case go without double quotes, i.e. the string notation (`"`).:
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

We execute the 3 notebooks following the next order. You can run these by just pressing the "Execute All" button:

   1. *01-EDA.ipynb*
   2. *02-model_training.ipynb*
   3. *03-metrics.ipynb*

![Running the notebooks](https://github.com/user-attachments/assets/f50a3cc2-90eb-48d3-b452-7bec0e5022c5)
  
Remember to choose **the right Python kernel** at the time of running the notebook.

![Python kernel](https://github.com/user-attachments/assets/3b3c57ca-a07e-4a42-aa1d-4fdd9ea8187e)

---

### ☁ Deploy the Database at a Cloud Provider

To perform the Airflow tasks related to Data Extraction and Loading we recommend **making use of a cloud database service**. Here are some guidelines for deploying your database in the cloud:

* [Microsoft Azure - Guide](https://github.com/mitgar14/etl-workshop-3/blob/main/docs/guides/azure_postgres.md)
* [Google Cloud Platform (GCP) - Guide](https://github.com/mitgar14/etl-workshop-3/blob/main/docs/guides/gcp_postgres.md)

---

### 🐳 Run Kafka in Docker

> [!IMPORTANT]
> Make sure that Docker is installed in your system.

To set up Kafka using Docker and run your `producer.py` and `consumer.py` scripts located in the `./kafka` directory, follow these steps:

1. 🚀 **Start Kafka and Zookeeper Services**

   Open your terminal or command prompt and navigate to the root directory of your cloned repository:

   ```bash
   cd etl-workshop-3
   ```

   Use the provided `docker-compose.yml` file to start the Kafka and Zookeeper services:

   ```bash
   docker-compose up -d
   ```

   This command will start the services in detached mode. Docker will pull the necessary images if they are not already available locally.

   Check if the Kafka and Zookeeper containers are up and running:

   ```bash
   docker ps
   ```

   You should see `kafka_docker` and `zookeeper_docker` in the list of running containers.

   #### Demonstration of the process

   *(gif demonstration docker 1)*

2. 📌 **Create a Kafka Topic**

   Create a Kafka topic that your producer and consumer will use. Make sure to name it `whr_kafka_topic` to not clash with the Python scripts:

   ```bash
   docker exec -it kafka_docker kafka-topics --create --topic whr_kafka_topic --bootstrap-server localhost:9092
   ```

   List the available topics to confirm that the `whr_kafka_topic` has been created:

   ```bash
   docker exec -it kafka_docker kafka-topics --list --bootstrap-server localhost:9092
   ```
  *(gif demonstration docker 2)*

3. 🏃 **Run the Producer Script**

   In Visual Studio Code, navigate to the `./kafka` directory and run the `producer.py` script **in a dedicated terminal**. The producer will start sending messages to the `happiness_topic`.

   *(gif demonstration docker 3)*

4. 👂 **Run the Consumer Script**

    Now navigate to the `./kafka` directory, and run the `consumer.py` script **in a dedicated terminal**. You should now see the consumer receiving it in real-time.

   *(gif demonstration docker 4)*

5. 🛑 **Shut Down the Services**

    When you're finished, you can stop and remove the Kafka and Zookeeper containers:

    ```bash
    docker-compose down
    ```
    
    *(gif demonstration docker 5)*
    
## Thank you! 💕

Thanks for visiting my project. Any suggestion or contribution is always welcome 🐍.
