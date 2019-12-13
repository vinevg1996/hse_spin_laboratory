#!/usr/bin/python

#s1 -> s2
#s1
{
  "flows": [
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": true,
      "deviceId": "of:0000000000000001",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "ALL"
          }
        ]
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": "1"
          },
          {
            "type": "ETH_SRC",
            "mac": "9a:d8:73:d8:90:6a"
          },
          {
            "type": "ETH_DST",
            "mac": "ff:ff:ff:ff:ff:ff"
          }
        ]
      }
    }
  ]
}

{
  "flows": [
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": true,
      "deviceId": "of:0000000000000001",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "2"
          }
        ]
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": "1"
          },
          {
            "type": "ETH_SRC",
            "mac": "9a:d8:73:d8:90:6a"
          },
          {
            "type": "ETH_DST",
            "mac": "9a:d8:73:d8:90:6b"
          }
        ]
      }
    }
  ]
}

#s2
{
  "flows": [
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": true,
      "deviceId": "of:0000000000000002",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "ALL"
          }
        ]
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": "2"
          },
          {
            "type": "ETH_SRC",
            "mac": "9a:d8:73:d8:90:6a"
          },
          {
            "type": "ETH_DST",
            "mac": "ff:ff:ff:ff:ff:ff"
          }
        ]
      }
    }
  ]
}

{
  "flows": [
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": true,
      "deviceId": "of:0000000000000002",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "1"
          }
        ]
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": "2"
          },
          {
            "type": "ETH_SRC",
            "mac": "9a:d8:73:d8:90:6a"
          },
          {
            "type": "ETH_DST",
            "mac": "9a:d8:73:d8:90:6b"
          }
        ]
      }
    }
  ]
}

#s2 -> s1
#s2
{
  "flows": [
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": true,
      "deviceId": "of:0000000000000002",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "ALL"
          }
        ]
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": "1"
          },
          {
            "type": "ETH_SRC",
            "mac": "9a:d8:73:d8:90:6b"
          },
          {
            "type": "ETH_DST",
            "mac": "ff:ff:ff:ff:ff:ff"
          }
        ]
      }
    }
  ]
}

{
  "flows": [
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": true,
      "deviceId": "of:0000000000000002",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "2"
          }
        ]
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": "1"
          },
          {
            "type": "ETH_SRC",
            "mac": "9a:d8:73:d8:90:6b"
          },
          {
            "type": "ETH_DST",
            "mac": "9a:d8:73:d8:90:6a"
          }
        ]
      }
    }
  ]
}

#s1
{
  "flows": [
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": true,
      "deviceId": "of:0000000000000001",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "ALL"
          }
        ]
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": "2"
          },
          {
            "type": "ETH_SRC",
            "mac": "9a:d8:73:d8:90:6b"
          },
          {
            "type": "ETH_DST",
            "mac": "ff:ff:ff:ff:ff:ff"
          }
        ]
      }
    }
  ]
}

{
  "flows": [
    {
      "priority": 40000,
      "timeout": 0,
      "isPermanent": true,
      "deviceId": "of:0000000000000001",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "1"
          }
        ]
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": "2"
          },
          {
            "type": "ETH_SRC",
            "mac": "9a:d8:73:d8:90:6b"
          },
          {
            "type": "ETH_DST",
            "mac": "9a:d8:73:d8:90:6a"
          }
        ]
      }
    }
  ]
}
