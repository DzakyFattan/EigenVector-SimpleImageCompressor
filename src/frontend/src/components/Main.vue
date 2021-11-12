<template>
  <div class="main">
    <label for="file-upload" class="custom-file-upload">
      <i class="fa fa-cloud-upload"></i> Upload Image
    </label>
    <input
      id="file-upload"
      accept="image/*"
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
                    :min="0"
                    :max="9"
                    v-model="range"
            />
      </div>
      <button id="apply" @click="showresult = true" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">Apply</button>
      <div id="preview">
        <img :src="uploadedImage" />
      </div>
      <div v-show="showresult">
        <div id="result">
          <img :src="uploadedImage" />
        </div>
        <img src="../assets/Arrow.png" class="imgarrow" />
        <div class="sizebefore">
          before : {{ before }}
        </div>
        <div class="sizeafter">after : {{ after }}
        </div>
        <div class="imgpercentage">
          Image pixel difference percentage : {{ percentage }}
        </div>
        <div class="imgtime">Image pixel compression time : {{ time }}</div>
        <button class="download"><i class="fa fa-download"></i> Download</button>
</a>
      </div>
    </div>
  </div>
</template>

<script>
import VueSimpleRangeSlider from 'vue-simple-range-slider';
import 'vue-simple-range-slider/dist/vueSimpleRangeSlider.css'
import axios from "axios";
const API_URL = "http://127.0.0.1:5000";
export default {
  name: "Main",
  components: { VueSimpleRangeSlider },
  data() {
    return {
      showresult: false,
      percentage: "",
      time: "",
      uploadedImage: "",
      range: 0,
      before: "",
      after : "",
    };
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      reader.onload = (e) => {
        this.uploadedImage = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    onUploadImage() {
      var params = new FormData();
      params.append("image", this.uploadedImage);
      axios.post(`${API_URL}`, params).then(function (response) {
        console.log(response);
      });
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

.imgarrow {
  position: absolute;
  max-width: 15%;
  top: 200px;
  left: 550px;
}

.imgtime {
  position: absolute;
  left: 70px;
  top: 560px;
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
  top: 520px;

  font-family: Nunito;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 33px;
  text-align: left;

  color: #000000;
}

.sizebefore {
  position: absolute;
  left: 70px;
  top: 470px;
  font-family: Nunito;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 33px;
  text-align: left;

  color: #000000;
}

.sizeafter {
  position: absolute;
  left: 770px;
  top: 470px;
  font-family: Nunito;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 33px;
  text-align: left;

  color: #000000;
}

.download {
  position: absolute;
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 30px;
  cursor: pointer;
  font-size: 20px;
  left: 1050px;
  top: 500px;
}
.download:hover {
  background-color: RoyalBlue;
}
</style>