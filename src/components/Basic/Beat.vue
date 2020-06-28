<template>
    <div class="ss_beat" v-bind:style="{width: width + 'px', height: height + 'px'}">
        <ul class="music">
            <li :attr="random(note)" v-for="index in note" :key="index" v-bind:style="{width: width / (note << 1) + 'px', marginLeft: width / (note << 1) + 'px'}"></li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Beat",
        props: {
            width: {
                type: Number,
                required: false,
                default: 1440
            },
            height: {
                type: Number,
                required: false,
                default: 30
            },
            note: {
                type: Number,
                required: false,
                default: 100,
            }
        },
        methods: {
            random(value) {
                return Math.round(Math.random()*value)
            }
        }
    }
</script>

<style scoped>
    .ss_beat {
        position: relative;
        overflow: hidden;
    }
    .ss_beat ul{
        position: absolute;
        bottom: 0;
        display: inline-block;
        vertical-align: baseline;
        font-size: 0;
        height: 100%;
    }
    .ss_beat ul li {
        background: lightgray;
        display: inline-block;
        height: 100%;
    }
    [attr$="0"] {
        animation: .8s .0s living linear infinite backwards normal;
        animation-delay: -1.0s;
    }
    [attr$="1"] {
        animation: .8s .1s living linear infinite backwards normal;
        animation-delay: -1.1s;
    }
    [attr$="2"] {
        animation: .7s .2s living linear infinite backwards normal;
        animation-delay: -1.2s;
    }
    [attr$="3"] {
        animation: .7s .3s living linear infinite backwards normal;
        animation-delay: -1.3s;
    }
    [attr$="4"] {
        animation: .5s .4s living linear infinite backwards normal;
        animation-delay: -1.4s;
    }
    [attr$="5"] {
        animation: .5s .5s living linear infinite backwards normal;
        animation-delay: -1.5s;
    }
    [attr$="6"] {
        animation: .7s .6s living linear infinite backwards normal;
        animation-delay: -1.6s;
    }
    [attr$="7"] {
        animation: .8s .7s living linear infinite backwards normal;
        animation-delay: -1.7s;
    }
    [attr$="8"] {
        animation: .8s .8s living linear infinite backwards normal;
        animation-delay: -1.8s;
    }
    [attr$="9"] {
        animation: .8s .9s living linear infinite backwards normal;
        animation-delay: -1.9s;
    }
    @keyframes living{
        0%{-webkit-transform:scaleY(1);-ms-transform:scaleY(1);transform:scaleY(1);-webkit-transform-origin:0 120px;-ms-transform-origin:0 120px;transform-origin:0 120px}
        50%{-webkit-transform:scaleY(.3);-ms-transform:scaleY(.3);transform:scaleY(.3);-webkit-transform-origin:0 120px;-ms-transform-origin:0 120px;transform-origin:0 120px}
        100%{-webkit-transform:scaleY(1);-ms-transform:scaleY(1);transform:scaleY(1);-webkit-transform-origin:0 120px;-ms-transform-origin:0 120px;transform-origin:0 120px}
    }
</style>