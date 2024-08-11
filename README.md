# Image Encryption Tool

## Overview

This project is a simple image encryption tool that uses pixel manipulation to encrypt images. The tool supports operations like adding a key value to each pixel's RGB components. It uses the Python `Pillow` library for image processing.

## Features

- Encrypts an image by modifying its pixel values based on a given key.
- Saves the encrypted image to a specified path.

## Prerequisites

- Python 3.x
- `Pillow` library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/SaiKrishna033/SCT_CS_2.git
    cd image-encryption-tool
    ```

2. **Install the required Python libraries:**

    ```sh
    pip install pillow
    ```

## Usage

1. **Run the script:**

    ```sh
    python image_encryption_tool.py
    ```

2. **Follow the prompts to input the paths and encryption key:**

    ```plaintext
    Enter the path to the image: <path to your image file>
    Enter the path to save the encrypted image: <path to save the encrypted image>
    Enter the encryption key (an integer): <encryption key>
    ```

After running the script, the encrypted image will be saved to the specified path.
