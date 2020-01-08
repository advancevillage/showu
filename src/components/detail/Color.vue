<template>
    <div>
        <div class="detail_color">
            <section>
                <div class="color_warp" v-for="(item, index) in context" :key="index" >
                    <b-tag class="color" v-bind:style="{'background-color': item}"></b-tag>
                </div>
            </section>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Color",
        data() {
            return {
                context: [
                    "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                    "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                    "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                    "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)",
                    "rgba(255,0,0,0.8)", "rgba(0,255,0,1)", "rgba(0,0,255,1)", "rgba(255,255,0,1)"
                ]
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
    }
    .color_warp {
        float: left;
        width: 25px;
        height: 25px;
        margin-right: 2px;
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