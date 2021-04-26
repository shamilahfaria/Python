#
# Complete the 'subscription_summary' function below.
#

def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: how many months each account purchased
      ad_free_months: how many months each account paid for ad free viewing
      video_on_demand_purchases: how many Videos on Demand each account purchased
    """
    
    print("Welcome to the Ada+ Account Dashboard")
    
# initialize list of customer dictionaries
customer_information = []

# populate customer information with dicts of input information
for i in range(0,3): 
    # first dict key / value will be appended because there is no existing list index there
    customer_information.append({"customer": input("Please enter customer name: ")})
    # further dict key / values can be associated with that iteration's list item
    cumonths_subscribed = int(input(f'Please enter how many months {customer_information[i]["customer"]} has purchased: '))
    
    ad_free_months = int(input(f'Please enter how many months of ad free viewing {customer_information[i]["customer"]} has paid for: '))
    
    video_on_demand_purchases = int(input(f'Please enter how many videos on demand {customer_information[i]["customer"]} has purchased: '))
    
    
# calculate a summary of earnings for each customer
# loop through dicts (use existing loop), pull information, calculate & add to dict 1) months 2) Ad-free, 3)VOD 4) summary 

    months = (cumonths_subscribed//3)*18 + cumonths_subscribed%3*7
    ad_free = ad_free_months*2
    VOD = video_on_demand_purchases*27.99
    summary = months + ad_free + VOD
    
    customer_information[i].update({'months': months, "ad_free": ad_free, "VOD": VOD,"summary": summary})
    
    print(f'{customer_information[i]["customer"]} earned ${summary}.')

# calculate total earnings for all customers 
# loop thru list, for summary keys, sum values, return sum
summary_sum = 0
VOD_adfree = 0
max = 0
customer = ""
for i in range(0,len(customer_information)):
    
    summary_sum += customer_information[i].get("summary")
    VOD_adfree = summary_sum - customer_information[i].get("months")
    if customer_information[i].get("summary") > max:
        max = customer_information[i].get("summary")
        customer = customer_information[i].get("customer")
    
print(f'The total earning for all customers is ${format(summary_sum,".2f")}.')
print(f'The total earned from Ad-Free watching and Videos on Demand is {VOD_adfree}.')
print(f'The most profitable customer is {customer}.')

# calculate from ad free watching + VOD
# loop thru list, for month key, subtract from previous sum, return new value

# corresponding name for max(summary) -- there must be an efficient way to do this 
