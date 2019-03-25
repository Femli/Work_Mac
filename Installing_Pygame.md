# How to install Pygame for Python 3 on Mac OS X

1. Install **Xcode**: In Finder, open Applications, App Store. Search for Xcode and click Get to install the Xcode developer tools. You’ll need these developer tools to run some of the command-line instructions in a Terminal window below.

2. Install **XQuartz**: Go to http://xquartz.macosforge.org and download the current version of XQuartz (2.7.7 as of this writing). Open your Downloads folder, double-click on the XQuartz-2.7.7.dmg file, then double-click on the XQuartz.pkg package file and follow the instructions to complete the installation.

3. Open a **Terminal** (command-line) window: Go to Applications, Utilities, and double-click Terminal. Your command-line Terminal window will open. All the following commands must be typed exactly as they appear in the Terminal window, one line at a time.

4. Install **Homebrew**: At the Terminal command line prompt, type the following as a single full line (you may want to expand your Terminal window wider to allow it to fit, but it’s okay if it wraps around):
```
ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”
```
then, hit return. Homebrew is a free program that helps you install Python, Pygame, and other programs on a Mac.

5. Prepare Homebrew for use: At the Terminal prompt, type each of the following three commands exactly as shown – the second two may take a few moments to run and will show several screens of information, but keep following the steps one line at a time.
```
echo export PATH=’/usr/local/bin:$PATH’ >> ~/.bash_profile
brew update
brew doctor
```
6. Install Python 3 for Pygame: At the Terminal prompt, type:
```
brew install python3
```
This will install a separate Python 3 specifically for Pygame use – this is required for all the following steps to work.

7. Install Mercurial: Still at the Terminal prompt, type:
```
brew install mercurial
```
<sub>*Mercurial is a free source control management system that this installation of Pygame requires on a Mac.</sub>

8. Install Pygame dependencies: Pygame requires several other helper programs, called dependencies, so that it can show animations, play sounds, and create game graphics. Type the following three lines at the Terminal command prompt, hitting return after each line
```
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
brew tap homebrew/headonly
brew install smpeg
```
<sub>*(NOTE 18JUL2015: Updated to reflect changes to the smpeg library; if you have any trouble here, try brew install –HEAD smpeg instead, with two dashes/hyphens before the HEAD option).</sub>

Each command will take a few moments to run and display screens full of information; keep going, you’re almost done…

9. Install Pygame: Type the following line at the Terminal prompt and hit return:
```
sudo pip3 install hg+http://bitbucket.org/pygame/pygame
```
You may have to enter an administrator password (your password, or ask an IT administrator for help at school, work, or the library), and the installation may take a few minutes.

As mentioned in step 6 above, this process creates a second full Python environment (under /usr/local/Cellar) on your Mac. You’ll want easy access to your Pygame-enabled Python…

## Create a desktop shortcut to your new Pygame IDLE editor:

The new Pygame and Python 3 that you just installed creates a separate IDLE editor app that you’ll use especially for Pygame-enabled apps. (Note: You can use this new IDLE for all your Python development, if you wish.)

1. Go to Finder > Go > Go to Folder…

2. In the Go to the folder: window prompt, type __/usr/local/Cellar/python3__ and click Go.

3. Double-click to open the folder inside – it will be named with a version number (3.4.2_1 as of this writing), but the version is unimportant, just open the folder.

4. Inside this folder, you will find the IDLE 3 app. Hold down the control key and click on the IDLE 3 icon. Pressing control+clicking on the icon will open a popup menu; select the Make Alias option from that menu.

5. A new alias, or shortcut icon, will appear, with a name like IDLE 3 alias. Click on the file name to edit it, and rename the alias pygame IDLE or something similar, to help you remember that this IDLE has Pygame installed.

6. Drag the pygame IDLE icon to your Desktop. This will allow you to access the correct IDLE for Pygame programming right from your Desktop.

7. Double-click the pygame IDLE icon. The Pygame-enabled IDLE editor window will open. Type import pygame and hit return. IDLE should respond with a >>> prompt and no errors.

You’re ready to program Pygame apps on your Mac!
