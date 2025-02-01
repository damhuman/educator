import sys
import json
from datetime import datetime

def convert_to_json(input_file, output_file=None):
    """
    Reads a Markdown or Text file and converts its content into JSON format.

    Args:
        input_file (str): Path to the input file (Markdown or Text).
        output_file (str, optional): If provided, the JSON is written
                                   to this file; otherwise, it is printed.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create JSON structure with metadata
        json_data = {
            "content": content,
            "metadata": {
                "source_file": input_file,
                "conversion_date": datetime.now().isoformat(),
                "file_size_bytes": len(content)
            }
        }
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=4)
            print(f"JSON content written to: {output_file}")
        else:
            print(json.dumps(json_data, indent=4))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check for the required input file argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file> [<output_file.json>]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    convert_to_json(input_file, output_file)
