model = torch.load("../neuro/model")

from PIL import Image, ImageFile
import torch.nn.functional as F

def inspect(path):
        
    labels = ['trash','tweets']

    img = Image.open(path) # "../data/val/tweets/0_c5mv1911cqo21.jpg"

    img_transforms = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    img = img_transforms(img).to(device)
    img = torch.unsqueeze(img, 0)

    model.eval()
    prediction = F.softmax(model(img), dim=1)
    prediction = prediction.argmax()
    print(labels[prediction]) 
    return labels[prediction]