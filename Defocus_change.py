import os
import numpy as np
import matplotlib.pyplot as plt

# Load the .cs file
cs_file_path = "/Users/manil/Desktop/Tom_Lab_sept_2023/BAD_CTF_PARTICLES/J348_particles_exported.cs"
data = np.load(cs_file_path, allow_pickle=True)

# Assuming 'ctf/df1_A' and 'ctf/df2_A' are the defocus values
defocus_before = data['ctf/df1_A']
defocus_after = data['ctf/df2_A']

# Set the defocus threshold (change it according to your requirement)
defocus_thresh = 4500

# Filter particles based on defocus change
mask = np.abs(defocus_after - defocus_before) < defocus_thresh

# Apply the mask to keep only the selected particles
filtered_data = data[mask]

# Save the filtered data to a new .cs file
output_cs_file_path = "/Users/manil/Desktop/Tom_Lab_sept_2023/BAD_CTF_PARTICLES/Results/filtered_particles.cs"
np.save(output_cs_file_path, filtered_data)

print(f"Filtered particles saved to {output_cs_file_path}")

# Updated paths for the filtering and histogram script
path_to_exported_parent_particles = "/Users/manil/Desktop/Tom_Lab_sept_2023/BAD_CTF_PARTICLES/J345_particles_exported.cs"
path_to_exported_refined_particles = "/Users/manil/Desktop/Tom_Lab_sept_2023/BAD_CTF_PARTICLES/J348_particles_exported.cs"
result_folder = "/Users/manil/Desktop/Tom_Lab_sept_2023/BAD_CTF_PARTICLES/Results"

# Load actual data from .cs files
before_data = np.load(path_to_exported_parent_particles, allow_pickle=True)
after_data = np.load(path_to_exported_refined_particles, allow_pickle=True)

defocus_thresh = 4500  # maximum change in defocus to keep, set this to the value in A as you wish

# Show histogram of defocus change before filtering
hist_before_filtering_path = os.path.join(result_folder, "hist_before_filtering.png")
fig1 = plt.figure()
plt.hist(after_data['ctf/df1_A'] - before_data['ctf/df1_A'], bins=500)
plt.savefig(hist_before_filtering_path)
print(f"Histogram before filtering saved to {hist_before_filtering_path}")

# Filter based on defocus
mask = np.abs(after_data['ctf/df1_A'] - before_data['ctf/df1_A']) < defocus_thresh
after_filtered_data = after_data[mask]

# See updated histogram after filtering
hist_after_filtering_path = os.path.join(result_folder, "hist_after_filtering.png")
fig2 = plt.figure()
plt.hist(after_filtered_data['ctf/df1_A'] - before_data['ctf/df1_A'][mask], bins=500)
plt.savefig(hist_after_filtering_path)
print(f"Histogram after filtering saved to {hist_after_filtering_path}")

# Now save the output data in the result folder
output_folder = os.path.join(result_folder, "Filtered_Particles")
os.makedirs(output_folder, exist_ok=True)

# Save the filtered data to a new .cs file
output_cs_file_path = os.path.join(output_folder, "filtered_particles.cs")
np.save(output_cs_file_path, after_filtered_data)

print(f"Filtered particles saved to {output_cs_file_path}")
