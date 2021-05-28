# Parcel Tracking Bot

Bot developed to track multiple shipment details from different carriers, don't spend hours tracking your shipments, instead just run the application and get all details you need with our amazing integrated user interface.


## Requirements

- Python
- PySyde2
- Qt Designer
- Selenium
- Pandas

## Quick Start

The bot *should* work if all requierements are properly installed.

The funcionality of the bot is relatively simple:

- Run the application.
- Select Carrier [CEVA, DHL,EXPEDITORS, FEDEX, UPS, UPS-SCS]
- Enter Tracking Number/s
- All details you need will be exported to a .csv file where you installed your application.
- Done!

Additional details:

1. Make sure you modify all icon locations within the code in case you moved the "Imageformats" folder to a different location or you just want to replace the icons:

    ```
    See example below:
    *In case you want to replace the default icon, just simply replace the folder location *

    self.resize(680,400)
    self.setWindowTitle("TRACKING BOT")
    self.setStyleSheet("color: rgb(220, 220, 220);background: rgb(47, 69, 92); border-radius: 20px;")  
    self.setWindowIcon(QtGui.QIcon(r"C:\ExampleFolder\\ExampleFile.ico")) 
    ```
2. Make sure you install the Google Chrome driver in the default Location or modify the code and add the desired location:

    ```
    Default Location:
    
    driverPath = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(driverPath, options=options)

    Or just simply modify the location in all scripts:
    
    driverPath = "C:\FolderExample\chromedriver.exe"
    driver = webdriver.Chrome(driverPath, options=options)    
    
    ```
    
    **In general the code is really intuitve and you can identify the structure and modify what you desire or even add aditional carrier following the same structure.**
    
3. Once you are done with your modifications, just simply run the following comand in the console:

    ```
    pyinstaller --clean --onefile --windowed main.py
    
    *Make sure you direct to the folder where you have the "main.py" folder*
    
    ```

## OverView

![image](https://user-images.githubusercontent.com/84207679/120042811-6bf12280-bfd0-11eb-9f6f-5e05b3484d59.png)

![image](https://user-images.githubusercontent.com/84207679/120042831-74495d80-bfd0-11eb-8dbd-f23a9e375538.png)





