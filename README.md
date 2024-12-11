# UpdateGoogleSheet
Take information from ERP system .csv pull and populate it into a dynamic Google Sheet - placed in a 'data' tab so that the other tabs can dynamically populate based on the incoming information.

Used to keep track of Orders that are late in shipment, or have backorders that require representative intervention.

Requires python
Requires libraries;
pygsheets
pandas

Requires a .json account key with [type,project_it,private_key_it,private_key,client_email,client_id,auth_uri,token_uri], and permission from your google account for the key to access (Google Search if need to).
