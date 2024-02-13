import whois

domain = input("Enter your Domain : ")
domain_info = whois.whois(domain)

for key, value in domain_info.items():
    print(f"{key} : {value}")