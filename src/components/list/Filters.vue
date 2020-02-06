<template>
    <div>
        <!--尺码-->
        <div class="card">
            <!-- 过滤项 头部-->
            <header class="card-header">
                <p class="card-header-title">
                    {{size.header}}
                </p>
                <b-tag class="clear" size="is-small" type="is-text">{{clear.text}}</b-tag>
            </header>
            <!-- 内容 -->
            <div class="card-content">
                <section>
                    <b-tag class="size" v-for="(item, index) in size.context" :key="index">{{item}}</b-tag>
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
                <b-tag class="clear" size="is-small" type="is-text">{{clear.text}}</b-tag>
            </header>
            <!-- 内容 -->
            <div class="card-content">
                <section>
                    <div class="color_warp" v-for="(item, index) in color.context" :key="index" >
                        <b-tag class="color" v-bind:style="{'background-color': item}"></b-tag>
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
                        <b-slider rounded v-model="price.context" type="is-info" size="is-small" :min="price.min" :max="price.max" :step="price.step">
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
                <b-tag class="clear" size="is-small" type="is-text">{{clear.text}}</b-tag>
            </header>
            <!-- 内容 -->
            <div class="card-content">
                <section>
                    <b-tag class="style" v-for="(item, index) in style.context" :key="index">{{item}}</b-tag>
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
                <b-tag class="clear" size="is-small" type="is-text">{{clear.text}}</b-tag>
            </header>
            <!-- 内容 -->
            <div class="card-content">
                <section>
                    <b-tag class="fabric" v-for="(item, index) in fabric.context" :key="index">{{item}}</b-tag>
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
                    context: ["XS/36", "S/37", "L/42", "M/43", "L"]
                },
                color: {
                    header: "Color",
                    context: [
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                        "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
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
                    context: ["Tanks", "Tees", "Dress", "Boho"]
                },
                fabric: {
                    header: "Fabric",
                    context: ["100% Cotton", "Poly-Cotton", "Satin", "Lace", "Tulle", "Chiffon", "100% Cotton", "Poly-Cotton"]
                },
                clear: {
                    text: "clear"
                }
            }
        }
    }
</script>

<style scoped>
    .size, .color, .color_warp, .style, .fabric {
        float: left;
        height: 20px;
        width: 40px;
        margin: 5px;
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
        min-height: 100px;
    }
</style>