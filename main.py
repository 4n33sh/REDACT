# @Author: 4n33sh (Aneesh SP) (aneesh.sp222@gmail.com) 
# @version: v4.5 (as of 06/02/2025)

#! /root/my_virt_envs/bin/python3

#above microprocessor executes code directly form python .venv package. modify to suit your venv. path
#for linux terminal implementation/execution: source /location/to/venv/bin/activate

#before running the script, install dependencies from requirements.txt: pip install -r requirements.txt

import os
import re
import time
import tkinter as tkin
from tkinter import messagebox
from tkinter import scrolledtext
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
import PyPDF2
from fpdf import FPDF
from pydub import AudioSegment
import spacy
from faker import Faker
import pytesseract
from PIL import Image
import speech_recognition as sr
from pydub import AudioSegment
import pyttsx3
import numpy as np
import sounddevice as sd
import fitz
import tensorflow as tf
from transformers import BertTokenizer, TFBertForTokenClassification
import unicodedata

#pre-load spaCy model (large) (user can choose from small/med/large) for NLP/NER and faker 

nlp = spacy.load("en_core_web_lg")	
fake = Faker()

#load BeRT Tokenizer and model for ML-based entity recog.
#this will require internet connection (1st time downl. only - later stored in local cache)

tokenizer = BertTokenizer.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
bert_model = TFBertForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")

#for strictly offline use, download model at https://huggingface.co/dbmdz/bert-large-cased-finetuned-conll03-english

#following code is for offline implementation of huggingface/transformers BeRT model (uncomment 4 use)
#model_dir = "/path/to/local/model/directory"
#tokenizer = BertTokenizer.from_pretrained(model_dir)
#bert_model = TFBertForTokenClassification.from_pretrained(model_dir)

#function to handle the case sensitivity checkbox toggle
def toggle_case_sensitive():
	global case_sensitive
	case_sensitive = case_sensitive_checkbox.get()
	print("Case-Sensitive CheckBox status:", case_sensitive)

#function to handle the ML-choice checkbox toggle
def toggle_ml_choice():
	global use_ml
	use_ml = ml_choice_checkbox.get()
	print("ML Model CheckBox status:", use_ml)

#func. to handle the NLP Trainer model checkbox toggle
def toggle_NLP_choice():
	global utilize_NLP_trainer_model_with_JSON
	utilize_NLP_trainer_model_with_JSON = NLP_choice_checkbox.get()
	print("NLP Trainer CheckBox status:", utilize_NLP_trainer_model_with_JSON)
	
def toggle_lock():

	#set the 'lock' emoji to unlocked at start
	global locked
	locked = not locked
	
	entry1.configure(state='disabled' if locked else 'normal')

	#change the 'lock' button text, emoji and colour
	if locked:
		lock_button.configure(text="\U0001f512", fg_color="red", text_color="black")  #red background when locked
	else:
		lock_button.configure(text="\U0001f513", fg_color="green", text_color="black")  #green background means unlocked
		
def redact_phone(match,redaction_level):

	phone = match.group(0)
	if redaction_level == "LOW":
		return "[REDACTED PHONE]"
	elif redaction_level == "MID":
		#mask phone number with 'XXX-XXX-XXXX'
		return 'XXX-XXX-' + phone[-4:]
	elif redaction_level == "HIGH":
		return fake.phone_number()
		
def redact_credit_card(match,redaction_level):

	cc = match.group(0)
	if redaction_level == "LOW":
		return "[REDACTED CREDIT CARD]"
	elif redaction_level == "MID":
		#mask credit card with 'XXXX-XXXX-XXXX' (as-per luhn's algo.)
		return 'XXXX-XXXX-XXXX-' + cc[-4:]
	elif redaction_level == "HIGH":
		return fake.credit_card_number()
		
def redact_ssn(match,redaction_level):

	ssn = match.group(0)
	if redaction_level == "LOW":
		return "[REDACTED SSN]"
	elif redaction_level == "MID":
		#mask ssn 'XXX-XX'
		return 'XXX-XX-' + ssn[-4:]
	elif redaction_level == "HIGH":
		return fake.ssn()
		
