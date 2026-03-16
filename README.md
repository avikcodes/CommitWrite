# CommitWrite

> Stop writing commit messages. Let AI do it.

CommitWrite reads your staged git diff and generates 
a clean conventional commit message using Qwen via Groq.
Free, fast, and runs entirely from your terminal.

![demo](Animation.gif)

## How It Works

1. Stage your changes — `git add .`
2. Run — `commitwrite`
3. Copy the message → `git commit -m "..."`

## Installation

pip install -r requirements.txt

## Setup

1. Get a free Groq API key at console.groq.com
2. Copy `.env.example` to `.env`
3. Add your key

## Usage

commitwrite

## Example Output

feat: add initial implementation of commit message generator using Groq API

## Why

Writing commit messages is friction. This removes it.

## Tech

- Python
- Groq API
- llama-3.1-8b-instant

## License

MIT
