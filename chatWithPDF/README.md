# chatWithPDF
This project allows you to upload a PDF document and ask questions about its content. It uses langchain, openapi ai model, and Facebook Ai Similarity Search(FAISS) library to process the text in the PDF and provide answers to questions pertaining to the document.

## Demo
https://github.com/MatthewRamsey/ai-labs/assets/14944537/d3172a3d-7e59-446c-9e7a-13df8f915f4d

### Cost
![image](https://github.com/john-thuo1/chatWithPDF/assets/108690517/c4a72a25-1aeb-447c-b4f4-90b38225f9d3)


## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/MatthewRamsey/chatWithPDF
   cd into your directory/ open with vscode
   ```
2. Create a Virtual Environment:
    ```shell
    python -m venv env
    ```
3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```
4. Create OpenAI API Key and add it to your .env file:
   [openai](https://platform.openai.com/)
   
5. Run the application:

   ```shell
   streamlit run App.py
   ```