def redact_aadhar(match,redaction_level):

	aadhar = match.group(0)
	if redaction_level == "LOW":
		return "[REDACTED AADHAR]"
	elif redaction_level == "MID":
		#mask aadhaar with 'XXXX-XXXX-' and then leave the rest of digits as open val.
		return 'XXXX-XXXX-' + aadhar[-4:]
	elif redaction_level == "HIGH":
		return fake.ssn()  #aaadhar is 12-digit number, but fake.ssn() can moonlight for gen. format regex discovery

class PDF(FPDF):

	#generate the header of PDF file
	def header(self):
		#add PDF title
		self.set_font('Arial', 'B', 12)
		self.cell(0, 10, 'My PDF Title', 0, 1, 'C')
		self.ln(10)
	
	#generate footer of PDF file
	def footer(self):
		#add page num.
		self.set_y(-15)
		self.set_font('Arial', 'I', 8)
		self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def show_scroll_messagebox(title, message):

	#create an new top-level window
	messagebox = tkin.Toplevel()
	messagebox.title(title)

	#create a scrolled-Text widget
	text_area = scrolledtext.ScrolledText(messagebox, wrap=tkin.WORD, width=50, height=10)
	text_area.insert(tkin.END, message)
	text_area.config(state=tkin.DISABLED)  #read-only config.
	text_area.pack(padx=10, pady=10)

	#added an 'OK' button to close the dialog
	ok_button = tkin.Button(messagebox, text="OK", command=messagebox.destroy)
	ok_button.pack(pady=(0, 10))

	messagebox.transient()  #make it modal (set to: transient)
	messagebox.grab_set() #prevent interaction with other windows when displayed/window-overlay

def text_to_speech(text, output_path):

	#initialize text-to-speech engine
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')

	#set synthesizer properties(voice, rate, volume)
	engine.setProperty('rate', 18)  #speed of speech (18wpm instead of 120-135wpm bcz it then becomes incomprehensible)
	engine.setProperty('volume', 1.0)  #vol @(0.0 to 1.0) range
	
	engine.setProperty('voice', voices[1].id)  #change da index to select different voices
	
	#use a callback to get the audio data
	def callback(indata, frames, time, status):
		if status:
			print(status)
		sd.play(indata, samplerate=44100)

	#generate tempo audio file
	engine.save_to_file(text, "/tmp/text-to-speech-output.wav")
	engine.runAndWait()

	audio = AudioSegment.from_wav("/tmp/text-to-speech-output.wav")
	faster_audio = audio.speedup(playback_speed=1.1)
	faster_audio.export(output_path + "/text-to-speech-out.wav", format="wav")

	#to play generated file in real-time (un-comment following lines)
	
	# audio_data = np.fromfile(output_path + "/text-to-speech-output.wav", dtype=np.int16)
	# sd.play(audio_data, samplerate=44100)
	# sd.wait()  # Wait until the sound has finished playing
    
def outputs(text, file_path):
	
	#find path of file and later-on output redacted-file with appropriate extension
	output_path = os.path.dirname(file_path)
	
	#create an new pdf with the redacted text formatted into it
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size = 15)
	formatted_text = text.replace("\n", "\n\n")
	pdf.multi_cell(0, 10, formatted_text)
	pdf.output(output_path + "/out.pdf")
	
	#clean the text before sending for txt-to-speech engine
	#eliminates anyother character (like cyrillic chars and numbers) than A-Z
	#here 'NFC' means we are considering cyrillic/partial-latin chatacters as pre-accented and one unit
	cleaned_text = re.sub(r'[^a-zA-Z\s]', '', unicodedata.normalize('NFC', text))
	
	#calls the text_to_speech function
	text_to_speech(cleaned_text, output_path)
	
#enhanced RegEx patterns 4 phone numbers (with area/country code support), credit cards, SSNs, and aadhar nos.
phone_pattern = r'\b(?:\+?\d{1,3}\s?[-.\(]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}|\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4})\b'
credit_card_pattern = r'\b(?:\d{4}[-\s]??\d{4}[-\s]??\d{4}[-\s]??\d{4})\b'	
ssn_pattern = r'\b\d{3}[-.\s]??\d{2}[-.\s]??\d{4}\b'
aadhar_pattern = r'\b\d{4}[-\s]??\d{4}[-\s]??\d{4}\b'

