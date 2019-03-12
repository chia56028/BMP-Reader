from PIL import Image
import csv
import numpy as np
import matplotlib.pyplot as plt
import os
from os import listdir

def get_file_name():
    print("reading files...")
    path = "input/"
    files_name = listdir(path)
    return files_name

def read_file(filename):
    with Image.open("input/"+filename) as image:
   	 width, height = image.size
   	 
   	 pixel = list(image.getdata())
   	 rgb = list(zip(*pixel))

    return pixel,rgb[0],rgb[1],rgb[2]

def count_pixel(pixel):
    r = [0]*256
    g = [0]*256
    b = [0]*256
    for i in pixel:
   	 r[i[0]] += 1
   	 g[i[1]] += 1
   	 b[i[2]] += 1

    return r,g,b

def count_mean(x):
    return round(np.mean(x),2)

def count_STD(x):
    return round(np.std(x),2)

def write_csv(r,g,b,csv_name,mean,STD):
    title = ["Index","Red","Green","Blue"]
    t = range(0,256)
    x = zip(*[t,r,g,b])

    with open(csv_name, 'w', newline='') as myfile:
   	 wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
   	 wr.writerow(title)
   	 wr.writerows(x)
   	 wr.writerow(mean)
   	 wr.writerow(STD)

def get_bar_graph(x,filename,c_name):
    xs = range(len(x))
    width = 2/3

    plt.xlabel('index')
    plt.ylabel('count')
    plt.bar(xs, x, width, color=c_name)

    plt.savefig('output/'+filename+'_'+c_name+'.png')
    plt.close('all')

def generate_csv_and_barGraph(filename):
    print("------------------------")
    print("   	"+filename)
    print("------------------------")
    filename = filename.replace(".bmp","")
    pixel, r_list, g_list, b_list = read_file(filename+".bmp")
    r, g, b = count_pixel(pixel)

    print("creating csv...")
    mean = ["Maen"]
    STD = ["STD"]
    for i in [r_list,g_list,b_list]:
   	 mean.append(count_mean(i))
   	 STD.append(count_STD(i))

    write_csv(r,g,b,'output/'+filename+".csv",mean,STD)

    print("creating bar_graph...")

    for i in [r,g,b]:
   	 for key,value in list(locals().items()):
   		 if type(value)==list and key!='i' and value==i:
   			 get_bar_graph(i,filename,str(key))

filenames = get_file_name()
for i in filenames:
    generate_csv_and_barGraph(i)

os.system("pause")
