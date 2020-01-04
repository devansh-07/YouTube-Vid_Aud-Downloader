#!/usr/bin/python3

"""
Written by DEVANSH SONI
I've mainly used Pytube and Tkinter to develop this application.
For any suggestions:
    Please contact: dsoni01@outlook.com
"""

import tkinter as tk
import tkinter.ttk as ttk
import urllib
import urllib.request
import urllib.error
from io import BytesIO
from pytube import YouTube
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry("450x190")
root.resizable(0, 0)
root.title("YT Downloader")

try:
    root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='ic.ico'))
except:
    pass

root.configure(bg="#141414")

tk.Label(root, text="- Dsoni01", pady=5, padx=5, fg="#414141", bg="#141414").place(relx=1.0, rely=1.0, x=0, y=0, anchor="se")

frs = tk.Frame(root, padx=10, pady=10, bg="#141414")
frs.pack()

fms = tk.Frame(root, bg="#141414", padx=0, pady=0).pack(side="left")

global yt, ad, stream


def an_err():
    root.geometry("450x190")
    tk.Label(fms, text="An Error occurred.", padx=18, pady=3, fg="#990f02", bg="#210000").place(rely=1.0, x=0, anchor="sw")


def get_things():
    global yt, ad, stream
    ad = str(link.get())
    try:
        yt = YouTube(ad)
        stream = yt.streams
        return True
    except:
        return False


def dwnl_vid():
    vid_str = stream.filter(progressive=True)
    try:
        vid_str.first().download()
        tk.Label(fms, text="Video Downloaded.", padx=15, pady=3, fg="green", bg="#001414").place(rely=1.0, anchor="sw")
    except:
        an_err()


def dwnl_aud():
    aud_str = stream.filter(only_audio=True)
    try:
        aud_str.first().download()
        tk.Label(fms, text="Audio Downloaded.", padx=15, pady=3, fg="green", bg="#001414").place(rely=1.0, anchor="sw")
    except:
        an_err()


def show_info():
    global frs, fms

    if frs:
        frs.destroy()
        frs = tk.Frame(root, padx=10, pady=10, bg="#141414")
        frs.pack(pady=(40, 5))
    else:
        pass

    if link.get():
        pass
    else:
        root.geometry("450x190")
        tk.Label(fms, text="Please Enter a URL.", padx=15, pady=3, fg="#990f02", bg="#210000").place(rely=1.0, anchor="sw")
        return

    try:
        urllib.request.urlopen("https://www.google.com", timeout=10)
    except urllib.error.URLError:
        root.geometry("450x190")
        tk.Label(fms, text="No Network Connection.", padx=0, pady=3, fg="#990f02", bg="#210000").place(rely=1.0, anchor="sw")
        return

    ch = get_things()
    if not ch:
        an_err()
        return

    root.geometry("450x410")

    ttk.Separator(root).place(x=0, y=190, relwidth=1)

    image_file = f'https://img.youtube.com/vi/{yt.video_id}/default.jpg'

    with urllib.request.urlopen(image_file) as u:
        raw_data = u.read()
    im = Image.open(BytesIO(raw_data))

    img = ImageTk.PhotoImage(im)
    p = tk.Label(frs, image=img, pady=20, padx=10)
    p.image = img
    p.pack(side="left")

    title = yt.title
    views = yt.views
    rt = "%.2f" % yt.rating

    tk.Label(frs, text=f"Title :  {title[:33]}\n{title[33:70]}\n{title[70:95]}", padx=15, pady=3, bg="#141414", underline=0).pack(side='top')

    tk.Label(frs, text=f"Views :  {views}", padx=15, pady=3, bg="#141414", underline=0).pack(side='top')

    tk.Label(frs, text=f"Rating :  {rt}", padx=15, pady=3, bg="#141414", underline=0).pack(side='top')

    tk.Label(frs, text=f"Download :", pady=3, bg="#141414", underline=0).pack(side="left", padx=(15, 0))

    tk.Button(frs, text='Video', bg="#001010", fg="#347c2c", padx=20, pady=3, font=10, borderwidth=2, command=dwnl_vid).pack(side='left', padx=10, pady=8)

    tk.Button(frs, text='Audio', bg="#001010", fg="#1338be", padx=20, pady=3, font=10, borderwidth=2, command=dwnl_aud).pack(side='right', padx=10, pady=8)


fr1 = tk.Frame(root, padx=10, pady=25, bg="#141414")
fr1.pack()
tk.Label(fr1, text="Enter URL   :", pady=15, padx=10, font=20, bg="#141414").pack(side="left")

link = tk.StringVar()

en = tk.Entry(fr1, font=10, width=32, textvariable=link, bg="#212121").pack(side="right", padx=10)

fr2 = tk.Frame(root, pady=0, padx=0, bg="#141414")
fr2.pack(pady=5)

tk.Button(fr2, text='Details', bg="#001010", padx=15, pady=3, font=10, borderwidth=2, command=show_info).pack(padx=10)

root.mainloop()


if __name__ != '__main__':
    pass
