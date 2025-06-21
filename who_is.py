import whois 

domain = input("Enter Domain: ")
domain_info = whois.whois(domain)
for key, value in domain_info.items():
    print(key, ':', value)