import subprocess as sp
import os

def LocalMenu():
    print("""
    1.Show IP
    2.List Content of /root
    3.AWS Services
    4.Partition
    5.Hadoop Services
    6.Docker Services
    7.Web Server
    8.Machine learning
    9.Change Preference(Local/menu)
    10.Exit
    """)

def RemoteMenu():
    print("""
    1.Show IP
    2.List Content of /root
    3.AWS Services
    4.Partition
    5.Hadoop Services
    6.Docker Services
    7.Web Server
    8.Change Preference(Local/menu)
    9.Exit
    """)

def dockerMenu():
    print("""
    1.Install Docker And Start Service
    2.Make Service Permanent enable
    3.Download Image
    4.See Downloaded Images
    5.See launched Container
    6.See All Container
    7.Launch Container
    8.Remove Container
    9.Remove All Container
    10.Remove Image
    11.Stop Contaianer
    12.Start Container
    13.Previous Menu
    14.Exit
    """)

def dockerLocalServices():
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Docker Local Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        dockerMenu()
        n=input("Enter your choice:")
        if n=='1:':
            os.system("clear")
            out=sp.getstatusoutput("dnf install docker-ce-18.06.3* --nobets -y")
            if out[0]==0:
                os.system("systemctl start docker")
                print("Docker Installed Successfully and Service started")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='2':
            os.system("clear")
            os.system("systemctl enable docker")
            input("\nPress Enter to Continue")
        elif n=='3':
            os.system("clear")
            image_name=input("Enter Image name to download(name:version):")
            os.system("docker pull %s"%(image_name))
            input("\nPress Enter to Continue")
        elif n=='4':
            os.system("clear")
            os.system("docker images")
            input("\nPress Enter to Continue")
        elif n=='5':
            os.system("clear")
            os.system("docker ps")
            input("\nPress Enter to Continue")
        elif n=='6':
            os.system("clear")
            os.system("docker ps -a")
            input("\nPress Enter to Continue")
        elif n=='7':
            os.system("clear")
            os_name=input("Enter Container name to Launch:")
            im_name=input("Enter Image Name(image:version):")
            out=sp.getstatusoutput("docker run -dit --name %s %s"%(os_name,im_name))
            if out[0]==0:
                print("Container Launched Successfully")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='8':
            os.system("clear")
            os_name=input("Enter Container name to Remove:")
            out=sp.getstatusoutput("docker rm -f %s"%(os_name))
            if out[0]==0:
                print("Container Removed Successfully")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='9':
            os.system("clear")
            confirm=input("Are you sure to remove all container(y/n)?")
            if confirm=='y':
                out=sp.getstatusoutput("docker rm -f $(docker ps -aq)")
                if out[0]==0:
                    print("Successfully Removed all Container")
                else:
                    print(out[1])
            else:
                continue
            input("\nPress Enter to Continue")
        elif n=='10':
            os.system("clear")
            im_name=input("Enter image name(image:version):")
            out=sp.getstatusoutput("docker rmi -f %s"%(im_name))
            if out[0]==0:
                print("Image Removed SuccessFully")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='12':
            os.system("clear")
            os_name=input("Enter os name to start:")
            out=sp.getstatusoutput("docker start %s"%(os_name))
            if out[0]==0:
                print(os_name," Container Started")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='11':
            os.system("clear")
            os_name=input("Enter os name to stop:")
            out=sp.getstatusoutput("docker stop %s"%(os_name))
            if out[0]==0:
                print(os_name," Container Successfully Stopped")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='13':
            break
        elif n=='14':
            exit()
        else:
            os.system('tput setaf 1')
            print("Wrong option selected!!!....Enter Again")
            os.system('tput setaf 7')
            input("\nPress Enter to Continue")
        os.system("clear")


