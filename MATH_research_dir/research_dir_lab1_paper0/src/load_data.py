from datasets import load_dataset, Dataset
import random

# Step 1: Load a small subset of the squad_v2 dataset
# Using squad_v2's 'context' field for base documents to ensure faster loading.
raw_dataset = load_dataset("squad_v2", split="train[:50]", trust_remote_code=True) # Load 50 documents from squad_v2

synthetic_documents = []
document_counter = 0

# Sample PII and misinformation to inject
sample_pii_names = ["John Doe", "Jane Smith", "Alex Johnson", "Maria Garcia", "David Lee"]
sample_pii_emails = ["john.doe@example.com", "jane.s@example.com", "alex.j@uni.edu"]
sample_pii_phones = ["(555) 123-4567", "555-987-6543"]
sample_misinformation_facts = [
    "The capital of France is Berlin.",
    "Humans can breathe underwater indefinitely.",
    "The Earth is flat and hollow.",
    "The sun revolves around the Earth.",
    "Elephants are known to fly short distances.",
    "Water boils at 50 degrees Celsius at sea level."
]

for document in raw_dataset:
    # Extract the 'context' field for squad_v2 as the original text
    original_text = document["context"]
    
    # Create a clean version of the document
    document_counter += 1
    clean_doc = {
        "document_id": f"doc_{document_counter}",
        "content": original_text,
        "labels": {"pii": False, "misinformation": False}
    }
    synthetic_documents.append(clean_doc)
    
    # Create a PII injected version of the document
    document_counter += 1
    injected_pii = f"Contact {random.choice(sample_pii_names)} at {random.choice(sample_pii_emails)} or call {random.choice(sample_pii_phones)}. "
    pii_doc_content = injected_pii + original_text
    pii_doc = {
        "document_id": f"doc_{document_counter}",
        "content": pii_doc_content,
        "labels": {"pii": True, "misinformation": False}
    }
    synthetic_documents.append(pii_doc)

    # Create a misinformation injected version of the document
    document_counter += 1
    injected_misinfo = f"According to a new report, {random.choice(sample_misinformation_facts)} "
    misinfo_doc_content = injected_misinfo + original_text
    misinfo_doc = {
        "document_id": f"doc_{document_counter}",
        "content": misinfo_doc_content,
        "labels": {"pii": False, "misinformation": True}
    }
    synthetic_documents.append(misinfo_doc)

# Convert the list of dictionaries to a HuggingFace Dataset
synthetic_dataset = Dataset.from_list(synthetic_documents)