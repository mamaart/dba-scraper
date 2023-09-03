# DBA Scraper

This is a scraper for DBA (the blue newspaper - in danish) It is a danish version of ebay, also owned by ebay. 

The scraper is able to fetch information about products given a text from the main page.

For instance to get all furniture in Copenhagen area in the price range of 0 to 100 kroner sorted by newest:

```py
page = requests.get(
    url = 'https://www.dba.dk/til-boligen/spise-og-dagligstuemoebler/',
    params = {
        "reg": "koebenhavn-og-omegn",
        "pris": "(0-100)",
        "sort": "listingdate-desc", # "price", "price-desc" "listingdate"
    },
)
print(json.dumps(scrape_dba_list(page), indent=2))
```

## Extra features

> At the moment the login functionality is not implemented so both extre features does not work.

### Find krak

It is possible to find more information about the seller if they show their phone number. This can be used to get the coordinates to the pickup location _(assuming the sellers address is the pickup location)_

### Send a message


With the send message feature you can send a message about a product automatically.

## TODO

- [ ] Implement login functionality to get send message feature and to be able to get phone numbers from users.
- [ ] Consider reimplementing in golang 
- [ ] Write tests or examples
