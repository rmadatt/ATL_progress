import matplotlib.pyplot as plt
import numpy as np

# Define categories and progress values (0 to 1 scale)
categories = ['Core', 'Sensors', 'Vision', 'Communications', 'Haptics', 'Security', 'Tests']
values = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]  # 100% as 1.0, 0% as 0.0

# Number of variables
N = len(categories)

# Compute angle for each axis
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Complete the loop

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], categories, color='grey', size=12)

# Draw y-labels
ax.set_rlabel_position(0)
plt.yticks([0.25, 0.5, 0.75, 1.0], ["25%", "50%", "75%", "100%"], color="grey", size=10)
plt.ylim(0, 1)

# Plot data
values += values[:1]  # Complete the loop
ax.plot(angles, values, linewidth=2, linestyle='solid', label='Progress')
ax.fill(angles, values, 'b', alpha=0.1)

# Add title
plt.title('VisionGlove Project Coding Progress', size=16, color='black', y=1.1)

# Show the plot
plt.show()

# Optionally, save to file: plt.savefig('visionglove_radar_chart.png')
