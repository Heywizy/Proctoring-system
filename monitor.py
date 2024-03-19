import psutil
running_apps = []
for i in psutil.process_iter():
    running_apps.append(i.name())
    # print(running_apps)
if "chrome.exe" in running_apps:
        print("chrome is running, please close it before proceeding with the test")
elif "teamviewer.exe" in running_apps:
    print("teamviewer is running, please close it before proceeding with the test")
else:
    print("No suspicious app is running, you can proceed with the test")