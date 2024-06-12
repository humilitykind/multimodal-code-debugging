# Multimodal Code Debugging

## Overview
This project aims to develop a prototype system that can analyze screenshots containing code snippets and error logs to extract relevant features and provide suggestions for resolving errors. 

## Features
- Preprocesses screenshot images to enhance text extraction
- Extracts code snippets, error types, and other relevant information using OCR
- Generates suggestions for resolving errors using a pre-trained transformer model

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/multimodal-code-debugging.git
    cd multimodal-code-debugging
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.6+ installed. Then, install the required Python libraries:
    ```bash
    pip install opencv-python pytesseract transformers
    ```

3. **Install Tesseract-OCR**:
    Download and install Tesseract-OCR from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract). Ensure it is added to your system's PATH.

## Usage

To analyze a screenshot and extract information, use the following command:
```bash
python -m getgpt "path_to_your_screenshot.png"
