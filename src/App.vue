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
  .modal-background {
    background-color: rgba(10, 10, 10, 0.3);
  }
  input:focus {
    border: none;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
  /*swiper global css*/
  .swiper-pagination {
    bottom: 0;
    width: 100%;
  }
  .swiper-pagination-bullet {
    width: 20px;
    height: 20px;
    text-align: center;
    line-height: 20px;
    font-size: 12px;
    color:#000;
    opacity: 1;
    background: rgba(0,0,0,0.2);
  }
  .swiper-pagination-bullet-active {
    color:#fff;
    background: #007aff;
  }
  /* buefy steps */
  .b-steps .steps .step-items .step-item .step-details .step-title {
    font-size: 0.1rem;
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