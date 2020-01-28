import Vue from 'vue'
import VueRouter from 'vue-router'
import moment    from 'moment'
import languages from './language/languages'
import api       from './axios/api'
//引入组件库
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';

//安装插件 vue-router
Vue.use(VueRouter);
Vue.use(ViewUI);
Vue.prototype.$moment    = moment;
Vue.prototype.$languages = languages;
Vue.prototype.$api       = api;

//载入组件
import App            from './App.vue'
import Index          from './components/index/Index'          //组件之首页
import Common404      from './components/common/NotFound'      //404

//创建路由对象并配置路由规则
let router = new VueRouter({
  routes: [
    //首页
    { path: '/', component: Index },
    //404
    { path: '/404', component: Common404 },
    // 404 注意至于最底部
    { path: '*',  redirect: '/404' }
  ],
  mode: 'history' //hash(#)
});

//启动
new Vue({
  el: '#app',
  router: router, //可以简写router
  render: h => h(App),
});
