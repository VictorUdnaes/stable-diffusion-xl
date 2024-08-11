from diffusers import DiffusionPipeline
import torch
import os
from datetime import datetime

# Load the pipeline
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", 
    torch_dtype=torch.float16, 
    use_safetensors=True, 
    variant="fp16"
)

# Check if MPS is available and use it; otherwise, fall back to CPU
if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

pipe.to(device)

# Define the prompt
prompt = "A mystical grey-bearded wizard stands in the middle of a medieval tavern, smiling at the camera"

# Set low resolution for quick testing

# Generate the image with low resolution
image = pipe(prompt=prompt).images[0]

# Specify the output directory
output_dir = "./generated_images"

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Create a unique filename using a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
image_path = os.path.join(output_dir, f"image_{timestamp}.png")

# Save the image
image.save(image_path)

print(f"Image saved to {image_path}")