def redact_with_regex(page_text, pattern, page):
	matches = re.finditer(pattern, page_text)
	for match in matches:
		text = match.group(0)  #get the matched text
		text_instances = page.search_for(text)  #search for text in current page iteration (must work on intergating with black-box engine)
		for inst in text_instances:
			rect = fitz.Rect(inst) #calc. bound rectangle of the matched text for accurate bounding
			page.add_redact_annot(rect, fill=(0, 0, 0))  #add a black box over the matched text

#main function to redact keywords and sensitive information in the PDF
def redact_keyword_in_pdf(input_pdf_path, output_pdf_path, keyword=None):
	#open input PDF
	pdf_document = fitz.open(input_pdf_path)

	#iterate through each page
	for page in pdf_document:
		page_text = page.get_text("text")  #extract text from the page

		#if keyword is provided, redact it
		if keyword:
			text_instances = page.search_for(keyword)  #find instances of keyword
			for inst in text_instances:
				rect = fitz.Rect(inst)
				page.add_redact_annot(rect, fill=(0, 0, 0))  #add black box over keyword
			page.apply_redactions()  #save performed redactions for keyword

		else:  #if no keyword provided, proceed with NLP and regex-based redactions
			#redact spaCy recognized entities
			doc = nlp(page_text)
			for ent in doc.ents:
				if ent.label_ in ["PERSON", "ORG", "GPE", "DATE"]:  #add more labels if necessary
					text_instances = page.search_for(ent.text)  #search for the entity text
					for inst in text_instances:
						rect = fitz.Rect(inst)  #bound rectangle of the entity
						page.add_redact_annot(rect, fill=(0, 0, 0))  #add black box over entity

			#redact sensitive information using the provided regex patterns
			redact_with_regex(page_text, phone_pattern, page)  #redact phone numbers
			redact_with_regex(page_text, credit_card_pattern, page)  #redact credit cards
			redact_with_regex(page_text, ssn_pattern, page)  #redact SSNs
			redact_with_regex(page_text, aadhar_pattern, page)  #redact Aadhar numbers

			page.apply_redactions()  #apply redactions to the page
	
	#save the modified PDF to the output path
	pdf_document.save(output_pdf_path)

	#take and store logs for pdf
	logs_file = open(logs_name_file, "a") 
	logs_file.write(str(pdf_document.metadata)+"\n\n")
	logs_file.close()
	
	#close the pdf document to prevent process hangup/resourse waste
	pdf_document.close()
	
def get_bert_entities(text):

	#tokenize and also pre-fetch logits as-well as train
	#tokenize the input text
	inputs = tokenizer(text, return_tensors="tf", truncation=True, padding=True)
	
	#perform inference through the BeRT
	outputs = bert_model(**inputs)
	logits = outputs.logits

	#get predicted token IDs and convert them to labels
	predicted_ids = tf.argmax(logits, axis=-1)
	
	#convert token IDs back to actual tokens for NLP/NER engine further on..
	tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
	
	#map predicted IDs to tokens
	predicted_labels = [tokenizer.convert_ids_to_tokens(predicted_ids[0].numpy())]
	
	#create list of entities (ignoring "O" labels, which mean no entity)
	entity_labels = []
	for token, label in zip(tokens, predicted_labels[0]):
		if label != "O":  #as previously mentioned, "O" means no entity
			entity_labels.append((token, label))
	
	return entity_labels

#update (3) (major-2 revamp):
#implemented nlp/ml into single pass
#utilized re.sub and re.cache for faster replacement and dict. caching
#implemented helpr function for synthetic_data gen. and rep.
#must implement parallelization, better caching and Profiling (cProfile & line_profiler)
#added: trainer model and pre-trained dataset (in .json)
#update: stress tested in local win-11 host with CUDA. room for model (parameters) improvement exists

