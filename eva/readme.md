# Raw Data from Questionnaire

1. All replies are stored in [Data Excel File](llm4faas/eva/data.xlsx).
2. Prompt sample for 4 functions are [keyword](llm4faas/eva/keyword-prompt_template.md), [remote-control](llm4faas/eva/remote-control-prompt_template.md).


# Extract Data from Excel and Store to Markdown file
1. run [extract.py](llm4faas/eva/extract.py) for remote-control data and energy data.
2. run [extract-keyword.py](llm4faas/eva/extract-keyword-prompt.py) for keyword data and auto-adapt data.

# Change LLM models and store responses to Python file

## OpenAI API
1. change the OpenAI API key in [line4](scripts/openai_simple_generator.py)
2. change model, temperature, max_tokens in [line 5, 9, 10](scripts/openai_simple_generator.py) respectively.
3. change the prompt directory in [line 12](scripts/openai_simple_generator.py)
4. change output file name in [line 59](scripts/openai_simple_generator.py)
5. run the main() function to generate all user prompts.


## Gemini API
1. run [start_gemini.sh](scripts/start_gemini.sh) to start the Gemini API.
2. GOOGLE API KEY is stored in [env file](.env).
3. the response is stored in [gemini_output.py](gemini_output_file.py)

## Ollama
1. change the model in line 6 of [ollama generator](scripts/ollama_simple_generate.py).
2. change the function prompt directory in line 46 of [ollama generator](scripts/ollama_simple_generate.py).
3. run the main() function for all user prompts.

## Azure OpenAI gpt-3.5-turbo-16k
1. if there is an error about the httpx version, maybe just run the scripts from console.
2. 