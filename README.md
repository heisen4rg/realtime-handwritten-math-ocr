Real-Time Handwritten Math OCR (macOS)

A system-level macOS tool that enables real-time selection and accurate extraction of handwritten mathematical expressions from on-screen PDFs and images.

Current Features
- OS-level mouse drag detection
- Region-based screen capture
- Clean modular architecture (input → capture → processing)

Motivation
Inspired by limitations in macOS Preview, which detects handwritten text but fails to accurately extract mathematical symbols and expressions.

Tech Stack
- Python
- Pillow (ImageGrab)
- pynput
- macOS Accessibility & Screen Recording APIs

Status
🚧 In active development
