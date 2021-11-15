# Image Compressor | Algeo02-20003
Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar  
Aljabar Linier dan Geometri  
Kelompok 7  
2021

## General Info
**Image Compressor** is a web application that can be used to reduce the size of images 
submitted by users. Users may upload a picture (.jpg format) from their machine and pick a compression
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
│	├── build
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
   3. install package dependencies by running  
      `cd src/frontend`  
      `npm install`
2. Run the client by running `npm run dev`
3. Open a separate cmd in a same folder (src/frontend), run the server by running `npx json-server --watch img/image.json`
4. Also on a separate cmd in a same folder (src/frontend), Run the API by running  
   `cd ../backend`  
   `python -u api.py`
5. Go to the image compressor website by going to `http://localhost:8080/`

## Note
1. **Click on the RESET button first** before reloading the page, if the image has been uploaded or while the compression is still running.
   If you fail to do so, navigate to `src/frontend/img`, open image.json and delete everything inside a square bracket
   ```"image": [<delete everything here>]```

2. Save the compressed image by Clicking the download button.
3. The `Compress more!` button automatically reloads the page and reset the `image.json` file (The same behaviour that clicking the RESET button do).
