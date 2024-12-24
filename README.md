# REDACT - Rapid Efficient Data Anonymization & Content Transformation

**REDACT is an automatic confidential information masking/redaction tool for documents, images, audio and other file formats with minimal manual effort.** 

---

<img src="https://img.shields.io/badge/Lincense_-GPL%203.0-orange"> <img src="https://img.shields.io/badge/python_->=%203.1-blue"> [![Documentation Status](https://img.shields.io/:docs-latest-green.svg)](http://opennlp.apache.org/docs/index.html)

The tool handles various types of file formats, delete personal or confidential details and convert them back into their original/user-required format(s). 

### [Video Demo](https://www.youtube.com/watch?v=C47vACIMZC8) | [Examples](https://github.com/4n33sh/REDACT/tree/main/example-outputs)

# Technical Approach to Full-fledged application

![technical datagram](https://github.com/4n33sh/REDACT/blob/main/Technical%20Approach.png)

REDACT utilizes machine learning and natural entity recognition to obtain consistent redaction results & accuracy over time.

![prototype gui final](https://github.com/4n33sh/REDACT/blob/main/Prototype%20GUI%20%26%20Functionality.png)

It's an easy to use standalone offline program via an intuitive interface whilst being automated, hence saving time and effort (to operator) compared to manual redaction process.

# Prototype Functionality

Consider picture redaction, wherein the text is embedded onto the doc in the image. The following process is one of many ways redaction is performed:

![picture example](https://github.com/4n33sh/REDACT/blob/main/Image%20Redaction%20Flowchart.png)

# Installation and Running

* (optional) Create & activate new python virtual (.venv) environment :  ``` python3 -m venv ~/your/preffered/path && source ~/your/preffered/path/bin/activate ```

* Clone repo into your preferred directory : ``` git clone https://github.com/4n33sh/REDACT.git ```

* Change directory (cd) into REDACT : ``` cd REDACT ```

* Install the requirements : ``` pip install -r requirements.txt ```

* Install spaCy NLP (large) dataset (~540mb) : ``` python3 -m spacy download en_core_web_lg ```

* Alter permissions of file : ``` chmod u+x main.py ```

* Finally, run the script : ``` python3 main.py ```
