#before running the script, install dependencies from requirements.txt:
#pip install -r requirements.txt

# NOTE: The program is obfuscated + minified and comments explaining vital code snippets have been delibrately removed.
# EXPLANATION: Since the program is still in dev. the code is hence not fully revealed. It will be after final-stage/some time..
# EXPLANATION 2: In the meanwhile, you could still execute the program without any hinderance. Raise an issue if you encounter any problem.

#! /root/my_virt_envs/bin/python3

#above microprocessor executes code directly form python .venv package. modify to suit your venv. path
#for linux terminal implementation/execution: source /location/to/venv/bin/activate


q='[^a-zA-Z\\s]'
r='/out.pdf'
s='dbmdz/bert-large-cased-finetuned-conll03-english'
d='DATE'
e='GPE'
f='PERSON'
g=Exception
h=open
V=True
W='ORG'
X='disabled'
Y=str
O='Arial'
P='black'
M='white'
J='blue'
K=False
F='HIGH'
G='MID'
H='LOW'
B='normal'
C=print
import os,re as D,time,tkinter as L
from tkinter import messagebox as Z,scrolledtext as A5
import customtkinter as A
from tkinterdnd2 import DND_FILES as A6,TkinterDnD as A7
from PIL import Image
import PyPDF2
from fpdf import FPDF as t
from pydub import AudioSegment as i
import spacy
from faker import Faker
import pytesseract as A8
from PIL import Image
import speech_recognition as a
from pydub import AudioSegment as i
import pyttsx3,numpy as AT,sounddevice as A9,fitz as b,tensorflow as AA
from transformers import BertTokenizer as AB,TFBertForTokenClassification as AC
import unicodedata as u
v=spacy.load('en_core_web_lg')
E=Faker()
j=AB.from_pretrained(s)
AD=AC.from_pretrained(s)
def AE():global w;w=A4.get()
def AF():global x;x=p.get()
def AG():
	global Q;Q=not Q;R.configure(state=X if Q else B)
	if Q:o.configure(text='🔒',fg_color='red',text_color=P)
	else:o.configure(text='🔓',fg_color='green',text_color=P)
class AU(t):
	def header(A):A.set_font(O,'B',12);A.cell(0,10,'My PDF Title',0,1,'C');A.ln(10)
	def footer(A):A.set_y(-15);A.set_font(O,'I',8);A.cell(0,10,f"Page {A.page_no()}",0,0,'C')
def k(title,message):OO000O000O000O0O0=L.Toplevel();OO000O000O000O0O0.title(title);O0OOOOOO00O00O0OO=A5.ScrolledText(OO000O000O000O0O0,wrap=L.WORD,width=50,height=10);O0OOOOOO00O00O0OO.insert(L.END,message);O0OOOOOO00O00O0OO.config(state=L.DISABLED);O0OOOOOO00O00O0OO.pack(padx=10,pady=10);O000000OO00O00OO0=L.Button(OO000O000O000O0O0,text='OK',command=OO000O000O000O0O0.destroy);O000000OO00O00OO0.pack(pady=(0,10));OO000O000O000O0O0.transient();OO000O000O000O0O0.grab_set()
def AH(text,output_path):
	O0O000000O00O00O0='/tmp/text-to-speech-output.wav';O00O0O0OOOOO0OOOO=pyttsx3.init();OOOOOO0O0O0O00O0O=O00O0O0OOOOO0OOOO.getProperty('voices');O00O0O0OOOOO0OOOO.setProperty('rate',18);O00O0O0OOOOO0OOOO.setProperty('volume',1.);O00O0O0OOOOO0OOOO.setProperty('voice',OOOOOO0O0O0O00O0O[1].id)
	def O0OO0O0O000OO0OOO(indata,frames,time,status):
		O0000O0OOOO0OO0O0=status
		if O0000O0OOOO0OO0O0:C(O0000O0OOOO0OO0O0)
		A9.play(indata,samplerate=44100)
	O00O0O0OOOOO0OOOO.save_to_file(text,O0O000000O00O00O0);O00O0O0OOOOO0OOOO.runAndWait();O00O000OOOOO00000=i.from_wav(O0O000000O00O00O0);O00OOOOOO00OOOOOO=O00O000OOOOO00000.speedup(playback_speed=1.1);O00OOOOOO00OOOOOO.export(output_path+'/text-to-speech-out.wav',format='wav')
