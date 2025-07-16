# Auto Image Tagger with BLIP

This project uses the [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) model to automatically generate simple tags for your images based on their visual content. it processes `.jpg`, `.jpeg`, and `.png` files from a folder and outputs a `json` file with tags for each image.

---

## Requirements

Before running the program, install the required libraries:

```bash
pip install torch torchvision transformers pillow
```
## Folder structure

Make sure your project directory looks like this:
```
your_project/
├── images/ # put your .jpg, .jpeg, or .png files here
├── output/ # this will store the generated images.json file
├── main.py # the main script
```
> note: you need to manually create both the `images/` and `output/` folders before running the script.

## How to run

1. Add your images to the images/ folder
2. Ensure the output/ folder exists
3. Run the script:
```
python main.py
```

## Output

After running, a file named `images.json` will be created inside the output/ folder:

```
[
  {
    "filename": "cat.jpg",
    "tags": ["cat", "sitting", "indoor"]
  },
  {
    "filename": "beach.png",
    "tags": ["sand", "beach", "sunny"]
  }
]
```
Each image gets a list of unique, lowercase tags based on the model’s generated caption.

## Model details

The project uses the following pre-trained model from huggingface:

`Salesforce/blip-image-captioning-base`

This model is capable of generating captions from images, which are then tokenized into tags.


