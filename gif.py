from PIL import Image

# Open the GIF file
gif = Image.open("images/gta-wasted.gif")

# Set the number of frames you want to extract
num_frames_to_extract = 10

# Total number of frames in the GIF
total_frames = gif.n_frames

# Calculate the interval to extract frames evenly
frame_interval = total_frames // num_frames_to_extract

# Loop through and save the frames
for i in range(num_frames_to_extract):
    # Set the frame position
    gif.seek(i * frame_interval)
    
    # Save the frame as a PNG image
    frame = gif.copy()
    frame.save(f"dying_{i+1}.png")

print("Frames extracted successfully.")
