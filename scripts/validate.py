# Desc: Validates assistant files against the schema
import json
import sys
from jsonschema import validate
import os

def validate_assistant(assistant_file):
    print("Validating assistant file: {}".format(assistant_file))
    if not assistant_file.endswith('.json'):
        with open(assistant_file, 'r') as f:
            assistant = json.load(f)

        with open('./schema/v1/assistant.schema.json', 'r') as f:
            schema = json.load(f)

        validate(assistant, schema)

def validate_assistant_file(assistant_file):
    if os.path.isdir(assistant_file):
        for file in os.listdir(assistant_file):
            validate_assistant_file(os.path.join(assistant_file, file))
    else:
        try:
            validate_assistant(assistant_file)
            print("Assistant file is valid.")
        except Exception as e:
            print("Assistant file is invalid.")
            print(e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate.py <assistant_file>")
        sys.exit(1)

    assistant_file = sys.argv[1]
    validate_assistant_file(assistant_file)


