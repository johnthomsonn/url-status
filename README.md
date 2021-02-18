# url-status
Pings a specified URL to check the status of the site

### Usage
```
python url-status.py -u [--url] <url>
```
or to view the help
```
python url-status.py -h [--help]
```

### Description
This script pings the given url 5 times and records the number of successful replies. There are 3 outcomes: 
1. All packets are successfull (all contain 'Reply from') 
     * gives a website is operational message. 
1. No packets are successful (none contain 'Reply from')
     * gives a website down message.
1. Some packets are successful (some contain 'Reply from') 
     * gives a website probably up message
