# Simple Guide to Installing Pygame for Python3

## Pre-requisites: The pip package manager

Before we install Pygame, we need to make sure that pip is properly installed on your machine. 

### For Mac:
1. Open the **Terminal** by pressing the _command_ + _space_ keys, then enter 'Terminal'.

2. Once the application opens, enter the following: `python3 -m pip --version`

3. If you get an error that states '...not a valid command', then pip is not installed. Otherwise, if you get a version number in return (as of March 2019: _pip 19.0.3_) then pip is installed and you are ready to install Pygame!

4. If pip is **not** installed, then in the **Terminal** enter the following:
```
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
sudo python get-pip.py
```
<sub> *Note that you will be required to enter a password. Enter "member" (also note that you won't see any text when you enter the password, so don't freak out). Hit enter when complete. </sub>

5. Once installed, once again enter: `python3 -m pip --version`. You should have a version number returned. If not, check your code syntax and make sure spelling is correct.

Once installed, move on to installing Pygame.

### For Windows:
1. Open the **Command Prompt** by pressing the **Windows** key and entering 'cmd'. 

2. Once the application opens, enter the following: `python -m pip --version`

3. If you get an error that states '...not a valid command', then pip is not installed. Otherwise, if you get a version number in return (as of March 2019: _pip 19.0.3_) then pip is installed and you are ready to install Pygame!

4. Install pip by going to the webpage: https://bootstrap.pypa.io/get-pip.py and hover over the text and right-click, then select 'Save As...'. Save the file as: _get-pip.py_ and save it in your documents.

5. Go to the where you saved the _get-pip.py_ file and then hold **Shift** and right-click on the file. Select the 'Copy as path' option. Now open the **Command Prompt** and enter the following: `python [COPY AND PASTE YOUR PATH HERE]`. For example, if you saved in your documents, you should have something like this: `python "C:\User\Member\Documents\get-pip.py"`.

6. Once installed, once again enter: `python -m pip --version`. You should have a version number returned. If not, check your code syntax and make sure spelling is correct.

Once installed, move on to installing Pygame.

## Installing Pygame:

Once pip is installed on your machine, you are ready to install Pygame through the pip package manager.

### For Mac:
1. Open the **Terminal** and enter the following: `python3 -m pip install -U pygame --user`. You should see a statement 'Collecting pygame' along with a progress bar. 

2. Once completed, enter the following to test that pygame was installed correctly: `python3 -m pygame.examples.aliens`

3. That's it! If the game runs correctly with sound, then Pygame has successfully been installed in your machine!

### For Windows:
1. Open the **Terminal** and enter the following: `py -m pip install -U pygame --user`. You should see a statement 'Collecting pygame' along with a progress bar. 

2. Once completed, enter the following to test that pygame was installed correctly: `py -m pygame.examples.aliens`

3. That's it! If the game runs correctly with sound, then Pygame has successfully been installed in your machine!




