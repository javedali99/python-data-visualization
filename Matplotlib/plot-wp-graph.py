import matplotlib.pyplot as plt

# Data
years = [1980, 2000, 2015, 2020]
death_rate_wealthiest = [600, 650, 675, 700]
death_rate_poorest = [688, 847, 1002, 1148]

fig, ax = plt.subplots(figsize=(10, 7))

# Plot lines and fill
ax.fill_between(years, death_rate_wealthiest, death_rate_poorest, color="#E6E6FA")
ax.plot(years, death_rate_wealthiest, color="#C0C0C0", lw=2, marker="o")
ax.plot(years, death_rate_poorest, color="#8A2BE2", lw=2, marker="o")

# Annotations for the death rates and dotted lines
for y, w, p in zip(years, death_rate_wealthiest, death_rate_poorest):
    diff = p - w
    ax.text(y + 0.5, (w + p) / 2, f"{diff} more deaths", ha="center", va="center", fontsize=9, color="#8A2BE2")
    ax.plot([y, y], [w, p], linestyle="--", color="#8A2BE2", linewidth=0.5)

# Additional texts
ax.text(1983, 805, "Death rate in \npoorest areas", color="#8A2BE2", fontsize=9)
ax.text(1985, 520, "Death rate in \nwealthiest areas", color="#C0C0C0", fontsize=9)
ax.text(
    1995,
    900,
    "By 2000, the death rate gap\nhad grown so that people in the\npoorest areas were 27 percent\nmore likely to die each year.",
    fontsize=8,
    ha="left",
    color="#8A2BE2",
)
ax.text(
    2015,
    1010,
    "By 2015, people in the poorest\nareas were 49 percent more likely\nto die each year.",
    fontsize=8,
    ha="right",
    color="#8A2BE2",
)

# Styling
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_color("#C0C0C0")

# Grid Lines
ax.grid(axis="y", linestyle="--", linewidth=0.5, color="#C0C0C0")

# Title and Subtitle
ax.text(1978, 1392, "Small death gap has grown wide", fontsize=15, fontweight="bold", ha="left")
ax.text(
    1978,
    1265,
    "In the early 1980s, people in the poorest areas were 9 percent more likely to\ndie each year, with 88 more deaths per 100,000 people than their wealthy\ncounterparts. That gap has widened significantly over time.",
    fontsize=10,
    ha="left",
)

# Footer
footer = "Source: Centers for Disease Control and Prevention, U.S. Census Bureau"
ax.text(2000, -120, footer, fontsize=8, color="#C0C0C0")

# Adjusting y-axis limits and labels
ax.set_xlim(1978, 2022)
ax.set_ylim(0, 1200)

# Adjusting tick labels
ax.set_xticks([1980, 2000, 2015, 2020])
ax.set_yticks(range(0, 1201, 200))
ax.set_yticklabels([str(i) if i != 1200 else "1200 deaths per 100K" for i in range(0, 1201, 200)])

plt.tight_layout()
plt.show()
