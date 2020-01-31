<template>
    <div>
        <nav class="first-level-category"
             v-bind:class="{'first-level-category-hover': flagMenu > 0 }"
             v-on:mouseenter="flagMenu = 1"
             v-on:mouseleave="flagMenu = nav">
            <!-- 导航栏 -->
            <div class="category" v-for="(item, index) in categories.items" :key="index"
                 v-on:mouseenter="EnterCategories(index)"
                 v-on:mouseleave="flagCategory=-1">
                {{item.name[language]}}
                <em v-if="flagCategory === index"></em>
            </div>
            <!-- 登录状态 -->
            <div v-if="login" class="account-info">
                <div class="button">
                    Sign up
                </div>
                <div class="button" v-bind:style="{'border-color': 'white', 'border-radius': '10%', 'border': '1px solid'}">
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
            <div v-else class="account-info">
                <div class="button" v-on:click="Login">
                    Login
                </div>
                <div class="button">
                    Sign up
                </div>
                <div class="button" v-bind:style="{'border-color': 'white', 'border-radius': '100%', 'width': '40px', 'border': '1px solid', 'padding': '5px'}"
                     v-on:mouseenter="flagCartDetail=1">
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
        </nav>

        <div class="category-children"
             v-if="flagMenu >= 0 && flagCategory >= 0"
             v-on:mouseleave="flagMenu=nav; flagCategory=-1; flagCategoryDetail=-1"
             v-on:mouseenter="EnterChildCategories"
             >
            <div class="child-categories">
                <ul>
                    <li style="font-size: 0.8rem;">
                        <a :href="api.CreateListLink(categories.items[flagCategory].name, categories.items[flagCategory].id)">{{categories.items[flagCategory].name[language]}}</a>
                    </li>
                    <li v-for="(item, index) in this.children" :key="index">
                        <a :href="api.CreateListLink(item.name, item.id)">{{item.name[language]}}</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="cart"
             v-if="flagMenu >= 0 && flagCartDetail >= 0"
             v-on:mouseenter="flagMenu=1,  flagCartDetail=1"
             v-on:mouseleave="flagMenu=nav,flagCartDetail=-1">
        </div>
    </div>
</template>

<script>
    import Login from './Login'

    export default {
        name: "Menu",
        props: {
            nav: {
                type: Number,
                required: true,
            },
            language: {
                type: String,
                required: true,
            },
        },
        created() {
            this.flagMenu = this.nav;
        },
        data() {
            return {
                flagMenu: -1,
                flagCategory: -1,
                flagCategoryDetail: -1,
                flagCartDetail: -1,
                login: false,
                categories: {
                    total: 0,
                    items: []
                },
                children: [],
                api: this.$api
            }
        },
        mounted: function() {
            this.QueryCategories()
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
            QueryCategories: async function() {
                const params = {
                    level: 1
                };
                const headers = {
                   "x-language": this.language
                };
                this.categories = await this.$api.QueryCategories(params, headers) || {total: 0, items:[]}
            },
            QueryChildCategories: async function(cid) {
                const headers = {
                    "x-language": this.language
                };
                const params = {};
                this.children = [];
                this.children = await  this.$api.QueryChildCategories(cid, params, headers) || [];
            },
            EnterCategories(index) {
                this.flagCategory = index;
                this.flagCategoryDetail = index;
                this.QueryChildCategories(this.categories.items[this.flagCategory].id);
            },
            EnterChildCategories() {
                this.flagMenu = 1;
                this.flagCategory= this.flagCategoryDetail;
            }
        }
    }
</script>

<style scoped>
    .first-level-category, .category-children {
        width: 100%;
        padding: 0 2%;
        background-color: rgba(192, 192, 192, 0);
        z-index: 25;
        height: 40px;
    }
    .first-level-category-hover {
        background-color: rgba(192, 192, 192, 1);
    }
    .category {
        line-height: 2.5rem;
        margin: 0 5px;
        padding: 0;
        color: white;
        display: block;
        float: left;
        position: relative;
        font-family: serif;
    }
    .category > em {
        width: 0;
        height: 0;
        font-size: 0;
        opacity: 1;
        border: 4px solid rgb(192, 192, 192);
        border-bottom: 8px solid white;
        position: absolute;
        left: 45%;
        top: 30px;
    }
    .category:hover {
        color: black;
    }
    .category-children {
        position: absolute;
        height: 240px;
        border-top: 2px solid white;
        background-color: rgba(160, 160, 160, 0.9);
        top: 40px;
    }
    .child-categories {
        margin: 10px 0;
    }
    .child-categories ul li {
        width: 100px;
        text-align: left;
        font-size: 0.5rem;
        margin: 5px 0;
        color: black;
        text-decoration: underline;
    }
    .account-info, .account-info > .button {
        float: right;
        background-color: rgba(192,192,192,0);
        border: none;
        padding: 0;
        margin: 1px 5px;
        color: white;
    }
    .cart {
        width: 15%;
        border: 1px solid red;
        z-index: 30;
        position: absolute;
        right: 0;
        height: auto;
    }
</style>