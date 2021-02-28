# contacts-converter

Export, convert and save your contacts from Google Contacts.

# Introduction
This script converts the exported .csv file from Google Contacts to a more standardized form. 
It can be used to create a standardized backup ot to move synchronize contacts from Google to Outlook.

# Installation
The script is based on Python 3.8.
This script mainly uses pandas:
``` bash
pip install pandas
```
A ```requirements.txt``` is available though.
# Usage
The script can be used in Command Line given the file as an argument:
``` bash
python3 contacts_to_outlook.py contacts_to_outlook.py --file=FILENAME.CSV
```
If the conversion was successfully, the script generates a new file and a message will appear:
```bash
New file: 'contacts_outlook.csv' was created successfully!
```