def y(text,file_path):OO0000OO00000O0OO=os.path.dirname(file_path);OOO0O0000O0OO00OO=t();OOO0O0000O0OO00OO.add_page();OOO0O0000O0OO00OO.set_font(O,size=15);O000OOO0OOO00OO00=text.replace('\n','\n\n');OOO0O0000O0OO00OO.multi_cell(0,10,O000OOO0OOO00OO00);OOO0O0000O0OO00OO.output(OO0000OO00000O0OO+r);O0O0000OO0O0000O0=D.sub(q,'',u.normalize('NFC',text));AH(O0O0000OO0O0000O0,OO0000OO00000O0OO)
z='\\b(?:\\+?\\d{1,3}\\s?[-.\\(]?\\(?\\d{1,4}\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}|\\(?\\d{1,4}\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4})\\b'
A0='\\b(?:\\d{4}[-\\s]??\\d{4}[-\\s]??\\d{4}[-\\s]??\\d{4})\\b'
A1='\\b\\d{3}[-.\\s]??\\d{2}[-.\\s]??\\d{4}\\b'
A2='\\b\\d{4}[-\\s]??\\d{4}[-\\s]??\\d{4}\\b'
def c(page_text,pattern,page):
	OOOOO0O0O00OO000O=D.finditer(pattern,page_text)
	for O0O00OOOO00OO00O0 in OOOOO0O0O00OO000O:
		O0O000O0OO0OO0000=O0O00OOOO00OO00O0.group(0);O00O00OOOO0O0OO0O=page.search_for(O0O000O0OO0OO0000)
		for O0O0O0OO0OOOOO0OO in O00O00OOOO0O0OO0O:O0OO0OO0O0O000O00=b.Rect(O0O0O0OO0OOOOO0OO);page.add_redact_annot(O0OO0OO0O0O000O00,fill=(0,0,0))
def AI(input_pdf_path,output_pdf_path,keyword=None):
	OO0O0O0O000OOO00O=keyword;O00000000000OOO0O=b.open(input_pdf_path)
	for OO000O0OO0000OOO0 in O00000000000OOO0O:
		O0O000OOOOOOO0OO0=OO000O0OO0000OOO0.get_text('text')
		if OO0O0O0O000OOO00O:
			OOO00O0OO0000O0OO=OO000O0OO0000OOO0.search_for(OO0O0O0O000OOO00O)
			for O0O0000000O00OOO0 in OOO00O0OO0000O0OO:O0OOOOOOOO00OO0OO=b.Rect(O0O0000000O00OOO0);OO000O0OO0000OOO0.add_redact_annot(O0OOOOOOOO00OO0OO,fill=(0,0,0))
			OO000O0OO0000OOO0.apply_redactions()
		else:
			OO00O000O0O00000O=v(O0O000OOOOOOO0OO0)
			for OOO0O0OOO0O0OO0OO in OO00O000O0O00000O.ents:
				if OOO0O0OOO0O0OO0OO.label_ in[f,W,e,d]:
					OOO00O0OO0000O0OO=OO000O0OO0000OOO0.search_for(OOO0O0OOO0O0OO0OO.text)
					for O0O0000000O00OOO0 in OOO00O0OO0000O0OO:O0OOOOOOOO00OO0OO=b.Rect(O0O0000000O00OOO0);OO000O0OO0000OOO0.add_redact_annot(O0OOOOOOOO00OO0OO,fill=(0,0,0))
			c(O0O000OOOOOOO0OO0,z,OO000O0OO0000OOO0);c(O0O000OOOOOOO0OO0,A0,OO000O0OO0000OOO0);c(O0O000OOOOOOO0OO0,A1,OO000O0OO0000OOO0);c(O0O000OOOOOOO0OO0,A2,OO000O0OO0000OOO0);OO000O0OO0000OOO0.apply_redactions()
	O00000000000OOO0O.save(output_pdf_path);OO0O000O0O00OOOOO=h(A3,'a');OO0O000O0O00OOOOO.write(Y(O00000000000OOO0O.metadata)+'\n\n');OO0O000O0O00OOOOO.close();O00000000000OOO0O.close()
