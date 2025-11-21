# AI Skills & Experiments Workspace

This workspace contains experimental projects and demonstrations of various AI capabilities, focusing on multi-modal content generation and processing.

## 🗂️ Project Structure

```
test_skills/
├── projects/                    # Organized project categories
│   ├── image-generation/        # Image generation projects
│   ├── video-generation/        # Video generation projects  
│   ├── audio-generation/        # Audio generation projects
│   └── text-generation/        # Text generation projects
├── shared/                      # Shared utilities and configurations
│   ├── utils/                   # Common utility functions
│   └── config/                  # Configuration management
├── experiments/                 # Experimental work and research
│   ├── active/                  # Current experiments
│   ├── completed/               # Finished experiments
│   └── archived/                # Superseded experiments
├── src/                         # Source code for general utilities
├── docs/                        # Documentation
└── data/                        # Data files and datasets
```

## 🚀 Current Projects

### Image Generation ✅
- **CogView-4 Demo**: Complete Python client with API integration
- **Features**: Multiple models, auto-download, error handling
- **Location**: `projects/image-generation/`

### Video Generation 📋
- **Planned**: Text-to-video, video editing, motion graphics
- **Technologies**: Runway, Pika Labs, Stable Video Diffusion
- **Location**: `projects/video-generation/`

### Audio Generation 📋
- **Planned**: TTS, music generation, voice cloning
- **Technologies**: OpenAI TTS, ElevenLabs, local synthesis
- **Location**: `projects/audio-generation/`

### Text Generation 📋
- **Planned**: LLM integration, text processing, creative writing
- **Technologies**: OpenAI, Anthropic, local models
- **Location**: `projects/text-generation/`

## 🛠️ Shared Components

### Utilities
- HTTP client with retry logic
- API key management
- File handling and processing
- Logging configuration

### Configuration
- Environment variable support
- Settings management
- Constants and enums

## 🧪 Experiments

### Active Focus Areas
- Multi-modal integration
- Performance optimization
- New model exploration

### Recent Success
- **2024-11-21**: CogView-4 API integration completed

## 📦 Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for some projects)
- API keys for various services

### Installation
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies (if needed)
npm install
```

### Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Add your API keys
# Edit .env with your specific keys
```

## 📚 Usage Examples

### Image Generation
```bash
cd projects/image-generation
python3 cogview4_demo_fixed.py test
```

### Video Generation (Future)
```bash
cd projects/video-generation
python3 video_client.py --prompt "A sunset over mountains"
```

## 🔧 Development Guidelines

### Project Organization
- Each project in its own directory
- Shared utilities in `shared/`
- Experiments in `experiments/`
- Documentation in each project's README

### Code Standards
- Python type hints
- Comprehensive error handling
- Unit tests for utilities
- Clear documentation

### Git Workflow
- Feature branches for new projects
- Meaningful commit messages
- Tag releases of working demos
- Archive completed experiments

## 📊 Project Status

| Category | Status | Progress |
|----------|--------|----------|
| Image Generation | ✅ Complete | CogView-4 integrated |
| Video Generation | 📋 Planned | Research phase |
| Audio Generation | 📋 Planned | Research phase |
| Text Generation | 📋 Planned | Research phase |
| Shared Utils | 🔄 In Progress | Basic structure |

## 🎯 Next Steps

1. **Video Generation Research**
   - Explore available APIs
   - Create proof-of-concept
   - Test with sample prompts

2. **Audio Generation Setup**
   - Evaluate TTS services
   - Implement basic client
   - Create audio processing utils

3. **Multi-modal Pipeline**
   - Connect different modalities
   - Create unified interface
   - Build end-to-end examples

## 📝 Recent Changes

### 2024-11-21: Project Reorganization
- Restructured into organized categories
- Moved CogView-4 demo to dedicated folder
- Created project templates for future work
- Added shared utilities structure

### 2024-11-21: CogView-4 Integration
- Successfully integrated CogView-4 API
- Generated sample images
- Implemented error handling
- Created comprehensive documentation

## 🤝 Contributing

1. Create new project in appropriate category
2. Follow existing project structure
3. Add comprehensive documentation
4. Include examples and tests
5. Update this main README

## 📄 License

This workspace is for experimental and educational purposes. Please respect the terms of service of any third-party APIs used.