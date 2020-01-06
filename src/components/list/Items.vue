<template>
    <div>
        <div class="filters">

        </div>
        <div class="items">
            <div class="card" v-for="(item, index) in goods.items" :key="index" v-on:mouseenter="item.hover = true" v-on:mouseleave="item.hover = false">
                <div class="card-image">
                    <div class="tags">
                        <div class="left"></div>
                        <div class="right">
                            <svg class="star" width="15px" height="12px" viewBox="0 0 15 12" version="1.1"><g stroke-width="1" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"><g transform="translate(-384.000000, -173.000000)"><g transform="translate(373.000000, 160.000000)"><path d="M24.1870486,15.1337994 C23.0156479,13.7915995 21.0146777,13.6174702 19.6357465,14.7377957 C19.0576454,15.2115959 18.655296,15.8713213 18.4944667,16.6082814 C18.3352955,15.8721638 17.9348804,15.2124384 17.3587137,14.7377957 C15.9806115,13.6211213 13.9837864,13.7949698 12.8129383,15.1337994 C11.6169435,16.5248678 11.756771,18.6380112 13.125754,19.853546 C13.1564276,19.8807888 13.1873776,19.9074699 13.2191566,19.9335893 L17.900338,23.7840937 C18.2510121,24.0719688 18.7517383,24.0719688 19.1024124,23.7840937 L23.7808304,19.9335893 C25.1929223,18.7705741 25.4101247,16.6641713 24.2658052,15.228728 C24.2401057,15.1967106 24.2138535,15.1649742 24.1870486,15.1337994 L24.1870486,15.1337994 Z"></path></g></g></g></svg>
                        </div>
                    </div>
                    <img class="image" :src="item.frontImage" alt="Placeholder image">
                </div>
                <div class="card-content">
                    <span class="title">{{item.title}}</span>
                    <span class="price">{{item.price}}</span>
                    <div v-if="item.hover" class="color">
                        <b-tag class="color_warp" v-for="(itemColor, index) in item.colors" :key="index" v-bind:style="{'background-color': itemColor}"></b-tag>
                    </div>
                    <div v-else class="color_text">
                        <span>{{item.colors.length}} colors available</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer">
        </div>
    </div>
</template>

<script>
    export default {
        name: "Items",
        data() {
            return {
                goods: {
                    total: 36,
                    items: [
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        },
                        {
                            frontImage:"https://bulma.io/images/placeholders/1280x960.png",
                            backImage: "https://bulma.io/images/placeholders/1280x960.png",
                            desc: "hello show u",
                            hover: false,
                            title: "show u",
                            price: "$99",
                            colors: [
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                                "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                            ]
                        }


                    ],
                },
                color: {
                    header: "Color",
                    context: [
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                    ]
                },
            }
        }
    }
</script>

<style scoped>
    .filters {
        width: 100%;
        height: 50px;
    }
    .items {
        width: 100%;
        height: 90%;
        float: left;
        padding: 0 2%;
    }
    /* 列表页 图片 w/h=4/5 */
    .card-image, .card-image > .image {
        width: 337px;
        height: 422px;
    }
    .card-image > .tags {
        z-index: 30;
        position: absolute;
        float: left;
    }
    .card-image > .tags > .left, .card-image > .tags > .right {
        float: left;
        height: 100px;
        width: 100px;
    }
    .card-image > .tags > .right {
        margin-left: 137px;
    }
    .card-image > .tags > .right > .star {
        margin-top: 20%;
        margin-left: 60%;
    }
    /* 描述 */
    .card-content > .title, .card-content > .price, .card-content > .color {
        font-size: x-large;
        text-align: center;
    }
    .card-content > .price {
        float: right;
    }
    .card-content > .color, .card-content > .color_text {
        width: 100%;
        height: 40px;
        float: left;
        overflow: hidden;
        cursor: pointer;
    }
    .card-content > .color > .color_warp {
        width: 15px;
        height: 15px;
        border-radius: 100%;
        padding: 0;
        margin: 0 3px;
    }
    .card-content > .color > .color_warp:hover {
        border-radius: 0;
    }
    .card-content {
        padding: 0.5rem;
    }
    .card {
        width: 337px;
        height: 510px;
        float: left;
        margin-right: 1%;
        margin-bottom: 1%;
    }
</style>