# Mashov Covid-19 Automated Filler (+ Discord Webhook Integration)
A Python Application written with Python using PyImgur and some other libs
![image](https://user-images.githubusercontent.com/30008308/113910844-f479f080-97e1-11eb-8dc0-0e3600f6d4bf.png)
## Install
Use [PIP](https://pip.pypa.io/en/stable/) to install the following packages that are needed to run this app properly:
1. pyimgur
2. pyperclip
* If I forget something just download the package that is causing the error.
## Usage
in ./config/cfg.json find this code:
```
{
    "client_id": "?"
}

```
Replace the following:
* client_id: with your imgur API client ID(Google how to get)
## Explanation of process:
1. loads cfg.json
2. prints introduction and instructions
3. asks for the image to be dragged and dropped into the terminal(This will cause the image path!)
4. uploads the image to imgur
5. copies the uploaded image's link to the user's clipboard and prints the image link to the terminal
## Legal
DISCLAIMER: This is not affliated, endorsed or certified by Imgur. This is an independent and unofficial project that is strictly for educational purposes only and not intended to cause any harm. I am not responsible for anyone who decided to download my app and use it against my will and Imgur's will. Use at your OWN risk ONLY.
