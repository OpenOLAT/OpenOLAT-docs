# PayPal Configuration {: #PayPal}

The PayPal payment module allows authors of courses and project groups to charge money to grant access to those resources. Your clients can either pay by credit card or by their PayPal account if they have one. Note that your clients must not have a PayPal account to use this service, a credit card is enough. In the PayPal configuration in the system administration you can configure your PayPal business account information that is used for all payment processes on this system.

In order to use the PayPal payment method you must have a PayPal business account. Such an account can be created at the PayPal website at no cost. Within your PayPal account you can then create the so called API-Credentials. The API-Credentials consist of the API-username, the API-password and the API- signature. Those three security elements must be configured in the PayPal configuration section in the system administration. Below you find more information how to create the API-Credentials at the PayPal website.

## Usage in courses and project groups

In order to publish courses and project groups with payment restrictions you can select the PayPal offer style on the course details page or in the administration section of a project group. Make sure the PayPal module is configured properly in the system administration. You can find more information [here](../../manual_user/learningresources/Access_configuration.md){ class="shadow lightbox" }

!!! warning "Attention"
	Depending on the used currency, the country and the amount PayPal will charge you a transaction fee. The fee will be about 5% of the resource price you define and will be subtracted from the payment made by your clients.

[To the top of the page ^](#PayPal)


## Create the API Credentials

Log into your PayPal business account and make the necessary settings to connect to OpenOlat.

!!! note "Note"
	Please note that we do not maintain instructions for third-party providers. Below you will find the key reference points to help you get oriented. A step-by-step guide may be available in the documentation of the chosen tool.

- [x] Set up online payments in your business account.
- [x] Obtain API credentials.
- [x] Save both the Client ID and the key.
- [x] Make sure the correct currency is set.
- [x] Tip:
  a) "Allow incoming payments in another currency and convert to Swiss francs."
  b) "Avoid duplicate payments."
- [x] Log in to your OpenOlat system with a system administrator account.
  a) Click on the "Administration" tab.
  b) Click on "Payment method" in the navigation on the left, then on "PayPal".
  c) Activate the PayPal module in OpenOlat by switching PayPal on.
  d) Select "PayPal Smart Buttons" as the integration. Only with this variant is it possible to pay by credit card without the buyer having to open a PayPal account.
  e) Select the currency and then enter the "Client ID" and "Client secret" (=key) that you previously saved.

  
[To the top of the page ^](#PayPal)