import argparse
import vm_automation

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keyword", help="VM search parameter")
    parser.add_argument("-p1", "--powerOn", help="power on vm before snapshot", action="store_true")
    parser.add_argument("-p0", "--powerOff", help="power off vm before snapshot", action="store_true")
    parser.add_argument("hypervisorConfig", help="json hypervisor config")
    
    args = parser.parse_args()

    hypervisorDic = {}
    vmServer = vm_automation.esxiServer.createFromFile(args.hypervisorConfig, './snapshot.log')
    if vmServer != None:
        vmServer.enumerateVms()
        for vm in vmServer.vmList:
            if (args.keyword == None) or (args.keyword in vm.vmName):
                if args.powerOn:
                    vm.powerOn()
                if args.powerOff:
                    vm.powerOff()
    
if __name__ == "__main__":
    main()
