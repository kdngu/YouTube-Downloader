# YouTube-Downloader
This script uses Python 3.7 and the pytube module to download a YouTube video at a selected resolution.

### Prequisites
Install Python 3 and the pytube module

Optional:
Install pipenv and use pipenv to import the requirements.txt
```
pipenv install -r path/to/requirements. txt
```

### Running the Script
1. Enter in the URL for your desired YouTube video
2. Enter in the 'itag' number of your desired video quality. (A list of available video qualities will be shown, each with a different identifying 'itag' number.)
3. Enter in the path to the desired download location for the video.

### Note
Currently, progressive streams can only support up to 720p resolution. If you want to download a video at a higher quality, you can download a dash stream and audio stream separately and then merge them.

### Debugging
1. If you receive the following error: 
```
raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1049)>
```
you may need to navigate to your your Python 3 folder and double click on "Install Certificates.command" file.

2. If you receive the following error:

```
except KeyError:
    cipher_url = [parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)]
 ```

open the extract.py file and search for
```
line: parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
```
now replace 'cipher' with 'signatureCipher'.
