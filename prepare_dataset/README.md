# Prepare Dataset

This folder contains script to **prepare your dataset** for training the Face Artifact Removal GAN.  
It includes tools to convert images to compressed videos and extract frames from videos.

---

## Script

### `compresstract.py`

A single script that can perform **two tasks**:

1. **Convert images to compressed videos**
2. **Extract frames from videos**

This allows you to generate paired datasets of **original and compressed frames** for training.

---

## Python Dependencies

Before running the scripts, install the required packages:

```bash
pip install opencv-python imageio
```

---

## Usage

### 1. Convert images to compressed videos

```bash
python3 compresstract.py convert /path/to/images /path/to/output_videos --bitrate 500k --verbose
```

### 2. Extract frames from video

```bash
python3 compresstract.py extract /path/to/input_videos /path/to/output_frames --verbose
```
