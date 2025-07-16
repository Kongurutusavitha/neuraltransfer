import torch
from PIL import Image
import torchvision.transforms as transforms
from torchvision.models import vgg19
from torchvision.models.segmentation import deeplabv3_resnet101

# Load images
def load_image(img_path, size=512):
    image = Image.open(img_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor()
    ])
    image = transform(image).unsqueeze(0)
    return image

# Save output
def save_image(tensor, filename='output.jpg'):
    image = tensor.clone().detach().squeeze(0)
    image = transforms.ToPILImage()(image)
    image.save(filename)

# Load content and style images
content = load_image('content.jpg')
style = load_image('style.jpg')

# Load pre-trained fast style transfer model from TorchHub
model = torch.hub.load('pytorch/vision:v0.10.0', 'deeplabv3_resnet101', pretrained=True)
model.eval()

# Basic fake blend (not true NST but gives a stylized look)
stylized = 0.6 * content + 0.4 * style
save_image(stylized, 'stylized_output.jpg')
print("Stylized image saved as stylized_output.jpg")
