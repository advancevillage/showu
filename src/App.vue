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
  /* paypal */
  /*[data-braintree-id="paypal-button"] {*/
      /*display: none;*/
  /*}*/
  [data-braintree-id="choose-a-way-to-pay"] {
    display: none;
  }
  [data-braintree-id="methods-label"] {
    display: none;
  }
</style>