# Image Compressor | Algeo01_20003
Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar  
Aljabar Linier dan Geometri  
Kelompok 7  
2021

## General Info
**Image Compressor** is a web application that can be used to reduce the size of images 
submitted by users. Users may upload a picture from their machine and pick a compression
level according to their liking. The compressed image will be available to download
momentarily.

## Project Structure
```
.
├── doc
├── src
│   ├── backend
│   │   ├── img
│   │   │   └── image.jpg
│   │   ├── .flaskenv
│   │   ├── api.py
│   │   ├── img_compress.py
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── svd_matrix.py
│   └── frontend
│       ├── config
│       ├── img
│       ├── src
│       ├── static
│       ├── .babelrc
│       ├── .editorconfig
│       ├── .eslintignore
│       ├── .eslintrc.js
│       ├── .gitignore
│       ├── .postcssrc.js
│       ├── index.html
│       ├── package.json
│       ├── package-lock.json
│       ├── README.md
│       └── vue.config.js
├── test
├── .gitignore
└── README.md
```

## Setup
1. Install the dependencies  
   Assuming you've installed the latest version of Python and npm (if not, guides for it are widely available),
   1. ensure pip is installed by running `python -m ensurepip --upgrade`
   2. install the Python dependencies by running `pip install -r src/backend/requirements.txt`
   3. install Vue CLI by running `npm install vue-cli`
2. Run the client by running `npm run dev`
3. Run the server by running `npx json-server --watch img/image.json`
4. Run the API by running `python -u src/backend/api.py`
