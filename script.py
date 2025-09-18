import boto3

# Usando credenciais diretamente (não recomendado para produção)
ec2 = boto3.client(
    'ec2',
    aws_access_key_id='SUA_ACCESS_KEY',
    aws_secret_access_key='SUA_SECRET_KEY',
    region_name='us-east-1'
)

response = ec2.run_instances(
    ImageId='ami-0xxxxxxxxxxxxxx',  # Kali Linux AMI
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)
print("Instância criada:", response['Instances'][0]['InstanceId'])
