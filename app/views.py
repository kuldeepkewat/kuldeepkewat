import dns.resolver
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

'''
def dns_enumeration(request):
    # Set the target domain and record type
    target_domain = request.POST['domain']
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

    # Create a DNS resolver
    resolver = dns.resolver.Resolver()

    for record_type in record_types:
    # Perform DNS lookup for the target domain and record type
        try:
            answers = resolver.resolve(target_domain, record_type)
        except dns.resolver.NoAnswer:
            continue

    # Print the DNS records found
        print(f"DNS records for {target_domain} ({record_type}):")
        for rdata in answers:
            print(rdata)
    return render(request,'result.html', {'result':rdata})
    
    '''

def dns_enumeration(request):
    # Set the target domain and record type
    target_domain = request.POST['domain']
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

    # Create a DNS resolver
    resolver = dns.resolver.Resolver()

    results = []  # To store the results for all record types

    for record_type in record_types:
        # Perform DNS lookup for the target domain and record type
        try:
            answers = resolver.resolve(target_domain, record_type)
        except dns.resolver.NoAnswer:
            continue

        # Append the results to the list
        results.append({
            'target_domain': target_domain,
            'record_type': record_type,
            'answers': [str(rdata) for rdata in answers]
        })

    return render(request, 'result.html', {'results': results})
