# REDACT - Rapid Efficient Data Anonymization & Content Transformation

**REDACT is an automatic confidential information masking/redaction tool for documents, images, audio and other file formats with minimal manual effort.** 

<img src="https://img.shields.io/badge/Lincense_-GPL%203.0-orange"> <img src="https://img.shields.io/badge/python_->=%203.1-blue"> <img src="https://img.shields.io/badge/Maintained%3F-Yes-CD8335"> [![Documentation Status](https://img.shields.io/:docs-latest-green.svg)](http://opennlp.apache.org/docs/index.html) <img src="https://img.shields.io/badge/Developed%20on-Kali%20Linux-blueviolet">

### [Video Demo](https://youtu.be/HRD_wsZ9a1U) | [Examples](https://github.com/4n33sh/REDACT/tree/main/example-outputs) | [Test Material](https://github.com/4n33sh/REDACT/tree/main/test-material) | [Source Code](https://github.com/4n33sh/REDACT/blob/main/main.py)

---

# Technical Approach to Full-fledged application

During initial conception, some fundamental **constraints** were set before proceeding forward:

1. The tool must be **secure** and respect the **privacy of the user's files**.

2. **Machine Learning model** must be implemented for **constant** and **consistent training** and be designed for **easy modification** to meet the user's **specific needs/requirement**.

3. **Smart redaction** to redact basic **PIIs/PLLs** like Phone Nos., Names, Geo-locations, Dates, etc. through **Natural Language Processor(s)** and **RegEx identifiers**.

4. The tool must support **all** types of **file formats** and allow the user to **choose from a variety of available output formats**.

![technical datagram](https://github.com/4n33sh/REDACT/blob/main/Technical%20Approach.png)

The Privacy of user's data is ensured through **multiple security layers** such as **DMZ** (de-militarized zone) for isolation, **secure authenticators** (2FA and JSON for web-based access) and finally **encryption** for data (while in-transit and storage) to ensure that the training/user data stays secure.

**Entity recognition** is achieved through **spaCy's NLP** (through it's large dataset) and ML based Training by **BeRT** was implemented through **TensorFlow and HF transformers**.

![prototype gui final](https://github.com/4n33sh/REDACT/blob/main/Prototype%20GUI%20%26%20Functionality.png)

It's also has an easy to use **standalone offline program** via an **intuitive user interface**, hence saving time and effort (to operator) compared to manual redaction process/clunky interface.

# Prototype Functionality

Consider **picture/image** redaction, wherein the **text is embedded onto the doc in the image**. The following process is **one of many** ways redaction is performed:

![picture example](https://github.com/4n33sh/REDACT/blob/main/Image%20Redaction%20Flowchart.png)

The above process (just like any other file format) follows one of the **three grades** of redaction:

1. GRADE - 1 (LOW): Performs basic **black-box redaction/text-replacement** with placeholders like '[REDACT]'. Basic pattern discovery is performed with primitive techniques like **RegEx**, **Rule definitions**, **find & replace**, etc.

2. GRADE - 2 (MID): Redactable data is **anonymized/masked** and also follows grade 1 redaction methodology. The **BeRT Model** redacts previously left-out sensitive data by grade 1.

3. GRADE - 3 (HIGH): It's an combination of **grade 1 + grade 2** but, utilizes **spaCy NLP Toolkit** to identify potentially sensitive PIIs and also works in **compliment with BeRT**. The recognized data can be replaced with **synthetic data** to **preserve meaning/context** whilst **hiding sensitive data**.

After redaction has been performed, **Audio** (.wav), **.pdf**, **image** and **text formats** are made available for the user to save/download from. The previously redacted data will securely be added onto the ML dataset and be used later on as **Training data** for better future consistent redactions.

# Installation and Running

* (optional) **Create & activate** new python **virtual (.venv) environment** :  ``` python3 -m venv ~/your/preffered/path && source ~/your/preffered/path/bin/activate ```

* **Clone** repo into your preferred directory : ``` git clone https://github.com/4n33sh/REDACT.git ```

* Change directory **(cd)** into REDACT : ``` cd REDACT ```

* Install the **requirements** : ``` pip install -r requirements.txt ```

* Install spaCy NLP (large) **dataset** (~540mb) : ``` python3 -m spacy download en_core_web_lg ```

* Alter **permissions** of file : ``` chmod u+x main.py ```

* Finally, **run** the script : ``` python3 main.py ```

# Update Log
Following results convey raw performance by **benchmarking** the model (.csv/emails are also included within the dataset):

1. **CoNLL-03** Dataset Results:

| Entity Type         | Precision (%) | Recall (%) | F1-Score (%) |
|---------------------|---------------|------------|--------------|
| Overall             | 90.1          | 89.2       | 89.65        |
| Person (PER)        | 91.0          | 90.0       | 90.5         |
| Organization (ORG)  | 86.8          | 90.4       | 88.56        |
| Location (LOC)      | 90.8          | 96.2       | 93.42        |
| Miscellaneous (MISC)| 82.6          | 87.5       | 84.98        |

2. **F1-Score** Results:

| **Entity Type** | **Precision** | **Recall** | **F1-Score** | **Support** |
|-----------------|---------------|------------|--------------|-------------|
| Person (PER)    | 0.93          | 0.89       | 0.91         | 320         |
| Location (GPE/LOC) | 0.87          | 0.92       | 0.89         | 210      |
| Date            | 0.95          | 0.93       | 0.94         | 180         |
| Organization (ORG) | 0.88          | 0.86       | 0.87         | 140      |
| **Accuracy**    | ----->        | ----->     | **0.90**     | **850**     |
| **Macro avg**   | 0.88          | 0.88       | 0.88         | 850         |
| **Weighted avg**| 0.90          | 0.90       | 0.90         | 850         |

(confusion matrix excluded bcz results are gunky for True Negatives)

3. **Calibration Metrics** for individual redaction grades:

| **Grade** | **Probability Bin/range** | **Predicted Frequency** | **Observed Frequency/Accuracy** | **Calibration Error** | **Cumulative Error** |
|---------------------|---------------------|--------------------------|-----------------------------------|------------------------|-----------------------|
| **GRADE 1 (LOW)**   | 0.00 - 0.10         | 150                      | 0.09                              | 0.01                   | 0.01                  |
|                     | 0.10 - 0.20         | 250                      | 0.17                              | 0.03                   | 0.04                  |
|                     | 0.20 - 0.30         | 300                      | 0.27                              | 0.03                   | 0.07                  |
|                     | 0.30 - 0.40         | 400                      | 0.35                              | 0.05                   | 0.12                  |
|                     | 0.40 - 0.50         | 500                      | 0.45                              | 0.05                   | 0.17                  |
| **GRADE 2 (MID)**   | 0.50 - 0.60         | 400                      | 0.57                              | 0.03                   | 0.20                  |
|                     | 0.60 - 0.70         | 350                      | 0.64                              | 0.06                   | 0.26                  |
|                     | 0.70 - 0.80         | 300                      | 0.75                              | 0.05                   | 0.31                  |
|                     | 0.80 - 0.90         | 250                      | 0.88                              | 0.02                   | 0.33                  |
|                     | 0.90 - 1.00         | 200                      | 0.96                              | 0.04                   | 0.37                  |
| **GRADE 3 (HIGH)**  | 0.00 - 0.10         | 50                       | 0.08                              | 0.02                   | 0.02                  |
|                     | 0.10 - 0.20         | 100                      | 0.18                              | 0.02                   | 0.04                  |
|                     | 0.20 - 0.30         | 200                      | 0.28                              | 0.02                   | 0.06                  |
|                     | 0.30 - 0.40         | 300                      | 0.36                              | 0.04                   | 0.10                  |
|                     | 0.40 - 0.50         | 400                      | 0.49                              | 0.01                   | 0.11                  |

(certain predicted freqs. are capped to multiples of two)

# Contribution(s)
Contributions are Welcome! Please open an issue or submit a pull request on the [Github repo](https://github.com/4n33sh/REDACT). Please do mind to read the [code of conduct](https://github.com/4n33sh/REDACT/blob/main/CODE_OF_CONDUCT.md) before performing any actions.

# License
This project is licensed under the GPL-3.0 License. See the [LICENSE](https://github.com/4n33sh/REDACT/blob/main/LICENSE) file for more details.
