# Changes in this fork
I needed a utility to download all my comic books from HumbleBundle.
The forked project would let me download all eBooks, but this would download the PDF, PDF (HQ) and CBZ versions of the books.
I just wanted to get the CBZ version.
So with this utility, you can only download eBooks (and comics), but you can choose the format.
Just set the desired file-formats to true in hb-downloader-settings.yaml.

# hb-downloader
An automated utility to download your Humble Bundle eBook - purchases with support for the Authy token.

    http://www.humblebundle.com

This package is not endorsed, supported, or affiliated with Humble Bundle, Inc.

## Requirements
* Python 3.6
* requests library
* pyyaml library

## Python Installation
Several features particular to Python v3.6 might have been used during the development of this script.  To install Python v3.6 visit https://www.python.org/downloads/ and grab the latest 3.x.x release.

## Getting the Prerequisites
From a command prompt, enter:

    pip install requests
    pip install pyyaml

You'll either be informed that the requirement is already satisfied, or pip will retrieve, install, and configure the libraries for you.

## Getting the Installation Files
* Download the zip file from the releases page and unzip it to the directory of your choice.
* Check out the source with Git:  git clone git://github.com/MayeulC/hb-downloader.git

## Installation
There are five pieces of critical information required by the script.  Four (username, password, download location, and cookie location) of these pieces of information are configured in the hb-downloader-settings.yaml file.  The fifth (Authy token) is entered once as needed for authentication during the login process.

hb-downloader-settings.yaml is the configuration file for the script.  It contains all of the information that can be overridden during script execution.  The format (for the data we're concerned with) is 
 
     <variable name>: <variable value>
     
Edit the hb-downloader-settings.yaml file.  Change the username to reflect your humblebundle.com username; this is generally your email address.

    username:  <username value>
    
Change the password to reflect your humblebundle.com password.

    password: <password value>

download-location is where you want the files to be stored during and after their download from humblebundle.com.  This location needs to exist and be writable by the user executing the script.  It can be a Linux style directory (/mnt/Mila/Games/Humble Bundle), a UNC share (\\megatron\mila\games\humble bundle) or a Windows drive reference (C:\Users\Username\Downloads).

    download-location:  \\megatron\mila\games\humble bundle
    
cookie-location is where you want your session cookies stored after successful authentication with Humble Bundle.  If you're being repeatedly asked to provide your Auhy token this file is probably not being successfully created.  It should be writable by the script execution user; the default path is the script directory.

    cookie-location: cookies.txt
    
Once hb-downloader-settings.yaml has been setup you'll need to execute hb-downloader.py at least once prior to any automation.  The script will detect that you need to login and prompt you for your Authy token.  Once you've successfully authenticated, the _session_auth cookie will be stored in the file specified by the cookie filename and you won't have to enter any credentials.  (And, if you're the paranoid sort, you can remove your credentials from the hb-downloader-settings.yaml file.)

Alternatively, you can directly enter the value of the _simple_auth cookie from your browser in the yaml configuration file, or pass it trough the command line.

The sessions are occasionally invalidated by humblebundle.com so keep an eye out if executions begin to fail.

## Issues
If you encounter any issues or have suggestions (including constructive criticism of my disastrous Python) please let me know at bmschkerke@gmail.com.

## Known Issues
If you run the script in a terminal window under Windows you may receive:

     UnicodeEncodeError: 'charmap' codec can't encode character...
     
This only happens if you have an extended character in the name of one of your products.  The easiest fix is to export an environment variable so that Python knows the terminal can accept Unicode:

    set PYTHONIOENCODING=UTF-8
