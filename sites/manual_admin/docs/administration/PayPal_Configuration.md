# PayPal Configuration

The PayPal booking module allows authors of courses and project groups to
charge money to grant access to those resources. Your clients can either pay
by credit card or by their PayPal account if they have one. Note that your
client's must not have a PayPal account to use this service, a credit card is
enough. In the PayPal configuration in the system administration you can
configure your PayPal business account information that is used for all
payment processes on this system.

In order to use the PayPal booking method you must have a PayPal business
account. Such an account can be created at the PayPal website at no cost.
Within your PayPal account you can then create the so called API-Credentials.
The API-Credentials consist of the API-username, the API-password and the API-
signature. Those three security elements must be configured in the PayPal
configuration section in the system administration. Below you find more
information how to create the API-Credentials at the PayPal website.

##### Usage in courses and project groups

In order to publish courses and project groups with payment restrictions you
can select the PayPal booking method on the course details page or in the
administration section of a project group. Make sure the PayPal module is
configured properly in the system administration. You can find more
information under

Depending on the used currency, the country and the amount PayPal will charge
you a transaction fee. The fee will be about 5% of the resource price you
define and will be subtracted from the payment made by your clients.

##### Create the API Credentials

Log into your PayPal business account and perform the following steps:

Step 1: select "Profile"|
![](assets/paypalconfig1_en.png)  
---|---  
Step 2: select "My selling tools"|
![](assets/paypalconfig23_en.png)  
Step 3: select "API access"  
Step 4: selection option 2 to request the API-Credentials|
![](assets/paypalconfig4_en.png)  
Step 5: select the method with the API-Signature|
![](assets/paypalconfig56_en.png)  
Step 6: submit the form  
Step 7: copy the API Username, the API Password and the Signature to the
PayPal configuration form in OLAT|
![](assets/paypalconfig7_en.png)  
Step 8: go back in PayPal to step 2 and select "Block payments" in the selling
tools| ![](assets/paypalconfig8_en.png)  
Step 9: select the option "No, accept them and convert" for the configuration
"Block payments sent to me in a currency I do not hold" Step 10: Don't forget
to save| ![](assets/paypalconfig910_en.png)

