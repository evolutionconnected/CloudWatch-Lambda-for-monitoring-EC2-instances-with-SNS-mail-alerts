import json
import boto3


def lambda_handler(event, context):
    # TODO implement

    ec2_cli_obj=boto3.client(service_name="ec2", region_name="us-east-1")
    sns_client_obj=boto3.client(service_name="sns",region_name="us-east-1")

    response = ec2_cli_obj.describe_instances()

    for each_item in (response['Reservations']):
        for each_instance in (each_item['Instances']):
            print(each_instance['InstanceId'],each_instance['State']['Name'])

        if each_instance['State']['Name']=="stopped":
            print("This ec2 instance {} is not in running state now".format(each_instance['InstanceId']))
            sns_client_obj.publish(TargetArn="arn:aws:sns:us-east-1:745931408438:EC2-Mail-Alert",Message="The EC2 instance with id {} is in stopped state now".format(each_instance['InstanceId']),Subject="Instance Stop Alert!!!")
