import openai

# Function to describe an image using ChatGPT
def describe_image(image_path):
    # Note: Ensure you have the OpenAI API key set as an environment variable
    openai.api_key = "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"

    try:
        # Convert the image to bytes for API processing if needed
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()

        # Provide an initial prompt for ChatGPT to describe the image
        prompt = (
            "You are an expert in image recognition and storytelling. "
            "Based on the visual elements described, write a detailed description of the image. "
            "(Note: This assumes image analysis preprocessing already occurred.)"
        )

        # Simulated preprocessing or manual description input
        image_description = "Input visual details here, or replace this with real preprocessing output."

        # Generate a detailed description using ChatGPT
        response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-3.5-turbo" for a less expensive option
    messages=[
        {"role": "system", "content": "You are an expert in image recognition and storytelling."},
        {"role": "user", "content": "Describe the image based on the following visual details: <insert visual details>."}
    ],
    max_tokens=150,
    temperature=0.7
)


        # Extract and print the description from the response
        description = response.choices[0].text.strip()
        return description

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
image_path = "openai_test.jpg"  # Replace with the path to your image
print(describe_image(image_path))
