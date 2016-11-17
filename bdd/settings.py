CHROME_BINARY="chrome.exe"
FIREFOX_BINARY="firefox.exe"
IE_BINARY="iexplore.exe"
EDGE_BINARY="MicrosoftEdge.exe"

def get_binary_name(browser):
    name = browser.lower()
    if name=="chrome":
        return CHROME_BINARY
    if name=="firefox":
        return FIREFOX_BINARY
    if name == "ie":
        return IE_BINARY
    if name == "edge":
        return EDGE_BINARY