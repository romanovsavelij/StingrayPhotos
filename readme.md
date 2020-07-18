# Stringray Photos

Stingray Photos is an api service, written on Django. It is used for uploading pictures in 
[app](https://github.com/Artemut555/StingrayPhotos) for TV platform called Stingray.


## Install

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```shell
$ pip install django
```

## Run

```shell
$ python3 manage.py runserver 8000
```

## Run the tests

```shell
$ python3 manage.py test
```

## Methods

### GetKey
Returns random code

* **URL**

  /get_key

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ key : "8537" }`

### Sign in
Sign in with code, given by app

* **URL**

  /

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ![image](https://user-images.githubusercontent.com/32338211/87860126-8afc3e00-c943-11ea-9f2a-c1f24614187b.png)
    
### Upload menu
View and select files to upload

* **URL**

  /upload/:key

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `key=[integer]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ![image](https://user-images.githubusercontent.com/32338211/87859883-5be4cd00-c941-11ea-8ca6-e1a32b582841.png)   

### Upload files
Upload selected files

* **URL**

  /upload/:key

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   `key=[integer]`

* **Success Response:**

  * **Code:** 200 <br />
  
### Get image
Get uploaded images by your code. Returns one of the uploaded images.
If multiple images where uploaded, they will be returned 
following round-robin strategy.

* **URL**

  /get_image/:key

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `key=[integer]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** Image