def AJ(text):
	O00OO00OO0000O00O=j(text,return_tensors='tf',truncation=V,padding=V);O00OOOOO0OOOO00O0=AD(**O00OO00OO0000O00O);OO00OO00O0000OOOO=O00OOOOO0OOOO00O0.logits;O0O0000O0O0000OOO=AA.argmax(OO00OO00O0000OOOO,axis=-1);O0OOO00OO0O0OO0OO=j.convert_ids_to_tokens(O00OO00OO0000O00O['input_ids'][0]);OOOO000OOOOO0O0O0=[j.convert_ids_to_tokens(O0O0000O0O0000OOO[0].numpy())];OO00OOO0O0O00OO0O=[]
	for(OOOO0O000O0OO0O0O,OO0O00O0000OO00OO)in zip(O0OOO00OO0O0OO0OO,OOOO000OOOOO0O0O0[0]):
		if OO0O00O0000OO00OO!='O':OO00OOO0O0O00OO0O.append((OOOO0O000O0OO0O0O,OO0O00O0000OO00OO))
	return OO00OOO0O0O00OO0O
def AK(match,redaction_level):
	OO0O00O00OOOO00OO=redaction_level;O0O0OOO000O00O0OO=match.group(0)
	if OO0O00O00OOOO00OO==H:return'[REDACTED PHONE]'
	elif OO0O00O00OOOO00OO==G:return'XXX-XXX-'+O0O0OOO000O00O0OO[-4:]
	elif OO0O00O00OOOO00OO==F:return E.phone_number()
def AL(match,redaction_level):
	OOO0OOOOO0OO0O0O0=redaction_level;OOOOO0O00000O00OO=match.group(0)
	if OOO0OOOOO0OO0O0O0==H:return'[REDACTED CREDIT CARD]'
	elif OOO0OOOOO0OO0O0O0==G:return'XXXX-XXXX-XXXX-'+OOOOO0O00000O00OO[-4:]
	elif OOO0OOOOO0OO0O0O0==F:return E.credit_card_number()
def AM(match,redaction_level):
	O00000000OO00O000=redaction_level;O000OOO0O00OOO0OO=match.group(0)
	if O00000000OO00O000==H:return'[REDACTED SSN]'
	elif O00000000OO00O000==G:return'XXX-XX-'+O000OOO0O00OOO0OO[-4:]
	elif O00000000OO00O000==F:return E.ssn()
def AN(match,redaction_level):
	O0OOO0000O000000O=redaction_level;OOOO0000O000000O0=match.group(0)
	if O0OOO0000O000000O==H:return'[REDACTED AADHAR]'
	elif O0OOO0000O000000O==G:return'XXXX-XXXX-'+OOOO0000O000000O0[-4:]
	elif O0OOO0000O000000O==F:return E.ssn()
