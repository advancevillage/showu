<template>
    <div id="footer">
        <div class="footer_container_left">
            <div class="footer_container_left_items" v-for="(item, index) in footerContainerLeft.items" :key="index">
                <ul>
                    <li>{{item.key}}</li>
                    <li class="footer_container_left_item" v-for="(list, index) in item.values" :key="index">
                        <a :href="list.link">{{list.name}}</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="footer_container_right">
            <div class="footer_container_right_item">

            </div>
            <div class="footer_container_right_item">

            </div>
        </div>
        <div class="footer_container_footer">
            <ul>
                <li v-for="(item, index) in footerContainerFooter" :key="index">
                    <a :href="item.link">{{item.name}}</a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        data() {
            return {
                footerContainerLeft: {
                    items: [
                        {
                            key: "Account",
                            values: [
                                {
                                    link: "/",
                                    name: "order"
                                },
                                {
                                    link: "/",
                                    name: "info"
                                }
                            ]
                        },
                        {
                            key: "Company",
                            values: [
                                {
                                    link: "/",
                                    name: "order"
                                },
                                {
                                    link: "/",
                                    name: "info"
                                }
                            ]
                        },
                        {
                            key: "Contact",
                            values: [
                                {
                                    link: "/",
                                    name: "facebook"
                                },
                                {
                                    link: "/",
                                    name: "google"
                                },
                                {
                                    link: "/",
                                    name: "youtube"
                                },
                                {
                                    link: "/",
                                    name: "twitter"
                                }
                            ]
                        },
                    ]
                },
                footerContainerFooter: [
                    {
                        link: "/",
                        name: "© 2019 All Rights Reserved"
                    },
                    {
                        link: "/",
                        name: "Privacy Policy"
                    },
                    {
                        link: "/",
                        name: "Terms of Service"
                    },
                    {
                        link: "/",
                        name: "Sitemap Pages"
                    },
                ]
            }
        }
    }
</script>

<style scoped>
    #footer {
        width: 100%;
        height: 200px;
        background-color: rgba(192, 192, 192, 1);
        z-index: 25;
    }
    .footer_container_left {
        width: 75%;
        height: 85%;
        float: left;
        padding: 0 2%;
    }
    .footer_container_left_items {
        float: left;
        width: 12%;
        height: 100%;
    }
    .footer_container_left_items > ul {
        margin: 10%;
    }
    .footer_container_left_item {
        font-size: medium;
        margin: 2px 0;
    }
    .footer_container_left_item > a {
        color: rgba(232, 232, 232, 1)
    }
    .footer_container_right {
        width: 25%;
        height: 85%;
        float: left;
    }
    .footer_container_right_item {
        width: 100%;
        height: 50%;
    }
    .footer_container_footer {
        width: 100%;
        height: 15%;
        float: left;
        background: black;
        padding: 0 25%;
    }
    .footer_container_footer > ul > li {
        float: left;
        margin: 3px 0;
        padding: 0 2%;
        border-right: 1px solid white;
        text-align: center;
    }
    .footer_container_footer > ul > li > a {
        color: white;
    }
</style>