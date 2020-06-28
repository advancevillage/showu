<template>
    <div class="menu" v-bind:style="{width: width + 'px', height: height + 'px'}">
        <nav @mouseenter="v" @mouseleave="p" v-bind:style="[level > 0 || !opacity ? {backgroundColor: 'rgba(128,128,128,1)'}:{backgroundColor: 'rgba(128,128,128,0)'}]">
            <div class="category" v-for="(item, index) in categories" :key="index" v-on:mouseenter="cv(index)" v-on:mouseleave="cp">
                <span v-bind:style="[active === index ? {color: 'black', fontWeight: 'bolder'}:{}]" @click="go(item)">{{item.name[language]}}</span>
                <em v-bind:style="[active === index ? {display: 'block'}:{display: 'none'}]"></em>
            </div>
            <div class="cart">
                <Cart :items="carts" :height="height" :opacity="opacity" :language="language" @getCart="getCart"/>
            </div>
            <div class="user">
                <User :items="users" :height="height" :opacity="opacity" :language="language" :iconClickFn="userClickFn"/>
            </div>
        </nav>
        <div v-if="active > -1"  v-bind:style="[childActive > -1 ? {backgroundColor: 'rgba(192,192,192,1)'}:{backgroundColor: 'rgba(192,192,192,0.75)'}]" @mouseenter="ccv" @mouseleave="ccp">
            <div class="children">
                <div v-for="(child,index) in categories[active].children" :key="index" :class="child.id">
                    <ul>
                        <li v-for="(type,index) in child" :key="index" @click="go(type)">
                            {{type.name[language]}}
                        </li>
                    </ul>
                </div>
            </div>
            <div class="banner">
<!--                <Carousel :items="categories[active].banner" :width="width * 0.68" :height="240 * 0.9" :interval=2 />-->
                <Slide :items="categories[active].banner" :width="width * 0.35" :height="height * 2.5" />
            </div>
        </div>
    </div>
</template>

<script>
    import User  from './User'
    import Cart  from './Cart'
    import Slide    from "../Basic/Slide";

    export default {
        name: "Menu",
        components: {
            Slide,
            Cart,
            User,
        },
        props: {
            categories: {
                type: Array,
                required: true
            },
            users: {
                type: Array,
                required: true
            },
            carts: {
                type: Array,
                required: true
            },
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
            language: {
                type: String,
                required: false,
                default: "en"
            },
            opacity: {
                type: Boolean,
                required: false,
                default: false
            },
            userClickFn: {
                type: Function,
                required: false,
                default: null
            }
        },
        data() {
            return {
                languages: this.$languages,
                active: -1,
                childActive: -1,
                middleStatus: -1,
                level: 0,
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
            },
            go(cat) {
                let link = this.$api.GenerateLink("list", this.$project, cat.name, cat.id)
                this.$router.push({path: link})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(-1);
                    });
            },
            getCart() {
                this.$emit('getCart')
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
        height: auto;
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
        line-height: 4.5rem;
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
        bottom: 0;
    }
    .user, .cart {
        float: right;
    }
    .children, .banner {
        height: 100%;
        width: 25%;
        float: left;
        padding: 0;
    }
    .banner {
        width: 75%;
        padding: 0.5% 0 0;
    }
    .children ul {
        float: left;
        width: 30%;
    }
    .children li {
        display: block;
        width: 100%;
        margin: 1%;
        line-height: 1.5rem;
        text-align: center;
        font-size: x-small;
    }
    .children li:hover {
        font-weight: bolder;
        text-decoration: underline;
        cursor: pointer;
    }
    .children span {
        color: black;
        cursor: pointer;
        font-family: monospace;
    }
    .children span:hover {
        font-weight: bolder;
    }
</style>