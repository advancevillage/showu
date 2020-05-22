<template>
    <div class="header">
        <Notice :items="notices" :countries="countries" :width="width" :height="height/3" @getLanguage="getLanguage"/>
        <Menu :categories="categories" :users="users" :carts="carts" :width="width" :height="2 * height/3" :language="language" :opacity="opacity"/>
    </div>
</template>

<script>
    import Notice from "./Notice";
    import Menu   from "./Menu";

    export default {
        name: "Header",
        components: {
            Notice,
            Menu,
        },
        props: {
            width: {
                type: Number,
                required: true,
            },
            height: {
                type: Number,
                required: true,
            }
        },
        mounted() {
            this.QueryNotices();
            this.QueryCountries();
            this.QueryCategories();
        },
        data() {
            return {
                notices: [],
                countries: [],
                categories: [],
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
                language: "en",
                opacity: true
            }
        },
        methods: {
            async QueryNotices() {
                const params = {};
                const headers = {};
                let response = await this.$api.QueryNotices(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response)
                } else {
                    this.notices = response.data.items;
                }
            },
            async QueryCountries() {
                const params = {};
                const headers = {};
                let response = await this.$api.QueryCountries(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response)
                } else {
                    this.countries = response.data.items;
                }
            },
            async QueryCategories() {
                const params = {};
                const headers = {};
                let response = await this.$api.QueryCategories(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(this.response);
                } else {
                    this.categories = response.data.items;
                }
            },
            //多语言事件触发
            getLanguage(data) {
                this.language = data.key;
                this.$emit('getLanguage', this.language);
            }
        }
    }
</script>

<style scoped>

</style>