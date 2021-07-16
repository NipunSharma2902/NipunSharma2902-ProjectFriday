import pyttsx3 
import win32com.client 

converter = pyttsx3.init()

converter.setProperty('rate', 150) 
converter.setProperty('volume', 0.7) 

voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# Use female voice 
converter.setProperty('voice', voice_id) 
  
converter.runAndWait() 