def redact_text(text, redaction_level, keyword=None):
	#apply keyword redaction if provided
	if keyword:
		return text.replace(keyword, "[REDACTED]").replace(f" {keyword} ", " [REDACTED] ")

	#synthesize text (through NLP)
	doc = nlp(text)
	redacted_text = text

	#perform initial RegEx matches
	text = re.sub(phone_pattern, lambda match: "[REDACTED]", text)
	text = re.sub(credit_card_pattern, lambda match: "[REDACTED]", text)
	text = re.sub(ssn_pattern, lambda match: "[REDACTED]", text)
	text = re.sub(aadhar_pattern, lambda match: "[REDACTED]", text)

	#obtain BeRT entities (this would be a placeholder)
	bert_entities = get_bert_entities(text)  # Replace with actual BERT logic

	#combine BeRT and spaCy entities into one list (to prevent unnecessary iterations)
	entities_to_redact = []

	#add beRT entities (PER, ORG, LOC, MISC)
	if ml_choice_checkbox.get() == 1:  #rep. placeholder for ML choice
		print("ML Choice: Selected")
		for entity, label in bert_entities:
			if label in ["PER", "ORG", "LOC", "MISC"]:
				entities_to_redact.append((entity, label))
	else:
		print("ML Choice: Not Selected")

	#add spaCy entities (PERSON, ORG, GPE, DATE)
	for ent in doc.ents:
		if ent.label_ in ["PERSON", "ORG", "GPE", "DATE"]:
			entities_to_redact.append((ent.text, ent.label_))

	#already pre-compute synthetic data for high redaction level
	synthetic_data = {}

	def get_synthetic_data(label):
		"""Generate synthetic data for a specific entity label, caching results."""
		if label not in synthetic_data:
			if label == "PERSON":
				synthetic_data[label] = fake.name()
			elif label == "ORG":
				synthetic_data[label] = fake.company()
			elif label == "LOC" or label == "GPE":
				synthetic_data[label] = fake.city()
			elif label == "MISC":
				synthetic_data[label] = fake.word()
			elif label == "DATE":
				synthetic_data[label] = fake.date()
		return synthetic_data[label]

	#create replacement map for entities and their redacted forms
	replacement_map = {}

	#iterate through every entity and label 4 recognized tokens
	for entity, label in entities_to_redact:
		if redaction_level == "LOW":
			replacement_map[entity] = "[REDACTED]"

		elif redaction_level == "MID":
			masked_entity = entity[0] + '*' * (len(entity) - 2) + entity[-1] if len(entity) > 2 else entity
			replacement_map[entity] = masked_entity
		
		elif redaction_level == "HIGH":
			synthetic_entity = get_synthetic_data(label)
			replacement_map[entity] = synthetic_entity

	#use regex to replace all entities in one iteration
	def replace_entity(match):
		entity = match.group(0)
		return replacement_map.get(entity, entity)  #use replacement if found, else just return original

	#build regex pattern to match any of the entities to perform redaction
	entity_pattern = re.compile("|".join(re.escape(entity) for entity in replacement_map.keys()))
	redacted_text = entity_pattern.sub(replace_entity, text)

	#add  newly identified entities to the training data
	new_annotation = {
		"text": text,
		"entities": [(start, end, label) for start, end, label in doc.ents]
	}

	#append new annotation to TRAIN_DATA and save to JSON file formatt
	TRAIN_DATA.append(new_annotation)
	with open("train_data.json", "w") as f_dat_dump:
		json.dump(TRAIN_DATA, f_dat_dump, indent=4) #set to '4' (indent) for tab width

	return redacted_text
		
#implemented nlp/ml into single pass
#utilized re.sub and re.cache for faster replacement and dict. caching
#implemented helpr function for synthetic_data gen. and rep.
#must implement parallelization, better caching and Profiling (cProfile & line_profiler)

