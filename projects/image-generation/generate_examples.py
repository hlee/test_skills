#!/usr/bin/env python3
from cogview4_demo_fixed import CogView4Client
import time

API_KEY = '403c8e79ca7c4d419e05fc6ea5bdc4f8.1ro8LTJBgspzFp2X'
client = CogView4Client(API_KEY)

print('Generating additional example images...')
prompts = [
    'A futuristic cityscape with flying cars and neon lights at sunset',
    '一幅中国传统山水画，有山峰、流水和古松'
]

for i, prompt in enumerate(prompts, 1):
    print(f'\nGenerating image {i}: {prompt}')
    result = client.generate_image(
        prompt=prompt,
        model='cogview-4-250304',
        quality='standard',
        size='1024x1024'
    )
    
    if 'error' in result:
        print(f'Error: {result["error"]}')
        continue
    
    if 'data' in result and len(result['data']) > 0:
        image_url = result['data'][0]['url']
        print(f'Success! URL: {image_url}')
        filename = f'example_image_{i}_{int(time.time())}.png'
        client.download_image(image_url, filename)
    else:
        print('No image data in response')
    
    if i < len(prompts):
        print('Waiting 10 seconds...')
        time.sleep(10)