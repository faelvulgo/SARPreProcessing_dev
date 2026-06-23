<h1 align="center"> ESA SNAP SAR Batch Processing </h1>

![Python Version](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![ESA SNAP](https://img.shields.io/badge/ESA_SNAP-v8.0+-orange?style=for-the-badge)

# Description
This repository contains a Python automation script designed for batch processing Synthetic Aperture Radar (SAR) imagery using the **ESA SNAP Graph Processing Tool (GPT)**. 

Instead of processing images one by one through the SNAP Desktop GUI, this script automates the execution of a pre-defined XML processing workflow graph across an entire directory of `.zip` SAR data products, handling errors and tracking processing time.

# Features
- **Batch Processing:** Automatically scans and processes all `.zip` SAR images within a directory.
- **Idempotency (Skip Existing):** Checks the output folder and skips files that have already been processed, preventing redundant work if the script is restarted.
- **Robust Error Logging:** Catches runtime errors from the ESA SNAP execution and outputs them to an external `erros.log` file with detailed stack traces.
- **Progress Tracking:** Utilizes a visual progress bar (`tqdm`) showing remaining files and processing duration for each image.

# Prerequisites
Before running the script, ensure you have the following installed:
- **Python 3.8+**
- **ESA SNAP Software** (with the `gpt` executable verified in your system)
- Required Python packages:
  ```bash
  pip install tqdm

## License

This project is proprietary software. You are welcome to download and use the code strictly for **personal and private purposes**. 

However, commercial use, modification for public distribution, and direct redistribution of the source code are **strictly prohibited**. Any sharing must be done by linking directly to this original repository.

For full legal terms, please refer to the [LICENSE](https://github.com/faelvulgo/SARPreProcessing_dev/blob/main/LICENSE.txt) file.
