#!/usr/bin/python3

"""
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
from threading import Thread

root = tk.Tk()
root.geometry("450x190+700+300")
root.resizable(0, 0)
root.title("YT Downloader")

# try:
#     root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='ic.ico'))
# except FileNotFoundError:
#     pass

root.configure(bg="#141414")

tk.Label(root, text="- Dsoni01", pady=5, padx=5, fg="#414141", bg="#141414").place(relx=1.0, rely=1.0, x=0, y=0, anchor="se")

frs = tk.Frame(root, padx=10, pady=10, bg="#141414")
frs.pack()

fms = tk.Frame(root, bg="#141414", padx=0, pady=0).pack(side="left")

global yt, ad, stream


def an_err():
    root.geometry("450x190")
    er_lbl = tk.Label(fms, text="An Error occurred.", padx=18, pady=3, fg="#990f02", bg="#210000")
    er_lbl.place(rely=1.0, x=0, anchor="sw")
    er_lbl.after(5000, er_lbl.destroy)


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
        vid_lbl = tk.Label(fms, text="Video Downloaded.", padx=15, pady=3, fg="green", bg="#001414")
        vid_lbl.place(rely=1.0, anchor="sw")
        vid_lbl.after(5000, vid_lbl.destroy)
    except:
        an_err()


def dwnl_aud():
    aud_str = stream.filter(only_audio=True)
    try:
        aud_str.first().download()
        aud_lbl = tk.Label(fms, text="Audio Downloaded.", padx=15, pady=3, fg="green", bg="#001414")
        aud_lbl.place(rely=1.0, anchor="sw")
        aud_lbl.after(5000, aud_lbl.destroy)
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
        url_lbl = tk.Label(fms, text="Please Enter a URL.", padx=15, pady=3, fg="#990f02", bg="#210000")
        url_lbl.place(rely=1.0, anchor="sw")
        url_lbl.after(5000, url_lbl.destroy)
        return

    try:
        urllib.request.urlopen("https://www.google.com", timeout=10)
    except urllib.error.URLError:
        root.geometry("450x190")
        no_net_lbl = tk.Label(fms, text="No Network Connection.", padx=0, pady=3, fg="#990f02", bg="#210000")
        no_net_lbl.place(rely=1.0, anchor="sw")
        no_net_lbl.after(5000, no_net_lbl.destroy)
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

    tk.Label(frs, text=f"Title :  {title[:33]}\n{title[33:70]}\n{title[70:95]}", padx=15, pady=3, fg="#ffffff", bg="#141414", underline=0).pack(side='top')

    tk.Label(frs, text=f"Views :  {views}", padx=15, pady=3, fg="#ffffff", bg="#141414", underline=0).pack(side='top')

    tk.Label(frs, text=f"Rating :  {rt}", padx=15, pady=3, fg="#ffffff", bg="#141414", underline=0).pack(side='top')

    tk.Label(frs, text=f"Download :", pady=3, fg="#ffffff", bg="#141414", underline=0).pack(side="left", padx=(15, 0))

    tk.Button(frs, text='Video', bg="#001010", fg="#347c2c", padx=20, pady=3, font=10, borderwidth=2, command=dwnl_vid).pack(side='left', padx=10, pady=8)

    tk.Button(frs, text='Audio', bg="#001010", fg="#1338be", padx=20, pady=3, font=10, borderwidth=2, command=dwnl_aud).pack(side='right', padx=10, pady=8)


fr1 = tk.Frame(root, padx=10, pady=25, bg="#141414")
fr1.pack()
tk.Label(fr1, text="Enter URL   :", pady=15, padx=10, font=20, fg="#ffffff", bg="#141414").pack(side="left")

link = tk.StringVar()

en = tk.Entry(fr1, font=10, width=32, textvariable=link, fg="#ffffff", bg="#212121").pack(side="right", padx=10)

fr2 = tk.Frame(root, pady=0, padx=0, bg="#141414")
fr2.pack(pady=5)

tk.Button(fr2, text='Details', fg="#ffffff", bg="#001010", padx=15, pady=3, font=10, borderwidth=2, command=show_info).pack(padx=10)

root.mainloop()


if __name__ != '__main__':
    pass
