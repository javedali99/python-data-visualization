
# Group boxplots

# 1. Using colors to differentiate between "apples" and "oranges" and spacing to separate "A", "B" and "C".

from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes

# function for setting the colors of the box plots pairs
def setBoxColors(bp):
    setp(bp['boxes'][0], color='blue')
    setp(bp['caps'][0], color='blue')
    setp(bp['caps'][1], color='blue')
    setp(bp['whiskers'][0], color='blue')
    setp(bp['whiskers'][1], color='blue')
    setp(bp['fliers'][0], color='blue')
    setp(bp['fliers'][1], color='blue')
    setp(bp['medians'][0], color='blue')

    setp(bp['boxes'][1], color='red')
    setp(bp['caps'][2], color='red')
    setp(bp['caps'][3], color='red')
    setp(bp['whiskers'][2], color='red')
    setp(bp['whiskers'][3], color='red')
    setp(bp['fliers'][2], color='red')
    setp(bp['fliers'][3], color='red')
    setp(bp['medians'][1], color='red')

# Some fake data to plot
A= [[1, 2, 5,],  [7, 2]]
B = [[5, 7, 2, 2, 5], [7, 2, 5]]
C = [[3,2,5,7], [6, 7, 3]]

fig = figure()
ax = axes()
hold(True)

# first boxplot pair
bp = boxplot(A, positions = [1, 2], widths = 0.6)
setBoxColors(bp)

# second boxplot pair
bp = boxplot(B, positions = [4, 5], widths = 0.6)
setBoxColors(bp)

# thrid boxplot pair
bp = boxplot(C, positions = [7, 8], widths = 0.6)
setBoxColors(bp)

# set axes limits and labels
xlim(0,9)
ylim(0,9)
ax.set_xticklabels(['A', 'B', 'C'])
ax.set_xticks([1.5, 4.5, 7.5])

# draw temporary red and blue lines and use them to create a legend
hB, = plot([1,1],'b-')
hR, = plot([1,1],'r-')
legend((hB, hR),('Apples', 'Oranges'))
hB.set_visible(False)
hR.set_visible(False)

savefig('boxcompare.png')
show()

# ==========================================================================================

# 2. Another version. It stores data based on categories.

import matplotlib.pyplot as plt
import numpy as np

data_a = [[1,2,5], [5,7,2,2,5], [7,2,5]]
data_b = [[6,4,2], [1,2,5,3,2], [2,3,5,1]]

ticks = ['A', 'B', 'C']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(data_a, positions=np.array(xrange(len(data_a)))*2.0-0.4, sym='', widths=0.6)
bpr = plt.boxplot(data_b, positions=np.array(xrange(len(data_b)))*2.0+0.4, sym='', widths=0.6)
set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='Apples')
plt.plot([], c='#2C7BB6', label='Oranges')
plt.legend()

