# AWS Route 53 DNS Migration Script

This Python script is a simple yet powerful solution for migrating DNS records between two AWS accounts. 
It automates the process of transferring DNS records from an AWS Account A's hosted zone to an AWS Account B's 
hosted zone using AWS Route 53. This utility is perfect for those who need to quickly and accurately move DNS 
records between AWS accounts or consolidate infrastructure.

**Note**: If you want to transfer the domain registration from Account A to Account B, you can do so using the 
"Internal Transfer" function available inside Route 53. After the domain registration transfer is complete,
you can use this script to move the DNS records.

## Features

* Transfers DNS records between AWS accounts
* Supports all record types except SOA and NS
* Built using the powerful boto3 library for seamless AWS integration
* Easily customizable to suit your specific needs

## Prerequisites

To use this script, you'll need:

* Python 3.6 or later
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - The AWS SDK for Python
* AWS credentials for both accounts, configured using [AWS CLI](https://aws.amazon.com/cli/) or [AWS SDK](https://aws.amazon.com/sdk-for-python/) configuration files

## Setup

1. Clone this repository or download the script directly.
2. Install the required dependency, boto3, if you haven't already.

```bash
pip install boto3
```

3. Configure your AWS credentials for both accounts A and B using the AWS CLI or SDK.

## Usage

1. Open the script in your favorite text editor or IDE
2. Replace the following placeholder values with your own:
   * `aws_profile_name_account_a` with the AWS profile name for Account A
   * `aws_profile_name_account_b` with the AWS profile name for Account B7
   * `hosted_zone_id_account_a` with the hosted zone ID for Account A
   * `new_hosted_zone_id_account_b` with the new hosted zone ID for Account B
3. Save your changes
4. Run the script from the command line:

```bash
python dns_migration.py
```
 5. You should see the message "DNS records transferred successfully." after the script has completed. 
Verify the transfer by checking the DNS records in the new hosted zone in Account B

## Contributing

Feel free to open an issue or submit a pull request if you'd like to contribute to this project. All contributions are welcome!

## License

This script is released under the MIT License. See the [LICENSE](https://chat.openai.com/LICENSE) file for more information.

