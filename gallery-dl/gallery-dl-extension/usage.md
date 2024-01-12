# How to use (Windows only)
### Virtual enviroment
This extension will only work if you created a virtual enviroment for gallery-dl.
You can create it in the main gallery-dl folder
1. `Q:\programs\gallery-dl$ python -m venv .venv`
2. `Q:\programs\gallery-dl$ .venv\Scripts\activate.bat`
3. `Q:\programs\gallery-dl$ pip install -r requirements.txt`

### gallery-dl-mass.py usage
1. Download gallery-dl-mass.py and place it in the gallery-dl main folder
2. Create a file profiles.txt in which you store links to the profile of which you want to download media
  * You can place reddit and or twitter links in profiles.txt
3. Open CMD and change directory to the gallery-dl main folder. (e.x `cd /d Q:\programs\gallery-dl`)
4. Start the program with `python gallery-dl-mass.py`
5. After a profile was downloaded, its link gets removed from profiles.txt and placed in a new file calles profiles_done.txt
  * This is done to really get all media insted of every time only checking the first profiles for new media in case profiles.txt is big.
  * When profiles.txt is empty, profiles-done.txt has all the urls, previously stored in profiles.txt.
  * To now check all profiles for new media, swap the filenames.
