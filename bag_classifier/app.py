import gradio as gr
from fastai.vision.all import *
import skimage

learn = load_learner("luxury_bag_model.pkl")

labels = learn.dls.vocab


def predict(img):
    img = PILImage.create(img)
    pred, pred_idx, probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}


title = "Luxury Bag Classifier"
description = (
    "A luxury bag classifier trained on photos of a few brands. Created with resnet18 architecture."
)
article = "<p style='text-align: center'><a href='https://www.kaggle.com/code/sellde/fastai-chapter-2' target='_blank'>Model Source</a></p>"
examples = [["gucci.jpg"], ["chanel.jpg"], ["vuitton.jpg"]]
interpretation = "default"
enable_queue = True

gr.Interface(
    fn=predict,
    inputs=gr.inputs.Image(shape=(512, 512)),
    outputs=gr.outputs.Label(),
    title=title,
    description=description,
    article=article,
    examples=examples,
    interpretation=interpretation,
    enable_queue=enable_queue,
).launch()
