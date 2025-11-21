# CogView-4 Image Generation Demo

## Overview
This project demonstrates how to use the CogView-4 API to generate high-quality images from text prompts. The demo includes a complete Python client with error handling, image downloading, and multiple example prompts.

## Files Created
- `cogview4_demo_fixed.py` - Main demo script with full functionality
- `generate_examples.py` - Simple script to generate example images
- Multiple generated PNG images as examples

## Generated Images
The demo successfully generated the following example images:

1. **test_image_1763742465.png** - A cute kitten sitting on a sunny windowsill
2. **example_image_1_1763742575.png** - Futuristic cityscape with flying cars and neon lights
3. **example_image_1_1763742641.png** - Traditional Chinese landscape painting
4. **generated_image_1_1763742499.png** - Cat on windowsill (first attempt)
5. **generated_image_2_1763742554.png** - Futuristic cityscape
6. **generated_image_3_1763742577.png** - Chinese landscape painting
7. **generated_image_4_1763742601.png** - Japanese garden with cherry blossoms

## API Configuration
- **API Key**: Successfully configured with provided key
- **Model**: cogview-4-250304 (latest version)
- **Image Quality**: Standard (fast generation, ~5-10 seconds)
- **Resolution**: 1024x1024 pixels
- **Watermark**: Enabled (as required by API policy)

## Features Implemented

### CogView4Client Class
- ✅ API authentication with Bearer token
- ✅ Image generation with customizable parameters
- ✅ Automatic image downloading
- ✅ Error handling for network and API issues
- ✅ Content filter information display

### Supported Parameters
- `model`: cogview-4-250304, cogview-4, cogview-3-flash
- `prompt`: Text description of desired image
- `size`: Various resolutions (512px-2048px, divisible by 16)
- `quality`: standard or hd (cogview-4-250304 only)
- `watermark_enabled`: Control watermark presence
- `user_id`: Optional user tracking

### Usage Examples

#### Quick Test
```bash
python3 cogview4_demo_fixed.py test
```

#### Full Demo
```bash
python3 cogview4_demo_fixed.py
```

#### Generate Custom Images
```python
from cogview4_demo_fixed import CogView4Client

client = CogView4Client("your_api_key")
result = client.generate_image(
    prompt="A beautiful sunset over mountains",
    model="cogview-4-250304",
    quality="hd",
    size="1024x1024"
)
```

## API Response Format
```json
{
  "created": 1234567890,
  "data": [
    {
      "url": "https://example.com/generated_image.png"
    }
  ],
  "content_filter": [
    {
      "role": "assistant",
      "level": 1
    }
  ]
}
```

## Requirements
- Python 3.6+
- requests library (`pip3 install requests`)

## Notes
- Images are temporarily hosted for 30 days
- Rate limiting applies (10-second delays between requests)
- Content filtering is automatically applied
- Watermarks are enabled by default for policy compliance

## Success Metrics
- ✅ All test images generated successfully
- ✅ API integration working properly
- ✅ Image downloading functional
- ✅ Error handling robust
- ✅ Multiple prompt examples tested