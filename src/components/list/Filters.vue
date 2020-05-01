<template>
    <div>
        <!--尺码-->
        <div class="card">
            <!-- 过滤项 头部-->
            <header class="card-header">
                <p class="card-header-title">
                    {{size.header}}
                </p>
                <b-tag class="clear" size="is-small" type="is-text" v-on:click.native="clearSelected(size.context)">{{clear.text}}</b-tag>
            </header>
            <!-- 内容 -->
            <div class="card-content" :style="'height:' + (25 + (size.context.length + 3)/3 * 25) + 'px'">
                <section>
                    <b-tag class="size" v-for="(item, index) in size.context" :key="index" v-bind:style="[item.selected ? {background: 'black', fontWeight: 'bolder', color: 'white'} : {}]" v-on:click.native="item.selected = !item.selected">
                        {{item.value}}
                    </b-tag>
                </section>
            </div>
            <!-- 过滤项 尾部-->
            <footer class="card-footer">
            </footer>
        </div>
        <!--颜色-->
        <div class="card">
            <!-- 过滤项 头部-->
            <header class="card-header">
                <p class="card-header-title">
                    {{color.header}}
                </p>
                <b-tag class="clear" size="is-small" type="is-text" v-on:click.native="clearSelected(color.context)">{{clear.text}}</b-tag>
            </header>
            <!-- 内容 -->
            <div class="card-content" :style="'height:' + (25 + (color.context.length + 10)/10 * 25) + 'px'">
                <section>
                    <div class="color_warp" v-for="(item, index) in color.context" :key="index" v-on:click="item.selected = !item.selected">
                        <b-tag class="color" v-bind:style="{'background-color': item.value}">
                            <span v-if="item.selected" style="color: white;font-weight: bolder;">&radic;</span>
                        </b-tag>
                    </div>
                </section>
            </div>
            <!-- 过滤项 尾部-->
            <footer class="card-footer">
            </footer>
        </div>
        <!--价格-->
        <div class="card">
            <!-- 过滤项 头部-->
            <header class="card-header">
                <p class="card-header-title">
                    <span>{{price.header}}</span>
                </p>
                <b-tag class="clear" size="is-small" type="is-text">{{clear.text}}</b-tag>
            </header>
            <!-- 内容 -->
            <div class="card-content">
                <section>
                    <b-field>
                        <b-slider rounded v-model="price.context" type="is-dark" size="is-small" :min="price.min" :max="price.max" :step="price.step">
                            <b-slider-tick :value="price.context[price.left]">{{price.context[price.left]}}</b-slider-tick>
                            <b-slider-tick :value="price.context[price.right]">{{price.context[price.right]}}</b-slider-tick>
                        </b-slider>
                    </b-field>
                </section>
            </div>
            <!-- 过滤项 尾部-->
            <footer class="card-footer">
            </footer>
        </div>
        <!-- 款式 -->
        <div class="card">
            <!-- 过滤项 头部-->
            <header class="card-header">
                <p class="card-header-title">
                    {{style.header}}
                </p>
                <b-tag class="clear" size="is-small" type="is-text" v-on:click.native="clearSelected(style.context)">{{clear.text}}</b-tag>
            </header>
            <!-- 内容 -->
            <div class="card-content" :style="'height:' + (25 + (style.context.length + 3)/3 * 25) + 'px'">
                <section>
                    <b-tag class="style" v-for="(item, index) in style.context" :key="index" v-bind:style="[item.selected ? {background: 'black', fontWeight: 'bolder', color: 'white'} : {}]" v-on:click.native="item.selected = !item.selected">
                        {{item.value}}
                    </b-tag>
                </section>
            </div>
            <!-- 过滤项 尾部-->
            <footer class="card-footer">
            </footer>
        </div>
        <!-- 材质 -->
        <div class="card">
            <!-- 过滤项 头部-->
            <header class="card-header">
                <p class="card-header-title">
                    {{fabric.header}}
                </p>
                <b-tag class="clear" size="is-small" type="is-text" v-on:click.native="clearSelected(fabric.context)">{{clear.text}}</b-tag>
            </header>
            <!-- 内容 -->
            <div class="card-content" :style="'height:' + (25 + (fabric.context.length + 3)/3 * 25) + 'px'">
                <section>
                    <b-tag class="fabric" v-for="(item, index) in fabric.context" :key="index" v-bind:style="[item.selected ? {background: 'black', fontWeight: 'bolder', color: 'white'} : {}]" v-on:click.native="item.selected = !item.selected">
                        {{item.value}}
                    </b-tag>
                </section>
            </div>
            <!-- 过滤项 尾部-->
            <footer class="card-footer">
            </footer>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Filters",
        data() {
            return {
                size: {
                    header: "Size",
                    context: [
                        {value: "XS/36", selected: false},
                        {value: "S/37", selected: false},
                        {value: "L/42", selected: false},
                        {value: "M/43", selected: false},
                        {value: "L", selected: false}
                    ]
                },
                color: {
                    header: "Color",
                    context: [
                        {value : "rgba(255,0,0,0.8)", selected: false},
                        {value : "rgba(0,255,0,1)", selected: false},
                        {value : "rgba(0,0,255,1)", selected: false}
                    ]
                },
                price: {
                    header: "Price",
                    context: [50, 350],
                    min: 1,
                    max: 600,
                    step: 10,
                    left: 0,
                    right: 1,
                    symbol: "$"
                },
                style: {
                    header: "Style",
                    context: [
                        {value: "Tanks", selected: false},
                        {value: "Tees", selected: false},
                        {value: "Dress", selected: false},
                        {value: "Boho", selected: false}]
                },
                fabric: {
                    header: "Fabric",
                    context: [
                        {value: "100% Cotton", selected: false},
                        {value: "Poly-Cotton", selected: false},
                        {value: "Satin", selected: false},
                        {value: "Lace", selected: false},
                        {value: "Tulle", selected: false}
                    ]
                },
                clear: {
                    text: "clear"
                }
            }
        },
        methods: {
            clearSelected(items) {
                items = items || [];
                for (let i = 0; i < items.length; i++) {
                    items[i].selected = false;
                }
            }
        }
    }
</script>

<style scoped>
    .size, .color, .color_warp, .style, .fabric {
        float: left;
        height: 20px;
        width: auto;
        margin: 5px;
        cursor: pointer;
    }
    .size:hover, .style:hover, .fabric:hover {
        background: darkgray;
    }
    .color_warp {
        width: 25px;
        height: 25px;
        margin: 0;
    }
    .color {
        margin: 2px;
        width: 20px;
        border-radius: 100%;
    }
    .color:hover {
        margin: 0;
        width: 25px;
        height: 25px;
    }
    .fabric {
        min-width: 80px;
        margin: 2px;
    }
    .clear, .clear:hover {
        font-size: smaller;
        background: none;
        border: none;
        cursor: pointer;
        color: pink;
        text-decoration: underline;
    }
    .clear:hover {
        font-weight: bolder;
    }
    .card-content {
        padding: 0.5rem;
    }
</style>