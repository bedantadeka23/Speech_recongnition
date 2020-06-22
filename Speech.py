while(1):
        #importing lib 
    import speech_recognition as sr
    import sys
    import webbrowser as web
    
    def main():
        path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  %s"
        r = sr.Recognizer()
                #using the Microphone as a input(source)    
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)#removing the noice 
            print("##### SMALL SPEECH RECONGNITION SYSTEM #####")
            print("......Please say something sir .....")
            
            audio_data = r.listen(source)                   #load the source 
            
            print(".......Recognizing the file..........")
            
            try:
                data = r.recognize_google(audio_data)
                print("You have said : \n " + data )        #converting the audio to txt file
                
                if(data=="open Chrome"):
                    url='https://www.google.com/'
                    web.get(path).open_new_tab(url)
                   
                if(data=="open Facebook"):
                    url='https://www.facebook.com/'
                    web.get(path).open_new_tab(url)
                    
                if(data=="open Instagram"):
                    url='https://www.instagram.com'
                    web.get(path).open_new_tab(url)
                    
                elif(r.recognize_google(audio_data)=="bye-bye"):
                    print("Thank you sir !! ")
                    sys.exit()
                    #Error of audio
            except Exception as e:
                print("****ERROR*****" + str(e))
                
                    #savig the recored_audio in the local file manager in mp3 version   
            with open("recored_audio.mp3", "wb")as f:
                f.write(audio_data.get_wav_data())
                print("......Audio data saved!!........")
                
                
    if __name__ == "__main__":
        main()
        