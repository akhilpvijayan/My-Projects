#An Insta Profile Pic Downloader

import instaloader

n = instaloader.Instaloader()
pic = input("Enter Instagram Username : ")

n.download_profile(pic , profile_pic_only=True)
