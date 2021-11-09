<template>
  <div class="header">
    <img class="title" src="../assets/Logo.png" alt="IMG Compressor Logo" />
    <div class="header_text">
      This IMG Compressor uses a smart combination of the best optimization and
      lossy compression algorithms to shrink any type of image to the minimum
      possible size while keeping the required level of quality.
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>



<style>
.title {
  position: absolute;
  width: 600px;
  height: 600px;
  left: 39px;
  top: -220px;
}
.header_text {
  text-align: left;
  position: absolute;
  width: 742px;
  height: 129px;
  left: 107px;
  top: 127px;

  font-family: Nunito;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 33px;

  color: #000000;
}
</style>
