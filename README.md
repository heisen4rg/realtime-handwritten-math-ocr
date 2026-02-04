# Real-Time Screen OCR Pipeline (macOS)

A system-level macOS tool that enables real-time selection and extraction of on-screen text by capturing user-selected screen regions, preprocessing the image, and performing live OCR inference through a modular and extensible pipeline.

This project is built with a strong focus on **OS-level input handling, clean architecture, and OCR system design**, and serves as a foundation for future math-aware and handwritten OCR capabilities.

---

## Key Features

- Real-time mouse-based region selection
- OS-level screen capture on macOS
- Geometry normalization for robust bounding boxes
- Image preprocessing for OCR (grayscale conversion, upscaling)
- Live OCR inference using Tesseract
- Modular OCR engine abstraction (easy to swap models)
- Python package-based architecture for scalability

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
├── system/
│   ├── mouse_tracker.py      # OS-level mouse input & pipeline orchestration
│   └── screen_capture.py     # Screen capture utilities
├── ocr/
│   └── engine.py             # OCR engine abstraction & preprocessing logic
└── main.py                   # Entry point (future UI / overlay integration)
```

- **system/** handles OS and hardware interactions (mouse events, screen capture)
- **ocr/** encapsulates all OCR-related logic behind a clean interface
- Components are intentionally decoupled to support future model upgrades without refactoring the system layer

---

## Current OCR Engine (Baseline)

- Backend: **Tesseract 5.x** (via `pytesseract`)
- Preprocessing steps:
  - Grayscale conversion
  - Image upscaling using bicubic resampling
  - Page Segmentation Mode: `--psm 6` (uniform block of text)

This baseline is optimized for printed on-screen text and serves as a reliable starting point for more advanced OCR experimentation.

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
- Lightweight macOS UI overlay for seamless interaction

---

## Tech Stack

- Python 3.11
- Pillow
- pytesseract
- Tesseract OCR (installed via Homebrew)
- pynput (mouse input)
- macOS Accessibility & Screen Recording APIs

---

## Status

✅ Baseline real-time OCR pipeline is stable and functional  
🚧 Active development toward math-aware and handwritten OCR
