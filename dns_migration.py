import json
import boto3

# Replace these values
aws_profile_name_account_a = 'profile_A'
aws_profile_name_account_b = 'profile_B'
hosted_zone_id_account_a = 'zone_ID_account_A'
new_hosted_zone_id_account_b = 'zone_ID_account_B'

# Initialize a boto3 session for Account A
session_account_a = boto3.Session(profile_name=aws_profile_name_account_a)

# Initialize Route 53 client for Account A
route53_account_a = session_account_a.client('route53')

# Get the DNS records from Account A
response = route53_account_a.list_resource_record_sets(HostedZoneId=hosted_zone_id_account_a)

# Save the DNS records in a variable
dns_records = response['ResourceRecordSets']

# Initialize a boto3 session for Account B
session_account_b = boto3.Session(profile_name=aws_profile_name_account_b)

# Initialize Route 53 client for Account B
route53_account_b = session_account_b.client('route53')

# Iterate over the record sets and create them in the new hosted zone in Account B
for record_set in dns_records:
    if record_set['Type'] not in ('SOA', 'NS'):
        route53_account_b.change_resource_record_sets(
            HostedZoneId=new_hosted_zone_id_account_b,
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'CREATE',
                        'ResourceRecordSet': record_set
                    }
                ]
            }
        )

print("DNS records transferred successfully.")
