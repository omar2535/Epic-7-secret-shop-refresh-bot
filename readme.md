# Epic seven shop auto-refresher

This auto-refresher for epic seven saves you the time of shop-refreshing by doing it automagically for you.

## Getting started

There are a few steps involved with getting this set up. This guide is for windows 10 only.

### Step 1: Installing ADB

Install ADB onto your device by clicking this: [link](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)

Now unzip and move to a folder of your choosing. Remember that folder! We will need it later.

### Step 2: Adding ADB to path

- go to Control Panel > System and Security > System and click on `Advanced system settings`
- click on `environment variables` on the bottom right
- in `System variables`, edit the Path variable by double clicking on the `Path`
- click on `new` and paste the path of the `adb.exe` file that was extracted in step 1

    Something similar to this:

    ![adb_path](./documentation/adb_path.PNG)
- Now click OK to get rid of all the windows

### Step 3: Enabling ADB on bluestacks

- Go to settings on the bluestack instance
- Go to preferences
- Scroll down and make sure `Enable Android Debug Bridge (ADB)` is enabled

    Something like this:

    ![bluestacks_adb](./documentation/bluestacks_adb.PNG)

### Step 4: Installing Tesseract

Install either the 32 bit or 64 bit tesseract installer from [here](https://github.com/UB-Mannheim/tesseract/wiki)

### Step 5: Install python

Make sure python is installed on your machine. Link is [here](https://www.python.org/downloads/windows/)

### Step 6: Install python dependencies

Open a command prompt and navigate to where this project was downloaded to. Run

```sh
pip install -r requirements.txt
```

### Step 7: Set up config.yml

Open config.yml and make sure everything in there looks correct.

### Step 8: Run the script

In a command prompt, run 

```sh
python main.py
```

## Improvements / Suggestions

Message me for improvements.
