import os

import requests as req


def sum(a:int, b:int):
    return a + b

def download_and_save(url:str, file_name:str):
    r = req.get(url, allow_redirects=True, verify=False)
    os.makedirs("downloads", exist_ok=True)
    open(f"downloads/{file_name}", 'wb').write(r.content)

if __name__ == "__main__":
    a = 10
    b = 100
    print(f"{a}+{b}={sum(a,b)}")

    download_and_save("http://google.com/favicon.ico","google.ico")
    download_and_save("https://localhost:8443/wp-content/themes/twentytwentytwo/assets/images/flight-path-on-transparent-d.png","wordpress_bird.png")
