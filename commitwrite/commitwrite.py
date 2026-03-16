import os
import subprocess
import sys

from dotenv import load_dotenv
from groq import Groq


SYSTEM_PROMPT = (
    "You are a git commit message generator. Given a git diff, generate "
    "exactly one conventional commit message. Output only the commit "
    "message. No explanations, no extra text, no quotes."
)
MAX_DIFF_LENGTH = 3000


def load_api_key():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or not api_key.strip():
        print("Error: GROQ_API_KEY not found in .env file")
        sys.exit(1)
    return api_key


def get_staged_diff():
    try:
        result = subprocess.run(
            ["git", "diff", "--staged"],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        print("Error: Not a git repository.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Not a git repository.")
        sys.exit(1)

    diff = result.stdout
    if not diff.strip():
        print("No staged changes found. Run git add first.")
        sys.exit(1)

    if len(diff) > MAX_DIFF_LENGTH:
        print("Warning: Diff truncated to 3000 characters.")
        diff = diff[:MAX_DIFF_LENGTH]

    return diff


def generate_commit_message(api_key, diff):
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": "Generate a commit message for this diff: " + diff,
                },
            ],
        )
    except Exception:
        print("Error: Groq API call failed. Check your API key and internet connection.")
        sys.exit(1)

    return response.choices[0].message.content.strip()


def main():
    api_key = load_api_key()
    diff = get_staged_diff()
    commit_message = generate_commit_message(api_key, diff)
    print(commit_message)


if __name__ == "__main__":
    main()
