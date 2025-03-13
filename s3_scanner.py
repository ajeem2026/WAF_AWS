import subprocess
import json

def run_aws_cli(command):
    """Run an AWS CLI command and return JSON output if successful."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {' '.join(command)}: {e.stderr}")
        return None
    except json.JSONDecodeError:
        print("Failed to parse JSON output.")
        return None

def list_buckets():
    command = ['aws', 's3api', 'list-buckets', '--output', 'json']
    data = run_aws_cli(command)
    if data and "Buckets" in data:
        return [bucket['Name'] for bucket in data["Buckets"]]
    return []

def check_public_access_block(bucket_name):
    command = ['aws', 's3api', 'get-public-access-block', '--bucket', bucket_name, '--output', 'json']
    data = run_aws_cli(command)
    if data:
        config = data.get("PublicAccessBlockConfiguration", {})
        # Check if any of the settings that prevent public access are disabled
        if not all(config.get(flag, False) for flag in [
            "BlockPublicAcls", "IgnorePublicAcls", "BlockPublicPolicy", "RestrictPublicBuckets"
        ]):
            return False, config
        else:
            return True, config
    # If there's no configuration, assume it's not secured
    return False, {}

def check_bucket_acl(bucket_name):
    command = ['aws', 's3api', 'get-bucket-acl', '--bucket', bucket_name, '--output', 'json']
    data = run_aws_cli(command)
    if data and "Grants" in data:
        for grant in data["Grants"]:
            grantee = grant.get("Grantee", {})
            # Look for public grantees. This typically is denoted by a URI that indicates "AllUsers"
            if grantee.get("Type") == "Group" and "AllUsers" in grantee.get("URI", ""):
                return False, grant
        return True, None
    return True, None

def scan_buckets():
    buckets = list_buckets()
    if not buckets:
        print("No buckets found or unable to list buckets.")
        return

    issues_found = False
    for bucket in buckets:
        print(f"\nScanning bucket: {bucket}")
        public_access, pac_config = check_public_access_block(bucket)
        acl_secure, insecure_acl = check_bucket_acl(bucket)

        if not public_access:
            issues_found = True
            print("  [!] Public Access Block misconfiguration detected!")
            print(f"      Configuration: {pac_config if pac_config else 'Not Configured'}")
        if not acl_secure:
            issues_found = True
            print("  [!] Bucket ACL allows public access!")
            print(f"      Insecure Grant: {insecure_acl}")
        if public_access and acl_secure:
            print("  [+] Bucket appears secure based on Public Access Block and ACL settings.")

    if not issues_found:
        print("\nNo misconfigurations found.")

if __name__ == "__main__":
    scan_buckets()
