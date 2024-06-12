import re
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load a pre-trained model and tokenizer
try:
    model_name = "Salesforce/codet5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
except Exception as e:
    print(f"Error loading model and tokenizer: {e}")

def suggest_changes(code_snippet, error_type):
    try:
        prompt = f"Code Snippet:\n{code_snippet}\n\nError Type: {error_type}\n\nSuggest changes to resolve the error:"
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(inputs['input_ids'], max_length=200, num_return_sequences=1)
        suggestion = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return suggestion
    except Exception as e:
        print(f"Error generating suggestion: {e}")
        return ""

def extract_info(text):
    try:
        ide_pattern = r'IDE:\s*(\w+)'
        language_pattern = r'Language:\s*(\w+)'
        error_type_pattern = r'Error Type:\s*(\w+)'
        code_snippet_pattern = r'Code Snippet:\s*(.*?)(Error|$)'
        file_structure_pattern = r'File Structure:\s*(.*?)(Error|$)'

        ide = re.search(ide_pattern, text)
        language = re.search(language_pattern, text)
        error_type = re.search(error_type_pattern, text)
        code_snippet = re.search(code_snippet_pattern, text, re.DOTALL)
        file_structure = re.search(file_structure_pattern, text, re.DOTALL)

        code_snippet_text = code_snippet.group(1).strip() if code_snippet else None
        error_type_text = error_type.group(1) if error_type else None

        suggested_changes = suggest_changes(code_snippet_text, error_type_text) if code_snippet_text and error_type_text else None

        info = {
            "IDE": ide.group(1) if ide else None,
            "Language": language.group(1) if language else None,
            "Code Snippet": code_snippet_text,
            "Error Type": error_type_text,
            "File Structure": file_structure.group(1).strip() if file_structure else None,
            "Suggested Changes": suggested_changes
        }
        
        return info
    except Exception as e:
        print(f"Error in extracting info: {e}")
        return {}
