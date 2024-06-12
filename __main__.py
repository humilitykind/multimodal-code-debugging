import argparse
import json
from extract_text import extract_text
from extract_info import extract_info

def main():
    try:
        # Set up argument parsing
        parser = argparse.ArgumentParser(description='Analyze a screenshot containing code and error logs.')
        parser.add_argument('image_path', type=str, help='Path to the screenshot image file')
        args = parser.parse_args()
        
        # Extract text from the image
        text = extract_text(args.image_path)
        print("Extracted Text:\n", text)
        
        # Extract information from the text
        info = extract_info(text)
        
        # Print extracted information
        print("\nExtracted Information:\n")
        print(json.dumps(info, indent=4))

        # Save extracted information to a JSON file
        output_file = 'extracted_info.json'
        with open(output_file, 'w') as f:
            json.dump(info, f, indent=4)
        
        print(f"\nExtracted information saved to {output_file}")
    except Exception as e:
        print(f"Error in main function: {e}")

if __name__ == '__main__':
    main()
