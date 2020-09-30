import urllib.request

if __name__ == "__main__":
    x = urllib.request.urlopen('https://www.ya.ru/')
    print(x.read())