import boto3

access_key = "kja09d868"
secret_key = "0a78sdjf19"
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

def create_keypair(key_pair_name=None):

    if check_keypair_exist(check_key_pair_name=key_pair_name):
        
        return f"keypair {key_pair_name} already exists"

        
    else:

        response = client.create_key_pair(KeyName=key_pair_name,
                                     KeyType='rsa',
                                     KeyFormat='pem',
                                     TagSpecifications=
                                
                                        [
                                            {
                                        'ResourceType': 'key-pair',
                                        'Tags': 
                                                [{
                                                'Key': 'Name',
                                                'Value': key_pair_name
                                                 },
                                                {
                                                'Key': 'Project',
                                                'Value': f'{project_name}'
                                                 },
                                                {
                                                'Key': 'Env',
                                                'Value': f'{project_env}'
                                                 },
                                                {
                                                'Key': 'owner',
                                                'Value': f'{project_owner}'
                                                 }]
                                            }
                                        ] )
        return f"keypair {key_pair_name} created"


create_keypair(key_pair_name=keypair_name)
