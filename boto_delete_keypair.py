import boto3

access_key = "haaja926910"
secret_key = "538191017"
region     = "ap-south-1"

project_name = "zomato"
project_env  = "production"
project_owner= "anitta"
keypair_name = f'{project_name}-{project_env}'


client = boto3.client('ec2',aws_access_key_id=access_key,aws_secret_access_key=secret_key,region_name=region)

def check_keypair_exist(check_key_pair_name=None):

    key_exist = False
    
    description = client.describe_key_pairs()

    for keypair in description['KeyPairs']:
        
        if check_key_pair_name == keypair['KeyName']:

            key_exist = True
            
    if key_exist:

        return True
        
    else:
        
        return False

def delete_keypair(delete_keypair_name=None):

    if check_keypair_exist(check_key_pair_name=delete_keypair_name):

        client = boto3.client('ec2',aws_access_key_id=access_key,aws_secret_access_key=secret_key,region_name=region)

        response = client.delete_key_pair(KeyName=delete_keypair_name)

        print(f"{delete_keypair_name} deleted")
        
    else:

        print(f"{delete_keypair_name} does not exist")
delete_keypair(delete_keypair_name=keypair_name)
