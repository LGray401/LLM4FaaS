import time
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.environ["GOOGLE_API_KEY"]

# Initialize Google API Client
genai.configure(api_key=api_key)

# Define the directory containing the Markdown files
# md_dir = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/remote_control"
# md_dir = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/plans"
# md_dir = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/auto_adapt"
# md_dir = "/Users/minghe/llm4faas/logs_questionnaire_in_Chinese/energy"

md_dir = "/Users/minghe/llm4faas/logs_questionnaire_in_English/remote_control"
# md_dir = "/Users/minghe/llm4faas/logs_questionnaire_in_English/plans"
# md_dir = "/Users/minghe/llm4faas/logs_questionnaire_in_English/auto_adapt"
# md_dir = "/Users/minghe/llm4faas/logs_questionnaire_in_English/energy"

def comment_out_non_code(text):
    lines = text.split('\n')
    in_code_block = False
    result = []
    for line in lines:
        if line.startswith('```python'):
            in_code_block = True
            continue  # Skip this line
        elif line.startswith('```') and in_code_block:
            in_code_block = False
            continue  # Skip this line
        elif in_code_block:
            result.append(line)
        else:
            if line.strip() != '':
                result.append('# ' + line)
            else:
                result.append(line)
    return '\n'.join(result)

# Process each Markdown file in the directory
for filename in os.listdir(md_dir):
    if filename.endswith('.md'):
        md_name = os.path.join(md_dir, filename)
        print(f"Processing file: {md_name}")

        # Upload Markdown file
        md_file = genai.upload_file(path=md_name, display_name="test", mime_type="text/markdown")

        # Generate content using the model
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        response = model.generate_content(
            [
                "",
                md_file,
            ]
        )

        response_text = response.text

        # Define the file path where you want to save the response text
        base_name = os.path.basename(md_name).replace('.md', '')
        output_file_name = f'../../functions_en/gemini_en_functions/gemini_{base_name}_{time.time_ns()}.py'

        # Comment out non-code parts
        commented_response_text = comment_out_non_code(response_text)

        # Write the response text to the file
        with open(output_file_name, "w") as file:
            file.write(commented_response_text)

        print(f'Response text has been saved to {output_file_name}')

        # Delete the uploaded file
        genai.delete_file(name=md_file.name)
        print(f'Deleted file {md_file.display_name}')


# import google.generativeai as genai
# import os
# from dotenv import load_dotenv
#
# # Load environment variables from .env file
# load_dotenv()
# api_key = os.environ["GOOGLE_API_KEY"]
#
# # Initialize Google API Client
# genai.configure(api_key=api_key)
#
# md_name = "/Users/minghe/llm4faas/logs_questionnaire_in_English/plans/plan_1.md"
# md_file = genai.upload_file(path= md_name, display_name="test", mime_type="text/markdown")
#
# model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
# response = model.generate_content(
#     [
#         "",
#         md_file,
#     ]
# )
#
# response_text = response.text
#
# # Define the file path where you want to save the response text
# base_name = os.path.basename(md_name).replace('.md', '')
# output_file_name = f'../../functions_en/testtgemini_{base_name}.py'
#
#
# def comment_out_non_code(text):
#     lines = text.split('\n')
#     in_code_block = False
#     result = []
#     for line in lines:
#         if line.startswith('```python'):
#             in_code_block = True
#             continue  # Skip this line
#         elif line.startswith('```') and in_code_block:
#             in_code_block = False
#             continue  # Skip this line
#         elif in_code_block:
#             result.append(line)
#         else:
#             if line.strip() != '':
#                 result.append('# ' + line)
#             else:
#                 result.append(line)
#     return '\n'.join(result)
#
# # Comment out non-code parts
# commented_response_text = comment_out_non_code(response_text)
#
# # Write the response text to the file
# with open(output_file_name, "w") as file:
#     file.write(commented_response_text)
#
#
# print(f'Response text has been saved to {output_file_name}')
#
# genai.delete_file(name=md_file.name)
# print(f'Deleted file {md_file.display_name}')
