#import statements
import pandas as pd

#bokeh functions will be used to plot the data
from bokeh.plotting import *
import numpy as np
from bokeh.layouts import row
from bokeh.models import LinearAxis, Range1d, LabelSet, Label
import scipy.stats
import math

#csv data files are opened and data is transferred into variables
df = pd.read_csv('pinewood_os_d3s.csv')
df2 = pd.read_csv('pinewood_os_weather.csv')
cols = [0,1,2,3,4]
df1 = df.drop(df.columns[cols],axis = 1) #drops column names and keeps numerical value
def find_nearest(array, value):

    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

#Function is used to chunk the dataframes
#Each chunk contains 2000 data frames or approx 10000 minutes
def chunk(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

#Radiation data is chunked into appropriate divisions
time = []
dft = df[['deviceTime_unix']].copy()
for dft_chunk in chunk(dft,2000):
    time.append(dft_chunk.iloc[0]['deviceTime_unix'])

# For Pinewood, it is less important to sync times up because the sensors were installed at the same time, but
# nevertheless, it still remains a good idea to keep the time sync around just in case things don't match up

# data for the three y-axis variables are chunked and reorganized by time
temp = []
temp2 = []
temp3 = []
df3 = df2[['deviceTime_unix','humidity']].copy()
df4 = df2[['deviceTime_unix','temperature']].copy()
df5 = df2[['deviceTime_unix','pressure']].copy()

temptime = df3.as_matrix(columns=df3.columns[0:1]).ravel()
indx = find_nearest(temptime,time[0])
df3 = df3.drop(df3.index[0:indx])

temptime2 = df4.as_matrix(columns=df4.columns[0:1]).ravel()
indx = find_nearest(temptime2,time[0])
df4 = df4.drop(df4.index[0:indx])

temptime3 = df5.as_matrix(columns=df5.columns[0:1]).ravel()
indx = find_nearest(temptime3,time[0])
df5 = df5.drop(df5.index[0:indx])

for dftemp_chunk in chunk(df3,2000):
    temp.append(dftemp_chunk["humidity"].mean())

for dftemp_chunk in chunk(df4,2000):
    temp2.append(dftemp_chunk["temperature"].mean())

for dftemp_chunk in chunk(df5,2000):
    temp3.append(dftemp_chunk["pressure"].mean())


i = 0
channels = []
while i <=1023:
    channels.append(i) # Create the array of channel labels
    i= i+1

m = 200
bins = []
while m<=2800:
    bins.append(m) # Create array of bin edges
    m =m+5

total = [] # Bismuth Counts
totalk = [] # Potassium Counts
totalth = [] # Thallium Counts
totalt = [] # Overall Counts

# the chunked radiation data is used to find the peaks of Bismuth, Potassium, and Thorium decay
for df_chunk in chunk(df1, 2000):

    buckets = [0] * 1500

    arr = df_chunk.as_matrix(columns=df_chunk.columns[1:])
    conv = df_chunk.as_matrix(columns=df_chunk.columns[0:1]).ravel()

    k = 0

    while k < len(conv):

        kev = [i * conv[k] for i in channels]

        indexes = np.digitize(kev, bins).flatten()

        i = 0
        while i < len(indexes):
            buckets[indexes[i] - 1] = buckets[indexes[i] - 1] + arr[k][i]
            i = i + 1

        k = k + 1

    # -----------------------------------------------------------------------------------------------------------------------
    # In order to remove the background counts in the peaks, we create a line from the endpoints of the window, integrate under that line,
    # and subtract that value from the integral under the peak

    bismuthA = buckets[80:100]

    sumBA = (np.trapz(bismuthA, bins[80:100]))

    x1 = bins[80]
    x2 = bins[100]
    y1 = bismuthA[0]
    y2 = bismuthA[len(bismuthA) - 1]

    m = (math.log(y2) - math.log(y1)) / (x2 - x1)
    c = math.log(y1) - (m * x1)
    A = math.exp(c)

    xarino = np.arange(x1, x2)

    y = (A * np.exp((m * xarino)))

    bismuthbackground = (np.trapz(y, x=xarino))

    # -----------------------------------------------------------------------------------------------------------------------

    potassiumA = buckets[230:270]
    sumKA = (np.trapz(potassiumA, bins[230:270]))

    x1 = bins[230]
    x2 = bins[270]
    y1 = potassiumA[0]
    y2 = potassiumA[len(potassiumA) - 1]

    m = ((math.log(y2) - math.log(y1)) / (x2 - x1))
    c = math.log(y1) - (m * x1)
    A = math.exp(c)

    xarino = np.arange(x1, x2)

    y = (A * np.exp((m * xarino)))

    potassiumbackground = (np.trapz(y, x=xarino))

    # -----------------------------------------------------------------------------------------------------------------------

    thoriumA = buckets[423:450]
    sumTA = (np.trapz(thoriumA, bins[423:450]))

    x1 = bins[423]
    x2 = bins[450]
    y1 = thoriumA[0]
    y2 = thoriumA[len(thoriumA) - 1]

    m = ((math.log(y2)-math.log(y1))/(x2-x1))
    c = math.log(y1) - (m*x1)
    A = math.exp(c)

    xarino = np.arange(x1,x2)

    y = (A*np.exp((m*xarino)))

    thoriumbackground = (np.trapz(y,x=xarino))

    # -----------------------------------------------------------------------------------------------------------------------

    totalt.append(sum(buckets))
    total.append(sumBA-bismuthbackground)
    totalk.append(sumKA-potassiumbackground)
    totalth.append(sumTA-thoriumbackground)

# -----------------------------------------------------------------------------------------------------------------------


print (str(scipy.stats.pearsonr(total[0:len(temp)],temp)) + " This is bismuth")
print (str(scipy.stats.pearsonr(totalk[0:len(temp)],temp)) + " This is potassium")
print (str(scipy.stats.pearsonr(totalth[0:len(temp)],temp)) + " This is thallium")
print (str(scipy.stats.pearsonr(total[0:len(temp2)],temp2)) + " This is bismuth")
print (str(scipy.stats.pearsonr(totalk[0:len(temp2)],temp2)) + " This is potassium")
print (str(scipy.stats.pearsonr(totalth[0:len(temp2)],temp2)) + " This is thallium")
print (str(scipy.stats.pearsonr(total[0:len(temp3)],temp3)) + " This is bismuth")
print (str(scipy.stats.pearsonr(totalk[0:len(temp3)],temp3)) + " This is potassium")
print (str(scipy.stats.pearsonr(totalth[0:len(temp3)],temp3)) + " This is thallium")
# -----------------------------------------------------------------------------------------------------------------------

#Figures for Humidity correlation are created
p = figure(title='Bismuth Radiation vs Humidity')
p.circle(total[0:len(temp)],temp)
citation1 = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text=str(scipy.stats.pearsonr(total[0:len(temp)],temp)),
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
p.add_layout(citation1)
p.xaxis.axis_label = 'Radiation'

p.yaxis.axis_label = 'Humidity'
p2 = figure(title='Potassium Radiation vs Humidity')
p2.circle(totalk[0:len(temp)],temp)

citation2 = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text=str(scipy.stats.pearsonr(totalk[0:len(temp)],temp)),
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
p2.add_layout(citation2)
p2.xaxis.axis_label = 'Radiation'
p2.yaxis.axis_label = 'Humidity'

p3 = figure(title='Thorium Radiation vs Humidity')
p3.circle(totalth[0:len(temp)],temp)
citation3 = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text=str(scipy.stats.pearsonr(totalth[0:len(temp)],temp)), render_mode='css',
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
p3.add_layout(citation3)
p3.xaxis.axis_label = 'Radiation'
p3.yaxis.axis_label = 'Humidity'


#Figures for Pressure correlation are created
p4 = figure(title='Bismuth Radiation vs Pressure')
p4.circle(total[0:len(temp2)],temp2)
citation4 = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text=str(scipy.stats.pearsonr(total[0:len(temp2)],temp2)),
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
p4.add_layout(citation4)
p4.xaxis.axis_label = 'Radiation'
p4.yaxis.axis_label = 'Pressure'

p5 = figure(title='Potassium Radiation vs Pressure')
p5.circle(totalk[0:len(temp2)],temp2)

citation5 = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text=str(scipy.stats.pearsonr(totalk[0:len(temp2)],temp2)),
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
p5.add_layout(citation5)
p5.xaxis.axis_label = 'Radiation'
p5.yaxis.axis_label = 'Pressure'

p6 = figure(title='Thorium Radiation vs Pressure')
p6.circle(totalth[0:len(temp2)],temp2)

citation6 = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text=str(scipy.stats.pearsonr(totalth[0:len(temp2)],temp2)), render_mode='css',
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
p6.add_layout(citation6)
p6.xaxis.axis_label = 'Radiation'
p6.yaxis.axis_label = 'Pressure'


#Figures for Temperature correlation are created
p7 = figure(title='Bismuth Radiation vs Temperature')
p7.circle(total[0:len(temp2)],temp2)
citation7 = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text=str(scipy.stats.pearsonr(total[0:len(temp3)],temp3)),
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
p7.add_layout(citation7)
p7.xaxis.axis_label = 'Radiation'
p7.yaxis.axis_label = 'Temperature'

p8 = figure(title='Potassium Radiation vs Temperature')
p8.circle(totalk[0:len(temp2)],temp2)

citation8 = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text=str(scipy.stats.pearsonr(totalk[0:len(temp3)],temp3)),
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
p8.add_layout(citation8)
p8.xaxis.axis_label = 'Radiation'
p8.yaxis.axis_label = 'Temperature'

p9 = figure(title='Thorium Radiation vs Temperature')
p9.circle(totalth[0:len(temp2)],temp2)

citation9 = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text=str(scipy.stats.pearsonr(totalth[0:len(temp3)],temp3)), render_mode='css',
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)
p9.add_layout(citation9)
p9.xaxis.axis_label = 'Radiation'
p9.yaxis.axis_label = 'Temperature'