plt.xticks(xrange(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(0, 8)
plt.tight_layout()
plt.savefig('boxcompare.png')

# ===============================================================================================

# 3. A simple way to plot group boxplots by using pandas

import pandas as pd, numpy as np

df = pd.DataFrame(np.random.rand(12,2), columns=['Apples', 'Oranges'] )

df['Categories'] = pd.Series(list('AAAABBBBCCCC'))

pd.options.display.mpl_style = 'default'

df.boxplot(by='Categories')

# ===============================================================================================

# 4. We can use the Seaborn library for plots. First melt the dataframe to format data and then create the boxplot of your choice

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# fake data
df = pd.DataFrame({'Group':['A','A','A','B','C','B','B','C','A','C'],\
                  'Apple':np.random.rand(10),'Orange':np.random.rand(10)})
df = df[['Group','Apple','Orange']]

# viz
dd=pd.melt(df,id_vars=['Group'],value_vars=['Apple','Orange'],var_name='fruits')
sns.boxplot(x='Group',y='value',data=dd,hue='fruits')

# ==============================================================================================

# 5. A more elegant way to change the color of the box plot by iterating over the dictionary of the object itself

def color_box(bp, color):

    # Define the elements to color. You can also add medians, fliers and means
    elements = ['boxes','caps','whiskers']

    # Iterate over each of the elements changing the color
    for elem in elements:
        [plt.setp(bp[elem][idx], color=color) for idx in xrange(len(bp[elem]))]
    return

a = np.random.uniform(0,10,[100,5])    

bp = plt.boxplot(a)
color_box(bp, 'red')

# =====================================================================================================

# 6. A function to make slightly fancier grouped boxplots

def custom_legend(colors, labels, linestyles=None):
    """ Creates a list of matplotlib Patch objects that can be passed to the legend(...) function to create a custom
        legend.

    :param colors: A list of colors, one for each entry in the legend. You can also include a linestyle, for example: 'k--'
    :param labels:  A list of labels, one for each entry in the legend.
    """

    if linestyles is not None:
        assert len(linestyles) == len(colors), "Length of linestyles must match length of colors."

    h = list()
    for k,(c,l) in enumerate(zip(colors, labels)):
        clr = c
        ls = 'solid'
        if linestyles is not None:
            ls = linestyles[k]
        patch = patches.Patch(color=clr, label=l, linestyle=ls)
        h.append(patch)
    return h


def grouped_boxplot(data, group_names=None, subgroup_names=None, ax=None, subgroup_colors=None,
                    box_width=0.6, box_spacing=1.0):
    """ Draws a grouped boxplot. The data should be organized in a hierarchy, where there are multiple
        subgroups for each main group.

    :param data: A dictionary of length equal to the number of the groups. The key should be the
                group name, the value should be a list of arrays. The length of the list should be
                equal to the number of subgroups.
    :param group_names: (Optional) The group names, should be the same as data.keys(), but can be ordered.
    :param subgroup_names: (Optional) Names of the subgroups.
    :param subgroup_colors: A list specifying the plot color for each subgroup.
    :param ax: (Optional) The axis to plot on.
    """

    if group_names is None:
        group_names = data.keys()

    if ax is None:
        ax = plt.gca()
    plt.sca(ax)

    nsubgroups = np.array([len(v) for v in data.values()])
    assert len(np.unique(nsubgroups)) == 1, "Number of subgroups for each property differ!"
    nsubgroups = nsubgroups[0]

    if subgroup_colors is None:
        subgroup_colors = list()
        for k in range(nsubgroups):
            subgroup_colors.append(np.random.rand(3))
    else:
        assert len(subgroup_colors) == nsubgroups, "subgroup_colors length must match number of subgroups (%d)" % nsubgroups

    def _decorate_box(_bp, _d):
        plt.setp(_bp['boxes'], lw=0, color='k')
        plt.setp(_bp['whiskers'], lw=3.0, color='k')

        # fill in each box with a color
        assert len(_bp['boxes']) == nsubgroups
        for _k,_box in enumerate(_bp['boxes']):
            _boxX = list()
            _boxY = list()
            for _j in range(5):
                _boxX.append(_box.get_xdata()[_j])
                _boxY.append(_box.get_ydata()[_j])
            _boxCoords = zip(_boxX, _boxY)
            _boxPolygon = plt.Polygon(_boxCoords, facecolor=subgroup_colors[_k])
            ax.add_patch(_boxPolygon)

        # draw a black line for the median
        for _k,_med in enumerate(_bp['medians']):
            _medianX = list()
            _medianY = list()
            for _j in range(2):
                _medianX.append(_med.get_xdata()[_j])
                _medianY.append(_med.get_ydata()[_j])
                plt.plot(_medianX, _medianY, 'k', linewidth=3.0)

            # draw a black asterisk for the mean
            plt.plot([np.mean(_med.get_xdata())], [np.mean(_d[_k])], color='w', marker='*',
                      markeredgecolor='k', markersize=12)

    cpos = 1
    label_pos = list()
    for k in group_names:
        d = data[k]
        nsubgroups = len(d)
        pos = np.arange(nsubgroups) + cpos
        label_pos.append(pos.mean())
        bp = plt.boxplot(d, positions=pos, widths=box_width)
        _decorate_box(bp, d)
        cpos += nsubgroups + box_spacing

    plt.xlim(0, cpos-1)
    plt.xticks(label_pos, group_names)

    if subgroup_names is not None:
        leg = custom_legend(subgroup_colors, subgroup_names)
        plt.legend(handles=leg)
		
# use of the function
data = { 'A':[np.random.randn(100), np.random.randn(100) + 5],
         'B':[np.random.randn(100)+1, np.random.randn(100) + 9],
         'C':[np.random.randn(100)-3, np.random.randn(100) -5]
       }

grouped_boxplot(data, group_names=['A', 'B', 'C'], subgroup_names=['Apples', 'Oranges'], subgroup_colors=['#D02D2E', '#D67700'])
plt.show()

# =======================================================================================================================================

# 7. Grouped boxplots, towards subtle academic publication styling

# --- Your data, e.g. results per algorithm:
data1 = [5,5,4,3,3,5]
data2 = [6,6,4,6,8,5]
data3 = [7,8,4,5,8,2]
data4 = [6,9,3,6,8,4]

# --- Combining your data:
data_group1 = [data1, data2]
data_group2 = [data3, data4]

# --- Labels for your data:
labels_list = ['a','b']
xlocations  = range(len(data_group1))
width       = 0.3
symbol      = 'r+'
ymin        = 0
ymax        = 10

ax = plt.gca()
ax.set_ylim(ymin,ymax)
ax.set_xticklabels( labels_list, rotation=0 )
ax.grid(True, linestyle='dotted')
ax.set_axisbelow(True)
ax.set_xticks(xlocations)
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('title')

# --- Offset the positions per group:
positions_group1 = [x-(width+0.01) for x in xlocations]
positions_group2 = xlocations

plt.boxplot(data_group1, 
            sym=symbol,
            labels=['']*len(labels_list),
            positions=positions_group1, 
            widths=width, 
#           notch=False,  
#           vert=True, 
#           whis=1.5,
#           bootstrap=None, 
#           usermedians=None, 
#           conf_intervals=None,
#           patch_artist=False,
            )

plt.boxplot(data_group2, 
            labels=labels_list,
            sym=symbol,
            positions=positions_group2, 
            widths=width, 
#           notch=False,  
#           vert=True, 
#           whis=1.5,
#           bootstrap=None, 
#           usermedians=None, 
#           conf_intervals=None,
#           patch_artist=False,
            )

plt.savefig('boxplot_grouped.png')  
plt.savefig('boxplot_grouped.pdf')    # when publishing, use high quality PDFs
#plt.show()                   # uncomment to show the plot.

# ==========================================================================================

# 8. A flexible generic solution with matplotlib

# --- Your data, e.g. results per algorithm:
data1 = [5,5,4,3,3,5]
data2 = [6,6,4,6,8,5]
data3 = [7,8,4,5,8,2]
data4 = [6,9,3,6,8,4]
data6 = [17,8,4,5,8,1]
data7 = [6,19,3,6,1,1]


# --- Combining your data:
data_group1 = [data1, data2, data6]
data_group2 = [data3, data4, data7]
data_group3 = [data1, data1, data1]
data_group4 = [data2, data2, data2]
data_group5 = [data2, data2, data2]

data_groups = [data_group1, data_group2, data_group3] #, data_group4] #, data_group5]

# --- Labels for your data:
labels_list = ['a','b', 'c']
width       = 0.3
xlocations  = [ x*((1+ len(data_groups))*width) for x in range(len(data_group1)) ]

symbol      = 'r+'
ymin        = min ( [ val  for dg in data_groups  for data in dg for val in data ] )
ymax        = max ( [ val  for dg in data_groups  for data in dg for val in data ])

ax = pl.gca()
ax.set_ylim(ymin,ymax)

ax.grid(True, linestyle='dotted')
ax.set_axisbelow(True)

pl.xlabel('X axis label')
pl.ylabel('Y axis label')
pl.title('title')

space = len(data_groups)/2
offset = len(data_groups)/2


ax.set_xticks( xlocations )
ax.set_xticklabels( labels_list, rotation=0 )
# --- Offset the positions per group:

group_positions = []
for num, dg in enumerate(data_groups):    
    _off = (0 - space + (0.5+num))
    print(_off)
    group_positions.append([x-_off*(width+0.01) for x in xlocations])

for dg, pos in zip(data_groups, group_positions):
    pl.boxplot(dg, 
                sym=symbol,
    #            labels=['']*len(labels_list),
                labels=['']*len(labels_list),           
                positions=pos, 
                widths=width, 
    #           notch=False,  
    #           vert=True, 
    #           whis=1.5,
    #           bootstrap=None, 
    #           usermedians=None, 
    #           conf_intervals=None,
    #           patch_artist=False,
                )

pl.show()





















