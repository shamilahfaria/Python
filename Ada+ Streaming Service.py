# Complete the 'subscription_summary' function below.

def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
       
    """
    
    # initialize list of customer dictionaries
    customer_information = []
    max_summary = 0
    summary_sum = 0
    
    # loop through input arrays to populate dicts with individual customer information 
    for i in range(0,len(months_subscribed)): 
        # if i < len(months_subscribed)-1:
        #     # create a new dict in the list 
        #     customer_information.append({})
        
        # calculate a summary of earnings for each customer
        # customer specific
        months = (months_subscribed[i]//3)*18 + months_subscribed[i]%3*7
        ad_free = ad_free_months[i]*2
        VOD = video_on_demand_purchases[i]*27.99
        summary = months + ad_free + VOD

        # dictionary wide
        summary_sum += summary
        max_summary = max(summary, max_summary)

        # add to dictionary
        customer = {'months':months,
        'ad_free': ad_free,
        'VOD': VOD,
        'summary': summary
        }
       
        # append dictionary to list
        customer_information.append(customer)

        # test: customer information was accurately collected    
        # print(customer_information) 
       
   
    print("Welcome to the Ada+ Account Dashboard")
    
    # calculate from ad free watching + VOD    
    VOD_adfree = sum(customer["VOD"] for customer in customer_information) + sum(customer["ad_free"] for customer in customer_information)
    # max_summary = max(summary_list)
    # max_index = [i for i, j in enumerate(summary_list) if j == max_summary]
    
    # finding max index in dict
    max_index = []
    cust_num = 0
    for customer in customer_information:
        cust_num += 1  
        if customer["summary"] == max_summary:
            max_index.append(cust_num)

    # convert each max index item to str for printing later 
    max_index = list(map(str,max_index))

    # print customer-specific information
    for i in range(0,len(customer_information)):
        print(f'\nAccount {i+1} made ${customer_information[i].get("summary"):.2f} total') 
        print(f'>>> ${customer_information[i].get("months"):.2f} from monthly subscription fees') 
        print(f'>>> ${customer_information[i].get("ad_free"):.2f} from Ad-free upgrades')
        print(f'>>> ${customer_information[i].get("VOD"):.2f} from Video on Demand purchases')

    # print dictionary information 
    print(f'\nCombined all accounts made ${summary_sum:.2f} total')
    print(f'Premium content (Ad-free watching and Video on Demand) made ${VOD_adfree:.2f} total\n')
    print(f'${max_summary:.2f} was the most earned by any single account')
    print('The accounts that earned the most were: #' + ', #'.join(max_index))
    
subscription_summary([1,2,2], [1,0,2], [3,0,1])

subscription_summary([13,4,10], [1,2,10], [3,1,3])

subscription_summary([13,10,10], [1,10,10], [3,3,3])

    
# if __name__ == '__main__':    
#     months_subscribed = []
#     ad_free_months = []
#     video_on_demand_purchases = []
    
#     header = input().strip()

#     while header == "months_subscribed:":
#         line = input().strip()
#         try:
#             months_subscribed.append(int(line))
#         except ValueError:
#             header = line

#     while header == "ad_free_months:":
#         line = input().strip()
#         try:
#             ad_free_months.append(int(line))
#         except ValueError:
#             header = line

#     while header == "video_on_demand_purchases:":
#         try:
#             line = input().strip()

#             video_on_demand_purchases.append(int(line))
#         except EOFError:
#             header = None
            
#     subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases)