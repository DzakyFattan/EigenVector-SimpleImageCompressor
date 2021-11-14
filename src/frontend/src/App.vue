<template>
  <div id="App">
    <Header />
    <Footer />
    <router-view />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import Main from "./components/Main.vue";
import Compress from "./components/Compress.vue";
export default {
  name: "App",
  components: {
    Header,
    Footer,
    Main,
    Compress,
  },
  data() {
    return {};
  },
  provide() {
    return {};
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
