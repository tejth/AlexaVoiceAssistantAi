from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
from engine.helper import extract_yt_term

from engine.command import speak
import os

import pywhatkit as kit

#playing assistant sound function
@eel.expose
def playAssistantSound():
    music_dir = "C:\\Users\\tejth\\Desktop\\Jarvis\\www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    if query!="":
        speak("Opening "+query)
        os.system("start "+query)
    else:
        speak("not found")
        
        
        
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)
