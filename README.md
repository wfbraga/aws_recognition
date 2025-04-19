# Celebrity Recognition with Amazon Rekognition

This is a Python console application that uses Amazon Rekognition to identify celebrities in images.

## Prerequisites

1. Python 3.6 or higher
2. AWS account with Rekognition access
3. AWS credentials configured on your machine (either through AWS CLI or environment variables)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Configure your AWS credentials:
   - Either set up AWS CLI with `aws configure`
   - Or set the following environment variables:
     - AWS_ACCESS_KEY_ID
     - AWS_SECRET_ACCESS_KEY
     - AWS_DEFAULT_REGION

## Usage

Run the script with the path to an image file as an argument:

```bash
python celebrity_recognition.py path/to/your/image.jpg
```

The script will output:
- Names of recognized celebrities
- Confidence level for each recognition
- Number of unrecognized faces (if any)

## Example Output

```
Celebrities found in the image:
--------------------------------------------------
Name: Tom Hanks
Confidence: 98.50%
--------------------------------------------------
Name: Meryl Streep
Confidence: 95.20%
--------------------------------------------------

Number of unrecognized faces: 2
```

## Notes

- The image should be in a format supported by Amazon Rekognition (JPEG, PNG, etc.)
- The maximum image size is 5MB
- Make sure you have sufficient AWS Rekognition permissions 