# test task from DATAOX
---
### Task: Scraping the website
---
### Two ways to start the program:

### option #1 via virtual environment:
To run the script, you need:
Clone the repository on your computer. 
To do this, in the terminal run the command
`git clone https://github.com/svoboda-core/dataox-test-task.git`

Create virtual environment:
`python -m venv venv`

Activation of virtual sharpening:
Windows - `venv\Scripts\activate`
Linux - `source venv/bin/activate`

Install the requirements:
`pip install -r requirements.txt`

Run script:
Windows - `python main.py`
Linux - `python3 main.py`

### option #2 Docker:
To run the script, you need:
Clone the repository on your computer. 
To do this, in the terminal run the command
`git clone https://github.com/svoboda-core/dataox-test-task.git`

Create Docker images:
`docker build -t data-ox-test-task .`

Run script:
`docker run data-ox-test-task`


### !!! Attention: As a result of the script, data will be written to mongodb, and a JSON file with data from mongodb will be generated in the folder. !!!