def dockerRemoteServices(user,rip):
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Docker Remote Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        dockerMenu()
        n=input("Enter your choice:")
        if n=='1':
            os.system("clear")
            out=sp.getstatusoutput("ssh %s@%s dnf install docker-ce-18.06.3* --nobets -y"%(user,rip))
            if out[0]==0:
                os.system("ssh %s@%s systemctl start docker"%(user,rip))
                print("Docker Installed Successfully and Service started")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='2':
            os.system("clear")
            os.system("ssh %s@%s systemctl enable docker"%(user,rip))
            input("\nPress Enter to Continue")
        elif n=='3':
            os.system("clear")
            image_name=input("Enter Image name to download(name:version):")
            os.system("ssh %s@%s docker pull %s"%(user,rip,image_name))
            input("\nPress Enter to Continue")
        elif n=='4':
            os.system("clear")
            os.system("ssh %s@%s docker images"%(user,rip))
            input("\nPress Enter to Continue")
        elif n=='5':
            os.system("clear")
            os.system("ssh %s@%s docker ps"%(user,rip))
            input("\nPress Enter to Continue")
        elif n=='6':
            os.system("clear")
            os.system("ssh %s@%s docker ps -a"%(user,rip))
            input("\nPress Enter to Continue")
        elif n=='7':
            os.system("clear")
            os_name=input("Enter Container name to Launch:")
            im_name=input("Enter Image Name(image:version):")
            out=sp.getstatusoutput("ssh %s@%s docker run -dit --name %s %s"%(user,rip,os_name,im_name))
            if out[0]==0:
                print("Container Launched Successfully")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='8':
            os.system("clear")
            os_name=input("Enter Container name to Remove:")
            out=sp.getstatusoutput("ssh %s@%s docker rm -f %s"%(user,rip,os_name))
            if out[0]==0:
                print("Container Removed Successfully")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='9':
            os.system("clear")
            confirm=input("Are you sure to remove all container(y/n)?")
            if confirm=='y':
                out=sp.getstatusoutput("ssh {1}@{0} docker rm -f $(ssh {1}@{0} docker ps -aq)".format(rip,user))
                if out[0]==0:
                    print("Successfully Removed all Container")
                else:
                    print(out[1])
            else:
                continue
            input("\nPress Enter to Continue")
        elif n=='10':
            os.system("clear")
            im_name=input("Enter image name(image:version):")
            out=sp.getstatusoutput("ssh %s@%s docker rmi -f %s"%(user,rip,im_name))
            if out[0]==0:
                print("Image Removed SuccessFully")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='12':
            os.system("clear")
            os_name=input("Enter os name to start:")
            out=sp.getstatusoutput("ssh %s@%s docker start %s"%(user,rip,os_name))
            if out[0]==0:
                print(os_name," Container Started")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='11':
            os.system("clear")
            os_name=input("Enter os name to stop:")
            out=sp.getstatusoutput("ssh %s@%s docker stop %s"%(user,rip,os_name))
            if out[0]==0:
                print(os_name," Container Successfully Stopped")
            else:
                print(out[1])
            input("\nPress Enter to Continue")
        elif n=='13':
            break
        elif n=='14':
            exit()
        else:
            os.system('tput setaf 1')
            print("Wrong option selected!!!....Enter Again")
            os.system('tput setaf 7')
            input("\nPress Enter to Continue")
        os.system("clear")

def LocalWebMenu():
    print("""
    1.Start Services
    2.Stop Services
    3.Edit/Create Web Page
    4.To Copy Web Page
    5.Install Apache Web Server
    6.Previous Menu
    7.Exit
    """)

def LocalWebServices():
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Web Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        LocalWebMenu()
        op=input("Enter your choice: ")
        if op=='1':
            os.system("clear")
            out=os.system("systemctl start httpd")
            if out==0:
                print("Services Started....")
            input("\nPress Enter To Continue: ")
        elif op=='2':
            os.system("clear")
            out=os.system("systemctl stop httpd")
            if out==0:
                print("Services Stopped....")
            input("\nPress Enter To Continue: ")
        elif op=='3':
            while 1:
                os.system("clear")
                os.system('tput setaf 3')
                print("\t\t---------------------------------------")
                print("\t\t\t    Create/Edit Web Page")
                print("\t\t---------------------------------------")
                os.system('tput setaf 7')
                print("""
                1.) To Create/Edit Web page 
                2.) To Create/Edit Backend Page
                3.) Previous Menu""")
                x = input("Enter Your Choice :")
                if x == '1':
                    os.system("clear")
                    file1 = input("Enter web page Name: ")
                    os.system("vi /var/www/html/%s"%file1)
                    input("\nPress Enter To Continue: ")
                elif x == '2':
                    os.system("clear")
                    file1 = input("Enter Backend File Name: ")
                    os.system("vi /var/www/cgi-bin/%s"%file1)
                    os.system("chmod +x /var/www/cgi-bin/%s"%file1)
                    input("\nPress Enter To Continue: ")
                elif int(x) == 3:
                    break
                os.system("clear")
        elif op=='4':
            while 1:
                os.system("clear")
                os.system('tput setaf 3')
                print("\t\t---------------------------------------")
                print("\t\t\t    Copy Web Page")
                print("\t\t---------------------------------------")
                os.system('tput setaf 7')
                print("""
                1. To Copy HTML File
                2: To Copy Backend file
                3: Exit
                """)
                x=input("Enter your choice:")
                if x == '1':
                    os.system("clear")
                    file1 = input("Enter HTML Source File Location")
                    os.system("cp %s /var/www/html"%file1)
                    input("\nPress Enter To Continue: ")
                elif x == '2':
                    os.system("clear")
                    file1 = input("Enter your cgi-bin file location")
                    os.system("cp %s /var/www/cgi-bin"%file1)
                    input("\nPress Enter To Continue: ")
                elif x == '3':
                    break
                os.system("clear")
        elif op=='5':
            os.system("dnf install httpd -y")
        elif op == '6':
            break
        elif op == '7':
            exit()
        os.system("clear")

def RemoteWebMenu():
    print("""
    1.Start Services
    2.Stop Services
    3.Upload Web Page
    4.To Copy Web Page
    5.Install Apache Web Server
    6.Previous Menu
    7.Exit
    """)

