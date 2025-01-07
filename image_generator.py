import requests
from PIL import Image, ImageTk
import io
import tkinter as tk
from urllib.parse import quote

def generate_image(prompt, width=1280, height=720, seed=42, model="flux"):
    # URL encode the prompt
    encoded_prompt = quote(prompt)

    # Pollinations API URL with parameters
    image_url = f"https://pollinations.ai/p/{encoded_prompt}?width={width}&height={height}&seed={seed}&model={model}"
    
    return image_url

def display_image_from_url(image_url):
    # Fetch the image from the URL
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))

        # Create Tkinter window and display image
        root = tk.Tk()
        root.title("Generated Image")

        tk_image = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=tk_image)
        label.image = tk_image  # Keep reference to avoid garbage collection
        label.pack()

        # Download button
        def download_image():
            with open("downloaded_image.jpg", "wb") as file:
                file.write(response.content)
            print("Image downloaded successfully.")
            root.quit()  # Close the window after download

        download_button = tk.Button(root, text="Download Image", command=download_image)
        download_button.pack()

        root.mainloop()
    else:
        print(f"Failed to fetch image. Status code: {response.status_code}")

def image_generator():
    print("\n[Image Generator]")
    prompt = input("What do you want to generate: ")
    print("Generating image...")

    try:
        # Generate the image URL
        image_url = generate_image(prompt)
        display_image_from_url(image_url)
    except Exception as e:
        print(f"Error during image generation: {e}")

if __name__ == "__main__":
    image_generator()