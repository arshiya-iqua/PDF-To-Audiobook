import pyttsx3 # Text to speech conversion
import PyPDF2 # PDF manipulation
from tkinter.filedialog import *

book=askopenfilename() # Open file dialog to select a PDF file

with open(book,'rb') as pdf_file: # Open the selected PDF file in binary read mode
    pdfreader=PyPDF2.PdfReader(pdf_file) # Create a PDF reader object
    pages=len(pdfreader.pages) # Get the number of pages in the PD          
    
    player=pyttsx3.init() # Initialize the text-to-speech engineF
    
    for num in range(0,pages):
        page=pdfreader.pages[num] # Get the page object
        text=page.extract_text() # Extract text from the page
        
        if text:
            player.say(text) # Convert the extracted text to speech
       
    player.runAndWait() # Play the speech
