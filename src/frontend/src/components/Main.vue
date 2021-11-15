<template>
  <div class="main">
    <label for="file-upload" class="custom-file-upload">
      <i class="fa fa-cloud-upload"></i> Upload Image
    </label>
    <input
      id="file-upload"
      accept="image/jpeg"
      type="file"
      @change="onFileChange"
      @click="showresult = false"
    />
    <div v-if="uploadedImage" class="card">
      <div class="compress">Compression rate :</div>
      <div class="range">
        <VueSimpleRangeSlider
          style="width: 100px"
          barColor="#15d3fd"
          :default="0"
          :min="1"
          :max="10"
          v-model="range"
        />
      </div>
      <button
        id="apply"
        v-on:click="onUploadImage"
        class="
          mdl-button mdl-js-button
          mdl-button--raised
          mdl-js-ripple-effect
          mdl-button--accent
        "
      >
        Apply
      </button>
      <button
        id="reset"
        v-on:click="reset"
        class="
          mdl-button mdl-js-button
          mdl-button--raised
          mdl-js-ripple-effect
          mdl-button--accent
        "
      >
        Reset
      </button>
      <div v-show="resetClicked">
        <div class="resetClicked">
          Reset! Save to reload!
        </div>
      </div>
      <div id="preview">
        <img :src="uploadedImage" />
      </div>
      <div v-show="showresult">
        <div id="result">
          <img :src="convertedImage" />
        </div>
        <img src="../assets/Arrow.png" class="imgarrow" />
        <div class="imgpercentage">
          Image pixel difference percentage : {{ range * 10 }}%
        </div>
        <div class="imgtime">Image pixel compression time : {{ dur }}</div>
        <button class="compressbtn" @click="reloadPage">
          <i class="fa fa-chevron-circle-right"></i> Compress more!
        </button>
        <button @click="onClick()" class="download"><i class="fa fa-download"></i> Download</button>
      </div>
    </div>
  </div>
</template>

<script>
import VueSimpleRangeSlider from "vue-simple-range-slider";
import "vue-simple-range-slider/dist/vueSimpleRangeSlider.css";
import axios from "axios";
const init_s = 0;
const up_s = 1;
const conv_s = 2;
export default {
  name: "Main",
  components: { VueSimpleRangeSlider },
  data() {
    return {
      showresult: false,
      resetClicked: false,
      uploadStatus: init_s,
      imgFile: "",
      imgUrl: "",
      uploadedImage: "",
      convertedImage: "",
      toJson: "",
      range: 1,
      percentage: "",
      s_time: "",
      f_time: "",
      dur: "",
      before: "",
      after: "",
    };
  },
  methods: {
    onClick() {
              axios({
                    url: this.convertedImage,
                    method: 'GET',
                    responseType: 'blob',
                }).then((response) => {
                     var fileURL = window.URL.createObjectURL(new Blob([response.data]));
                     var fileLink = document.createElement('a');
   
                     fileLink.href = fileURL;
                     fileLink.setAttribute('download', 'img.jpg');
                     document.body.appendChild(fileLink);
   
                     fileLink.click();
                });
    },
    reset() {
      this.time = 0;
      this.uploadStatus = init_s;
      fetch("http://localhost:3000/image/1", {
        method: "DELETE",
      });
      this.resetClicked = true;
    },
    reloadPage() {
      this.reset()
      window.location.reload();
    },
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      this.imgFile = files[0];
      this.createImage(this.imgFile);
    },
    createImage(file) {
      let reader = new FileReader();
      reader.onload = (e) => {
        this.uploadedImage = e.target.result;
      };
      reader.readAsDataURL(file);
      this.uploadStatus = up_s;
    },
    onUploadImage() {
      console.log(this.range);
      const reader = new FileReader();
      reader.readAsDataURL(this.imgFile);
      reader.addEventListener("load", () => {
        this.imgUrl = reader.result;
        this.toJson = {
          'base64': this.imgUrl,
          'percentage': this.range,
          'fileName': this.imgFile.name,
        };
        fetch("http://localhost:3000/image", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.toJson)
        });
      });

      this.getCompImage();
    },
    getCompImage() {
      this.uploadStatus = conv_s;
      this.timer(0);
      axios
        .get("http://localhost:5000/compress",{responseType: 'blob'})
        .then((res) => {
          this.timer(1);
          this.dur = (this.f_time - this.s_time) / 1000;
          this.getFile = res.data;
          console.log(this.getFile);
          const dataRead = new FileReader();
          dataRead.readAsDataURL(this.getFile);
          dataRead.addEventListener("load", () => {
            this.convertedImage = dataRead.result;
            console.log(this.convertedImage);
          });
          this.showresult = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    timer(c) {
      var d = new Date();
      if (c == 0) {
        this.s_time = d.getTime();
      } else if (c == 1) {
        this.f_time = d.getTime();
      }
    },
  },
};
</script>

<style scoped>
.card {
  box-shadow: inset 0 4px 4px 0 rgba(0, 0, 0, 0.25);
  transition: 0.3s;
  padding: 16px;
  margin-bottom: 20px;
  width: 1256px;
  height: 580px;
  left: 92px;
  top: 50px;
  border-radius: 14px;
  border: 1px solid #15d3fd;
  position: absolute;
}
.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-height: 400px;
  max-width: 450px;
  position: absolute;
  left: 70px;
  top: 70px;
}

#result {
  display: flex;
  justify-content: center;
  align-items: center;
}

#result img {
  max-height: 400px;
  max-width: 450px;
  position: absolute;
  left: 770px;
  top: 70px;
}

input[type="file"] {
  display: none;
}
.custom-file-upload {
  border: 1px solid #ccc;
  display: inline-block;
  padding: 6px 12px;
  cursor: pointer;
  position: absolute;
  left: 15px;
}

.main {
  position: absolute;
  width: 1256px;
  height: 641px;
  left: 92px;
  top: 275px;
}

.compress {
  position: absolute;
  left: 70px;

  font-family: Nunito;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 33px;
  text-align: left;

  color: #000000;
}

.range {
  position: absolute;
  left: 280px;
  top: -7px;
}

#apply {
  color: white;

  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  position: absolute;
  left: 400px;
  top: 18px;
}

.resetClicked {
  position: absolute;
  left: 770px;
  top: 18px;
  font-family: Nunito;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 33px;
  text-align: left;

  color: #000000;
}

#reset {
  color: white;

  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  position: absolute;
  left: 600px;
  top: 18px;
}

.imgarrow {
  position: absolute;
  max-width: 15%;
  top: 200px;
  left: 550px;
}

.imgtime {
  position: absolute;
  left: 70px;
  top: 480px;
  font-family: Nunito;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 33px;
  text-align: left;

  color: #000000;
}
.imgpercentage {
  position: absolute;
  left: 70px;
  top: 510px;

  font-family: Nunito;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 33px;
  text-align: left;

  color: #000000;
}

.compressbtn {
  position: absolute;
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 30px;
  cursor: pointer;
  font-size: 20px;
  left: 960px;
  top: 480px;
}
.compressbtn:hover {
  background-color: RoyalBlue;
}

.download {
  position: absolute;
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 30px;
  cursor: pointer;
  font-size: 20px;
  left: 760px;
  top: 480px;
}
.download:hover {
  background-color: RoyalBlue;
}
</style>