from campaigns import createCamp
from campaigns import readCampaigns
from adsets import createAdset

x = 'yes'
while(x == 'y' or x == 'yes'):
    print('Starting the App:-')
    print('What would you like to do?')
    print('1. Create a Campaign')
    print('2. Create Adset within a Campaign')
    print('3. Create Ad within a Adset')
    print('4. Read Campaign')
    print('5. Read Adset')

    userInput = input('Your Input: ')

    if (userInput == '1' or userInput == 'campaign' or userInput == 'Campaign'):
        print('Creating Campaign')
        campID = createCamp()
        print('Campaign with ID: ', campID, ' created!')

    elif(userInput == '2' or userInput == 'adset' or userInput == 'Adset'):
        print('Creating Adset')
        print('campID: ', campID)
        adSetID = createAdset(campID)
        print('Adset with ID: ', adSetID, 'created!')

    elif(userInput == '3' or userInput == 'Ad' or userInput == 'ad'):
        print('Creating Ad')

    elif(userInput == '4'):
        print('Printing Campaign')
        readCampaigns()

    elif(userInput == '5'):
        print('Printing Adset')
    
    x = input('Would you like to continue(y/n)?')
