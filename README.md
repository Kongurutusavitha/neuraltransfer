# neuraltransfer

Company:CODTECH IT SOLUTIONS

Name:K SAVITHA

INTERN ID:CT06DF1652

Domain:Artificial Intelligence

Duration:6 weeks

Mentor:Neela Santhosh

Project Description: Neural Image Stylization Using PyTorch
This project demonstrates a basic implementation of image stylization using PyTorch, blending the artistic characteristics of a style image with the structural content of a content image. Inspired by the concept of Neural Style Transfer (NST), the approach uses deep learning models and image processing libraries to achieve a visually stylized output. Although not a full implementation of neural style transfer algorithms such as those using Gram matrix optimization, this method applies a fast and lightweight image blending technique and leverages PyTorch's deep learning capabilities to process and manipulate images.

Tools and Libraries Used
1. PyTorch
PyTorch is a powerful open-source deep learning framework developed by Facebook AI Research. It supports dynamic computation graphs, making it especially suitable for image processing and neural network-based applications. In this project, PyTorch is used to handle tensor operations, model loading, and blending of image data.

2. Torchvision
Torchvision is a companion library to PyTorch that provides common datasets, model architectures, and image transformation utilities. It simplifies preprocessing and model integration. Specifically:

torchvision.transforms is used to resize, normalize, and convert images to tensors.

Pre-trained models like deeplabv3_resnet101 and vgg19 (commented in parts) come from torchvision’s model zoo.

3. PIL (Python Imaging Library) / Pillow
The Python Imaging Library (now maintained as Pillow) is used for loading and saving images in various formats. In this project, it handles reading .jpg images and converting tensors back to image files for saving the stylized output.

Workflow Overview
Image Loading
The load_image() function loads content and style images from disk using Pillow, converts them to RGB format, resizes them to a uniform size (512x512 pixels), and transforms them into PyTorch tensors using ToTensor(). A batch dimension is added using unsqueeze(0) to match the input requirements for models.

Model Loading
Although the code includes the loading of the deeplabv3_resnet101 segmentation model from TorchHub, it isn't actively used in the stylization in this simplified version. The intention is to demonstrate how pre-trained models can be integrated, potentially for tasks like semantic segmentation or to refine stylization based on object boundaries in future enhancements.

Stylization Process
Instead of a computationally expensive optimization loop, a simplified stylization method is used: weighted blending of the content and style image tensors. This gives a basic stylized effect by combining the pixel values of both images:

stylized
=
0.6
×
content
+
0.4
×
style
stylized=0.6×content+0.4×style
While this method lacks the high-fidelity transfer of neural style transfer algorithms, it demonstrates the concept effectively and runs efficiently.

Output Saving
The blended tensor is converted back into an image using ToPILImage() and saved as stylized_output.jpg using the save_image() function.

OUTPUT

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/61a64cd3-ce80-4c88-a058-315faf25963e" />


