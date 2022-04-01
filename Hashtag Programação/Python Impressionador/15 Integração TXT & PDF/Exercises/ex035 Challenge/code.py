"""
Sales Funnel
Find where that client found the company:
    if "nan" or without org= Ads

    else:
        * hashtag_site_org → Site hashtag
        * hashtag_yt_org
        * hashtag_ig_org → Instagram
        * hashtag_fb_org → Facebook
"""

# with open("students", "r") as students:
#     students.read()

file = open("students", "r")

ads = org = igfb = youtube = site = 0

lines = file.readlines()
del lines[:4]

for line in lines:
    # Unpacking
    email, origin = line.split(",")
    data = zip(email, origin)
    if "_org" in origin:
        org += 1
        if "hashtag_yt_org" in origin:
            youtube += 1
        if "hashtag_site_org" in origin:
            site += 1
        if "hashtag_ig_org" in origin or "hashtag_igfb_org" in origin:
            igfb += 1
    else:
        ads += 1


print(ads)
print(org)
print(igfb)
print(youtube)
print(site)

with open("result", "w") as result:
    result.write(f"{ads}\n{org}\n{igfb}\n{youtube}\n{site}")



file.close()