# Site Information Tool

This project built with Python to get information about websites.

**Status**: Development

# Endpoints

All endpoints will return json format.

## /dns

**http verbs: ['POST']**

**Parameters: ['domain']**

It will show dns records. You can extend record types like below:

```python
m_dns.types.append('AAAA')
```

## /port

**http verbs: ['POST']**

**Parameters: ['domain', 'port']**

It will show port status of domain you declared

## /find_admin

**http verbs: ['POST']**

**Parameters: ['domain']**

It will try to find admin panel of website. You can extend panel endpoints like below:

```python
m_admin_finder.endpoints.append('myadmin')
```

## /site_info

**http verbs: ['POST']**

**Parameters: ['domain']**

It will show site info for example:

- cms (Eg: WordPress, Drupal, Discourse)
- status_code
- title
- scripts
- css_list
- links (tag)
- meta

## /cve

**http verbs: ['POST']**

**Parameters: ['keyword']**

It will show CVE results from NVD. Return type will be json like below (search for linux):

```json
{
    "page_count": 234,
    "total": "4,675"
},
{
    "description": "A vulnerability has been identified in Siveillance VMS Video for Android (All versions < V12.1a (2018 R1)), Siveillance VMS Video for iOS (All versions < V12.1a (2018 R1)). Improper certificate validation could allow an attacker in a privileged network position to read data from and write data to the encrypted communication channel between the app and a server. The security vulnerability could be exploited by an attacker in a privileged network position which allows intercepting the communication channel between the affected app and a server (such as Man-in-the-Middle). Furthermore, an attacker must be able to generate a certificate that results for the validation algorithm in a checksum identical to a trusted certificate. Successful exploitation requires no user interaction. The vulnerability could allow reading data from and writing data to the encrypted communication channel between the app and a server, impacting the communication's confidentiality and integrity. At the time of advisory publication no public exploitation of this security vulnerability was known. Siemens confirms the security vulnerability and provides mitigations to resolve the security issue.",
    "publish": "May 03, 2018; 09:29:00 AM -04:00",
    "severity": "\r\n                            (not available)\r\n                        ",
    "title": "CVE-2018-4849",
    "url": "/vuln/detail/CVE-2018-4849"
},
```

## /ip

It will show your local and public IP address.

**http verbs: ['POST']**

**Parameters: no**

## /pwned

It will show have you been pwned.

**http verbs: ['POST']**

**Parameters: ['type => have_i_been_pwned, hacked_emails, password', 'keyword => mail or plaintext password']**

# To-Do

- [ ] Improvement for admin finder
- [x] Improvement for site info
- [ ] Front-end
- [x] Technology checker (Eg: wordpress, ghost, joomla)
- [x] CVE Search
- [x] IP Information
- [x] Have I been Pwned?
- [ ] New ideas