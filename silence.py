import subprocess
from pathlib import Path
wd = Path().absolute()
ffmpeg_path = wd / "ffmpeg" / "bin" / "ffmpeg.exe"


def silence(inpath):
    outpath = Path(inpath).stem + "-silent" + Path(inpath).suffix
    subprocess.check_call([ffmpeg_path, "-i", inpath, "-c", "copy", "-an", outpath],
                          stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    files = list(Path().glob("*.mp4"))
    num_files = len(files)
    print(str(num_files) + " files found. Silence all? (Y/n)")
    go = input("> ")
    if go.lower() == "y":
        ctr = 1
        for file in files:
            print("Silencing '%s'... (%i/%i)" % (file.name, ctr, num_files))
            silence(str(file))
        print("Done.")
        input()
