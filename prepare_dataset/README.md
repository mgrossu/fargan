# Prepare Dataset

This folder contains scripts to **prepare your dataset** for training the Face Artifact Removal GAN.  
It includes tools to convert images to compressed videos and extract frames from videos.

---

## Scripts

### `prepare_dataset.py`

A single script that can perform **two tasks**:

1. **Convert images to compressed videos**
2. **Extract frames from videos**

This allows you to generate paired datasets of **original and compressed frames** for training.

---

## Usage

### 1. Convert images to compressed videos

```bash
python prepare_dataset.py convert /path/to/images /path/to/output_videos --bitrate 500k --verbose

