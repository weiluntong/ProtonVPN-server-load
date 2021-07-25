# ProtonVPN-server-load

Alternative to checking https://protonvpn.com/vpn-servers everytime you want to connect to a ProtonVPN server

Uses the ProtonVPN API [here](https://api.protonmail.ch/vpn/logicals)

Servers are restricted based on your plan (free, basic, plus), which corresponds to the Tier value of each server. Tier 0 is free, Tier 1 is basic, Tier 2 is plus.

## Usage:

```py
>>> import vpn_servers as vpns
>>> vpns.find_a_server_in(locations=["US"], tiers=[0])
US-FREE#5: 83%
US-FREE#7: 83%
>>> vpns.find_a_server_in(["JP"], [1,2])
JP#25: 6%
>>> vpns.find_a_server_in(["CH"]) # Switzerland
CH#5: 15%
>>> vpns.find_a_server_in(tiers=[1,2])
HK#1: 0%
HK#2: 0%
US-NY#8: 0%
US-NY#6: 0%
US-NY#7: 0%
US-WA#13: 0%
US-WA#14: 0%
US-WA#15: 0%
US-WA#16: 0%
US-NY#16: 0%
US-NY#17: 0%
US-NY#18: 0%
US-NY#19: 0%
US-NY#20: 0%
US-GA#21: 0%
US-GA#22: 0%
US-GA#23: 0%
US-GA#24: 0%
CA#37: 0%
CA#38: 0%
CA#39: 0%
CA#40: 0%
```

You can get the country codes [here](https://protonvpn.com/vpn-servers)

## Development
### Requirements
- Python Poetry 1.1.7
### Initialization
`poetry install`
### Testing
`poetry run pytest`