def RemoteWebServices(user,rip):
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Remote Web Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        RemoteWebMenu()
        op=input("Enter your choice: ")
        if op=='1':
            os.system("clear")
            out=os.system("ssh %s@%s systemctl start httpd"%(user,rip))
            if out==0:
                print("Services Started....")
            input("\nPress Enter To Continue: ")
        elif op=='2':
            os.system("clear")
            out=os.system("ssh %s@%s systemctl stop httpd"%(user,rip))
            if out==0:
                print("Services Stopped....")
            input("\nPress Enter To Continue: ")
        elif op=='3':
            while 1:
                os.system("clear")
                os.system('tput setaf 3')
                print("\t\t---------------------------------------")
                print("\t\t\t    Upload Web Page")
                print("\t\t---------------------------------------")
                os.system('tput setaf 7')
                print("""
                1.) To Upload Web page 
                2.) To Upload Backend Page
                3.) Previous Menu""")
                x = input("Enter Your Choice :")
                if x == '1':
                    os.system("clear")
                    file1 = input("Enter web page Name: ")
                    os.system("scp %s %s@%s:/var/www/html/"%(file1,user,rip))
                    input("\nPress Enter To Continue: ")
                elif x == '2':
                    os.system("clear")
                    file1 = input("Enter Backend File Name: ")
                    os.system("scp %s %s@%s:/var/www/cgi-bin"%(file1,user,rip))
                    os.system("ssh %s@%s chmod +x /var/www/cgi-bin/%s"%(user,rip,file1))
                    input("\nPress Enter To Continue: ")
                elif int(x) == 3:
                    break
                os.system("clear")
        elif op=='4':
            while 1:
                os.system("clear")
                os.system('tput setaf 3')
                print("\t\t---------------------------------------")
                print("\t\t\t    Copy Web Page")
                print("\t\t---------------------------------------")
                os.system('tput setaf 7')
                print("""
                1. To Copy HTML File
                2: To Copy Backend file
                3: Exit
                """)
                x=input("Enter your choice:")
                if x == '1':
                    os.system("clear")
                    file1 = input("Enter HTML Source File Location")
                    os.system("ssh %s@%s cp %s /var/www/html"%(user,rip,file1))
                    input("\nPress Enter To Continue: ")
                elif x == '2':
                    os.system("clear")
                    file1 = input("Enter your cgi-bin file location")
                    os.system("ssh %s@%s cp %s /var/www/cgi-bin"%(user,rip,file1))
                    input("\nPress Enter To Continue: ")
                elif x == '3':
                    break
                os.system("clear")
        elif op=='5':
            os.system("clear")
            os.system("ssh %s@%s dnf install httpd -y"%(user,rip))
            input("\nPress Enter To Continue: ")
        elif op == '6':
            break
        elif op == '7':
            exit()
        os.system("clear")

def MLMenu():
    print("""
    1.Create Model
    2.Show database
    3.Load Model And Predict Output
    4.Accuracy Prediction
    5.Previous Menu
    6.Exit
    """)

def MLServices():
    import numpy as np
    import pandas as pd
    import joblib
    from sklearn.linear_model import LinearRegression
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    ML Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        MLMenu()
        op=input("Enter Your Choice: ")
        if op=='1':
            os.system("clear")
            fname=input("Enter File To Analyse: ")
            data=pd.read_csv(fname)
            model=LinearRegression()
            area=data['area'].values
            area=area.reshape(-1,1)
            price=data['prices'].values
            price=price.reshape(-1,1)
            print(data)
            pred=input("What to predict? ")
            if pred=='price':
                model.fit(area,price)
            elif pred=='area':
                model.fit(price,area)
            else:
                os.system('tput setaf 3')
                print("Enter right coloumn name!!!!")
                os.system('tput setaf 3')
                break
            print("model coefficient is ",model.coef_)
            mfile=input("Enter the file name to save the created model: ")
            joblib.dump(model,'%s'%mfile)
            input("\nPress Enter To Continue:")
        elif op=='2':
            os.system("clear")
            fname=input("Enter File To See: ")
            data=pd.read_csv('%s'%fname)
            print(data)
            input("\nPress Enter To Continue:")
        elif op=='3':
            os.system("clear")
            data=pd.read_csv("/root/file.csv")
            print(data)
            prd=input("What do you wants to predict? ")
            if prd=='price':
                model=joblib.load("/root/predict_price.pk1")
                value=int(input("Enter area to predict price: "))
                output=model.predict([[value]])
                print("Price for {0}m{1} area is ${2}".format(value,'\u00B2',output))
            elif prd=='area':
                model=joblib.load("/root/predict_area.pk1")
                value=int(input("Enter price to predict area: "))
                output=model.predict([[value]])
                print("Area for ${0} price is {1}m{2}".format(value,output,'\u00B2'))
            else:
                os.system('tput setaf 1')
                print("Wrong Column Selected or Column Doesn't Exist...")
                os.system('tput setaf 7')
            input("\nPress Enter To Continue:")
        elif op=='4':
            os.system("clear")
            fl=input("Enter the csv file path: ")

            data=pd.read_csv(fl)#loading the csv file for creating the model
            area=data['area'].values
            area=area.reshape(-1,1)
            price=data['prices'].values
            price=price.reshape(-1,1)
            filename=input("Enter model name to check accuracy: ")
            if 'price' in filename:
                model=joblib.load(filename)
                print("Accuracy of the model is: ",model.score(area,price))
            elif 'area' in filename:
                model=joblib.load(filename)
                print("Acuracy of the model is: ",model.score(price,area))
            input("\nPress Enter To Continue:")
        elif op=='5':
            break
        elif op=='6':
            exit()
        else:
            os.system('tput setaf 1')
            print("Wrong option Selected....")
            os.system('tput setaf 7')
            input("\nPress Enter To Continue:")
        os.system("clear")

