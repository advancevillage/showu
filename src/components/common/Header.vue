<template>
    <!--v-bind:style= "[condition ? {styleA} : {styleB}]"-->
    <div id="header" v-bind:style="[scroll > 24 ? {position: 'fixed'} : {}]">
        <!--通知栏-->
        <div class="notice">
            <Notice :language="lang" v-on:selectedLanguage="selectedLanguage"/>
        </div>
        <!-- 菜单页 -->
        <div class="menu">
            <Menu :language="lang" :nav="nav"/>
        </div>
    </div>
</template>

<script>
    import  Notice from './header/Notice'
    import  Menu   from './header/Menu'

    export default {
        name: "Header",
        props: {
            language: {
                type: String,
                required: false,
                default: "chinese"
            },
            nav: {
                type: Number,
                required: false,
                default: -1,
            },
        },
        components: {
            Notice,
            Menu
        },
        data() {
            return {
                lang: this.language,
                scroll: 0
            }
        },
        mounted() {
            window.addEventListener('scroll', this.fixedHeader, true)
        },
        destroyed () {
            window.removeEventListener('scroll', this.fixedHeader,true);
        },
        methods: {
            selectedLanguage(lang) {
                this.lang = lang;
                this.$emit("selectedLanguage", this.lang)
            },
            fixedHeader() {
                this.scroll = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
            }
        }
    }
</script>

<style scoped>
    #header {
        width: 100%;
        height: 24px;
        background: black;
        z-index: 25;
    }
    /* 通知栏 */
    .notice {
        width: 100%;
        height: 24px;
        padding: 0 1%;
    }
    /* 菜单栏 */
    .menu {
        width: 100%;
        height: 40px;
        margin: 0;
        padding: 0;
        z-index: 25;
        position: absolute;
    }
</style>