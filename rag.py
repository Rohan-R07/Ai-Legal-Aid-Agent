import os

def load_law_context(issue_type: str) -> str:
    """
    Loads the legal context from a text file based on the issue type.

    Args:
        issue_type (str): The category of the legal issue (e.g., "consumer", "employment").

    Returns:
        str: The content of the corresponding text file.
    """
    # Define the path to the data directory
    data_dir = "data"
    
    # Sanitize the issue_type to create a valid filename
    # For example, "Consumer Law" -> "consumer_law.txt"
    filename = f"{issue_type.lower().replace(' ', '_')}.txt"
    filepath = os.path.join(data_dir, filename)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "No specific legal context found for this issue type. Please provide a general response."
    except Exception as e:
        return f"An error occurred while loading the legal context: {e}"

