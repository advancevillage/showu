import Vue from 'vue'
import VueRouter from 'vue-router'
//引入组件库
import BueFy from 'buefy'
import 'buefy/dist/buefy.css'
import api     from './axios/api'
import lang    from './language/languages'
import utils   from './storage/utils'
import moment  from 'moment'
import '@mdi/font/css/materialdesignicons.css'

//安装插件 vue-router
Vue.use(VueRouter);
Vue.use(BueFy);
Vue.prototype.$api       = api;
Vue.prototype.$languages = lang;
Vue.prototype.$utils     = utils;
Vue.prototype.$bus       = new Vue(); //事件总线
Vue.prototype.$moment    = moment;
Vue.prototype.$project   = "kelly"

//载入组件
import App            from './App.vue'
import Index          from './pages/Index'          //组件之首页
// import List           from './components/list/List'            //组件之列表页
import List           from './pages/List'
import Checkout       from "./pages/Checkout";
import Detail         from './pages/Detail'        //组件之详情页
// import Cart           from './components/cart/Cart'            //组件之购物车
import Account        from './components/account/Account'      //组件之账户页
import AccountOrder   from './components/account/Order'        //组件之账户订单页
import Order          from './components/order/Order'              //组件之支付页
import Common404      from './components/common/NotFound'      //404
import Test           from './pages/Test'                 //Debug 页面

//创建路由对象并配置路由规则
let router = new VueRouter({
  routes: [
    //首页
    { path: '/', component: Index, },
    //列表页
    { path: '/list/*', component: List },
    //详情页
    { path: '/products/*', component: Detail },
    //购物车
    { path: '/checkout', component: Checkout },
    //账户页
    { path: '/account', component: Account,
      children: [
        // path not /
        {path: 'order', component: AccountOrder}
      ]
    },
    //订单支付页
    { path: '/orders', component: Order},
    //404
    { path: '/404', component: Common404 },
    // 404 注意至于最底部
    { path: '*',  redirect: '/404' },
      //test 页面
    { path: '/test', component: Test},
  ],
  mode: 'history' //hash(#)
});

//启动
new Vue({
  el: '#app',
  router: router, //可以简写router
  render: h => h(App),
});
