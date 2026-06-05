from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from tkinter import Tk, filedialog

print("Loading model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Image"
)

if not file_path:
    print("No image selected")
    exit()

image = Image.open(file_path).convert("RGB")

inputs = processor(images=image, return_tensors="pt")

output = model.generate(**inputs)

caption = processor.decode(
    output[0],
    skip_special_tokens=True
)

print("\nCaption:")
print(caption)