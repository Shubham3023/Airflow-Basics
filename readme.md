# Apache Airflow Basics Tutorial

## Prerequisites
- Python 3.7 or higher
- pip package manager

## Step 1: Enable Windows subsystem for linux (WSL) and install ubuntu

[WSL Installation](https://learn.microsoft.com/en-us/windows/wsl/install)

```bash
wsl --install 
```
## Step 1A: Update ubuntu system and install python3 and pip
After first install, you will be asked to set username and password for ubuntu

```bash
sudo apt update  
```
```bash
sudo apt install python3 pip
```

## Step 2: Create and activate Virtual Environment
```bash
sudo apt install python3-venv
```
```bash
cd ~
mkdir airflow
cd airflow
```
```bash
python3 -m venv airflowenv
```
Activate the environment:
- **Linux:** `source airflow_env/bin/activate`

## Step 2A: Install Apache Airflow
```bash
pip install apache-airflow
```

## Step 3: Initialize Airflow Database
```bash
airflow db init
airflow db migrate
```

## Step 3A: Initialize Airflow
```bash
airflow standalone
```
Open a New terminal, activate the env and run the below to see the ID and PW for Airflow
```bash
cat simple_auth_manager_passwords.json.generated
```
Type the following in Termianl to get the IP address of scope global host
```bash
ip a
```
Open the browser and paste your ip --> <ipAddress>:8080 and enter the ID and PW from above step.


## Step 5: Create Your First DAG

Create a folder `dags` inside airflow folder
```bash
mkdir dags
```

Create a file `dags/first_dag.py` and add the code from the `dags/first_dag.py` file.

Run the following to compile dag

```bash
python3 first_dag.py
```

Go to the Airflow Webserver and access this dag under dags tab and trigger the tasks.

## Note: To Open airflow again in VS code after you close the project
Open CMD and type `wsl` and hit enter.
Go to home directory by typing `cd ~` and enter.
Type `code .` to open the VS code