# Real-Time Screen OCR Pipeline

A real-time screen-based OCR system that allows users to select arbitrary on-screen regions, capture the selected content, preprocess the image, and extract text using a modular OCR pipeline.

The project is designed with a strong emphasis on **system-level input handling, clean architecture, and extensibility**, and serves as a foundation for future math-aware and handwritten OCR capabilities.

---

## Key Features

- User-driven rectangular region selection
- Screen capture with geometry-normalized bounding boxes
- Robust image preprocessing (grayscale, upscaling)
- Live OCR inference using Tesseract
- Modular OCR engine abstraction
- Clean, package-based Python architecture

---

## High-Level Pipeline

```
Mouse Drag
→ Bounding Box Normalization
→ Screen Region Capture
→ Image Preprocessing
→ OCR Inference
→ Text Output
```

---

## Architecture Overview

```
src/
├── ui/
│   └── overlay_selector.py   # Full-screen overlay & region selection
├── system/
│   ├── mouse_tracker.py      # Mouse-driven selection (fallback path)
│   └── screen_capture.py     # Screen capture utilities
├── ocr/
│   └── engine.py             # OCR engine & preprocessing logic
└── main.py                   # Pipeline entry point
```

- **ui/** handles user interaction and region selection
- **system/** provides low-level input and screen capture utilities
- **ocr/** encapsulates all OCR-related logic behind a clean interface
- **main.py** orchestrates the end-to-end pipeline

---

## Current OCR Engine (Baseline)

- Backend: **Tesseract 5.x** (via `pytesseract`)
- Preprocessing steps:
  - Grayscale conversion
  - Image upscaling using bicubic resampling
  - Page Segmentation Mode: `--psm 6` (uniform block of text)

This baseline is optimized for printed on-screen text and provides a stable foundation for future OCR model experimentation.

---

## Motivation

While reviewing handwritten math PDFs and on-screen notes, existing tools such as macOS Preview were able to *detect* handwritten regions but failed to accurately extract mathematical symbols and expressions.

This project was started to explore whether a **real-time, system-level OCR pipeline** — operating directly on screen content — could bridge that gap, with a long-term goal of math-aware and handwritten OCR.

---

## Future Work

- OCR post-processing (spacing correction, confidence estimation)
- Math-aware OCR (symbol constraints, equation parsing)
- Handwritten text recognition
- Model replacement (TrOCR, Im2LaTeX-style architectures)
- Cross-platform UI exploration (macOS / Windows / Linux)

---

## Tech Stack

- Python 3.11
- Pillow
- pytesseract
- Tesseract OCR
- pynput (mouse input)
- Tkinter (UI overlay)

---

## Status

✅ Real-time screen OCR pipeline is stable and functional  
✅ Cross-platform UI overlay implemented using Tkinter  
🚧 Active development toward math-aware and handwritten OCR
