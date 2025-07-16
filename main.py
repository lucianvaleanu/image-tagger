from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os
import json

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

image_folder = 'images'
output = []

for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(image_folder, filename)
        image = Image.open(img_path).convert('RGB')

        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

        tags = caption.lower().replace(',', '').split()
        output.append({
            'filename': filename,
            'tags': list(set(tags))
        })

with open('output/images.json', 'w') as f:
    json.dump(output, f, indent=2)

print("Tags generated and saved to output/images.json")
