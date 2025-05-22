import json

input_file = "stackoverflow_qna.jsonl"
output_file = "fine_tune_ready.jsonl"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        data = json.loads(line)
        
        for answer in data["answers"]:
            answer_content = data["answers"]["body"]

            messages = [
                {"role": "user", "content": f"{data['question']}"},
                {"role": "assistant", "content": answer_content},
            ]

        json.dump({"messages": messages}, outfile)
        outfile.write("\n")
