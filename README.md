# 📊 [UserPatienceTest]

> English version | 🇵🇱 [Zobacz wersję po polsku](README.pl.md)

## 👥 Authors
- Filip Gumiński ([@Fifikula](https://github.com/Fifikula))
- Kacper Kozłowski ([@KacperK2003](https://github.com/KacperK2003))
- Adam Rachuba ([@rachu033](https://github.com/rachu033))

## 📄 License

- The **source code** in this repository is licensed under the [MIT License](LICENSE).
- The **research materials** (e.g., `KCK.pdf`, charts, reports) are licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

Please credit the original authors if you use or reference any part of the research.

## 🧪 Description
The project aims to examine how different types of loading animations affect users' perceived patience in a web application environment. The summary of the study is in the KCK.pdf file. 

## 🛠️ Technologies
- **Languages:** JavaScript, Python, HTML, CSS 
- **Framework:** Flask
- **Database:** SQLite

## 🚀 Running the project

### 1. Cloning the repository
```bash
git clone https://github.com/KacperK2003/UserPatienceTest.git
cd UserPatienceTest
```

### 2. Creating and running the virtual environment:
Windows:
```cmd
python -m venv .venv
.\.venv\Scripts\activate
```
If there is the error ".venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system" use 
```cmd
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

### 3. Installing the libraries:
```cmd
pip install -r .\requirements.txt
```


### 4. Creating the .env file:
Create the .env file with those variables:
- DEBUG=TRUE or DEBUG=FALSE
- PORT={port number}

### 5. Initializing the SQLite database:
```cmd
flask db init
flask db migrate
flask db upgrade
```


### 6. Running the project:
```cmd
python main.py
```
