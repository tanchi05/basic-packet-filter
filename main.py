import random
import time

def gen_random_ip():
    return f"192.168.1.{random.randint(0, 24)}"

def check_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

def main():
  firewall_rules = {
      "192.168.1.1" : "block",
      "192.168.1.3" : "block",
      "192.168.1.11": "block",
      "192.168.1.14": "block",
      "192.168.1.13": "block",
      "192.168.1.23": "block",
      "192.168.1.5": "block",
      "192.168.1.9": "block"
  }

  for i in range(24):
    ip = gen_random_ip()
    action = check_rules(ip,firewall_rules)
    random_number = random.randint(0,9999)
    print(f"{ip} : {action} :{random_number}")
    time.sleep(0.5)

if __name__ == "__main__":
    main()
