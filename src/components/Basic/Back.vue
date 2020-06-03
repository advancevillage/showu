<template>
    <div class="ss_back" v-bind:style="{width: width + 'px', height: height + 'px'}">
        <span class="back" @click="goto(go)"><em></em>{{title}}</span>
    </div>
</template>

<script>
    export default {
        name: "Back",
        props: {
            width: {
                type: Number,
                required: false,
                default: 1440
            },
            height: {
                type: Number,
                required: false,
                default: 20
            },
            title: {
                type:  String,
                required: true
            },
            go: {
                type: String,
                required: true,
            }
        },
        methods: {
            goto(url) {
                this.$router.push({path: url})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(-1);
                    });
            }
        }
    }
</script>

<style scoped>
    .ss_back {
        overflow: hidden;
    }
    .back {
        border-bottom: 1px solid black;
        width: 100%;
        display: block;
        line-height: 1.5rem;
        cursor: pointer;
        font-size: small;
        font-family: monospace;
        font-weight: bolder;
        margin-bottom: 5%;
    }
    .back > em {
        border: 5px solid white;
        border-right: 10px solid black;
        width: 0;
        height: 0;
        font-size: 0;
        margin-right: 5px;
        position: relative;
        top: -4px;
        left: 0;
    }
</style>