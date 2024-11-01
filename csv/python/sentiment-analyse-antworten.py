import os
import shutil
from transformers import pipeline

# Define the base directory to search
base_directory = '/home/lucy/Documents/Notes/bachelorarbeit/csv'

def sentiment_analysis_on_answers():
    # Initialize the sentiment analysis pipeline for German
    sentiment_pipeline = pipeline("sentiment-analysis", model="oliverguhr/german-sentiment-bert", tokenizer="oliverguhr/german-sentiment-bert")

    for root, dirs, files in os.walk(base_directory):
        if os.path.basename(root) == 'file':
            for file in files:
                if file.endswith('.txt'):
                    txt_file_path = os.path.join(root, file)
                    process_text_file(txt_file_path, sentiment_pipeline)

    print("Sentiment analysis completed for all files.")

def process_text_file(txt_file_path, sentiment_pipeline):
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
            # Split the content into individual answers
            answers = [answer.strip() for answer in content.strip().split('\n\n') if answer.strip()]

            # Create a directory with the same name as the text file (without .txt)
            question_name = os.path.splitext(os.path.basename(txt_file_path))[0]
            question_dir = os.path.join(os.path.dirname(txt_file_path), question_name)

            # If the directory exists, delete it to overwrite
            if os.path.exists(question_dir):
                shutil.rmtree(question_dir)
            os.makedirs(question_dir, exist_ok=True)

            # Lists to hold answers based on sentiment
            neutral_answers = []
            positive_answers = []
            negative_answers = []

            for answer in answers:
                result = sentiment_pipeline(answer)[0]
                label = result['label']
                if label == 'positive':
                    positive_answers.append(answer)
                elif label == 'negative':
                    negative_answers.append(answer)
                else:
                    neutral_answers.append(answer)

            # Write categorized answers into separate files
            write_answers(os.path.join(question_dir, 'positive.txt'), positive_answers)
            write_answers(os.path.join(question_dir, 'negative.txt'), negative_answers)
            write_answers(os.path.join(question_dir, 'neutral.txt'), neutral_answers)

        print(f"Processed sentiment analysis for: {txt_file_path}")
    except Exception as e:
        print(f"Error processing {txt_file_path}: {e}")

def write_answers(file_path, answers):
    # Overwrite existing files if they exist
    with open(file_path, 'w', encoding='utf-8') as outfile:
        outfile.write('\n\n'.join(answers))

if __name__ == "__main__":
    sentiment_analysis_on_answers()

