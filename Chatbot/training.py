import openai
import os

# Retrieve the API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Step 1: Upload file
file = openai.files.create(
    file=open("fine_tune_ready.jsonl", "rb"),
    purpose="fine-tune"
)

# Step 2: Start fine-tune
job = openai.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"
)

print("✅ Fine-tuning started! Job ID:", job.id)
