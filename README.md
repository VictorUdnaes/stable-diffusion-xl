# How to use Stable Diffusion XL base model for Mac



### Install dependencies
The model uses the pytorch library to generate images so first install these dependencies to be able to run the model:
```bash
pip install diffusers --upgrade
```
```bash
pip install invisible_watermark transformers accelerate safetensors
```

<br>

## How to run the base model:
You can run the  **StableDiffusionController.py** file in terminal directly and the script will generate a **generated_images** in your current directory and save the generated image there.
To set the prompt just change the prompt variable in the script.
If you want to change the resolution you can add width and height variables like this:
```python
# Set low resolution for quick testing
height = 128  # Low height in pixels
width = 128   # Low width in pixels

# Generate the image with low resolution
image = pipe(prompt=prompt, height=height, width=width).images[0]
```
**Note: changing the base resolution can affect the generation time, and setting it to low can significantly affect the quality of the picture. It's reccomended to not change the resolution manually.**