def AWSLocalServices():
    volumes={

    }

    instances={

    }
    subnet={
        "mumbai 1a":"subnet-9eede6f6",
        "mumbai 1b":"subnet-6e651d22",
        "mumbai 1c":"subnet-d2ed6fa9"
    }
    s_group={
        "all traffic":"sg-0e247b3b358604db0",
        "ssh":"sg-0d6b47fe401f699ae",
        "icmp":"sg-01411e283342112a7",
        "default":"sg-54f88e33"
    }
    instance_type={
        "t2 micro":"t2.micro",
        "t2 nano":"t2.nano",
        "t2 small":"t2.small",
        "t2 large":"t2.large",
    }
    Ami={
        "redhat":"ami-052c08d70def0ac62",
        "amazon 2":"ami-001e484a60bb07f8d",
        "windows":"ami-0f438f5108bf5217e",
    }
    keys={
        "default":"kpawanhzb"
    }

    AZ={
        "mumbai 1a":"ap-south-1a",
        "mumbai 1b":"ap-south-1b",
        "mumbai 1c":"ap-south-1c",
    }
    Region={
    "mumbai":"ap-south-1"
    }
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Local AWS Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        AWSMenu()
        n=input("Enter your choice[1-10]:")
        if n=='1':
            os.system("clear")
            print("Availabe Instances are:")
            os.system("aws ec2 describe-instances")
            input("\nPress Enter key to Continue:")
        elif n=='2':
            os.system("clear")
            subnet_name=input("Which Subnet: ")
            subnet_id=subnet.get(subnet_name)
            print("Subnet-id- {}".format(subnet_id))
            ami_name=input("Which AMI: ")
            ami_id=Ami.get(ami_name)
            print("AMI-id- {}".format(ami_id))
            ins_type=input("Instance Type: ")
            count=input("Number of instance: ")
            sg_name=input("Security Group: ")
            sg_id=s_group.get(sg_name)
            print("sg-group: {}".format(sg_id))
            key=input("Keyname: ")
            tag=input("Tag for instance: ")
            tag_value=input("Tag Value for instance: ")
            instance_id=sp.getstatusoutput("aws ec2 run-instances --image-id %s --instance-type %s --subnet-id %s --count %s --security-group-ids %s --key-name %s --tag-specifications \'ResourceType=instance,Tags=[{Key=%s,Value=%s}]\'  --query \'Instances[*].[InstanceId]\' --output text"%(ami_id,ins_type,subnet_id,count,sg_id,key,tag,tag_value))
            if instance_id[0]==0:
                print("Instance Launched")
                instances[tag_value]=instance_id[1]
            else:
                print(instance_id[1])
                print("Something Went wrong")
            input("\nPress Enter key to Continue:")
        elif n=='3':
            os.system("clear")
            az_name=input("Enter Availability zone:")
            az_id=AZ.get(az_name)
            print(az_id)
            sz=int(input("Enter size:"))
            tag=input("Tag for volume: ")
            tag_value=input("Vlaue For Tag:")
            output=sp.getstatusoutput("aws ec2 create-volume --availability-zone %s --size %s --tag-specifications \'ResourceType=volume,Tags=[{Key=%s,Value=%s}]\' --query \'[VolumeId]\' --output text"%(az_id,sz,tag,tag_value))
            if output[0]==0:
                print("volume Created")
                volumes[tag_value]=output[1]
            else:
                print(output[1])
                print("Something went wrong")
            input('Press Enter key to continue:')
        elif n=='4':
            os.system("clear")
            group_name=input("Enter Group Name:")
            desc=input("Enter Description:")
            os.system("aws ec2 create-security-group --description {0} --group-name {1}".format(desc,group_name))
            input('Press Enter key to continue:')
        elif n=='5':
            os.system("clear")
            key_name=input("Enter Key-Name:")
            os.system("aws ec2 create-key-pair --key-name {0}".format(key_name))
            input('Press Enter key to continue:')
        elif n=='6':
            os.system("clear")
            device=input("Device Name(/dev/sd[f-p])")
            vol_name=input("Which Volume to Attach:")
            vol_id=volumes.get(vol_name)
            instance_name=input("Which Instance to Attach:")
            instance_id=instances.get(instance_name)
            os.system("aws ec2 attach-volume --device {0} --instance-id {1} --volume-id {2}".format(device,instance_id,vol_id))
            input('Press Enter key to continue:')
        elif n=='7':
            os.system("clear")
            instance_name=input("Which instance you want to Start:")
            print(instance_name)
            instance_id=instances.get(instance_name)
            print(instance_id)
            print("starting instance {}....".format(instance_name))
            out=os.system("aws ec2 start-instances --instance-ids {0}".format(instance_id))
            if out==0:
                print("Instance Started")
            else:
                print("Some went wrong")
            input("Enter Enter key to continue")
        elif n=='8':
            os.system("clear")
            instance_name=input("Which instance you want to Stop:")
            print(instance_name)
            instance_id=instances.get(instance_name)
            print(instance_id)
            print("stoping instance {}....".format(instance_name))
            out=os.system("aws ec2 stop-instances --instance-ids {0}".format(instance_id))
            if out==0:
                print("Instance Stoped")
            else:
                print("Instance Not found!!!! Please try again")
            input("Press Enter key to continue")
        elif n=='9':
            os.system("clear")
            instance_name=input("Which instance you want to Terminate:")
            print(instance_name)
            instance_id=instances.get(instance_name)
            print(instance_id)
            print("Terminating instance {}....".format(instance_name))
            out=os.system("aws ec2 terminate-instances --instance-ids {0}".format(instance_id))
            if out==0:
                print("Instance Terminated")
            else:
                print("Instance Not found!!!! Please try again")
            input("Enter Enter key to continue")
        elif n=='10':
            break
        elif n=='11':
            exit()
        else:
            os.system('tput setaf 1')
            print("Wrong option selected!!! Try again....")
            os.system('tput setaf 7')
        os.system("clear")

