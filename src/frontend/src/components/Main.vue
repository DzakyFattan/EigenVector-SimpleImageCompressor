<template>
<div class="main">
<label for="file-upload" class="custom-file-upload">
    <i class="fa fa-cloud-upload"></i> Upload Image
</label>
<input id="file-upload" type="file" @change="onFileChange" />
  <div v-if="url" class="card">
    <div class="compress">Image compression rate : </div>
    <input class="inputcompress" type="text" v-model="ratio">
    <div id="preview">
    <img :src="url" />
    </div>
    <button @click="showresult=true" class="button">Apply</button>
    <div v-show="showresult">
      <img src="../assets/Arrow.png" class="imgarrow">
      <div class="imgpercentage">Image pixel difference percentage : {{percentage}}</div>
      <div class="imgtime">Image pixel compression time : {{time}}</div>
    
    </div>
  </div>
</div>
</template>

<script>
  export default {
    name:'Main',
    data () {
    return {
       url: null,
       ratio :'',
       showresult : false,
       percentage : '20',
       time: '30',
    }
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    }
  },
}
</script>

<style scoped>
.card {
    box-shadow: inset 0 4px 4px 0 rgba(0, 0, 0, 0.25);
    transition: 0.3s;
    padding: 16px;
    margin-bottom: 20px;
    width: 1256px;
    height:580px;
    left: 92px;
    top: 50px;
    border-radius: 14px;
    border: 1px solid #15D3FD;
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

.compress{
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
  background-color: #4FE4F9;
  color: white;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  position: absolute;
  left: 400px;
  top: 18px;
  
}
input[type=text] {
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
.imgpercentage{
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