# Test task from DATAOX
---
### Task: Scraping the website
---
### Two ways to start the program:

### option #1 via virtual environment:<br>
To run the script, you need:<br>
Clone the repository on your computer.<br>
To do this, in the terminal run the command <br>
`git clone https://github.com/svoboda-core/dataox-test-task.git`

Create virtual environment:<br>
`python -m venv venv`

Activation of virtual sharpening:<br>
Windows - `venv\Scripts\activate`<br>
Linux - `source venv/bin/activate`

Install the requirements:<br>
`pip install -r requirements.txt`<br>

Run script:<br>
Windows - `python main.py`<br>
Linux - `python3 main.py`

### option #2 Docker:
To run the script, you need: <br>
Clone the repository on your computer.<br>
To do this, in the terminal run the command<br>
`git clone https://github.com/svoboda-core/dataox-test-task.git`

Create Docker images:<br>
`docker build -t data-ox-test-task .`

Run script:<br>
`docker run data-ox-test-task`


### !!! Attention: As a result of the script, data will be written to Mongodb, and a JSON file with data from Mongodb will be generated in the folder. !!!