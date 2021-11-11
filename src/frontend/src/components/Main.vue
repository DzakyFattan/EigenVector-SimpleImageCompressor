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
    />
    <div v-if="uploadedImage" class="card">
      <div class="compress">Compression rate :</div>
      <input
        class="inputcomprate"
        type="text"
        placeholder="integer (1-9)"
        v-model="ratio"
      />
      <button @click="showresult = true" class="button">Apply</button>
      <div id="preview">
        <img :src="uploadedImage" />
      </div>
      <div v-show="showresult">
        <img src="../assets/Arrow.png" class="imgarrow" />
        <div class="imgpercentage">
          Image pixel difference percentage : {{ percentage }}
        </div>
        <div class="imgtime">Image pixel compression time : {{ time }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:5000";
export default {
  name: "Main",
  data() {
    return {
      url: null,
      ratio: "",
      showresult: false,
      percentage: "20",
      time: "30",
      uploadedImage: "",
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
.button {
  background-color: #4fe4f9;
  color: black;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  position: absolute;
  left: 600px;
  top: 18px;
}
input[type="text"] {
  border: 2px solid;
  width: 2%;
  border-radius: 4px;
  position: absolute;
  left: 350px;
  top: 23px;
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
  top: 550px;
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
  top: 500px;

  font-family: Nunito;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 33px;
  text-align: left;

  color: #000000;
}
</style>