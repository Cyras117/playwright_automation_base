BASE_URL = 'https://aicontent-dev.venturus.dev.br'

ROUTES = {
    'home':'/pixsee-home'
          }

ALL_BROWSERS_DEVICES = {
    "chrome":{
        "browser":"chromium",
        "channel":"chrome",
        "device":None
    },
    "edge":{
        "browser":"chromium",
        "channel":"msedge",
        "device":None
    },
    "firefox":{
        "browser":"firefox",
        "channel":None,
        "device":None
    },
    "safari":{
        "browser":"webkit",
        "channel":None,
        "device":None
    },
    "iphone":{
        "browser":"webkit",
        "channel":None,
        "device":"iPhone 15"
    },
    "android":{
        "browser":"chromium",
        "channel":"chrome",
        "device":"Galaxy S24"
    }
}
