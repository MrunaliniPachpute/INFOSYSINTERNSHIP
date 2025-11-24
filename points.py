import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.lines import Line2D

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("Indian_Traffic_Violations.csv")
violations = df.groupby("Location").size().reset_index(name="Violation_Count")
violations["Location"] = violations["Location"].str.strip().str.title()

# -------------------------------
# LOAD SHAPEFILE
# -------------------------------
path = r"C:\Users\mruna\Desktop\InfosysInternship\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India-State-and-Country-Shapefile-Updated-Jan-2020-master\India_State_Boundary.shp"
states = gpd.read_file(path)
states["State_Name"] = states["State_Name"].str.strip().str.title()

# -------------------------------
# MERGE DATA
# -------------------------------
merged = states.merge(
    violations,
    left_on="State_Name",
    right_on="Location",
    how="left"
)

# -------------------------------
# REPROJECT TO METRIC CRS (meters)
# -------------------------------
merged_proj = merged.to_crs(epsg=3857)

# -------------------------------
# COMPUTE CENTROIDS AND AREA FOR FONT SIZE
# -------------------------------
merged_proj["centroid"] = merged_proj.geometry.centroid
merged_proj["x"] = merged_proj.centroid.x
merged_proj["y"] = merged_proj.centroid.y
merged_proj["area"] = merged_proj.geometry.area  # in m²

# Function to scale font size by area
min_font, max_font = 8, 16
area_min, area_max = merged_proj["area"].min(), merged_proj["area"].max()
def area_to_fontsize(area):
    return min_font + (area - area_min) / (area_max - area_min) * (max_font - min_font)

# -------------------------------
# PLOT CHOROPLETH
# -------------------------------
fig, ax = plt.subplots(1, 1, figsize=(16,10))
merged_proj.plot(
    column="Violation_Count",
    cmap="Reds",
    legend=True,
    edgecolor="black",
    linewidth=0.5,
    missing_kwds={"color": "lightgrey", "label": "No Data"},
    ax=ax
)
plt.title("Traffic Violations in India by State", fontsize=20)
plt.axis("off")

# -------------------------------
# CENTER AND FIX ASPECT
# -------------------------------
minx, miny, maxx, maxy = merged_proj.total_bounds
x_pad = (maxx - minx) * 0.05
y_pad = (maxy - miny) * 0.05
ax.set_xlim(minx - x_pad, maxx + x_pad)
ax.set_ylim(miny - y_pad, maxy + y_pad)
ax.set_aspect('equal')

# -------------------------------
# ADD FLOW ARROWS BETWEEN STATES
# -------------------------------
sorted_states = merged_proj.dropna(subset=["Violation_Count"]).sort_values(by="Violation_Count", ascending=False)

for i in range(len(sorted_states)-1):
    row_source = sorted_states.iloc[i]
    row_target = sorted_states.iloc[i+1]

    diff = row_source["Violation_Count"] - row_target["Violation_Count"]
    linewidth = 0.5 + (diff / sorted_states["Violation_Count"].max()) * 2  # scale line width

    arrow = FancyArrowPatch(
        (row_source["x"], row_source["y"]),
        (row_target["x"], row_target["y"]),
        connectionstyle="arc3,rad=0.3",
        color="black",
        alpha=0.8,
        linewidth=linewidth,
        arrowstyle="Simple,head_length=10,head_width=5,tail_width=1"
    )
    ax.add_patch(arrow)

# -------------------------------
# COMPUTE RANKS AND ADD LABELS
# -------------------------------
ranked_states = sorted_states.copy()
ranked_states["Rank"] = range(1, len(ranked_states)+1)  # 1 = most violations

for idx, row in ranked_states.iterrows():
    fontsize = area_to_fontsize(row["area"])
    # default label
    x, y = row["x"], row["y"]
    
    # Move only the label for Rank 6
    if row["Rank"] == 6:
        y += 60000  # shift it up
    
    ax.text(
        x,
        y,  
        str(row["Rank"]),
        fontsize=10,
        fontweight='bold',
        color='yellow',
        ha='center',
        va='center',
        zorder=5
    )


# -------------------------------
# ADD CUSTOM LEGEND ON RIGHT
# -------------------------------
legend_elements = [Line2D([0], [0], marker='o', color='w', label=f'Rank {i}',
                          markerfacecolor='yellow', markersize=10) for i in range(1, len(ranked_states)+1)]
ax.legend(handles=legend_elements, title="Violation Rank", loc='best',
          bbox_to_anchor=(0, 0.5))  # move outside to the right

plt.show()