def AWSMenu():
    print("""
    1.See Launched Instances
    2.Launch/Run Insance
    3.Create Volume
    4.Create Security-Group
    5.Create key-pair
    6.Attach Volume to Instance
    7.Start Instance
    8.Stop Instance
    9.Terminate Instance
    10.Previous Menu
    11.Exit
    """)

def AWSRemoteServices(user,rip):
    volumes={

    }

    instances={

    }
    subnet={
        "mumbai 1a":"subnet-9eede6f6",
        "mumbai 1b":"subnet-6e651d22",
        "mumbai 1c":"subnet-d2ed6fa9"
    }
    s_group={
        "all traffic":"sg-0e247b3b358604db0",
        "ssh":"sg-0d6b47fe401f699ae",
        "icmp":"sg-01411e283342112a7",
        "default":"sg-54f88e33"
    }
    instance_type={
        "t2 micro":"t2.micro",
        "t2 nano":"t2.nano",
        "t2 small":"t2.small",
        "t2 large":"t2.large",
    }
    Ami={
        "redhat":"ami-052c08d70def0ac62",
        "amazon 2":"ami-001e484a60bb07f8d",
        "windows":"ami-0f438f5108bf5217e",
    }
    keys={
        "default":"kpawanhzb"
    }

    AZ={
        "mumbai 1a":"ap-south-1a",
        "mumbai 1b":"ap-south-1b",
        "mumbai 1c":"ap-south-1c",
    }
    Region={
    "mumbai":"ap-south-1"
    }

    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Remote AWS Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        AWSMenu()
        n=input("Enter your choice[1-10]:")
        if n=='1':
            os.system("clear")
            print("Availabe Instances are:")
            os.system("ssh %s@%s aws ec2 describe-instances |less"%(user,rip))
            input("\nPress Enter key to Continue:")
        elif n=='2':
            os.system("clear")
            subnet_name=input("Which Subnet: ")
            subnet_id=subnet.get(subnet_name)
            print("Subnet-id- {}".format(subnet_id))
            ami_name=input("Which AMI: ")
            ami_id=Ami.get(ami_name)
            print("AMI-id- {}".format(ami_id))
            ins_type=input("Instance Type: ")
            count=input("Number of instance: ")
            sg_name=input("Security Group: ")
            sg_id=s_group.get(sg_name)
            print("sg-group: {}".format(sg_id))
            key=input("Keyname: ")
            instance_id=sp.getstatusoutput("ssh %s@%s aws ec2 run-instances --image-id %s --instance-type %s --subnet-id %s --count %s --security-group-ids %s --key-name %s --query \'Instances[*].[InstanceId]\' --output text"%(user,rip,ami_id,ins_type,subnet_id,count,sg_id,key))
            if instance_id[0]==0:
                print("Instance Launched")
                #instances[tag_value]=instance_id[1]
            else:
                print(instance_id[1])
                print("Something Went wrong")
            input("\nPress Enter key to Continue:")
        elif n=='3':
            os.system("clear")
            az_name=input("Enter Availability zone:")
            az_id=AZ.get(az_name)
            print(az_id)
            sz=int(input("Enter size:"))
            name=input("Name Tag for volume")
            output=sp.getstatusoutput("ssh %s@%s aws ec2 create-volume --availability-zone %s --size %s --tag-specifications --query \'[VolumeId]\' --output text"%(user,rip,az_id,sz))
            if output[0]==0:
                print("volume Created")
                #volumes[name]=output[1]
            else:
                print(output[1])
                print("Something went wrong")
            input('Press Enter key to continue:')
        elif n=='4':
            os.system("clear")
            group_name=input("Enter Group Name:")
            desc=input("Enter Description:")
            os.system("ssh {0}@{1} aws ec2 create-security-group --description {2} --group-name {3}".format(user,rip,desc,group_name))
            input('Press Enter key to continue:')
        elif n=='5':
            os.system("clear")
            key_name=input("Enter Key-Name:")
            os.system("ssh {0}@{1} aws ec2 create-key-pair --key-name {2}".format(user,rip,key_name))
            input('Press Enter key to continue:')
        elif n=='6':
            os.system("clear")
            device=input("Device Name(/dev/sd[f-p])")
            vol_name=input("Which Volume to Attach:")
            instance_name=input("Which Instance to Attach:")
            print("aws ec2 attach-volume --device {0} --instance-id {1} --volume-id {2}".format(device,instance_name,vol_name))
            input('Press Enter key to continue:')
        elif n=='7':
            os.system("clear")
            instance_name=input("Which instance you want to Start:")
            print(instance_name)
            #instance_id=instances.get(instance_name)
            #print(instance_id)
            print("starting instance {}....".format(instance_name))
            out=os.system("ssh {0}@{1} aws ec2 start-instances --instance-ids {2}".format(user,rip,instance_name))
            if out==0:
                print("Instance Started")
            else:
                print("Some went wrong")
            input("Enter Enter key to continue")
        elif n=='8':
            os.system("clear")
            instance_name=input("Which instance you want to Stop:")
            print(instance_name)
            #instance_id=instances.get(instance_name)
            #print(instance_id)
            print("stoping instance {}....".format(instance_name))
            out=os.system("ssh {0}@{1} aws ec2 stop-instances --instance-ids {2}".format(user,rip,instance_name))
            if out==0:
                print("Instance Stoped")
            else:
                print("Instance Not found!!!! Please try again")
            input("Press Enter key to continue")
        elif n=='9':
            os.system("clear")
            instance_name=input("Which instance you want to Terminate:")
            print(instance_name)
            #instance_id=instances.get(instance_name)
            #print(instance_id)
            print("Terminating instance {}....".format(instance_name))
            out=os.system("ssh {0}@{1} aws ec2 terminate-instances --instance-ids {2}".format(user,rip,instance_name))
            if out==0:
                print("Instance Terminated")
            else:
                print("Instance Not found!!!! Please try again")
            input("Enter Enter key to continue")
        elif n=='10':
            break
        elif n=='11':
            exit()
        else:
            os.system('tput setaf 1')
            print("Wrong option selected!!! Try again....")
            os.system('tput setaf 7')
        os.system("clear")

