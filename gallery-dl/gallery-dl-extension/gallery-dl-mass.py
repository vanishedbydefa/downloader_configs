import subprocess
import os

#virtual env activation command
#virtualenv_activation_command = 'call .venv\\Scripts\\activate.bat'
virtualenv_activation_command = '.venv\\Scripts\\activate'

profiles = []
with open('twitter_profiles.txt', "r") as f:
    profiles = [line.rstrip('\n') for line in f.readlines() if line.strip()]
    f.close()

while True:
    # Check if all profiles are downloaded
    if len(profiles) == 0:
        break
    
    # Get new profile to download
    profile = profiles[0]
    profilename = profile.split("/")[-1:][0]
    print(f"Downloading: {profilename}")

    download_command = f'gallery-dl -c gallery-dl-example.conf -d Q:/ {profile}'
    
    # Run activation and download commands in a single subprocess
    command = f'{virtualenv_activation_command} && {download_command}'
    
    os.system(command)
      
    
    print(f"Downloading {profilename} executed successfully")
    #write profile to downloaded profiles
    with open("twitter_profiles_done.txt", 'a+') as f:
        f.write(profile + '\n')
    
    #remove profile from to download profiles
    profiles = [line for line in profiles if line.strip() != profile.strip()]

    # Write the updated contents back to the file
    with open("twitter_profiles.txt", 'w') as f:
        for profile in profiles:
            f.write(profile + '\n')
