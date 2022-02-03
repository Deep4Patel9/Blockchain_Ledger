# Blockchain_Ledger

A blockchain-based ledger system with a user-friendly web interface. This ledger sets the framework to allow individuals or institutions to conduct financial transactions and to verify the integrity of the data in the ledger.

---

## Technologies

This project uses python 3.7 along with jupyter lab 3.0.14 with the following packages:


* [pandas](https://github.com/pandas-dev/pandas) - For data manipulation and analysis

* [streamlit](https://docs.streamlit.io/) - Used to build and deploy web applications using python

* [hashlib](https://docs.python.org/3/library/hashlib.html) - To hash information using SHA256

* [dataclasses](https://docs.python.org/3/library/dataclasses.html) - To create data classes 

* [typing](https://docs.python.org/3/library/typing.html) - Support for gradual typing

* [datetime](https://docs.python.org/3/library/datetime.html) - To pull utc datetime

---

## Installation Guide

Before running the application first install the following dependencies:

```python
$ pip install pandas
$ pip install streamlit

```

---

## Usage

To use this simply clone the files to your machine and open the terminal in the folder which contains the ledger.py file. Then simply type in the command streamlit run ledger.py to launch the ledger in your browser. This app takes the information inputted into the interface and creates a chain using the hashs from previous blocks. You can adjust the difficulty of the proof of work with the slider on the sidebar from 1-5 or higher if you modify the code a little bit. You can also view the individual records stored in each block from the sidebar. After adding a few blocks at the bottom of the page is a validation button to allow you to validate the intergrity of the chain.

---

## Contributors

Deep Patel -- Deep4Patel9@gmail.com

---

## License

MIT License

Copyright (c) 2022  

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.