def l(text,redaction_level,keyword=None):
	O00O000000OOOOO0O='MISC';O0OOOO00OO0OO000O='LOC';O00O00OO0OOO0OO0O='[REDACTED]';OO0OO0O00000O00O0=keyword;OO0O000OOOO00000O=redaction_level;OO0OOO00O00000OO0=text
	if OO0OO0O00000O00O0:return OO0OOO00O00000OO0.replace(OO0OO0O00000O00O0,O00O00OO0OOO0OO0O).replace(f" {OO0OO0O00000O00O0} ",' [REDACTED] ')
	O0OO000O00OO0O000=v(OO0OOO00O00000OO0);OOOOO000O00OO0OOO=OO0OOO00O00000OO0;OO0OOO00O00000OO0=D.sub(z,lambda match:AK(match,OO0O000OOOO00000O),OO0OOO00O00000OO0);OO0OOO00O00000OO0=D.sub(A0,lambda match:AL(match,OO0O000OOOO00000O),OO0OOO00O00000OO0);OO0OOO00O00000OO0=D.sub(A1,lambda match:AM(match,OO0O000OOOO00000O),OO0OOO00O00000OO0);OO0OOO00O00000OO0=D.sub(A2,lambda match:AN(match,OO0O000OOOO00000O),OO0OOO00O00000OO0);OOOO0O0OO0OOO0O0O=AJ(OO0OOO00O00000OO0);OOO0000OO00O000OO=[]
	if p.get()==1:
		C('ML Choice: Selected')
		for(OO00OOO00O0OOOOO0,OOOOO00000OO00OO0)in OOOO0O0OO0OOO0O0O:
			if OOOOO00000OO00OO0 in['PER',W,O0OOOO00OO0OO000O,O00O000000OOOOO0O]:OOO0000OO00O000OO.append((OO00OOO00O0OOOOO0,OOOOO00000OO00OO0))
	else:C('ML Choice: Not Selected')
	for O0O00O00000OO0OO0 in O0OO000O00OO0O000.ents:
		if O0O00O00000OO0OO0.label_ in[f,W,e,d]:OOO0000OO00O000OO.append((O0O00O00000OO0OO0.text,O0O00O00000OO0OO0.label_))
	O0000000O0OO0O0O0={}
	def OO0O00O000O0O000O(label):
		O0OOOO00O000O0OO0=label
		if O0OOOO00O000O0OO0 not in O0000000O0OO0O0O0:
			if O0OOOO00O000O0OO0==f:O0000000O0OO0O0O0[O0OOOO00O000O0OO0]=E.name()
			elif O0OOOO00O000O0OO0==W:O0000000O0OO0O0O0[O0OOOO00O000O0OO0]=E.company()
			elif O0OOOO00O000O0OO0==O0OOOO00OO0OO000O or O0OOOO00O000O0OO0==e:O0000000O0OO0O0O0[O0OOOO00O000O0OO0]=E.city()
			elif O0OOOO00O000O0OO0==O00O000000OOOOO0O:O0000000O0OO0O0O0[O0OOOO00O000O0OO0]=E.word()
			elif O0OOOO00O000O0OO0==d:O0000000O0OO0O0O0[O0OOOO00O000O0OO0]=E.date()
		return O0000000O0OO0O0O0[O0OOOO00O000O0OO0]
	OOO000000OO0OO0OO={}
	for(OO00OOO00O0OOOOO0,OOOOO00000OO00OO0)in OOO0000OO00O000OO:
		if OO0O000OOOO00000O==H:OOO000000OO0OO0OO[OO00OOO00O0OOOOO0]=O00O00OO0OOO0OO0O
		elif OO0O000OOOO00000O==G:OOOOOOOOO000OO0O0=OO00OOO00O0OOOOO0[0]+'*'*(len(OO00OOO00O0OOOOO0)-2)+OO00OOO00O0OOOOO0[-1]if len(OO00OOO00O0OOOOO0)>2 else OO00OOO00O0OOOOO0;OOO000000OO0OO0OO[OO00OOO00O0OOOOO0]=OOOOOOOOO000OO0O0
		elif OO0O000OOOO00000O==F:OOOO0OO00O000O0OO=OO0O00O000O0O000O(OOOOO00000OO00OO0);OOO000000OO0OO0OO[OO00OOO00O0OOOOO0]=OOOO0OO00O000O0OO
	def OOO0OO0OO0O00OOOO(match):O0O0O00O00O00O00O=match.group(0);return OOO000000OO0OO0OO.get(O0O0O00O00O00O00O,O0O0O00O00O00O00O)
	O0O0O000OOOOOO00O=D.compile('|'.join(D.escape(OOOO000OO0O00O0O0)for OOOO000OO0O00O0O0 in OOO000000OO0OO0OO.keys()));OOOOO000O00OO0OOO=O0O0O000OOOOOO00O.sub(OOO0OO0OO0O00OOOO,OO0OOO00O00000OO0);return OOOOO000O00OO0OOO
def AO(audio_file):
	O0O0O0O00O00000O0=i.from_file(audio_file).set_channels(1).set_frame_rate(16000);O000OOOO000O0OO00='/tmp/output-processed-audio.wav';O0O0O0O00O00000O0.export(O000OOOO000O0OO00,format='wav');O0OO00O00OO0O0OOO=a.Recognizer()
	with a.AudioFile(O000OOOO000O0OO00)as O0O0000OO0O0O0O00:O0O00OOO00OO00000=O0OO00O00OO0O0OOO.record(O0O0000OO0O0O0O00)
	try:OOO0OO00O00OOO0OO=O0OO00O00OO0O0OOO.recognize_sphinx(O0O00OOO00OO00000);C('Processed Audio Speech:',OOO0OO00O00OOO0OO);return OOO0OO00O00OOO0OO
	except a.UnknownValueError:C('Sorry, the audio could not be deciphered. Please provide a clear .wav/.flacc audio file.')
	except a.RequestError as O00O00O00000O000O:C(f"Could not perform conversion: {O00O00O00000O000O}")
	os.remove(O000OOOO000O0OO00)
