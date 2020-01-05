<template>
    <div id="header">
        <nav class="level">
            <p class="level-item has-text-centered"></p>
            <p class="level-item has-text-centered"><b-icon pack="fas" icon="user" size="is-medium" type="is-success"></b-icon><a class="header_notice_text">{{noticeText}}</a></p>
            <p class="level-item has-text-centered"></p>
            <!-- Right side -->
            <div class="level-right">
                <p v-for="item in selectItems" :key='item.id' >
                    <a class="header_select_items" :href="item.url">{{item.value}}</a>
                </p>
            </div>
        </nav>
        <!-- 菜单页 -->
        <div class="container_menu">
            <b-navbar class="container_menu_items" :class="{'container_menu_items_hover': containerMenu.hover}" v-on:mouseenter.native="containerMenuItemsMouseEnter()" v-on:mouseleave.native="containerMenuItemsMouseLeave()">
                <template slot="start">
                    <b-navbar-item :key="index" href="#" v-for="(cat, index) in containerMenu.categories"
                                   v-on:mouseenter.native="containerMenuItemMouseEnter(index)"
                                   v-on:mouseleave.native="containerMenuItemMouseLeave()">
                        <span class="container_menu_item" :class="{'container_menu_item_hover': showContainerMenuItem(index) }">{{cat.categoryName}}</span>
                    </b-navbar-item>
                </template>
                <template slot="end">
                    <b-navbar-item href="#" >
                        <span class="container_menu_item">{{containerMenu.user.userNickName}}</span>
                    </b-navbar-item>
                    <b-navbar-item href="#" >
                        <b-button class="container_menu_item_cart">{{containerMenu.user.userCartCount}}</b-button>
                    </b-navbar-item>
                </template>
            </b-navbar>
            <div class="container_menu_item_context" :class="{'container_menu_item_context_show': showContainerMenuItemContext() }"  v-on:mouseenter="containerMenuItemContextMouseEnter()" v-on:mouseleave="containerMenuItemContextMouseLeave()">
                <div class="container_menu_item_context_list">
                    <div class="container_menu_item_context_list_item" v-for="(item, index) in containerMenu.itemContext.list" :key="index">
                        {{item.categories}}
                    </div>
                </div>
                <div class="container_menu_item_context_images">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                noticeText: "Show You! More Confident And Beautiful",
                selectItems: [
                    {id: "country", url: "/", value: "CN"},
                    {id: "themes", url: "/", value: ""},
                ],
                containerMenu: {
                    position: "is-left",
                    size: "is-medium",
                    categories: [
                        {categoryName: "NewIn", categoryId: "1111111111"},
                        {categoryName: "NewIn", categoryId: "2222222222"},
                        {categoryName: "NewIn", categoryId: "3333333333"},
                    ],
                    hover: false,
                    item: {
                        hover: -1
                    },
                    itemContext: {
                        hover: -1,
                        list: [
                            {categories: [1, 2, 3]},
                            {categories: [4, 5, 6]},
                            {categories: [7, 8 ,9]}
                        ]
                    },
                    user: {
                        userNickName: "richard",
                        userId: "11111",
                        userCartCount: 3
                    },
                },
            }
        },
        name: "Header",
        methods: {
            getCarouselImageUrl: function (value) {
                return `https://picsum.photos/id/43${value}/1230/500`
            },
            /*菜单页*/
            containerMenuItemsMouseEnter() {
                this.containerMenu.hover = true;
            },
            containerMenuItemsMouseLeave() {
                this.containerMenu.hover = false;
            },
            containerMenuItemMouseEnter(index) {
                this.containerMenu.item.hover = index;
                this.containerMenu.itemContext.hover = index;
            },
            containerMenuItemMouseLeave() {
                this.containerMenu.item.hover = -1;
            },
            containerMenuItemContextMouseEnter() {
                this.containerMenu.hover = true;
                this.containerMenu.item.hover = this.containerMenu.itemContext.hover;
            },
            containerMenuItemContextMouseLeave() {
                this.containerMenu.hover = false;
                this.containerMenu.item.hover = -1;
                this.containerMenu.itemContext.hover = -1;
            },
            showContainerMenuItem(index) {
                return this.containerMenu.hover && this.containerMenu.item.hover === index
            },
            showContainerMenuItemContext() {
                return this.containerMenu.hover && this.containerMenu.item.hover !== -1
            }
        }
    }
</script>

<style scoped>
    #header {
        width: 100%;
        height: 45px;
        background: black;
        z-index: 25;
    }
    /* 通知顶部栏 */
    .level {
        margin: 0;
    }
    .level-item {
        padding: 0.5% 0;
    }
    .header_notice_text {
        color: white;
        text-align: center;
        text-decoration: underline;
    }
    .header_select_items {
        color: white;
        text-align: center;
        margin: 0 10px;
    }
    /* 顶部导航栏 */
    .container_menu_items {
        padding: 0 2%;
        background: rgba(192, 192, 192, 0);
    }
    .container_menu_items_hover {
        background: rgba(192, 192, 192, 1);
    }
    .container_menu_item {
        width: 100%;
        text-align: center;
        color: white;
    }
    .container_menu_item_hover {
        font-weight: bolder;
        border-bottom: 2px solid white;
    }
    .container_menu_item_cart {
        background-color: darkgray;
        border-radius: 50px;
    }
    .container_menu_item_context {
        width: 100%;
        height: 240px;
        padding: 0 2%;
        display: none;
        position: absolute;
        z-index: 25;
    }
    .container_menu_item_context_show {
        display: block;
        background: rgba(216, 216, 216, 0.9);
        border-top: 2px solid white;
    }
    .container_menu_item_context_list {
        float: left;
        width: 45%;
        height: 100%;
    }
    .container_menu_item_context_list_item {
        width: 25%;
        height: 100%;
        float: left;
        margin: 1%;
    }
    .container_menu_item_context_images {
        float: left;
        width: 55%;
        height: 100%;
    }
    a.navbar-item:focus, a.navbar-item:focus-within, a.navbar-item:hover {
        background-color: rgba(128, 128, 128, 0);
    }
</style>