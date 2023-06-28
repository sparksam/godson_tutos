import os

import requests as req
import math


def sum(n:list):
    assert len(n) > 0
    result = 0
    for i in n:
        result += i
    return result

def multiply(n:list):
    assert len(n) > 0
    result = 1 
    for i in n:
        result *= i
    return result

def division(n:list):
    assert len(n) >= 2
    result = n[0]
    for i in range (1,len(n)):
        result /= n[i]
    return result

def factoriel(n:int):
    result = n
    for i in range(1,n):
        result *= i
    return result

def nfactoriel(n:list):
    result = 0
    for i in n:
        result += factoriel(i)
    return result

#def download_and_save(url:str, file_name:str):
    r = req.get(url, allow_redirects=True, verify=False)
    os.makedirs("downloads", exist_ok=True)
    open(f"downloads/{file_name}", 'wb').write(r.content)

if __name__ == "__main__":
    n = [1,2,3,4,5]
    print(f"{n} summed is {sum(n)}")
    
    n = [4,2,3]  
    print(f"{n} multiplied is {multiply(n)}")

    n = [4,2]  
    print(f"{n} divided is {division(n)}")

    n = 5
    print(f"{n} factored is {factoriel(n)}")

    n = [4,2,3]
    print(f"The sum of the factoriel of {n} is {nfactoriel(n)}")


    #download_and_save("http://google.com/favicon.ico","google.ico")
    #download_and_save("https://localhost:8443/wp-content/themes/twentytwentytwo/assets/images/flight-path-on-transparent-d.png","wordpress_bird.png")
