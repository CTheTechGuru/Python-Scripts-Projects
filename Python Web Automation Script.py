## Python Web Automation Script
## Steps 
import webbrowser as wb  ##Import webbrowser

def workauto(): #create function that will find the path of the browser and create a list of urls. 
    Chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' #Web path Variable
    URLS = ['www.google.com',] #List of urls

    for url in URLS:# loop through the list which will have each tab open. 
        wb.get(Chrome_path).open(url) #module and method to open url
    

workauto() # call the function 