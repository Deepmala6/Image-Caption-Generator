from PIL import Image
import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration

class ImageCaption:
    def __init__(self):
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        
    def generate(self, img):
        if isinstance(img, str):
            img = Image.open(img)
        text = "Explain This Image :-- " 
        inputs = self.processor(images=img, text = text, return_tensors='pt')
        output = self.model.generate(**inputs)
        
        caption = self.processor.decode(output[0], skip_special_tokens=True)
        return caption
    
if __name__ == '__main__':
    #img_path = r"C:\Users\deepm\Downloads\isaac-ibbott-JNvT73PnNWo-unsplash.jpg"
    ic = ImageCaption()
    #caption = ic.generate(img_path)    
    #print("Caption of image: ", caption)
    
    app = gr.Interface(
        fn = ic.generate,
        inputs = gr.Image(type = 'pil'),
        outputs = "text",
        description = "Upload An Image To Generate Caption :)"
    )
    app.launch(share=True)

    