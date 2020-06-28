<template>
    <div class="ss_split" v-bind:style="{width: width + 'px', height: height + 'px'}">
        <span class="ss_split_warp"></span>
        <span v-if="item.name[language]" class="ss_split_label" v-bind:style="{fontSize: height / 5 + 'px'}" @click="goto(item)">{{item.name[language]}}</span>
        <span v-else-if="item.name" class="ss_split_label" v-bind:style="{fontSize: height / 5 + 'px'}" @click="goto(item)">{{item.name}}</span>
        <span v-else class="ss_split_label" v-bind:style="{fontSize: height / 5 + 'px'}" @click="goto(item)">{{item}}</span>
    </div>
</template>

<script>
    export default {
        name: "Split",
        props: {
            width: {
                type: Number,
                required: false,
                default: 1440
            },
            height: {
                type: Number,
                required: false,
                default: 150
            },
            item: {
                type: Object,
                required: true
            },
            language: {
                type: String,
                required: false,
                default: "en"
            }
        },
        methods: {
            goto(item) {
                if (!item.link) {
                    return
                }
                this.$router.push({path: item.link})
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
    .ss_split {
        overflow: hidden;
        position: relative;
    }
    .ss_split_warp {
        position: absolute;
        border: 1px solid lightgray;
        width: 100%;
        top: 50%;
    }
    .ss_split_label {
        text-align: center;
        display: inline-block;
        position: absolute;
        z-index: 1;
        left: 50%;
        top: 35%;
        background: white;
        font-size: x-large;
        font-family: monospace;
        text-transform:capitalize;
    }
    .ss_split_label:hover {
        font-weight: bolder;
        text-decoration: underline;
        cursor: pointer;
    }
</style>