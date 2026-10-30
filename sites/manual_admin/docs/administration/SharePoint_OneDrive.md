# SharePoint / OneDrive {: #sharepoint_onedrive}

!!! info "frentix customers"

    For frentix customers, their customer advisor at frentix takes care of the activation.


## SharePoint [:octicons-tag-16:{ title="from Release 19.0.0 (OO-7510)" }](https://track.frentix.com/issue/OO-7510){:target="_blank"} {: #sharepoint}

Only a single Microsoft Azure app is set up for the integration of SSO via Microsoft Entra ID, Microsoft Teams Online Meetings and Microsoft SharePoint integration.

### Requirements

SSO via Microsoft Entra ID (formerly Microsoft Azure AD Authentication) is a prerequisite for using the Microsoft SharePoint integration in OpenOlat. For this, only the corresponding authorization is added in the login app.

!!! tip "Tip"

    As part of this configuration, **Office for the web** can also be activated. However, this setting does not need to be configured in the Microsoft Azure App, but only in the system administration under `Administration > External tools > Document editors`, tab "Office for the web".


### Configuration sequence

1. Creation of Microsoft Azure app registration
2. Addition of authorizations in app registration for SSO via Microsoft Entra ID and for Microsoft SharePoint integration
3. Generation of key / secret for OpenOlat
4. Activation of SSO via Microsoft Azure AD Authentication (Microsoft Entra ID) in OpenOlat
5. As required: Activation of Microsoft SharePoint integration in OpenOlat


### Activation in the OpenOlat administration

You find the configuration in the system administration under:<br>
`Administration > External tools > Microsoft SharePoint / OneDrive`

**Please note:**<br>
SharePoint and OneDrive can be integrated individually and independently of each other.

![Module activation, role selection and lists of allowed and excluded sites and drives of the Microsoft SharePoint / OneDrive integration](assets/sharepoint_config_v1_de.png){ class="shadow lightbox" title="Microsoft SharePoint / OneDrive page in the system administration" }

---

## OneDrive {: #onedrive}

The integration of OneDrive is very similar to SharePoint and can be carried out in the same way as described above.










