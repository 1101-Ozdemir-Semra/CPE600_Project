import subprocess
import pandas as pd

# Function to run tshark command and capture output
def run_tshark(pcap_file, tshark_fields):
    tshark_command = [
        "tshark",
        "-r", pcap_file,
        "-T", "fields"
    ]
    for field in tshark_fields:
        tshark_command.extend(["-e", field])
    
    result = subprocess.run(tshark_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode != 0:
        print(f"Error running tshark: {result.stderr}")
        return None
    
    return result.stdout

# Define the fields you want to extract
fields = [
    "frame.number",
    "frame.time",
    "ip.src",
    "ip.dst",
    "tcp.srcport",
    "tcp.dstport",
    "frame.len"
]

# Path to your pcap file
pcap_file_path = "./Data/Day_1.pcap"

# Output CSV file path
csv_file_path = "./data_day1.csv"

# Run tshark and get the output
output = run_tshark(pcap_file_path, fields)

# Parse the output and save to CSV
if output:
    # Split the output into lines
    lines = output.strip().split("\n")
    
    # Split each line into fields
    data = [line.split("\t") for line in lines]
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=fields)
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)
    
    print(f"Output saved to {csv_file_path}")