def PartitionMenu():
    print("""
    1.Show Availabe Disks
    2.Create And Format Partition
    3.Mount Partition
    4.Show Mounted Partitions
    5.Go To Previous Menu
    6.Exit
    """)

def PartitionLocalServices():
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Partition Local Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        PartitionMenu()
        n=input("Enter Your Choice: ")
        if n=='1':
            os.system("clear")
            os.system("fdisk -l |less")
            input("\nPress Enter to Continue:")
        elif n=='2':
            os.system("clear")
            dev_name=input("Enter Device Name: ")
            out=os.system("fdisk %s"%(dev_name))
            if out==0:
                print("Partition Created Successfully")
                part=input("Enter Partition Name:")
                out1=os.system("mkfs.ext4 %s"%(part))
                if out1==0:
                    print("Partition has been created and formated successfully")
                else:
                    print("Something went wrong:")
            else:
                print("Something went wrong")
            input("\nPress Enter to Continue:")
        elif n=='3':
            os.system("clear")
            part=input("Enter Partition Name To Mount: ")
            dr=input("Enter Directory To Mount: ")
            out=os.system("mount %s %s"%(part,dr))
            if out==0:
                print("Partition Mounted Successfully:")
            else:
                print("Something went wrong:")
            input("\nPress Enter to Continue:")
        elif n=='4':
            os.system("clear")
            os.system("df -h")
            input("\nPress Enter to Continue:")
        elif n=='5':
            break
        elif n=='6':
            exit()
        os.system("clear")


