<template>
    <div :style="'height:' + (30 + (colors.length)/4 * 30) + 'px'">
        <div class="detail_color">
            <section>
                <div class="color_warp" v-for="(item, index) in colors" :key="index" @click="selected = index">
                    <b-tag class="color" v-bind:style="{'background-color': item.rgb}">
                        <span v-if="index === selected" v-bind:style="{color: reversalColor(item.rgb),fontWeight: 'bolder'}">&radic;</span>
                    </b-tag>
                </div>
            </section>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Color",
        props: {
            colors: {
                type: Array,
                required: true,
            },
        },
        data() {
            return {
                selected: 0,
            }
        },
        methods: {
            //计算颜色值的反色，colorStr格式为：rgb(0,0,0),#000000或者#f00
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
    .detail_color {
        width: 100%;
        height: 100%;
    }
    .color, .color_warp {
        margin: 0;
        padding: 0;
        width: 20px;
        height: 20px;
        border-radius: 100%;
        cursor: pointer;
        float: left;
    }
    .color_warp {
        float: left;
        width: 25px;
        height: 25px;
    }
    .color {
        margin: 2px
    }
    .color:hover {
        margin: 0;
        width: 25px;
        height: 25px
    }
</style>