<template>
    <div>
        <Header :language="language" :nav="1" v-on:selectedLanguage="selectedLanguage"/>
        <div id="container">
            <div class="container_warp">
                <b-tabs v-model="tab" class="tabs" vertical size="is-small" type="is-boxed">
                    <b-tab-item v-for="(item, i) in tabs" :key="i" :label="languages.Account[item.key][language]">
                        <Order :sn="sn" v-if="item.key === 'orderReturn'"/>
                        <div v-else>
                            <p>hello others</p>
                        </div>
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
    import Order   from './Order'

    export default {
        name: "Account",
        components: {
            Header,
            Footer,
            Order,
        },
        created() {
           let href = this.$route.query.href || "";
           switch (href.toLowerCase()) {
               case "order":
                   this.tab = 1;
                   break;
               case "ship":
                   this.tab = 2;
                   break;
               default:
                   this.tab = 0
           }
           this.sn = this.$route.query.sn || "";
           switch (this.sn.length) {
               case 18:
                   break;
               default:
                   this.sn = "";
           }
        },
        data() {
            return {
                language: "chinese",
                languages: this.$languages,
                tab: 1,
                sn: "",
                tabs: [
                    { key: "account", icon: "/account"},
                    { key: "orderReturn", icon: "/account?href=order"},
                    { key: "shipping", icon: "/account?href=ship"},
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