def PartitionRemoteServices(user,rip):
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Partition Remote Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        PartitionMenu()
        n=input("Enter Your Choice: ")
        if n=='1':
            os.system("clear")
            os.system("ssh %s@%s fdisk -l |less"%(user,rip))
            input("\nPress Enter to Continue:")
        elif n=='2':
            os.system("clear")
            dev_name=input("Enter Device Name: ")
            out=os.system("ssh %s@%s fdisk %s"%(user,rip,dev_name))
            if out==0:
                print("Partition Created Successfully")
                part=input("Enter Partition Name:")
                out1=os.system("ssh %s@%s mkfs.ext4 %s"%(user,rip,part))
                if out1==0:
                    print("Partition has been created and formated successfully")
                else:
                    print("Something went wrong:")
            else:
                print("Something went wrong")
            input("\nPress Enter to Continue:")
        elif n=='3':
            os.system("clear")
            part=input("Enter Partition Name To Mount: ")
            dr=input("Enter Directory To Mount: ")
            out=os.system("ssh %s@%s mount %s %s"%(user,rip,part,dr))
            if out==0:
                print("Partition Mounted Successfully:")
            else:
                print("Something went wrong:")
            input("\nPress Enter to Continue:")
        elif n=='4':
            os.system("clear")
            os.system("ssh %s@%s df -h"%(user,rip))
            input("\nPress Enter to Continue:")
        elif n=='5':
            break
        elif n=='6':
            exit()
        os.system("clear")

def HadoopMenu():
    print("""
    1.Show status
    2.Configure Master/Slave
    3.Stop Name-Node
    4.Stop Data-Node
    5.Show Data-Node Connected
    7.Change Replication[By Default 3]
    8.Change Block Size[By Default 64MB]
    9.Go to Previous Menu
    10.Exit
    """)

def HadoopLocalServices():
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Hadoop Local Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        HadoopMenu()
        inp=input("Enter your choice:")
        if inp=='1':
            os.system("clear")
            os.system("jps")
            input("\nPress Enter key to Continue:")
        elif inp=='2':
            os.system("clear")
            print("Storage Type(name/data)?",end="")
            stype=input()
            print("Enetr directory:",end="")
            directory=input()
            print("Enter IP Address:",end="")
            ip=input()
            print("Enter Port No.:",end="")
            port=input()
            os.system("""echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
            
<!-- Put site-specific property overrides in this file. -->
            
<configuration>
<property>
<name>dfs.{0}.dir</name>
<value>/{1}</value>
</property>
</configuration>\' > /etc/hadoop/hdfs-site.xml""".format(stype,directory))

            os.system("""echo \'<?xml version=\"1.0\"?>
            
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
            
<!-- Put site-specific property overrides in this file. -->
            
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{0}:{1}</value>
</property>
</configuration>\' > /etc/hadoop/core-site.xml""".format(ip,port))
            if stype=='name':
                os.system("hadoop namenode -format -Y")
                os.system("hadoop-daemon.sh start namenode")
            elif stype=='data':
                os.system("hadoop-daemon.sh start datanode")
            else:
                os.system('tput setaf 1')
                print("Plzz enter write option as name/data")
                os.system('tput setaf 1')
            input("Press Enter key to Continue")
        elif inp=='3':
            os.system("clear")
            os.system("hadoop-daemon.sh stop namenode")
            input("\nPress Enter key to Continue:")
        elif inp=='4':
            os.system("clear")
            os.system("hadoop-daemon.sh stop datanode")
            input("\nPress Enter key to Continue:")
        elif inp=='5':
            os.system("clear")
            os.system("hadoop dfsadmin -report")
            input("\nPress Enter key to Continue:")
        elif inp=='9':
            os.system("clear")
            break
        elif inp=='10':
            exit()
        else:
            os.system('tput setaf 1')
            print("Wrong option selected!!!Try again")
            os.system('tput setaf 7')
            input("\nPress Enter key to Continue:")
        os.system("clear")

def HadoopRemoteServices(user,rip):
    while 1:
        os.system("clear")
        os.system('tput setaf 3')
        print("\t\t---------------------------------------")
        print("\t\t\t    Hadoop Remote Services")
        print("\t\t---------------------------------------")
        os.system('tput setaf 7')
        HadoopMenu()
        inp=input("Enter your choice:")
        if inp=='1':
            os.system("clear")
            os.system("ssh %s@%s jps"%(user,rip))
            input("\nPress Enter key to Continue:")
        elif inp=='2':
            os.system("clear")
            print("Storage Type(name/data)?",end="")
            stype=input()
            print("Enetr directory:",end="")
            directory=input()
            print("Enter IP Address:",end="")
            ip=input()
            print("Enter Port No.:",end="")
            port=input()
            os.system("""echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
            
<!-- Put site-specific property overrides in this file. -->
            
<configuration>
<property>
<name>dfs.{0}.dir</name>
<value>/{1}</value>
</property>
</configuration>\' | ssh {2}@{3} -T \'cat > /etc/hadoop/hdfs-site.xml\'""".format(stype,directory,user,rip))

            os.system("""echo \'<?xml version=\"1.0\"?>
            
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>
            
<!-- Put site-specific property overrides in this file. -->
            
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{0}:{1}</value>
</property>
</configuration>\' | ssh {2}@{3} -T \'cat > /etc/hadoop/core-site.xml\'""".format(ip,port,user,rip))
            if stype=='name':
                os.system("ssh %s@%s hadoop namenode -format -Y"%(user,rip))
                os.system("ssh %s@%s hadoop-daemon.sh start namenode"%(user,rip))
            elif stype=='data':
                os.system("ssh %s@%s hadoop-daemon.sh start datanode"%(user,rip))
            else:
                os.system('tput setaf 1')
                print("Plzz enter write option as name/data")
                os.system('tput setaf 1')
            input("Press Enter key to Continue")
        elif inp=='3':
            os.system("clear")
            os.system("ssh %s@%s hadoop-daemon.sh stop namenode"%(user,rip))
            input("\nPress Enter key to Continue:")
        elif inp=='4':
            os.system("clear")
            os.system("ssh %s@%s hadoop-daemon.sh stop datanode"%(user,rip))
            input("\nPress Enter key to Continue:")
        elif inp=='5':
            os.system("clear")
            os.system("ssh %s@%s hadoop dfsadmin -report"%(user,rip))
            input("\nPress Enter key to Continue:")
        elif inp=='6':
            os.system("clear")
            print("Installing hadoop services")
            input("\nPress Enter key to continue:")
        elif inp=='9':
            break
        elif inp=='10':
            exit()
        else:
            os.system('tput setaf 1')
            print("Wrong option selected!!!Try again")
            os.system('tput setaf 7')
            input("\nPress Enter key to Continue:")
        os.system("clear")

