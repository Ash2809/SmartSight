# SmartSight
VisionAI/
│
├── main.py                 # Main program that runs the full pipeline
├── requirements.txt        # All Python dependencies for easy setup
│
├── models/                 # Optional: store YOLO models or custom weights
│   └── yolov8n.pt
│
├── utils/                  # Helper modules
│   ├── detection.py        # YOLOv8 object detection functions
│   ├── tts.py              # Text-to-speech functions
│   ├── voice_input.py      # Speech recognition functions
│   └── ai_agent.py         # LangChain/Gemini interaction functions
│
├── config/                 # Configuration files
│   └── settings.yaml       # e.g., TTS voice, LangChain API keys, model paths
│
└── assets/                 # Optional: sample images, test videos, icons
