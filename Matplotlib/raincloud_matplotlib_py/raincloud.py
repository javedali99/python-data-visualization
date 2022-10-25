from matplotlib.pyplot import subplots, rc, rcdefaults, rc_context
from matplotlib.transforms import offset_copy
from matplotlib.cbook import boxplot_stats
from matplotlib.collections import LineCollection
from seaborn import kdeplot, boxplot, swarmplot, load_dataset

from numpy import zeros_like, column_stack, row_stack

rcdefaults()
rc('font', size=14)
rc('axes.spines', top=False, right=False, left=False)

df = load_dataset('mpg')
plot_df = df.query('cylinders == [4, 6, 8]')
colors = ['tab:orange', 'tab:blue', 'tab:red']
box_width = .3

fig, ax = subplots(dpi=150)

for (cyl, group), c in zip(plot_df.groupby('cylinders'), colors):
    bxpstats = boxplot_stats(group['mpg'])
    ax.bxp(
        bxpstats, positions=[cyl], vert=False, widths=[box_width],
        patch_artist=True, boxprops={'facecolor': c}, capwidths=[0],
        medianprops={'color': 'k'}
    )

    transform = offset_copy(ax.get_yaxis_transform(), y=5, fig=fig, units='points')
    density_ax = ax.inset_axes([0, cyl + box_width * .5, 1, 2 - box_width * 1.5], transform=transform, sharex=ax)
    density_ax.axis('off')
    density_ax.margins(0)

    kdeplot(
        group, x='mpg', ax=density_ax, fill=True, bw_adjust=.25, alpha=.5,
        color=c
    )

    transform = offset_copy(ax.get_yaxis_transform(), y=-5, fig=fig, units='points')
    hist_ax = ax.inset_axes([0, cyl - 2 + box_width, 1, 2 - 1.5 * box_width], transform=transform, sharex=ax)
    hist_ax.axis('off')

    icicles = group.groupby('mpg')['mpg'].count()
    starts = zeros_like(icicles)

    segments = (
        column_stack([icicles.index, starts, icicles.index,  icicles])
        .reshape(-1, 2, 2)
    )

    collection = LineCollection(segments, color=c)
    hist_ax.add_collection(collection)
    hist_ax.set_ylim(0, icicles.max())
    hist_ax.margins(0)
    hist_ax.invert_yaxis()

ax.set_ylim(2, 10)
ax.autoscale_view()
ax.set(ylabel='Cylinders', xlabel='MPG')
fig.savefig('raincloud.png', bbox_inches='tight')
