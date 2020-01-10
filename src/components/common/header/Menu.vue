<template>
    <div>
        <nav class="navbar" role="navigation" aria-label="main navigation"
             v-bind:class="{'navbar_hover': navBar < 0}"
             v-on:mouseenter="navBar=1"
             v-on:mouseleave="navBar=-1">
            <!-- 导航栏 -->
            <div class="navbar-menu">
                <a class="navbar-item category" v-for="(item, index) in categories" :key="index" :href="item.categoryUrl"
                    v-on:mouseenter="navItem=index; navDetail=index"
                    v-on:mouseleave="navItem=-1">
                    {{item.categoryName}}
                    <em v-if="navItem === index"></em>
                </a>
            </div>
            <!-- 用户信息 -->
            <div class="navbar-end">
                <div class="navbar-item">
                    <!-- 登录状态 -->
                    <div v-if="login" class="buttons">
                        <div class="button account">
                            Sign up
                        </div>
                        <div class="button account" v-bind:style="{'border-color': 'white', 'border-radius': '10%', 'border': '1px solid'}">
                            <svg version="1.1" x="0px" y="0px" width="40px" height="40px" viewBox="0 0 40 40">
                                <g>
                                    <path stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="M6.588,19.992c0,1.434-1.159,2.594-2.589,2.594"></path>
                                    <path stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="M16.456,13.569c0-2.507,2.029-4.54,4.531-4.54c2.503,0,4.532,2.033,4.532,4.54"></path>
                                    <path stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d=" M16.605,13.591h-3.403c-3.652,0-6.614,2.966-6.614,6.626v6.355l-0.614,2.967c0,0.791,0.64,1.433,1.429,1.433h27.166 c0.791,0,1.431-0.642,1.431-1.433l-0.614-3.171v-6.151c0-3.66-2.962-6.626-6.614-6.626h-3.253"></path>
                                    <line stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="21.936" y1="13.591" x2="16.457" y2="13.591"></line>
                                </g>
                            </svg>
                        </div>
                    </div>
                    <!-- 登出状态 -->
                    <div v-else class="buttons">
                        <div class="button account" v-on:click="Login">
                            Login
                        </div>
                        <div class="button account">
                            Sign up
                        </div>
                        <div class="button account" v-bind:style="{'border-color': 'white', 'border-radius': '100%', 'width': '40px', 'border': '1px solid'}"
                            v-on:mouseenter="cartDetail=1">
                            <svg version="1.1" x="0px" y="0px" width="40px" height="40px" viewBox="0 0 40 40">
                                <g>
                                    <path stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="M6.588,19.992c0,1.434-1.159,2.594-2.589,2.594"></path>
                                    <path stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="M16.456,13.569c0-2.507,2.029-4.54,4.531-4.54c2.503,0,4.532,2.033,4.532,4.54"></path>
                                    <path stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d=" M16.605,13.591h-3.403c-3.652,0-6.614,2.966-6.614,6.626v6.355l-0.614,2.967c0,0.791,0.64,1.433,1.429,1.433h27.166 c0.791,0,1.431-0.642,1.431-1.433l-0.614-3.171v-6.151c0-3.66-2.962-6.626-6.614-6.626h-3.253"></path>
                                    <line stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="21.936" y1="13.591" x2="16.457" y2="13.591"></line>
                                </g>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
        <div v-if="navBar >= 0 && navItem >= 0" class="navbar_detail"
             v-on:mouseenter="navBar=1; navItem=navDetail"
             v-on:mouseleave="navBar=-1; navItem=-1; navDetail=-1">
        </div>
        <div v-if="navBar >= 0 && cartDetail >= 0" class="cart_detail"
            v-on:mouseenter="navBar=1, cartDetail=1"
            v-on:mouseleave="navBar=-1,cartDetail=-1">
            <div class="card">

            </div>
        </div>
    </div>
</template>

<script>
    import Login from './Login'

    export default {
        name: "Menu",
        data() {
            return {
                navBar: -1,
                navItem: -1,
                navDetail: -1,
                cartDetail: -1,
                login: false,
                categories: [
                    {
                        categoryId: "xxxxxxxxxxx",
                        categoryName: "test",
                        categoryUrl: "/",
                        child: []
                    },
                    {
                        categoryId: "xxxxxxxxxxx",
                        categoryName: "test",
                        categoryUrl: "/",
                        child: []
                    },
                    {
                        categoryId: "xxxxxxxxxxx",
                        categoryName: "test",
                        categoryUrl: "/",
                        child: []
                    },
                    {
                        categoryId: "xxxxxxxxxxx",
                        categoryName: "test",
                        categoryUrl: "/",
                        child: []
                    },
                    {
                        categoryId: "xxxxxxxxxxx",
                        categoryName: "test",
                        categoryUrl: "/",
                        child: []
                    },
                    {
                        categoryId: "xxxxxxxxxxx",
                        categoryName: "test",
                        categoryUrl: "/",
                        child: []
                    },
                    {
                        categoryId: "xxxxxxxxxxx",
                        categoryName: "test",
                        categoryUrl: "/",
                        child: []
                    }
                ]
            }
        },
        methods: {
            Login() {
                this.$buefy.modal.open({
                    parent: this,
                    component: Login,
                    hasModalCard: true,
                    trapFocus: true
                });
            },
        }
    }
</script>

<style scoped>
    .navbar, .navbar_detail {
        width: 100%;
        padding: 0 2%;
        background-color: rgba(192, 192, 192, 1);
        z-index: 25;
    }
    .navbar_hover {
        background-color: rgba(192, 192, 192, 0);
    }
    .category, .account {
        color: white;
    }
    .category:hover {
        color: pink;
        background: none;
    }
    .category > em {
        width: 0;
        height: 0;
        font-size: 0;
        opacity: 1;
        border: 8px solid rgb(192, 192, 192);
        border-bottom: 8px solid white;
        position: absolute;
        left: 33%;
        top: 73%;
    }
    .navbar_detail {
        position: absolute;
        height: 240px;
        border-top: 2px solid white;
        background: deepskyblue;
    }
    .account {
        background-color: rgba(192,192,192,0);
        width: 60px;
        height: 40px;
        border: none;
        padding: 5px;
    }
    .cart_detail {
        width: 25%;
        border: 1px solid red;
        z-index: 30;
        position: absolute;
        left: 75%;
        height: 200px;
    }
</style>