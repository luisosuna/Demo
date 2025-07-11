import openai

openai.api_key = "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"

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
