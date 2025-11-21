# Shared Utilities

This directory contains common utilities, helpers, and configurations that can be used across different projects.

## Structure

### config/
- `api_keys.py` - API key management
- `settings.py` - Global settings
- `constants.py` - Common constants

### utils/
- `http_client.py` - HTTP client utilities
- `file_handler.py` - File operations
- `logger.py` - Logging configuration
- `validators.py` - Input validation
- `image_processor.py` - Image processing utilities

## Usage

### Importing utilities
```python
from shared.utils.http_client import make_request
from shared.config.settings import get_config
from shared.utils.logger import setup_logger
```

### Configuration management
```python
from shared.config.api_keys import get_api_key

api_key = get_api_key('cogview4')
```

## Common Features

### API Key Management
- Secure storage of API keys
- Environment variable support
- Configuration file support

### HTTP Client
- Retry logic
- Error handling
- Rate limiting

### File Handling
- Download utilities
- Upload functionality
- Format conversion

### Logging
- Structured logging
- Multiple output formats
- Log rotation

## Future Enhancements
- [ ] Add caching utilities
- [ ] Implement batch processing
- [ ] Add monitoring and metrics
- [ ] Create test utilities