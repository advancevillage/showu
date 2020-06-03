<template>
    <div class="color-group" v-bind:style="{width: width + 'px', height: (items.length * 30/width * 20 + height) + 'px'}">
        <header>
            <p v-if="title.length > 0" v-bind:style="{width: (100 - 6 - 1 - (clear.length * 7) * 100 / width) + '%'}">{{title}}</p>
            <button v-if="clear.length > 0" v-bind:style="{width: ((clear.length * 7) * 100 / width) + '%'}" @click="reset">{{clear}}</button>
        </header>
        <section>
            <span class="warp" v-for="(item, index) in items" :key="index" v-on:click="get(index)">
                <span v-if="selected[index].key" class="color"  v-bind:style="{backgroundColor: item.rgb, color: reversalColor(item.rgb), fontWeight: 'border', fontFamily: 'serif'}">&radic;</span>
                <span v-if="!selected[index].key" class="color" v-bind:style="{backgroundColor: item.rgb}"></span>
            </span>
        </section>
    </div>
</template>

<script>
    export default {
        name: "ColorGroup",
        props: {
            items: {
                type: Array,
                required: true,
            },
            width: {
                type: Number,
                required: false,
                default: 200
            },
            height: {
                type: Number,
                required: false,
                default: 100
            },
            title: {
                type: String,
                required: false,
                default: "TagGroup"
            },
            clear: {
                type: String,
                required: false,
                default: "clear"
            }
        },
        data() {
            return {
                selected: []
            }
        },
        mounted() {
            for (let i = 0; i < this.items.length; i++) {
                this.selected.push({key: false})
            }
        },
        watch: {
            items() {
                for (let i = 0; i < this.items.length; i++) {
                    this.selected.push({key: false})
                }
            }
        },
        methods: {
            reset() {
                for (let i = 0; i < this.items.length; i++) {
                    this.selected[i].key = false
                }
                let data = [];
                this.$emit('get', data)
            },
            get(index) {
                this.selected[index].key = !this.selected[index].key;
                let data = [];
                for (let i = 0; i < this.items.length; i++) {
                    if (this.selected[index].key) {
                        data.push(this.items[i])
                    }
                }
                this.$emit('get', data)
            },
            reversalColor(colorStr) {
                let sixNumReg = /^#(\w{2})(\w{2})(\w{2})$/ig;
                let threeNumReg = /^#(\w{1})(\w{1})(\w{1})$/ig;
                let rgbReg = /^rgb\((\w{1,3}), (\w{1,3}), (\w{1,3})\)$/ig;
                let c1=0, c2=0, c3=0;
                let parseHexToInt = function(hex){
                    return parseInt(hex,16);
                };
                let parse = function() {
                    if(sixNumReg.test(colorStr)){
                        sixNumReg.exec(colorStr);
                        c1 = parseHexToInt(RegExp.$1);
                        c2 = parseHexToInt(RegExp.$2);
                        c3 = parseHexToInt(RegExp.$3);
                    } else if(threeNumReg.test(colorStr)){
                        threeNumReg.exec(colorStr);
                        c1 = parseHexToInt(RegExp.$1+RegExp.$1);
                        c2 = parseHexToInt(RegExp.$2+RegExp.$2);
                        c3 = parseHexToInt(RegExp.$3+RegExp.$3);
                    } else if(rgbReg.test(colorStr)){
                        //rgb color 直接就是十进制，不用转换
                        rgbReg.exec(colorStr);
                        c1 = RegExp.$1;
                        c2 = RegExp.$2;
                        c3 = RegExp.$3;
                    } else {
                        throw new Error("Error color string format. eg.[rgb(0,0,0),#000000,#f00]");
                    }
                    // c1 = parseIntToHex(255 - c1);
                    // c2 = parseIntToHex(255 - c2);
                    // c3 = parseIntToHex(255 - c3);
                    if (c1 >= 192 && c2 >= 192 && c3 >= 192) {
                        return '#000';
                    } else {
                        return '#fff';
                    }
                };
                return parse();
            }
        }
    }
</script>

<style scoped>
    .color-group {
        font-family: monospace;
        margin: 2px;
        line-height: 1rem;
    }
    .color-group header {
        border-bottom: 1px solid darkgray;
        margin-bottom: 3%;
        float: left;
        width: 100%;
    }
    .color-group header > p {
        float: left;
        text-align: left;
        margin: 1%;
        color: black;
    }
    .color-group header > button {
        float: left;
        margin: 2%;
        text-align: center;
        outline: none;
        box-shadow: none;
        text-decoration: underline;
        border: none;
        cursor: pointer;
        color: black;
        background-color: rgba(128,128,128,0);
    }
    .color-group header > button:hover {
        font-weight: bolder;
    }
    .warp {
        width: 24px;
        height: 24px;
        float: left;
        cursor: pointer;
        margin: 0;
        border-radius: 100%;
    }
    .color {
        width: 20px;
        height: 20px;
        display: inline-block;
        border-radius: 100%;
        background-color: rgb(16, 0, 0);
        color: rgb(255, 255, 255);
        font-family: monospace;
        font-weight: bolder;
        padding: 0 2px 0;
    }
    .color:hover {
        margin: 0;
        width: 24px;
        height: 24px;
        padding: 0 6px 0;
    }
</style>