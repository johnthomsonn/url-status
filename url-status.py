import getopt,sys
from pythonping import ping

def get_url_status(url):
    try:
        successful_pings = 0
        response = ping(url, timeout=10, count=5)
        for line in response:
            if "Reply from " in str(line):
                successful_pings += 1
        
        if successful_pings == len(response):
            print("All packets were successful:",url,"is operational")
        elif successful_pings == 0:
            print("Failed to ping " + url + ". looks like " + url + " is down")
        else:
            print("Only " + str(successful_pings) + "/" + str(len(response)) + " packets were successful.",url," is probably up.")
        
        
    except Exception as e:
        print(e)

def run():
    if len(sys.argv) == 1:
        print("Please specify a url with -u or --url or ask for help with -h or --help")
        return

    url = None
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:", ["help","url="])
    except getopt.GetoptError as e:
        print("A flag not recognised. If you need help use the flag -h or --help")
        return

    for opt, arg in opts:
        if opt in ['-h','--help']:
            print("usage: python url-status.py -u/--url <url> ")
            print("for help: python url-status.py -h/--help")
            return
        elif opt in ['-u', '--url']:
            url = arg

    if url != None :
        get_url_status(url)



if __name__ == "__main__":
    run()