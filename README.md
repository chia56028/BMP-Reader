BMP Reader
===
## Features
- Read BMP file
- Get RGB values for each pixel
    - Create bar charts of RGB
- Calculate the mean and STD
    - Write CSV file

## Install Packages 
```bash
pip install numpy
pip install Pillow
pip install matplotlib
```
If you want to create `EXE file` after programming, also install this:
```bash
pip install pyinstaller
```

## Run the program
Just put the picture inside the `input` folder, then execute the code:
```bash
python BMP_reader.py
```
After that, your find the csv file and bar charts in the `output` folder.

### Example
#### Input:
<img src="https://i.imgur.com/JToN5Ot.jpg" width="280" height="490">

Download from: [❤ 动画精品](https://www.pinterest.com/anniemeiguoooo/%E5%8A%A8%E7%94%BB%E7%B2%BE%E5%93%81/)

#### Output:
<p float="left">
    <img src="https://i.imgur.com/ZlCqAJ2.png" width="290">
    <img src="https://i.imgur.com/ZzaOqj5.png" width="290">
    <img src="https://i.imgur.com/9tJyvpU.png" width="290">
</p>

## References
- [How to read the RGB value of a given pixel in Python?](https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python)
- [How to get name of list](https://bytes.com/topic/python/answers/854009-how-get-name-list)