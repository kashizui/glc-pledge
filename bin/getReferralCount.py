#!/usr/bin/python
import cgi
import json
import pledger

# TODO: provide the real name of the referrer

form = cgi.FieldStorage()
referrer = form.getfirst("referrer")
count = pledger.get_referral_counts(referrer)
response = {
        "count" : count
        }

# Generate JSON response
print "Content-Type: application/json"
print
print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
