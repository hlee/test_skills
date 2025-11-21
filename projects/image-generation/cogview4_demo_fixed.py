#!/usr/bin/env python3
"""
CogView-4 Image Generation Demo

This script demonstrates how to use the CogView-4 API to generate images from text prompts.
It supports multiple models: cogview-4-250304, cogview-4, and cogview-3-flash.
"""

import requests
import json
import time
import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class CogView4Client:
    def __init__(self, api_key: str):
        """
        Initialize the CogView-4 client.
        
        Args:
            api_key (str): Your API key from BigModel.cn
        """
        self.api_key = api_key
        self.base_url = "https://open.bigmodel.cn/api/paas/v4/images/generations"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def generate_image(
        self,
        prompt: str,
        model: str = "cogview-4-250304",
        size: str = "1024x1024",
        quality: str = "standard",
        watermark_enabled: bool = True,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate an image from text prompt.
        
        Args:
            prompt (str): Text description of the desired image
            model (str): Model to use (cogview-4-250304, cogview-4, cogview-3-flash)
            size (str): Image size (default: 1024x1024)
            quality (str): Image quality (standard or hd, only for cogview-4-250304)
            watermark_enabled (bool): Whether to add watermark
            user_id (str, optional): Unique user ID for tracking
        
        Returns:
            Dict containing the API response
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "size": size,
            "watermark_enabled": watermark_enabled
        }
        
        # Only add quality parameter for cogview-4-250304
        if model == "cogview-4-250304":
            payload["quality"] = quality
        
        if user_id:
            payload["user_id"] = user_id
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}
        except json.JSONDecodeError as e:
            return {"error": f"JSON decode error: {str(e)}"}
    
    def download_image(self, image_url: str, filename: str) -> bool:
        """
        Download generated image to local file.
        
        Args:
            image_url (str): URL of the generated image
            filename (str): Local filename to save the image
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            response = requests.get(image_url, timeout=30)
            response.raise_for_status()
            
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            print(f"Image downloaded successfully: {filename}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image: {str(e)}")
            return False

def main():
    """Main demo function."""
    # Your API key
    API_KEY = os.getenv("COGVIEW4_API_KEY")
    
    if not API_KEY:
        print("Error: COGVIEW4_API_KEY not found in environment variables.")
        print("Please set it in your .env file or as an environment variable.")
        return
    
    # Initialize client
    client = CogView4Client(API_KEY)
    
    # Example prompts
    prompts = [
        "一只可爱的小猫咪，坐在阳光明媚的窗台上，背景是蓝天白云",
        "A futuristic cityscape with flying cars and neon lights at sunset",
        "一幅中国传统山水画，有山峰、流水和古松",
        "A serene Japanese garden with cherry blossoms in spring"
    ]
    
    print("CogView-4 Image Generation Demo")
    print("=" * 50)
    
    # Generate images for each prompt
    for i, prompt in enumerate(prompts, 1):
        print(f"\nGenerating image {i}/{len(prompts)}")
        print(f"Prompt: {prompt}")
        
        # Generate image
        result = client.generate_image(
            prompt=prompt,
            model="cogview-4-250304",
            quality="standard",
            size="1024x1024",
            watermark_enabled=True
        )
        
        if "error" in result:
            print(f"Error: {result['error']}")
            continue
        
        if "data" in result and len(result["data"]) > 0:
            image_url = result["data"][0]["url"]
            created_time = result.get("created", int(time.time()))
            
            print(f"Image generated successfully!")
            print(f"Image URL: {image_url}")
            print(f"Created at: {time.ctime(created_time)}")
            
            # Download image
            filename = f"generated_image_{i}_{int(time.time())}.png"
            client.download_image(image_url, filename)
            
            # Show content filter info if available
            if "content_filter" in result:
                for filter_info in result["content_filter"]:
                    role = filter_info.get("role", "unknown")
                    level = filter_info.get("level", "N/A")
                    print(f"Content filter - {role}: level {level}")
        else:
            print("No image data in response")
        
        print("-" * 50)
        
        # Add delay between requests to avoid rate limiting
        if i < len(prompts):
            print("Waiting 10 seconds before next request...")
            time.sleep(10)

def test_single_image():
    """Test function to generate a single image quickly."""
    API_KEY = os.getenv("COGVIEW4_API_KEY")
    
    if not API_KEY:
        print("Error: COGVIEW4_API_KEY not found in environment variables.")
        print("Please set it in your .env file or as an environment variable.")
        return
    
    client = CogView4Client(API_KEY)
    
    print("Testing single image generation...")
    
    # Simple test prompt
    prompt = "一只可爱的小猫咪，坐在阳光明媚的窗台上"
    
    result = client.generate_image(
        prompt=prompt,
        model="cogview-4-250304",
        quality="standard",
        size="1024x1024"
    )
    
    if "error" in result:
        print(f"Error: {result['error']}")
        return
    
    if "data" in result and len(result["data"]) > 0:
        image_url = result["data"][0]["url"]
        print(f"Success! Image URL:
