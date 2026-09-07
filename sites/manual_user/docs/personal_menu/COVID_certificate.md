# Personal configuration: COVID certificate {: #covid_certificate}

![Section Configuration in the personal menu with the entries Profile, Settings and Password, the entry Profile is selected](assets/pers_menu_profile_v1_de.png){ class="aside-right lightbox"}

![Icon Profile](assets/icon_profile.png)

If administrators have enabled the COVID certificate in the system administration under `Administration > Modules > COVID certificate`, users will find the tab "COVID certificate" under "Profile" in the personal menu. Here you add a new personal COVID certificate or view the status of your existing certificate. The tab appears only in your own profile.

![Turquoise-highlighted tab COVID certificate to the right of the tabs Profile and My visiting card, in the profile of the personal menu](assets/pers_menu_profile_covid_v1_de.png){ class="shadow lightbox" }

!!! info "Important"

    The certificate itself is **not** stored. OpenOlat stores only the date until which the proof is valid.

:octicons-device-camera-video-24: **Video Introduction (German)**: [COVID certificates in OpenOlat](<https://www.youtube.com/embed/863v3ug_QaM>){:target="_blank"}

## Add COVID certificate {: #add_covid_certificate}

Click on "Add new COVID certificate".

Under "Automatically", you scan the QR code of your certificate with "Scan QR code" or upload the certificate with "Upload certificate" as an image or PDF (maximum 10 MB). The validation is done automatically, see [Validation status](#validation_status). The option "Automatically" is only available if administrators have enabled the scanning of COVID certificates.

If automatic adding does **not** work, select "Manually". There you specify the type of certificate (Vaccination, Recovery, PCR test, Antigen Test or Medical Certificate) and the corresponding date. Manually entered data is not validated automatically, see [Validation status](#validation_status).

In both cases you confirm that all the information provided is true. With the option "Send email before certificate expiration", OpenOlat notifies you by email before your certificate expires.

![Card COVID certificate with name and user name, red 3G status display with cross and current time, and the button Add new COVID certificate, in the tab COVID certificate of the profile](assets/Bildschirmfoto 2021-10-01 um 17.01.19.png){ class="shadow lightbox" }

## Validation status {: #validation_status}

In addition to the colour, the status display shows the current time.

### Green

![Green 3G status display with check mark and current time: validated certificate](assets/Bildschirmfoto%202021-10-01%20um%2017.05.13.png){ class="shadow lightbox" }

Your certificate is validated and valid.

### Orange

![Orange 3G status display with question mark and current time: certificate recorded but not yet validated](assets/Bildschirmfoto%202021-10-01%20um%2017.03.01.png){ class="shadow lightbox" }

You have recorded data, but it has not yet been validated.

If you have added your certificate manually, the status is always orange.

Contact the COVID commissioners of your organisation to have your certificate validated or if the automatic capture did not work.

### Red

![Red 3G status display with cross and current time: no valid certificate recorded](assets/Bildschirmfoto%202021-10-01%20um%2017.02.23.png){ class="shadow lightbox" }

No certificate has been recorded, the certificate has expired or the automatic capture of the certificate could not be completed.

First name, last name and date of birth on the certificate must match your user data in OpenOlat, otherwise you will receive a message.

Contact the COVID commissioners of your organisation if you have problems adding your COVID certificate.

## Further information {: #further_information}

[Personal Configuration >](Personal_Configuration.md)<br>
[Profile >](Profile.md)<br>
[Modules: Overview (administration manual) >](../../manual_admin/administration/Modules.md)

**youtube**<br>
[COVID certificates in OpenOlat](<https://www.youtube.com/embed/863v3ug_QaM>)

[To the top of the page ^](#covid_certificate)
