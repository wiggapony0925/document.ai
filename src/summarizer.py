import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def summarize_text(text, instruction, style):
    # Create a mapping of styles to language styles
    styles = {
        'Professional': 'Please summarize this in a professional tone.',
        'Funny': 'Please summarize this in a humorous tone.',
        'Gratitude': 'Please summarize this expressing gratitude.'
    }
    
    # Get the language style corresponding to the user-selected style
    style_prompt = styles.get(style, style)
    
    # Generate the prompt for GPT-3 by combining the instruction, style, and text
    prompt = f"{instruction}:\n{style_prompt}\n\n{text}"
    
    # Use OpenAI's GPT-3 to generate the summary
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.3,
      max_tokens=150
    )

    return response.choices[0].text.strip()
