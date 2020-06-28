<template>
    <div class="footer" v-bind:style="{width: width + 'px'}">
        <div v-for="(group, index) in footers" :key="index">
            <div class="group" v-for="(items, key) in group" :key="key">
                <span>{{key}}</span>
                <ListGroup :items="items" :width="width * 0.08" :height="height"/>
            </div>
        </div>
        <span class="mdi mdi-copyright copyright">{{year}}&nbsp;&nbsp;{{company}}</span>
    </div>
</template>

<script>
    import ListGroup from "../Basic/ListGroup";

    export default {
        name: "Footer",
        components: {
            ListGroup,
        },
        props: {
            width: {
                type: Number,
                required: false,
                default: 1440,
            },
            height: {
                type: Number,
                required: false,
                default: 300,
            }
        },
        data() {
            return {
                footers: [],
                company: "",
                year: 2050,
            }
        },
        mounted() {
            this.QueryFooters();
        },
        methods: {
            async QueryFooters() {
                const params = {};
                const headers = {};
                let response = await this.$api.QueryFooters(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response)
                } else {
                    this.footers = response.data.items;
                    this.company = response.data.company;
                    this.year    = response.data.year;
                }
            }
        }
    }
</script>

<style scoped>
    .footer {
        overflow: hidden;
        background: lightgray;
        line-height: 1.5rem;
        margin: 0;
        padding: 0;
        height: auto;
    }
    .footer > div {
        float: left;
        padding: 1%;
        height: 90%;
        text-align: left;
    }
    .group > span {
        display: inline-block;
        text-align: center;
        width: 100%;
        font-family: monospace;
        text-transform:capitalize;
        font-size: x-large;
        margin-bottom: 5%;
        color: black;
    }
    .copyright {
        width: 100%;
        font-family: monospace;
        background: black;
        color: white;
        text-align: center;
        display: inline-block;
    }
</style>