# REDACT - Rapid Efficient Data Anonymization & Content Transformation

**REDACT is an automatic confidential information masking/redaction tool for documents, images, audio and other file formats with minimal manual effort.** 

<img src="https://img.shields.io/badge/Lincense_-GPL%203.0-orange"> <img src="https://img.shields.io/badge/python_->=%203.1-blue"> [![Documentation Status](https://img.shields.io/:docs-latest-green.svg)](http://opennlp.apache.org/docs/index.html)

### [Video Demo](https://www.youtube.com/watch?v=C47vACIMZC8) | [Examples](https://github.com/4n33sh/REDACT/tree/main/example-outputs) | [Test Material](https://github.com/4n33sh/REDACT/tree/main/test-material) | [Source Code] (https://github.com/4n33sh/REDACT/blob/main/main.py)

---

# Technical Approach to Full-fledged application

During initial conception of the tool, some fundamental **constraints** were set before proceeding forward:

1. The tool must be **secure** and respect the **privacy of the user's files**.

2. **Machine Learning models** must be implemented for **constant and consistent training** and be designed for **easy model modification** to meet the user's **specific needs**.

3. **Smart redaction** must be included to redact basic **PIIs/PLLs** like Phone No., Names, Geo-locations, etc. through **natural language processors** and **RegEx identifiers**.

4. The tool must **support all types of file formats** and allow the user to **choose from a variety of output formats**.

![technical datagram](https://github.com/4n33sh/REDACT/blob/main/Technical%20Approach.png)

The Privacy of user's data is ensured through **multiple secure layers** such as **DMZ** (de-militarized zone) for isolation, **secure authenticators** (2FA and JSON) and finally **encryption** for data (while in-transit and storage) to ensure that the training/user data stays secure.

**Entity recognition** is achieved through **spaCy's NLP** (with it's large dataset) and the ML Training as well as **TensorFlow's BeRT** model was implemented through **transformers**.

![prototype gui final](https://github.com/4n33sh/REDACT/blob/main/Prototype%20GUI%20%26%20Functionality.png)

It's an easy to use **standalone offline program** via an **intuitive interface**, hence saving time and effort (to operator) compared to manual redaction process/clunky interface.

# Prototype Functionality

Consider **picture** redaction, wherein the **text is embedded onto the doc in the image**. The following process is **one of many** ways redaction is performed:

![picture example](https://github.com/4n33sh/REDACT/blob/main/Image%20Redaction%20Flowchart.png)

# Installation and Running

* (optional) **Create & activate** new python **virtual (.venv) environment** :  ``` python3 -m venv ~/your/preffered/path && source ~/your/preffered/path/bin/activate ```

* **Clone** repo into your preferred directory : ``` git clone https://github.com/4n33sh/REDACT.git ```

* Change directory **(cd)** into REDACT : ``` cd REDACT ```

* Install the **requirements** : ``` pip install -r requirements.txt ```

* Install spaCy NLP (large) **dataset** (~540mb) : ``` python3 -m spacy download en_core_web_lg ```

* Alter **permissions** of file : ``` chmod u+x main.py ```

* Finally, **run** the script : ``` python3 main.py ```