def redact_text(text, redaction_level, keyword=None):

	#apply keyword redaction if provided
	if keyword:
		return text.replace(keyword, "[REDACTED]").replace(f" {keyword} ", " [REDACTED] ")

	doc = nlp(text)
	redacted_text = text
	
	#apply regex-based redactions for phone numbers, credit cards, SSNs, and Aadhar numbers
	text = re.sub(phone_pattern, lambda match: redact_phone(match, redaction_level), text)
	text = re.sub(credit_card_pattern, lambda match: redact_credit_card(match, redaction_level), text)
	text = re.sub(ssn_pattern, lambda match: redact_ssn(match, redaction_level), text)
	text = re.sub(aadhar_pattern, lambda match: redact_aadhar(match, redaction_level), text)
		
	#obtain BeRT entities
	bert_entities = get_bert_entities(text)

	#Combine BeRT and spaCy entities into one list 4 a single pass
	entities_to_redact = []

	#Add BeRT entities (PER, ORG, LOC, MISC)
	if ml_choice_checkbox.get() == 1:
		print("ML Choice: Selected")
		for entity, label in bert_entities:
			if label in ["PER", "ORG", "LOC", "MISC"]:
				entities_to_redact.append((entity, label))
	else:
		print("ML Choice: Not Selected")

	#add spaCy entities (PERSON, ORG, GPE, DATE)
	for ent in doc.ents:
		if ent.label_ in ["PERSON", "ORG", "GPE", "DATE"]:
			entities_to_redact.append((ent.text, ent.label_))

	#pre-compute synthetic data 4 high redaction level (to prevent redundant generation)
	synthetic_data = {}

	def get_synthetic_data(label):
		"""Generate synthetic data for a specific entity label, caching results."""
		if label not in synthetic_data:
			if label == "PERSON":
				synthetic_data[label] = fake.name()
			elif label == "ORG":
				synthetic_data[label] = fake.company()
			elif label == "LOC" or label == "GPE":
				synthetic_data[label] = fake.city()
			elif label == "MISC":
				synthetic_data[label] = fake.word()
			elif label == "DATE":
				synthetic_data[label] = fake.date()
		return synthetic_data[label]

	#Create replacement map 4 entities and their redacted forms
	replacement_map = {}

	for entity, label in entities_to_redact:
	
		if redaction_level == "LOW":
			replacement_map[entity] = "[REDACTED]"

		elif redaction_level == "MID":

			#Mask all letters in b/w but the first and last character
			#entity[0] is first letter
			# '*' * (len(entity)-2) multiplies asterisk (excluding first and last letter)
			#entity[-1] is last letter
			#if else to check if greater than 2 letters
			
			masked_entity = entity[0] + '*' * (len(entity) - 2) + entity[-1] if len(entity) > 2 else entity
			replacement_map[entity] = masked_entity
		
		elif redaction_level == "HIGH":
		
			#Replace with synthetic data
			synthetic_entity = get_synthetic_data(label)
			replacement_map[entity] = synthetic_entity
    
	#utilize RegEx to replace all entities in 1 go
	def replace_entity(match):
		entity = match.group(0)
		return replacement_map.get(entity, entity)  #use the replacement if found, else just return original val.

	#Build an regular expression pattern (matching all entities)
	#We create the pattern that matches any of the entities to perform redaction
	entity_pattern = re.compile("|".join(re.escape(entity) for entity in replacement_map.keys()))

	#Perform the replacement in one pass using re.sub (instead of replace which is a bit inefficient)
	redacted_text = entity_pattern.sub(replace_entity, text)

	return redacted_text


def preprocess_and_recognize_audio(audio_file):

	audio = AudioSegment.from_file(audio_file).set_channels(1).set_frame_rate(16000)
	processed_file = "/tmp/output-processed-audio.wav"
	audio.export(processed_file, format="wav")
	
	recognizer = sr.Recognizer()
	
	with sr.AudioFile(processed_file) as source:
		audio_data = recognizer.record(source)
	try:
		text = recognizer.recognize_sphinx(audio_data)
		print("Processed Audio Speech:", text)
		return text
	except sr.UnknownValueError:
		print("Sorry, the audio could not be deciphered. Please provide a clear .wav/.flacc audio file.")
	except sr.RequestError as e:
		print(f"Could not perform conversion: {e}")
	
	os.remove(processed_file)

