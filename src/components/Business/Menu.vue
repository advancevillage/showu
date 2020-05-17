<template>
    <div class="menu" v-bind:style="{width: width + 'px', height: height + 'px'}">
        <nav @mouseenter="v" @mouseleave="p" v-bind:style="[level > 0 || opacity ? {backgroundColor: 'rgba(128,128,128,1)'}:{backgroundColor: 'rgba(128,128,128,0)'}]">
            <div class="category" v-for="(item, index) in items" :key="index" v-on:mouseenter="cv(index)" v-on:mouseleave="cp">
                <span v-bind:style="[active === index ? {color: 'black', fontWeight: 'bolder'}:{}]">{{item.name[language]}}</span>
                <em v-bind:style="[active === index ? {display: 'block'}:{display: 'none'}]"></em>
            </div>
            <div class="cart">
                <Cart :items="carts" :height="height"/>
            </div>
            <div class="user">
                <User :items="users" :height="height"/>
            </div>
        </nav>
        <div  v-if="active > -1" v-bind:style="[childActive > -1 ? {backgroundColor: 'rgba(192,192,192,1)'}:{backgroundColor: 'rgba(192,192,192,0.75)'}]" @mouseenter="ccv" @mouseleave="ccp">

        </div>
    </div>
</template>

<script>
    import User  from './User'
    import Cart  from './Cart'

    export default {
        name: "Menu",
        components: {
            Cart,
            User,
        },
        props: {
            width: {
                type: Number,
                required: false,
                default: 1440
            },
            height: {
                type: Number,
                required: false,
                default: 45
            },
            //i18n https://blog.csdn.net/u010987039/article/details/81671886 速查表
            language: {
                type: String,
                required: false,
                default: "en"
            },
            opacity: {
                type: Boolean,
                required: false,
                default: true
            }
        },
        data() {
            return {
                languages: this.$languages,
                active: -1,
                childActive: -1,
                middleStatus: -1,
                level: 0,
                items: [
                    {
                        name: {
                            en: "111"
                        }
                    },
                    {name: {
                            en: "222"
                        }},
                    {name: {
                            en: "3333"
                        }},
                ],
                users: [
                    { value: "中国", fn: function (data) {
                            console.log(data);
                        }},
                    { value: "开宝", link: "/"},
                    { value: "Kelly", link: "/"},
                    { value: "Richard", link: "/"},
                ],
                carts: [
                    {value: "color,size", count: 4, link: "", price: 19.9, imageUrl: "//localhost:13147/images/67/18/2636167883511603206718.png"},
                    {value: "color,size", count: 3, link: "", price: 19.9, imageUrl: "//localhost:13147/images/67/18/2636167883511603206718.png"},
                    {value: "color,size", count: 2, link: "", price: 19.9, imageUrl: "//localhost:13147/images/67/18/2636167883511603206718.png"},
                ],
            }
        },
        methods: {
            p() {
                this.level = 0;
            },
            v() {
                this.level = 1;
            },
            cp(){
                this.active = -1;
                this.p();
            },
            cv(i){
                this.active = i;
                this.middleStatus = i;
                this.v();
            },
            ccp() {
                this.childActive = -1;
                this.cp();
            },
            ccv() {
                this.childActive = this.middleStatus;
                this.cv(this.childActive);
            }
        }
    }
</script>

<style scoped>
    .menu {
    }
    .menu > nav , .menu > div {
        width: 100%;
        padding: 0 2% 0;
        background-color: rgba(128,128,128, 0.75);
        height: 100%;
    }
    .menu > nav {
        padding-right: 5%;
    }
    .menu > div {
        position: absolute;
        height: 240px;
        border-top: 2px solid white;
        background: darkgray;
        margin-top: -2px;
        z-index: 5;
    }
    .category {
        margin: 0;
        padding: 0 1%;
        color: black;
        display: block;
        float: left;
        position: relative;
        font-family: monospace;
        cursor: pointer;
        line-height: 2.5rem;
    }
    .category > em {
        width: 0;
        height: 0;
        font-size: 0;
        opacity: 1;
        border: 4px solid rgba(128,128,128,0);
        border-bottom: 8px solid black;
        position: absolute;
        left: 45%;
        bottom: -5px;
    }
    .user, .cart {
        float: right;
    }
</style>