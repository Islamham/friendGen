# friendGen

Don't have any friends? We got you. **friendGen** is an application that takes in a photo of you and adds a friend to it using generative AI. This way, at least you'll be popular on social media! 😭 

Built for the UBC CIC Hackathon 2024, friendGen combines advanced AI capabilities with a user-friendly interface to bring virtual companionship right to your photos. Here’s how it works and the tech that powers it.

# UI:
<br>
<img width="959" alt="image" src="https://github.com/andrewahn-ubc/FriendGen/assets/115388743/d7247ac6-52e6-4f16-a310-0312eb4b15a3">

## How friendGen Works

friendGen is all about making your photos pop with AI-generated companions. You upload a picture, and using Titan Image Generator’s image mask inpainting capability, the app inserts a virtual friend into the frame. Streamlit provides the easy-to-use interface, while AWS Bedrock ensures the AI works smoothly behind the scenes.

## Architecture Overview

friendGen’s architecture is designed to deliver a seamless experience, using a combination of AI models, cloud services, and a sleek frontend. Here's a breakdown of how we put this together:

1. **User Interface (Streamlit + CSS)**:
   - **Streamlit**: Powers the app’s interactive frontend, where users upload their photos and see the magic happen. Streamlit provides a clean and responsive interface for easy interaction.
   - **CSS**: Styles the interface, ensuring the app looks polished and user-friendly.

2. **Backend Processing (Python, AWS Bedrock)**:
   - **Python**: The core programming language used to manage data flow and processing between the user interface and AI models.
   - **AWS Bedrock**: Hosts Titan Image Generator, the powerhouse behind the inpainting capabilities that insert your AI friend into the photo with realistic detail.

3. **AI Models (AWS Bedrock)**:
   - **AWS Bedrock**: Handles the generation of AI content, making sure your virtual friend blends seamlessly into your photo.

4. **AWS Infrastructure (EC2)**:
   - **AWS EC2**: Hosts the entire application, providing a reliable environment to manage image processing and AI tasks efficiently.
   - **Red Hat**: Provides the operating system environment for EC2 instances, ensuring stability, security, and performance optimization.

## Workflow

The workflow of friendGen is designed to be user-friendly and efficient, ensuring a seamless experience from image upload to friend generation. Here’s a step-by-step breakdown:

1. **Image Upload** (`image_insertion_app.py`):
   - Users upload an image through the Streamlit interface. The image can be in PNG or JPG format.

2. **Parameter Selection** (`image_insertion_app.py`):
   - Users select the area where they want the AI-generated friend to be inserted. This is done through a multi-select option that defines the mask area for inpainting.

3. **Image Processing** (`image_insertion_lib.py`):
   - The uploaded image is processed to extract its bytes and prepare it for inpainting. The mask area is defined based on user input using the `get_bytesio_from_bytes` and `get_image_from_bytes` functions.

4. **AI Friend Generation** (`image_insertion_lib.py`):
   - The application sends a request to the Titan Image Generator hosted on AWS Bedrock. The request includes the original image, mask area, and a prompt describing the friend to be generated. This is handled by the `get_titan_image_insertion_request_body` function.

5. **Image Insertion** (`image_insertion_lib.py`):
   - The Titan Image Generator processes the request and returns an image with the AI-generated friend inserted into the specified area. The `get_titan_response_image` function processes the response.

6. **Result Display** (`image_insertion_app.py`):
   - The generated image is displayed on the Streamlit interface, allowing users to download or share their new friend-enhanced photo.

This workflow ensures that users can easily enhance their photos with AI-generated friends, making the process intuitive and efficient.

## Challenges and Solutions

1. **Quick Turnaround**: Building the app for a hackathon meant we had to prioritize key features and make efficient use of pre-existing AI models to deliver a functional prototype on time.

2. **Performance Optimization**: Keeping everything fast and responsive was crucial. We optimized API calls and backend processes to reduce latency and maintain a smooth user experience.

## Future Enhancements

- **Full Integration of AWS Lambda and S3**: To manage task execution dynamically and scale data handling as the application grows.
- **Enhanced RAG Implementation**: Continuously refining prompt tuning to improve the accuracy and quality of AI-generated friends.
- **Further AI Model Optimization**: Leveraging AWS Bedrock for ongoing improvements in model performance and output quality.