def drop_and_identify(file_path,grade):

	_, extension = os.path.splitext(file_path)

	if extension == ".pdf":
		keyword = entry1.get()
		try:
			with open(file_path, 'rb') as file:
				reader = PyPDF2.PdfReader(file)
				text = []
				for page in reader.pages:
					text.append(page.extract_text())
				red_text = "\n".join(text)

				#ensure the redacted output is properly encoded in UTF-8
				redacted_output = redact_text(red_text, grade, keyword)

				#assuming redact_keyword_in_pdf function handles PDF redaction well
				output_path = os.path.dirname(file_path) + "/out.pdf"
				redact_keyword_in_pdf(file_path, output_path, keyword)

				#display the redacted output with proper encoding
				show_scroll_messagebox("Redacted Output [PDF]", redacted_output)

		except Exception as exp:
			messagebox.showerror("Error", f"We've Encountered an error. Please provide a proper file within the specified formats and check for discrepancies.\n{str(exp)}")

	elif extension == ".wav":
		text = preprocess_and_recognize_audio(file_path)
		keyword = entry1.get()
		try:
			#handle redaction for Latin characters in the transcribed text
			redacted_text = redact_text(text, grade, keyword)

			#ensure UTF-8 encoding for the redacted text
			show_scroll_messagebox("Redacted Output [AUDIO]", redacted_text)
			outputs(redacted_text, file_path)

		except Exception as exp:
			messagebox.showerror("Error", f"We've Encountered an error. Please provide a proper file within the specified formats and check for discrepancies.\n{str(exp)}")

	elif extension == ".png" or extension == ".jpg" or extension == ".jpeg":
		try:
			text = pytesseract.image_to_string(file_path)
			print(f"Before Redaction: {text}")

			keyword = entry1.get()
			
			#clean the text before sending for img-to-txt engine
			#eliminates anyother character (like cyrillic chars and numbers) than A-Z
			#here 'NFC' means we are considering cyrillic chatacters as pre-accented and one unit
			cleaned_text = re.sub(r'[^a-zA-Z\s]', '', unicodedata.normalize('NFC', text))

			#Handle text redaction for Latin characters
			redacted_text = redact_text(cleaned_text, grade, keyword)

			#ensure UTF-8 encoding for the redacted text before print
			#display redacted text as-is
			show_scroll_messagebox("Redacted Output [IMAGE]", redacted_text)
			outputs(redacted_text, file_path)

		except Exception as exp:
			messagebox.showerror("Error", f"We've Encountered an error. Please provide a proper file within the specified formats and check for discrepancies.\n{str(exp)}")

	else:
		messagebox.showerror("Error", "We've Encountered an error. Please provide a proper file within the specified formats and check for discrepancies.")


def drag_and_drop(grade):

	#initialize root window with CustomTkinter
	root = TkinterDnD.Tk()
	
	root.title("Drag-n-Drop")
	root.geometry("500x200")
	root.resizable(False, False)
	
	label = tkin.Label(root, text="Drag-n-Drop The File Here! \n \n(PDF, TXT, PNG, JPEG, JPG, WAV, FLACC, MP3)", padx=10, pady=10, bd = 2, relief="raised")
	label.pack(expand=True, fill=tkin.BOTH)
    
	#Registering the drop target for drag and drop
	root.drop_target_register(DND_FILES)
	
	#Reset all buttons to normal state with gray background
	add_button1.configure(fg_color="white", bg_color="gray", state="normal")
	add_button2.configure(fg_color="white", bg_color="gray", state="normal")
	add_button3.configure(fg_color="white", bg_color="gray", state="normal")
	
	show_sidebar()
	
	#Change button styles based on the selected grade
	if grade == "LOW":
		add_button1.configure(fg_color="black", bg_color="yellow", state="disabled")
		add_button2.configure(fg_color="gray", bg_color="blue", state="normal")
		add_button3.configure(fg_color="gray", bg_color="blue", state="normal")
		print("LOW")
	elif grade == "MID":
		add_button1.configure(fg_color="gray", bg_color="blue", state="normal")
		add_button2.configure(fg_color="black", bg_color="yellow", state="disabled")
		add_button3.configure(fg_color="gray", bg_color="blue", state="normal")
		print("MID")
	elif grade == "HIGH":
		add_button1.configure(fg_color="gray", bg_color="blue", state="normal")
		add_button2.configure(fg_color="gray", bg_color="blue", state="normal")
		add_button3.configure(fg_color="black", bg_color="yellow", state="disabled")
		print("HIGH")
	root.dnd_bind('<<Drop>>', lambda event:drop_and_identify(event.data,grade))
	root.mainloop()
	
