import os
import requests
from PIL import Image
import io
from urllib.parse import quote

def generate_image(prompt, width=1280, height=720, seed=42, model="flux"):
    # URL encode the prompt
    encoded_prompt = quote(prompt)

    # Pollinations API URL with parameters
    image_url = f"https://pollinations.ai/p/{encoded_prompt}?width={width}&height={height}&seed={seed}&model={model}&nologo=true"
    
    return image_url

def save_image_from_url(image_url, prompt):
    # Fetch the image from the URL
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))

        # Ensure the `ai-images` folder exists
        folder_path = "ai-images"
        os.makedirs(folder_path, exist_ok=True)

        # Save the image with a filename based on the prompt
        sanitized_prompt = "".join(c if c.isalnum() or c in " _-" else "_" for c in prompt)
        file_path = os.path.join(folder_path, f"{sanitized_prompt}.jpg")
        image.save(file_path)
        print(f"Image saved successfully at: {file_path}")
    else:
        print(f"Failed to fetch image. Status code: {response.status_code}")

def image_generator():
    print("\n[Image Generator]")
    prompt = input("What do you want to generate: ")
    print("Generating image...")

    try:
        # Generate the image URL
        image_url = generate_image(prompt)
        save_image_from_url(image_url, prompt)
    except Exception as e:
        print(f"Error during image generation: {e}")

if __name__ == "__main__":
    image_generator()