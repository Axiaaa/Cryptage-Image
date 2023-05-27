import os, cryptage

try : 
    if not os.path.exists("Output") :
        os.makedirs("Output")
    if not os.path.exists("Input") : 
        os.makedirs("Input")


except Exception as e :
    print("Un problem est survenu ! {e}")