def show_sidebar():

	#show the right sidebar only when any grade button is clicked
	right_sidebar_frame.grid(row=0, column=2, sticky="nse", padx=10, pady=10)

	#xreate a scrollable frame in the sidebar
	scrollable_frame = ctk.CTkScrollableFrame(right_sidebar_frame, width=100, height=200)
	scrollable_frame.grid(row=0, column=0, pady=5, padx=10, sticky="nsew")

	#add some checkboxes for Name, Location, Organization, and Date
	name_checkbox = ctk.CTkCheckBox(scrollable_frame, text="NAME", command=lambda: print("NAME"))
	name_checkbox.pack(pady=5)

	location_checkbox = ctk.CTkCheckBox(scrollable_frame, text="LOC/GPE", command=lambda: print("LOC/GPE"))
	location_checkbox.pack(pady=5)

	organization_checkbox = ctk.CTkCheckBox(scrollable_frame, text="ORG", command=lambda: print("ORG"))
	organization_checkbox.pack(pady=5)

	date_checkbox = ctk.CTkCheckBox(scrollable_frame, text="DATE/TIME", command=lambda: print("DATE/TIME"))
	date_checkbox.pack(pady=5)
	
#set custom color theme
ctk.set_appearance_mode("dark")  #change to 'Light' or 'Dark' when needed
ctk.set_default_color_theme("blue") 

#create main window
window = ctk.CTk()
window.title("RE-DACT v4.5")
window.geometry("600x400")
window.resizable(True, True)

#configure grid for expandability
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)
window.grid_columnconfigure(2, weight=2)  #right side-bar column

#create log file
logs_name_file = "/root/Desktop/logs-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
logs_file = open(logs_name_file, "x")
logs_file.close()

#variables (pre-def to global)
locked = False
case_sensitive = False
use_ml = False

#sidebar frame (Left)
sidebar_frame = ctk.CTkFrame(window, corner_radius=10)
sidebar_frame.grid(row=0, column=0, sticky="nsw", padx=10, pady=10)

#main frame (Center)
main_frame = ctk.CTkFrame(window, corner_radius=10)
main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

#right sidebar frame (Expands with selection)
right_sidebar_frame = ctk.CTkFrame(window, corner_radius=10)

#config. frames to expand dynamically
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

#label and entry in the main frame
label1 = ctk.CTkLabel(main_frame, text="\nEnter The keyword to Redact: \n", font=("Arial", 15))
label1.grid(row=0, column=0, pady=(10, 5), sticky="n")

entry1 = ctk.CTkEntry(main_frame, placeholder_text="Enter keyword here...", width=200)
entry1.grid(row=1, column=0, pady=5)

lock_button = ctk.CTkButton(main_frame, text="\U0001f513", command=toggle_lock, width=50, fg_color="green")
lock_button.grid(row=2, column=0, pady=(10, 10))

#grade selector label
label2 = ctk.CTkLabel(main_frame, text="\nChoose the Grade of Redaction: \n", font=("Arial", 15))
label2.grid(row=3, column=0, pady=(10, 5))

#grade buttons (each button will trigger the right sidebar to show up)
add_button1 = ctk.CTkButton(main_frame, text="Grade - 1 (LOW)", command=lambda: drag_and_drop("LOW"))
add_button1.grid(row=4, column=0, pady=10)

add_button2 = ctk.CTkButton(main_frame, text="Grade - 2 (MID)", command=lambda: drag_and_drop("MID"))
add_button2.grid(row=5, column=0, pady=10)

add_button3 = ctk.CTkButton(main_frame, text="Grade - 3 (HIGH)", command=lambda: drag_and_drop("HIGH"))
add_button3.grid(row=6, column=0, pady=10)

case_sensitive_checkbox = ctk.CTkCheckBox(sidebar_frame, text="Case Sensitive", command=toggle_case_sensitive)
case_sensitive_checkbox.pack(pady=20)

ml_choice_checkbox = ctk.CTkCheckBox(sidebar_frame, text="ML Model", command=toggle_ml_choice)
ml_choice_checkbox.pack(pady=20)

NLP_choice_checkbox = ctk.CTkCheckBox(sidebar_frame, text="NLP Trainer", command=toggle_NLP_choice)
NLP_choice_checkbox.pack(pady=20)

window.mainloop()