os.system("clear")
os.system('tput setaf 3')
print("\t\t---------------------------------------")
print("\n\t\t\tWelcome to the ARTH")
os.system('tput setaf 7')
while 1:
    os.system('tput setaf 3')
    print("\t\t---------------------------------------")
    print("\t\t\t    Main Menu")
    print("\t\t---------------------------------------")
    os.system('tput setaf 7')
    print("""
    1.Local 
    2.Remote
    3.Exit
    """)
    option=input('Enter your choice:')
    if option=='1':
        while 1:
            os.system("clear")
            os.system('tput setaf 3')
            print("\t\t---------------------------------------")
            print("\t\t\t    Local Services")
            print("\t\t---------------------------------------")
            os.system('tput setaf 7')
            LocalMenu()
            ch=input("Enter your choice:")
            if ch=='1':
                os.system("clear")
                os.system("ifconfig enp0s3")
                input("\nPress Enter key to Continue:")
            elif ch=='2':
                os.system("clear")
                os.system("ls")
                input("\nPress Enter key to Continue:")
            elif ch=='3':
                os.system("clear")
                per=input("Wanna configure for AWS CLI(y/n)?")
                if per=='y':
                    print("aws configure")
                    os.system("aws configure")
                    AWSLocalServices()
                elif per=='n':
                    AWSLocalServices()
                else:
                    os.system('tput setaf 1')
                    print("Please enter (y/n)")
                    os.system('tput setaf 7')
            elif ch=='4':
                PartitionLocalServices()
            elif ch=='5':
                HadoopLocalServices()
            elif ch=='6':
                dockerLocalServices()
            elif ch=='7':
               LocalWebServices()
            elif ch=='8':
                MLServices()
            elif ch=='9':
                break
            elif ch=='10':
                exit()
            else:
                os.system('tput setaf 1')
                print("Wrong option selected!!!Try again")
                os.system('tput setaf 7')
                input("\nPress Enter key to Continue:")
            os.system("clear")
    elif option=='2':
        os.system("clear")
        ip=input("Enter IP of remote system: ")
        user=input("Enter User: ")
        while 1:
            os.system("clear")
            os.system('tput setaf 3')
            print("\t\t---------------------------------------")
            print("\t\t\t    Remote Services")
            print("\t\t---------------------------------------")
            os.system('tput setaf 7')
            RemoteMenu()
            ch=input("Enter your choice:")
            if ch=='1':
                os.system("clear")
                os.system("ssh %s@%s ifconfig enp0s3"%(user,ip))
                input("Press any key to Continue")
            elif ch=='2':
                os.system("clear")
                os.system("ssh %s@%s ls"%(user,ip))
                input("Press any key to Continue")
            elif ch=='3':
                os.system("clear")
                per=input("Wanna configure for AWS CLI(y/n)?")
                if per=='y':
                    os.system("aws configure")
                    AWSRemoteServices(user,ip)
                elif per=='n':
                    AWSRemoteServices(user,ip)
                else:
                    os.system('tput setaf 1')
                    print("Please ENter y/n")
                    os.system('tput setaf 7')
            elif ch=='4':
                PartitionRemoteServices(user,ip)
            elif ch=='5':
                HadoopRemoteServices(user,ip)
            elif ch=='6':
                dockerRemoteServices(user,ip)
            elif ch=='7':
                RemoteWebServices(user,ip)
            elif ch=='8':
                break
            elif ch=='9':
                exit()
            else:
                os.system('tput setaf 1')
                print("Wrong option selected!!!Try again")
                os.system('tput setaf 7')
                input("\nPress Enter key to Continue:")
            os.system("clear")
    elif option=='3':
        break
    else:
        os.system('tput setaf 1')
        print("Wrong option Selected!!!!! Enter Correct Option as 1,2,3....")
        os.system('tput setaf 7')
        input("\nPress Enter key to Continue:")
    os.system("clear")
