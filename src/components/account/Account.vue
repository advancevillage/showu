<template>
    <div>
        <Header :language="language" :nav="1" v-on:selectedLanguage="selectedLanguage"/>
        <div id="container">
            <div class="container_warp">
                <b-tabs v-model="tab" class="tabs" vertical size="is-small" type="is-boxed">
                    <b-tab-item v-for="(item, i) in tabs" :key="i" :label="languages.Account[item.key][language]">

                    </b-tab-item>
                </b-tabs>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header  from '../common/Header'
    import Footer  from '../common/Footer'
    import BTabItem from "buefy/src/components/tabs/TabItem";

    export default {
        name: "Account",
        components: {
            BTabItem,
            Header,
            Footer,
        },
        data() {
            return {
                language: "chinese",
                languages: this.$languages,
                tab: 1,
                tabs: [
                    { key: "account", icon: "/account"},
                    { key: "orderReturn", icon: "/account/orders"},
                    { key: "shipping", icon: "/account/shipping"},
                ]
            }
        },
        methods: {
            selectedLanguage(lang) {
                this.language = lang
            }
        }

    }
</script>

<style scoped>
    .container_warp {
        width: 100%;
        padding: 60px 2% 0;
    }
    .tabs {
        margin: 0 15%;
        font-size: 1rem;
        font-family: serif;
    }
</style>