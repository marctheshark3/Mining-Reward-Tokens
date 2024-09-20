import re
import pandas as pd

def extract_supported_tokens_table(readme_content):
    # Define the pattern for the Supported Tokens table
    pattern = r"(?s)Supported token list(.+?)###"
    
    # Search for the pattern in the README content
    match = re.search(pattern, readme_content)
    if match:
        # Extract the table content
        table_content = match.group(1).strip()
        return table_content
    else:
        return None

def parse_table(table_content):
    # Split the content into lines
    lines = table_content.split('\n')
    
    # Extract the headers
    headers = lines[0].strip('|').split('|')
    headers = [header.strip() for header in headers]
    
    # Extract the rows
    rows = []
    for line in lines[2:]:
        row = line.strip('|').split('|')
        row = [cell.strip() for cell in row]
        if len(headers) == len(row):
            rows.append(row)
    
    return headers, rows

def main():
    # Read the README file
    with open('README.md', 'r') as file:
        readme_content = file.read()
    
    # Extract the Supported Tokens table
    table_content = extract_supported_tokens_table(readme_content)
    print(table_content)
    
    if table_content:
        headers, rows = parse_table(table_content)
        
        # Print the headers and rows
        print("Headers:", headers)
        for row in rows:
            print("Row:", row)
        df = pd.DataFrame(rows, columns=headers)
        print(df.columns)
        swap_df = df[df['Swap'] == 'True']
        swap_df.to_csv('supported-swap-tokens.csv', index=False)
        df.to_csv('supported-tokens.csv', index=False)
        return df
    else:
        print("Supported Tokens table not found in the README.")
        

if __name__ == "__main__":
    df = main()
