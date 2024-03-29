
# YouTube Chat Scanner/Chat Compute/Video Downloader/Clipper

I got a job as an Integration Engineer and want to keep my programming skills sharp. 

While I was clipping some VTuber as a hobby. I thought "Could I automate this?"

## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

## Features

- Scan an archived YouTube livestream chat to get frequency of comments
- Download YouTube videos
- Compute chat data
- Clip your video based off chat data

## Documentation

[Documentation](https://github.com/ArisaBonsaiTree/YouTubeChatScannerJulyProject/blob/main/Documentation.md)

## Requirements

To run this project, you will need:

`FFMPEG` You will need to edit environment variables and edit Path under System variables to point to FFMPEG

C:\Users\<User>\AppData\Local\Programs\Python\Python39\Scripts

`Install modules from the requirements.txt` pip install -r requirements.txt



## Run Locally

Clone the project

```bash
  git clone https://github.com/ArisaBonsaiTree/YouTubeChatScannerJulyProject.git
```

Go to the project directory

```bash
  cd YouTubeChatScannerJulyProject
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the program

```bash
  python MainProgram.py 
```


## FAQ

#### FFMPEG Errors?

Make sure to download [FFMPEG](https://ffmpeg.org/) and add it to your environment variables

#### Module issues?

pip install -r requirements.txt

#### How to pin the Python file to my taskbar 

https://www.tenforums.com/tutorials/96525-pin-file-taskbar-windows-10-a.html

#### "Python" is not a recognized command

Do you have [Python](https://www.python.org/downloads/) installed?

#### Can't run "yt-dlp" or having errors with "ytDownload.sh"?

You will need to download [yt-dlp](https://github.com/yt-dlp/yt-dlp) and place in your C:\Users\[Name]\AppData\Local\Programs\Python\Python311\Scripts folder or in the same
folder where you have FFMPEG.exe.


#### What Operating Systems does this program run in?

Developed this using PyCharm on Windows 10

#### Does PyInstaller Work?

I used PyInstaller. File > Tools > External Tools

![image](https://user-images.githubusercontent.com/64375555/179183895-de1b1d5e-0bae-45c6-a86f-40e8687bdcca.png)

#### PyCharm giving you pytchat doesn't exist?
Go to File > Settings > Project: YouTubeCh... > Python Interpreter > Add Interpreter > (Not sure what I did 100%, but I used Python 3.10) 
I used Python 3.10, which was located at C:.../AppData/Local/Programs/Python/Python310/python.exe
You can check what version of Python you have installed by opening command prompt and typing "python" to see what version you have

## License

[GNU GPLv3 ](https://choosealicense.com/licenses/gpl-3.0/)

> GitHub [@ArisaBonsaiTree](https://github.com/ArisaBonsaiTree)
