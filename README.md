# REDACT - Rapid Efficient Data Anonymization & Content Transformation

**REDACT is an automatic confidential information masking/redaction tool for documents, images, audio and other file formats with minimal manual effort.** 

<img src="https://img.shields.io/badge/Lincense_-GPL%203.0-orange"> <img src="https://img.shields.io/badge/python_->=%203.1-blue"> [![Documentation Status](https://img.shields.io/:docs-latest-green.svg)](http://opennlp.apache.org/docs/index.html) <img src="https://img.shields.io/badge/Developed%20on-Kali%20Linux-blueviolet">

### [Video Demo](https://youtu.be/HRD_wsZ9a1U) | [Examples](https://github.com/4n33sh/REDACT/tree/main/example-outputs) | [Test Material](https://github.com/4n33sh/REDACT/tree/main/test-material) | [Source Code](https://github.com/4n33sh/REDACT/blob/main/main.py)

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

It's also has an easy to use **standalone offline program** via an **intuitive interface**, hence saving time and effort (to operator) compared to manual redaction process/clunky interface.

# Prototype Functionality

Consider **picture** redaction, wherein the **text is embedded onto the doc in the image**. The following process is **one of many** ways redaction is performed:

![picture example](https://github.com/4n33sh/REDACT/blob/main/Image%20Redaction%20Flowchart.png)

The above process (just like any file format) follows one of the **three grades** of redaction available to the user:

1. GRADE - 1 (LOW): This grade performs **basic black-box/text-replacement** redaction with '[REDACT]'. Here, basic pattern discovery is performed with **techniques** like **RegEx**, **Rule definitions**, **find & replace**, etc.

2. GRADE - 2 (MID): In this grade, the redactable data is **anonymized/masked** and also follows grade 1 redaction methodology. Here, **ML Trained model** redacts previously **left-out** sensitive data by grade 1.

3. GRADE - 3 (HIGH): It is an combination of **grade 1 + grade 2** but, utilizes **NLP** to identify potentially sensitive PIIs and also works in **compliment with TensorFlow's BeRT**. Here, the data recognized can be replaced with **synthetic data** to **preserve meaning/context whilst hiding sensitive data**.

After redaction has been performed, **Audio** (.wav), **.pdf**, **image and text formats** are made available for the user to save/download from. The previously redacted data will securely be added onto the ML dataset and later-on be used as **Training data** for future consistent and better redaction(s).

# Installation and Running

* (optional) **Create & activate** new python **virtual (.venv) environment** :  ``` python3 -m venv ~/your/preffered/path && source ~/your/preffered/path/bin/activate ```

* **Clone** repo into your preferred directory : ``` git clone https://github.com/4n33sh/REDACT.git ```

* Change directory **(cd)** into REDACT : ``` cd REDACT ```

* Install the **requirements** : ``` pip install -r requirements.txt ```

* Install spaCy NLP (large) **dataset** (~540mb) : ``` python3 -m spacy download en_core_web_lg ```

* Alter **permissions** of file : ``` chmod u+x main.py ```

* Finally, **run** the script : ``` python3 main.py ```

# Contribution(s)
Contributions are Welcome! Please open an issue or submit a pull request on the [Github repo](https://github.com/4n33sh/REDACT). Please do mind to read the [code of conduct](https://github.com/4n33sh/REDACT/blob/main/CODE_OF_CONDUCT.md) before performing any actions.

# License
This project is licensed under the GPL-3.0 License. See the [LICENSE](https://github.com/4n33sh/REDACT/blob/main/LICENSE) file for more details.
