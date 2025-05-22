import openai

openai.api_key = ""

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
