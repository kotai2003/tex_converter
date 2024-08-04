Here is the revised translation with the "Installation" section removed:

---

# Markdown Converter App

This Markdown Converter App is a Streamlit application that converts ChatGPT-style Markdown documents into a format usable by Typora and Qiita. You can input the original Markdown on the left side, and after pressing the convert button, the converted Markdown will be displayed on the right. This app is particularly effective for converting Markdown documents containing equations.

[Access the app here](https://texconverter.streamlit.app/).

![Texconverter](https://github.com/user-attachments/assets/a143187d-b48f-4fe1-9a6c-2d28d6561cf9)

## Features

- **Simple UI**: Provides a clean interface that anyone can use easily.
- **Instant Preview**: Allows you to preview the converted Markdown immediately.
- **Equation Conversion**: Converts LaTeX-style equations into MathJax-compatible format.

## Setup Instructions

To run this app locally, follow these steps:

### Prerequisites

- Python 3.6 or higher
- pip

### Running the App

Start the Streamlit server:
```
streamlit run app.py
```
If the browser does not open automatically, please access `http://localhost:8501`.

## Usage

1. Paste the Markdown document you want to convert into the text box on the left side.
2. Press the "Convert" button.
3. The converted Markdown will be displayed on the right, along with a preview as Markdown.

## License

This project is released under the [MIT License](LICENSE). For details, refer to the `LICENSE` file.
