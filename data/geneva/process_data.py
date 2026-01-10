import json
import os

def process_jsonl_to_data(input_file, output_file):
    """
    Process JSONL file to tab-separated format: sentence \t offset[0] \t event_type
    """
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            data = json.loads(line.strip())
            
            # Get content (sentences)
            content = data.get('content', [])
            
            # Get events
            events = data.get('events', [])
            
            for event in events:
                # Get event type information
                event_type = event.get('type', '')
                
                mentions = event.get('mention', [])
                
                for mention in mentions:
                    # Get sentence id and offset
                    sent_id = mention.get('sent_id', 0)
                    offset = mention.get('offset', [0, 0])
                    
                    # Get the sentence
                    if sent_id < len(content):
                        sentence_data = content[sent_id]
                        tokens = sentence_data.get('tokens', [])
                        # sentence = ' '.join(tokens)
                        sentence = sentence_data.get('sentence', '')
                        
                        # Write in the format: sentence \t offset[0] \t event_type
                        f_out.write(f"{sentence}\t{offset[0]}\t{event_type}\n")

if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Process train.jsonl
    train_input = os.path.join(script_dir, 'train.jsonl')
    train_output = os.path.join(script_dir, 'train_data')
    
    if os.path.exists(train_input):
        print(f"Processing {train_input}...")
        process_jsonl_to_data(train_input, train_output)
        print(f"Saved to {train_output}")
    else:
        print(f"Warning: {train_input} not found")
    
    # Process test.jsonl
    test_input = os.path.join(script_dir, 'test.jsonl')
    test_output = os.path.join(script_dir, 'test_data')
    
    if os.path.exists(test_input):
        print(f"Processing {test_input}...")
        process_jsonl_to_data(test_input, test_output)
        print(f"Saved to {test_output}")
    else:
        print(f"Warning: {test_input} not found")
    
    print("Done!")
