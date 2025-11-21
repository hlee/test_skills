# Image Generation Projects

This directory contains projects related to AI-powered image generation.

## Current Projects

### CogView-4 Demo
- **Files**: `cogview4_demo_fixed.py`, `generate_examples.py`, `cogview-4.md`
- **Description**: Complete Python client for CogView-4 API with demo examples
- **Features**: 
  - Multiple model support (cogview-4-250304, cogview-4, cogview-3-flash)
  - Automatic image downloading
  - Error handling and content filtering
  - Customizable parameters (quality, size, watermarks)

## Usage

### Quick Start
```bash
cd projects/image-generation
python3 cogview4_demo_fixed.py test
```

### Full Demo
```bash
python3 cogview4_demo_fixed.py
```

### Custom Generation
```python
from cogview4_demo_fixed import CogView4Client

client = CogView4Client("your_api_key")
result = client.generate_image(
    prompt="A beautiful sunset over mountains",
    model="cogview-4-250304"
)
```

## Requirements
- Python 3.6+
- requests library (`pip install requests`)

## Future Projects
- [ ] DALL-E integration
- [ ] Midjourney API client
- [ ] Stable Diffusion implementation
- [ ] Image-to-image translation
- [ ] Style transfer experiments