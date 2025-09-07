from transformers import Blip2Processor, Blip2ForConditionalGeneration
# import torch
# from PIL import Image

print("Test script for BLIP-2 model")

# # Load model and processor
# processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
# model = Blip2ForConditionalGeneration.from_pretrained(
#     "Salesforce/blip2-flan-t5-xl", 
#     torch_dtype=torch.float16, 
#     device_map="auto"
# )

# # Example input
# image = Image.open("example.jpg")
# inputs = processor(images=image, text="Describe this image", return_tensors="pt").to("cuda", torch.float16)

# # Generate output
# output_ids = model.generate(**inputs)
# print(processor.decode(output_ids[0], skip_special_tokens=True))
