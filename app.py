from campaigns import createCamp
from campaigns import readCampaigns
from campaigns import deleteCampaigns
from campaigns import pauseCamp
from campaigns import startCamp
from adsets import createAdset
from adsets import readAdsets
from adsets import deleteAdset
from adsets import pauseAdset
from adsets import startAdset
from ads import adcreate
from ads import readADS
from ads import deleteAd
from ads import pauseAD
from ads import startAd

x = 'yes'
while(x == 'y' or x == 'yes'):
    print('Starting the App:-')
    print('What would you like to do?')
    print('1. Create a Campaign')
    print('2. Create Adset within a Campaign')
    print('3. Create Ad within a Adset')
    print('4. Read Campaign')
    print('5. Read Adset')
    print('6. Read Ad')
    print('7. Delete Campaign')
    print('8. Delete Adset')
    print('9. Delete Ad')
    print('10. Turn Off Campaign')
    print('11. Turn Off Adset')
    print('12. Turn Off Ad')
    print('13. Activate a Campaign')
    print('14. Activate a Adset')
    print('15. Activate a Ad')
        
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
        print('Adset ID: ',adSetID)
        adID = adcreate(adSetID)
        print('Ad with ID: ', adID,' created!')

    elif(userInput == '4'):
        print('Printing Campaign')
        readCampaigns()

    elif(userInput == '5'):
        print('Printing Adset')
        readAdsets()
    
    elif(userInput == '6'):
        print('Previewing Ad')
        readADS()

    elif(userInput == '7'):
        print('Deleting Campaign')
        campIDD = input('Please enter the campaign ID: ')
        deleteCampaigns(campIDD)

    elif(userInput == '8'):
        print('Deleting Adset')
        adSetID = input('Please enter the Adset ID: ')
        deleteAdset(adSetID)
    
    elif(userInput == '9'):
        print('Deleting Ad')
        adIDD = input('Please enter Ad ID you wish to delete:   ')
        deleteAd(adIDD)

    elif(userInput == '10'):
        print('Turning Off Campaign')
        campIDD = input('Please enter the Campaign ID you wish to pause: ')
        pauseCamp(campIDD)
    
    elif(userInput == '11'):
        print('Turning Off Adset')
        adSetID = input('Please enter the Adset ID you wish to pause: ')
        pauseAdset(adSetID)

    elif(userInput == '12'):
        print('Turning Off Ad')
        adID = input('Please enter the Ad ID you wish to pause: ')
        pauseAD(adID)

    elif(userInput == '13'):
        campID = input('CampID: ')
        startCamp(campID)
    
    elif(userInput == '14'):
        adSetID = input('Adset ID: ')
        startAdset(adSetID)

    elif(userInput == '15'):
        adIDD = input('Ad ID: ')
        startAd(adIDD)

    else:
        print('Please select valid options')
    
    x = input('Would you like to continue(y/n)?')
