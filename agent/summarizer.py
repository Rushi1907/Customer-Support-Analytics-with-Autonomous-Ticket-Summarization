from transformers import pipeline

# Load the summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_ticket(subject, description):
    text = subject.strip() + ". " + description.strip()
    
    # Hugging Face models have token limits (~1024 tokens for BART)
    if len(text.split()) > 500:
        text = " ".join(text.split()[:500])

    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)[0]['summary_text']
    return summary
