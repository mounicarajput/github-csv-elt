
# EL Automation Project
This project automates the Extract-Load (EL) process for data integration. It uses open-source tools to extract data from a source system and load it into a target system.

## Features
1. Currently Support Github Extractor and CSV Target.
2. Easily configurable using UI.


## Getting Started
To use this project, you will need to clone this repository to your local machine.

### Prerequisites
Python 3.x\
pip


Step 1: Clone the repository

```
git clone https://github.com/mounicarajput/github-csv-elt.git
```

Step 2: Change the Directory

```
cd github-csv-elt
```

Step 3: Install Requirements
```
pip install -r requirements.txt
meltano install extractor tap-github
meltano install loader target-csv
```

Step 4: Run the Application
```
python app.py
```

## Contributing
Contributions to this project are welcome. If you would like to contribute, please open an issue or pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