def AP(file_path,grade):
	OO0O0O000O0OOO0OO=grade;OO0O00O0000OO0000='Error';OO0O00OOO0OOO0O0O=file_path;OOOO0000O0O0O0OOO,OOO0O0OOO00O00O00=os.path.splitext(OO0O00OOO0OOO0O0O)
	if OOO0O0OOO00O00O00=='.pdf':
		O0OOOOOO00000OOO0=R.get()
		try:
			with h(OO0O00OOO0OOO0O0O,'rb')as O0O000OOOOO0O00OO:
				O0O0O0O0O000O000O=PyPDF2.PdfReader(O0O000OOOOO0O00OO);O0OO0O00O0OOOOOO0=[]
				for OOOO0O0OOO0O0OOOO in O0O0O0O0O000O000O.pages:O0OO0O00O0OOOOOO0.append(OOOO0O0OOO0O0OOOO.extract_text())
				OO0O00OO00OOOOO00='\n'.join(O0OO0O00O0OOOOOO0);OOOO0OO00O0O0O000=l(OO0O00OO00OOOOO00,OO0O0O000O0OOO0OO,O0OOOOOO00000OOO0);O0OO0OO0O0OO0O0OO=os.path.dirname(OO0O00OOO0OOO0O0O)+r;AI(OO0O00OOO0OOO0O0O,O0OO0OO0O0OO0O0OO,O0OOOOOO00000OOO0);k('Redacted Output [PDF]',OOOO0OO00O0O0O000)
		except g as OO0O0OO000OO0O0OO:Z.showerror(OO0O00O0000OO0000,f"We've Encountered an error. Please provide a proper file within the specified formats and check for discrepancies.\n{Y(OO0O0OO000OO0O0OO)}")
	elif OOO0O0OOO00O00O00=='.wav':
		O0OO0O00O0OOOOOO0=AO(OO0O00OOO0OOO0O0O);O0OOOOOO00000OOO0=R.get()
		try:OO00OO00OOOOO0O0O=l(O0OO0O00O0OOOOOO0,OO0O0O000O0OOO0OO,O0OOOOOO00000OOO0);k('Redacted Output [AUDIO]',OO00OO00OOOOO0O0O);y(OO00OO00OOOOO0O0O,OO0O00OOO0OOO0O0O)
		except g as OO0O0OO000OO0O0OO:Z.showerror(OO0O00O0000OO0000,f"We've Encountered an error. Please provide a proper file within the specified formats and check for discrepancies.\n{Y(OO0O0OO000OO0O0OO)}")
	elif OOO0O0OOO00O00O00=='.png'or OOO0O0OOO00O00O00=='.jpg'or OOO0O0OOO00O00O00=='.jpeg':
		try:O0OO0O00O0OOOOOO0=A8.image_to_string(OO0O00OOO0OOO0O0O);C(f"Before Redaction: {O0OO0O00O0OOOOOO0}");O0OOOOOO00000OOO0=R.get();OOO000O000OOO0O0O=D.sub(q,'',u.normalize('NFC',O0OO0O00O0OOOOOO0));OO00OO00OOOOO0O0O=l(OOO000O000OOO0O0O,OO0O0O000O0OOO0OO,O0OOOOOO00000OOO0);k('Redacted Output [IMAGE]',OO00OO00OOOOO0O0O);y(OO00OO00OOOOO0O0O,OO0O00OOO0OOO0O0O)
		except g as OO0O0OO000OO0O0OO:Z.showerror(OO0O00O0000OO0000,f"We've Encountered an error. Please provide a proper file within the specified formats and check for discrepancies.\n{Y(OO0O0OO000OO0O0OO)}")
	else:Z.showerror(OO0O00O0000OO0000,"We've Encountered an error. Please provide a proper file within the specified formats and check for discrepancies.")
