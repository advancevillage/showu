<template>
  <div id="app">
    <!-- very important -->
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    data(){
      return {}
    }
  }
</script>

<style>
  * {
    margin: 0;
    padding: 0;
  }
  #app {
    min-height: 720px;
    min-width: 1024px;
    width: 100%;
    height: 100%;
  }
  #container {
    min-height: 720px;
    min-width: 1024px;
    width: 100%;
    height: 100%;
    z-index: 5;
  }
</style>