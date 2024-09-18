import os
from openai import OpenAI

# Directly placing the token
token = "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"
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def generate_blog_post(details: str):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that writes blog posts."},
        {"role": "user", "content": f"Write a blog post with the following details: {details}"},
    ]

    response = client.chat.completions.create(
        messages=messages,

        model=model_name,
        temperature=0.7,
        max_tokens=1000,
        top_p=1.0,




        
    )

    return response.choices[0].message.content

# Example usage
blog_details = "I want a blog post about the benefits of using AI in healthcare. Discuss the impact on patient care, cost reduction, and future trends."
blog_post = generate_blog_post(blog_details)
print(blog_post)