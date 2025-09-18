import serial
import boto3
import subprocess
import time

# Conectar ao ATtiny85
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Conectar AWS
ec2 = boto3.client(
    'ec2',
    aws_access_key_id='SUA_ACCESS_KEY',
    aws_secret_access_key='SUA_SECRET_KEY',
    region_name='us-east-1'
)

while True:
    if ser.in_waiting:
        cmd = ser.readline().decode().strip()
        if cmd == "OPEN_KALI_CLOUD":
            print("Criando instância Kali Linux...")
            response = ec2.run_instances(
                ImageId='ami-0xxxxxxxx',  # AMI Kali Linux
                InstanceType='t2.micro',
                MinCount=1,
                MaxCount=1
            )
            instance_id = response['Instances'][0]['InstanceId']
            print(f"Instância criada: {instance_id}")

            # Esperar instância ficar pronta
            waiter = ec2.get_waiter('instance_running')
            waiter.wait(InstanceIds=[instance_id])
            
            # Obter IP público
            desc = ec2.describe_instances(InstanceIds=[instance_id])
            public_ip = desc['Reservations'][0]['Instances'][0]['PublicIpAddress']
            print(f"Acessando instância em: {public_ip}")

            # Abrir terminal SSH interativo
            subprocess.run([
                "ssh", "-i", "kali-key.pem",
                f"kali@{public_ip}"
            ])
