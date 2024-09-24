# FriendGen

Don't have any friends? We got you. **FriendGen** is an application that takes in a photo of you and adds a friend to it using generative AI. This way, at least your social media will think you're popular! 😉

Built in just 9 hours for the UBC CIC Hackathon 2024, FriendGen combines advanced AI capabilities with a user-friendly interface to bring virtual companionship right to your photos. Here’s how it works and the tech that powers it.

# Homepage:
<br>
<img width="959" alt="image" src="https://github.com/andrewahn-ubc/friendGen/assets/115388743/d7247ac6-52e6-4f16-a310-0312eb4b15a3">

# Before:
<br>
<img width="512" alt="image" src="https://github.com/andrewahn-ubc/friendGen/assets/115388743/286f1728-375d-4e38-9ed6-fa3593a33ce3">


# After:
<br>
<img width="512" alt="image" src="https://github.com/andrewahn-ubc/friendGen/assets/115388743/c42c55f8-ec77-4caa-a0ac-3dbf983e996b">

## Architecture Overview

FriendGen’s architecture is designed to deliver a seamless experience, using a combination of AI models, cloud services, and a sleek frontend. Here's a breakdown of how we put this together:

1. **User Interface (Streamlit + CSS)**:
   - **Streamlit**: Powers the app’s interactive frontend, where users upload their photos and see the magic happen. Streamlit provides a clean and responsive interface for easy interaction.
   - **CSS**: Styles the interface, ensuring the app looks polished and user-friendly.

2. **Backend Processing (Python, Langchain, AWS Bedrock)**:
   - **Python**: The core programming language used to manage data flow and processing between the user interface and AI models.
   - **Langchain**: Enhances the AI’s ability to fine-tune prompts and pull in relevant data, ensuring that your generated friends fit perfectly into the photo.
   - **AWS Bedrock**: Hosts Titan Image Generator, the powerhouse behind the inpainting capabilities that insert your AI friend into the photo with realistic detail.

3. **AI Models (Stability AI, Claude v2.1)**:
   - **Stability AI**: Handles the generation of AI content, making sure your virtual friend blends seamlessly into your photo.
   - **Claude v2.1**: Provides advanced natural language processing, refining how AI understands the context of each photo and enhancing the friend generation process.

4. **AWS Infrastructure (EC2, Knowledge Base)**:
   - **AWS EC2**: Hosts the entire application, providing a reliable environment to manage image processing and AI tasks efficiently.
   - **Knowledge Base**: A key part of the Retrieval-Augmented Generation (RAG) process, storing critical data that AI models use to fine-tune responses, improving the relevance and context of generated content.

5. **OS and Deployment (Red Hat Linux)**:
   - **Red Hat**: Provides the operating system environment for EC2 instances, ensuring stability, security, and performance optimization.

## How FriendGen Works

FriendGen is all about making your photos pop with AI-generated companions. You upload a picture, and using Titan Image Generator’s image mask inpainting capability, the app inserts a virtual friend into the frame. Streamlit provides the easy-to-use interface, while AWS Bedrock ensures the AI works smoothly behind the scenes.

## Challenges and Solutions

1. **Quick Turnaround**: Building the app in just 9 hours meant we had to prioritize key features and make efficient use of pre-existing AI models to deliver a functional prototype on time.
   
2. **Fine-Tuning AI with RAG**: Generating contextually appropriate friends is no small feat. By integrating RAG and using a dedicated Knowledge Base, we ensured that each AI addition felt natural in the scene.

3. **Performance Optimization**: Keeping everything fast and responsive was crucial. We optimized API calls and backend processes to reduce latency and maintain a smooth user experience.

## Future Enhancements

- **Full Integration of AWS Lambda and S3**: To manage task execution dynamically and scale data handling as the application grows.
- **Enhanced RAG Implementation**: Continuously refining prompt tuning to improve the accuracy and quality of AI-generated friends.
- **Further AI Model Optimization**: Leveraging AWS Bedrock and Stability AI for ongoing improvements in model performance and output quality.


