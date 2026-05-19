# Stateless Packet Filter Simulation
A simple python prototype simulating a stateless firewall.

This script processes a simulated continuous stream of network traffic and filters inbound packets based on an Access Control list (ACL) implemented via a blacklisted IP dictionary

## Features
- **Inspection**: Processes inbound packets individually against defined security policies
- **Traffic simulation**: Generates random mock IPV4 traffic to demonstrate active allowing/blocking in real time
Delay time also added for easy following of program execution

## Logic Workflow
* **Traffic Generation**: The system simulates incoming packets by generating random ip addresses
* **Policy checking**: The packet's source IP is extracted and passed to the rule engine
* **Action Execution**: The engine checks the source IP against the blacklisted IPs dictionary.If a match
is found the traffic is denied.If no match is found the traffic is allowed

## How to run
Ensure you have python 3 installed

Execute the script via the terminal
```bash
python3 main.py #For unix based systems

python main.py #For windows
```