#Figures are initiated and displayed
show(row(p,p2,p3,p4,p5,p6,p7,p8,p9))




# -----------------------------------------------------------------------------------------------------------------------
p = figure()

p.circle(time,total,color = 'firebrick')

p.extra_y_ranges = {"foo": Range1d(start=0, end=35)}
p.add_layout(LinearAxis(y_range_name="foo"), 'right')

p.circle(time,temp, y_range_name='foo', color='blue')
p.yaxis.axis_label = 'Pressure'
# -----------------------------------------------------------------------------------------------------------------------

p3 = figure()
p3.circle(time,totalth,color = 'green')

p3.extra_y_ranges = {"foo": Range1d(start=0, end=35)}
p3.add_layout(LinearAxis(y_range_name="foo"), 'right')

p3.circle(time,temp, y_range_name='foo', color='blue')
p3.yaxis.axis_label = 'Pressure'
# -----------------------------------------------------------------------------------------------------------------------

p2 = figure()
p2.circle(time,totalk,color = 'orange')

p2.extra_y_ranges = {"foo": Range1d(start=0, end=35)}
p2.add_layout(LinearAxis(y_range_name="foo"), 'right')

p2.circle(time,temp, y_range_name='foo', color='blue')
#line 65535
p2.yaxis.axis_label = 'Pressure'