def m(grade):
	O0000O0O0000000OO='yellow';OOOO00OOO00OO000O=grade;O0OO00OO0OO00O000='gray';O00O0O00O00O0O00O=A7.Tk();O00O0O00O00O0O00O.title('Drag-n-Drop');O00O0O00O00O0O00O.geometry('600x200');O00O0O00O00O0O00O.resizable(K,K);O000000000O0OO000=L.Label(O00O0O00O00O0O00O,text='Drag-n-Drop The File Here! \n \n(PDF, TXT, PNG, JPEG, JPG, WAV, FLACC, MP3)',padx=10,pady=10,bd=2,relief='raised');O000000000O0OO000.pack(expand=V,fill=L.BOTH);O00O0O00O00O0O00O.drop_target_register(A6);S.configure(fg_color=M,bg_color=O0OO00OO0OO00O000,state=B);T.configure(fg_color=M,bg_color=O0OO00OO0OO00O000,state=B);U.configure(fg_color=M,bg_color=O0OO00OO0OO00O000,state=B)
	if OOOO00OOO00OO000O==H:S.configure(fg_color=P,bg_color=O0000O0O0000000OO,state=X);T.configure(fg_color=O0OO00OO0OO00O000,bg_color=J,state=B);U.configure(fg_color=O0OO00OO0OO00O000,bg_color=J,state=B);C(H)
	elif OOOO00OOO00OO000O==G:S.configure(fg_color=O0OO00OO0OO00O000,bg_color=J,state=B);T.configure(fg_color=P,bg_color=O0000O0O0000000OO,state=X);U.configure(fg_color=O0OO00OO0OO00O000,bg_color=J,state=B);C(G)
	elif OOOO00OOO00OO000O==F:S.configure(fg_color=O0OO00OO0OO00O000,bg_color=J,state=B);T.configure(fg_color=O0OO00OO0OO00O000,bg_color=J,state=B);U.configure(fg_color=P,bg_color=O0000O0O0000000OO,state=X);C(F)
	O00O0O00O00O0O00O.dnd_bind('<<Drop>>',lambda event:AP(event.data,OOOO00OOO00OO000O));O00O0O00O00O0O00O.mainloop()
A.set_appearance_mode('dark')
A.set_default_color_theme(J)
N=A.CTk()
N.title('RE-DACT v4.1')
N.geometry('600x400')
N.resizable(K,K)
A3='/root/Desktop/logs-'+time.strftime('%Y%m%d-%H%M%S')+'.txt'
AQ=h(A3,'x')
AQ.close()
Q=K
w=K
x=K
n=A.CTkFrame(N,width=300,height=400,corner_radius=10)
n.pack(side='left',fill='y',padx=10,pady=10)
I=A.CTkFrame(N,width=500,height=400,corner_radius=10)
I.pack(side='left',fill='both',expand=V,padx=10,pady=10)
AR=A.CTkLabel(I,text='\nEnter The keyword to Redact: \n',font=(O,15),text_color=M)
AR.pack(pady=(10,5))
R=A.CTkEntry(I,placeholder_text='Enter keyword here...',width=250,text_color=M)
R.pack(pady=5)
o=A.CTkButton(I,text='🔓',command=AG,width=50,fg_color='green')
o.pack(pady=(10,10))
AS=A.CTkLabel(I,text='\nChoose the Grade of Redaction: \n',font=(O,15),text_color=M)
AS.pack(pady=(10,5))
S=A.CTkButton(I,text='GRADE - 1 (LOW)',command=lambda:m(H),width=150)
S.pack(pady=5)
T=A.CTkButton(I,text='GRADE - 2 (MID)',command=lambda:m(G),width=150)
T.pack(pady=5)
U=A.CTkButton(I,text='GRADE - 3 (HIGH)',command=lambda:m(F),width=150)
U.pack(pady=5)
A4=A.CTkCheckBox(n,text='Case Sensitive',command=AE)
A4.pack(pady=40)
p=A.CTkCheckBox(n,text='   ML Model',command=AF)
p.pack(pady=30)
N.mainloop()
