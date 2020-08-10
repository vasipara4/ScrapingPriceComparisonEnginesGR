# ScrapingPriceComparisonEnginesGR
___
A web scraping script for items of the most popular price comparison engines in Greece (Skroutz, Bestprice)

You set the URLs of your favorite item and your desired price. The script notifies you when the price is smaller than yours.

For this script, you’ll use some Python’s libraries. Type the following in your terminal to install them:
```
 pip3 install requests
 pip3 install beautifulsoup4
 pip install win10toast
```

In the script, you have to replace the default values with yours (lines 7-10). If you don't want to add either a skroutz_url or a bestprice_url, set its value to None.

The results are given through Windows notifications. So, automate your script with Task Scheduler and never miss a drop price!
