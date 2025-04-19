import boto3
import sys
import os
from PIL import Image
import argparse

def recognize_celebrities(image_path):
    # Initialize the Rekognition client
    rekognition = boto3.client('rekognition')
    
    # Check if file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return
    
    try:
        # Read the image file
        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()
        
        # Call Amazon Rekognition
        response = rekognition.recognize_celebrities(
            Image={'Bytes': image_bytes}
        )
        
        # Process the response
        if 'CelebrityFaces' in response:
            print("\nCelebrities found in the image:")
            print("-" * 50)
            for celebrity in response['CelebrityFaces']:
                name = celebrity['Name']
                confidence = celebrity['MatchConfidence']
                print(f"Name: {name}")
                print(f"Confidence: {confidence:.2f}%")
                print("-" * 50)
        else:
            print("No celebrities were recognized in the image.")
            
        if 'UnrecognizedFaces' in response and response['UnrecognizedFaces']:
            print(f"\nNumber of unrecognized faces: {len(response['UnrecognizedFaces'])}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Recognize celebrities in an image using Amazon Rekognition')
    parser.add_argument('image_path', help='Path to the image file')
    args = parser.parse_args()
    
    recognize_celebrities(args.image_path)

if __name__ == "__main__":
    main() 