import serial
import boto3
import time

# Configuração da porta serial do ATtiny85
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Configuração AWS
ec2 = boto3.client('ec2', region_name='us-east-1')

while True:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        if line == "OPEN_KALI_CLOUD":
            print("Comando recebido! Abrindo Kali Linux...")
            
            # Criar instância EC2 (exemplo genérico)
            response = ec2.run_instances(
                ImageId='ami-0xxxxxxxxxxxxxx', # Kali Linux AMI
                InstanceType='t2.micro',
                MinCount=1,
                MaxCount=1,
                KeyName='sua-chave-aws',
                SecurityGroupIds=['sg-xxxxxxxx'],
                SubnetId='subnet-xxxxxxxx'
            )
            instance_id = response['Instances'][0]['InstanceId']
            print(f"Instância criada: {instance_id}")