# -----------------------------------------------------------------------------------------------------------------------
p4 = figure()

p4.circle(time,total,color = 'firebrick')

p4.extra_y_ranges = {"foo": Range1d(start=0, end=35)}
p4.add_layout(LinearAxis(y_range_name="foo"), 'right')

p4.circle(time,temp2, y_range_name='foo', color='blue')
p4.yaxis.axis_label = 'Pressure'
# -----------------------------------------------------------------------------------------------------------------------

p6 = figure()
p6.circle(time,totalth,color = 'green')

p6.extra_y_ranges = {"foo": Range1d(start=0, end=35)}
p6.add_layout(LinearAxis(y_range_name="foo"), 'right')

p6.circle(time,temp2, y_range_name='foo', color='blue')
p6.yaxis.axis_label = 'Pressure'
# -----------------------------------------------------------------------------------------------------------------------

p5 = figure()
p5.circle(time,totalk,color = 'orange')

p5.extra_y_ranges = {"foo": Range1d(start=0, end=35)}
p5.add_layout(LinearAxis(y_range_name="foo"), 'right')

p5.circle(time,temp2, y_range_name='foo', color='blue')
#line 65535
p5.yaxis.axis_label = 'Pressure'


# -----------------------------------------------------------------------------------------------------------------------
p7 = figure()

p7.circle(time,total,color = 'firebrick')

p7.extra_y_ranges = {"foo": Range1d(start=0, end=35)}
p7.add_layout(LinearAxis(y_range_name="foo"), 'right')

p7.circle(time,temp3, y_range_name='foo', color='blue')
p7.yaxis.axis_label = 'Pressure'
# -----------------------------------------------------------------------------------------------------------------------

p9 = figure()
p9.circle(time,totalth,color = 'green')

p9.extra_y_ranges = {"foo": Range1d(start=0, end=35)}
p9.add_layout(LinearAxis(y_range_name="foo"), 'right')

p9.circle(time,temp3, y_range_name='foo', color='blue')
p9.yaxis.axis_label = 'Pressure'
# -----------------------------------------------------------------------------------------------------------------------

p8 = figure()
p8.circle(time,totalk,color = 'orange')

p8.extra_y_ranges = {"foo": Range1d(start=0, end=35)}
p8.add_layout(LinearAxis(y_range_name="foo"), 'right')

p8.circle(time,temp3, y_range_name='foo', color='blue')
p8.yaxis.axis_label = 'Pressure'
