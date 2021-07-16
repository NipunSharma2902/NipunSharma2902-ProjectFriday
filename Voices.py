    # Import the gTTS module for text  
    # to speech conversion  
    import os
    from gtts import gTTS
      
    # It is a text value that we want to convert to audio  
    text_val = 'Hello, everyone. This is an example of Text to Speech'  
      
      
    # Passing the text and language to the engine,  
    # here we have assign slow=False. Which denotes  
    # the module that the transformed audio should  
    # have a high speed  
    obj = gTTS(text=text_val, lang='en', slow=False)  
      
    #Here we are saving the transformed audio in a mp3 file named  
    # exam.mp3  
    obj.save("TextToSpeech.mp3")  
      
    # Play the exam.mp3 file  
    os.system("TextToSpeech.mp3")