import sys

def convert_to_oneline(input_file, output_file=None):
    """
    Reads a Markdown or Text file and converts its content into one line.

    Args:
        input_file (str): Path to the input file (Markdown or Text).
        output_file (str, optional): If provided, the one-line text is written
                                     to this file; otherwise, it is printed.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace newline characters with a space
        oneline = content.replace('\n', ' ')
        # Remove multiple spaces
        oneline = ' '.join(oneline.split())
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(oneline)
            print(f"Converted content written to: {output_file}")
        else:
            print(oneline)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check for the required input file argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file> [<output_file.txt>]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    convert_to_oneline(input_file, output_file)
